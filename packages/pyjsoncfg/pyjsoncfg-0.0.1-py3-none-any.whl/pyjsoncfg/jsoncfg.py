
import os
import sys

import json
import copy


VERSION = "v0.0.1"

class _cfg_namespace:
    
    def __init__( self, cfg ):
        
        self.__dict__.update( cfg )
        
        for k,v in self.__dict__.items():
            if isinstance( v, dict ):
                self.__dict__.update( { k: _cfg_namespace(v) } )
            if isinstance( v, _cfg_namespace ):
                self.__dict__.update( { k: _cfg_namespace(v.__dict__) } )

    def __iter__(self):
        for k,v in self.items():
            yield k
            
    def __getitem__(self, key ):
        return self.__dict__[key]

    def __setitem__(self, key, v ):
        if isinstance( v, dict ):
            v = _cfg_namespace(v) 
        self.__dict__[key] = v

    def __delitem__(self, key ):
        del self.__dict__[key]

    def update(self, dict_ ):
        self.__dict__.update( dict_ )
        return self

    def items(self):
        return self.__dict__.items()
    
    def __repr__(self):
        d = self._dismantle(self.__dict__)
        return json.dumps(d)
    
    def _dismantle(self,dic):
        d = {}
        for k,v in dic.items():
            if isinstance( v, _cfg_namespace ):
                d[k] = self._dismantle(v.__dict__)
            else:
                d[k] = v
        return d
   
    def default(self,o):
        try:
            return self._dismantle(o.__dict__)
        except:
            return json.JSONEncoder.default(self, o)


class Config:

    DEFAULT_CONFIG_FILE = "cfg.json"

    # environment variables
    PYJSONCONFIG_BASE = "PYJSONCONFIG_BASE"
    
    def __init__(self, filename = DEFAULT_CONFIG_FILE, basepath=None, not_exist_ok=True, auto_conv=True ):
        if basepath is None:
            basepath = os.environ.setdefault( Config.PYJSONCONFIG_BASE, "." )
        self.basepath = basepath
        self.filename = filename
        self.clear()
        if not not_exist_ok and not self.exists():        
            raise Exception("file not exist", self._fullpath() )
        self.load()
        if auto_conv:
            self.conv()
        
    def __repr__(self):
        return f"<Config file={ self._fullpath() } content={ self.data }>"

    def _fullpath(self):
        fullpath = os.path.join(self.basepath,self.filename)
        userpath = os.path.expanduser( fullpath )        
        normpath = os.path.normpath( userpath )
        abspath = os.path.abspath( normpath )
        return abspath

    def clear(self):
        self.data = {}

    def conv(self):
        self.data = self._namespace()
        
    def isconv(self):
        return isinstance( self.data, _cfg_namespace )

    def default(self,o):
        # call the inner default here too ...
        # since it handles both (python and custom class)
        return o.data.default(o)
    
    def _namespace(self):
        
        """return a shallow copy of the namespace for this object"""
        
        if self.isconv():
            return _cfg_namespace(self.data.__dict__)
        return _cfg_namespace(self.data)

    def exists(self):
        
        """check if file exists and size > 0"""
        
        fp = self._fullpath()
        return os.path.exists(fp) and os.path.getsize(fp) > 0

    def load(self):
        if self.exists():
            with open(self._fullpath()) as f:
                self.data = json.load(f)
        return self.data
        
    def savefd(self,fd,indent=4,sort_keys=True):
        conv = None if isinstance( self.data, dict ) else self.data.default
        json.dump(self.data, fd, default=conv,indent=indent,sort_keys=sort_keys)
      
    def save(self,indent=4,sort_keys=True):
        with open(self._fullpath(), 'w') as f:        
            self.savefd(f,indent,sort_keys)
      
    def val( self, arr, defval = None, conv = None ):
        return self._getconfigval( arr, defval, conv )

    def str( self, arr, defval="" ):
        return self._getconfigval( arr, defval, str )

    def bool( self, arr, defval=True ):
        conf_bool = lambda t : str(t).lower() == "true" 
        return self._getconfigval( arr, defval, conf_bool )

    def int( self, arr, defval=0 ):
        conf_int = lambda t : int( t )
        return self._getconfigval( arr, defval, conf_int )

    def float( self, arr, defval=0.0 ):
        conf_float = lambda t : float( t )
        return self._getconfigval( arr, defval, conf_float )

    def __call__( self, evalstr=None ):
        if evalstr is None:
            return self.data
        path = evalstr.split(".")
        return path

    def _getconfigval( self, ar, defval = None, conf = None ):
        
        if not isinstance( ar, list):
            raise Exception( "arr must be list type")
        
        arr = []
        arr.extend(ar)
        last = arr.pop()
        e = self.data

        if self.isconv():
            for se in arr:
                if se in e.__dict__:
                    e = e.__dict__[se]
                else:
                    e = e.__dict__.update( { se, _cfg_namespace() } )
            
            if last in e.__dict__:
                val = e.__dict__[ last ]
            else:
                val = defval 

            if conf:
                val = conf( val )
            e.__dict__[ last ] = val
            return val

        else:
            for se in arr:
                e = e.setdefault( se, {} )            
            val = e.setdefault( last, defval )
                
            if conf:
                val = conf( val )
            e[last] = val
            return val

    
    def sanitize(self,addkeywords=[],_dict=None):
        
        """remove sensitive data from config"""
        
        keywords = [ "user", "pass", "url", "host", "remote", "port" ]
        keywords.extend(addkeywords)
        
        if _dict is None:
            _dict = self.__dict__
            
        for k,v in _dict.items():
            if isinstance( v, dict ):
                self.sanitize( addkeywords=addkeywords, _dict=v )
                continue
            if isinstance( v, _cfg_namespace ):
                self.sanitize( addkeywords=addkeywords, _dict=v.__dict__ )
                continue
            for kw in keywords:
                if k.lower().find(kw)>=0:
                    if k.lower().find("default") >= 0:
                        # dont process default settings even when keyword is found
                        continue
                    _dict[k] = f"*** {kw} ***"
        
    
import setuptools

with open("README.MD", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyjsoncfg", 
    version="v0.0.1",
    author="k.r. goger",
    author_email="k.r.goger+pyjsoncfg@gmail.com",
    description="python json config file handling",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kr-g/pyjsoncfg",
    packages=setuptools.find_packages(),
    license = 'MIT',
    keywords = 'python config json micropython esp8266 esp32',
    install_requires=[],    
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Operating System :: POSIX :: Linux',
        'Intended Audience :: Developers',
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires='>=3.6',
)


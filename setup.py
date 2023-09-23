from setuptools import setup, find_packages

VERSION = '0.0.2' 
DESCRIPTION = 'Contains functions used for my (Nikko Cleri\'s) research.'
LONG_DESCRIPTION = 'Functions to make plots and perform data and statistical analyses.'

# Setting up
setup(
       # the name must match the folder name 'nikkos_tools'
        name="nikkos_tools", 
        version=VERSION,
        author="Nikko Cleri",
        author_email="<nikko.cleri@gmail.com>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        readme = "README.md",
        packages=find_packages(),
        install_requires=['numpy', 'pandas', 'astropy', 'matplotlib',],
        keywords=['python', 'utilities'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
        ]
)
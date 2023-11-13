from setuptools import setup
from src.version import __version__

setup(
    name="randimania",
    version=__version__,
    python_requires="=>3.6",
    entry_points={
        "console_scripts":["randimania = src.main:main"]    
    },
)
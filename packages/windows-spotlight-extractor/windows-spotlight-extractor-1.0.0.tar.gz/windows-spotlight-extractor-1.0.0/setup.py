import pathlib

from setuptools import setup

setup(
    name='windows-spotlight-extractor',
    version='1.0.0',
    packages=['spotlight'],
    url='https://bitbucket.org/Jonathan_Turnock/windows-10-spotlight-extractor',
    license='MIT',
    author='Jonathan Turnock',
    author_email='Jonathan.Turnock@outlook.com',
    description='CLI Tool for exporting Windows 10 Spotlight Images as Wallpapers',
    long_description=(pathlib.Path(__file__).parent / "README.md").read_text(),
    long_description_content_type="text/markdown",
    install_requires=['pillow'],
    entry_points={
        'console_scripts': ['spotlight=spotlight.extractor:main'],
    }
)

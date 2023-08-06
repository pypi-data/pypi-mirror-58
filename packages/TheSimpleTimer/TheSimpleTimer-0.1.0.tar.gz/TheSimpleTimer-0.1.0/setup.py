from setuptools import setup
from os import path


def file_README():
    read_path = path.join(path.dirname(path.realpath(__file__)), "README.md")
    with open(read_path) as f:
        return f.read()


setup(
    name="TheSimpleTimer",
    version="0.1.0",
    description="Simple Timer with no real features",
    long_description=file_README(),
    long_description_content_type="text/markdown",
    url="https://github.com/cowboy8625/TheSimpleTimer",
    author="Cowboy8625",
    author_email="cowboy8625@protonmail.com",
    license="Apache License",
    packages=["thesimpletimer"],
    scripts=["bin/simpletimer", "bin/simpletimer.bat",],
    zip_safe=False,
)

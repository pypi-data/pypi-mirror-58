import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name="clitt",
    version="1.0.0",
    description="Use Twitter from your terminal!",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/leviosar/tt",
    author="Leviosar",
    author_email="maia.tostring@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=find_packages(exclude=("tests")),
    include_package_data=True,
    install_requires=["tweepy", "colorama"],
    entry_points={
        "console_scripts": [
            "leviosar=clitt.__main__:main",
        ]
    },
)
import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name="pygans",
    version="2.0.3",
    description="Simple Python Framework for creating GANs and seeing evolution through time",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/afzp99/pygans",
    author="Andres Felipe Zapata Palacio",
    author_email="afzp99@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=["numpy", "keras", "matplotlib", "tensorflow"],
)

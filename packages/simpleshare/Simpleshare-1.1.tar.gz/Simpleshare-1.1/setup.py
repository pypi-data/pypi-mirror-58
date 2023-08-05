# setup.py
import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

setup(
    name="Simpleshare",
    version="v1.1",
    description="A local file sharing utility written in Python. Uses multicast UDP to share the list of files, and TCP to transfer the files themselves.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/ssebs/simpleshare",
    author="Sebastian Safari",
    author_email="contact@ssebs.com",
    license="MIT",
    packages=find_packages(),
    include_package_data=True,
    python_requires=">=3.6.0",
    install_requires=["pyttk", "PyInstaller"],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        "Operating System :: OS Independent",
    ]
)
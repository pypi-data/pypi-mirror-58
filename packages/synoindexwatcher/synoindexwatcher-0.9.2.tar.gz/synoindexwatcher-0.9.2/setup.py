
import setuptools
import sys

# Define package dependencies for all Python versions

install_requires = ["inotifyrecursive>=0.2.5"]

if sys.version_info.major < 3 or (sys.version_info.major == 3 and sys.version_info.minor < 5):
    install_requires += ["configparser"]

if sys.version_info.major < 3 and sys.version_info.minor < 2:
    install_requires += ["argpase"]

# Use readme-file as long description

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="synoindexwatcher",
    version="0.9.2",
    author="Torben Haase",
    author_email="torben@pixelsvsbytes.com",
    description="An automated media-index updater for Synology DiskStations based on inotify and synoindex.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/letorbi/synoindexwatcher",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
    ],
    install_requires=install_requires,
)

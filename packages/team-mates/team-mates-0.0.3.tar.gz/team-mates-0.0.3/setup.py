import platform
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

# select os specific dependencies
operating_system = platform.system()
if operating_system == 'Windows':
    raise OSError("This module has no support for windows yet.")
elif operating_system == 'Linux':
    WSGI_SERVER = 'gunicorn'

setuptools.setup(
    name="team-mates",
    version="0.0.3",
    author="Sylvan LE DEUNFF",
    author_email="sylvan.ledeunff@gmail.com",
    description="A library to analyze team mates contributions to projects.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/team-mates",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'flask',
        WSGI_SERVER
    ],
    python_requires='>=3.6',
)

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="team_mates",
    version="0.0.1",
    author="Sylvan LE DEUNFF",
    author_email="sylvan.ledeunff@gmail.com",
    description="A library to analyze team-mates contributions to projects.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/team-mates",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

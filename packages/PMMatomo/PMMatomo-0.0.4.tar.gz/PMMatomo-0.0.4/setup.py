import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="PMMatomo",
    version="0.0.4",
    author="Philipp Mayr",
    author_email="me@philipp-mayr.de",
    description="A Python wrapper for the Matomo HTTP reporting API.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/philippmayrth/PMMatomo",
    packages=setuptools.find_packages(),
    install_requires=['requests', 'deprecated'],
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Topic :: Office/Business",
        "Topic :: Office/Business :: Financial :: Investment",
    ],
)

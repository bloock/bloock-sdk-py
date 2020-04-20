import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="enchaintesdk",
    version="0.0.1",
    author="Albert Canyelles Ruiz",
    author_email="acanyelles@enchainte.com",
    description="enchainte-sdk for python3",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/enchainte/enchainte-sdk-py",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
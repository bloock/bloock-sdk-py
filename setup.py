import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="enchaintesdk",
    version="0.1.2",
    author="Albert Canyelles Ruiz",
    author_email="acanyelles@enchainte.com",
    description="Enchainté SDK for Python3",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/enchainte/enchainte-sdk-py",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['requests>=2.24.0',
                      'web3>=5.6.0',
                      'pycryptodome>=3.0'],

    python_requires='>=3.5',
)

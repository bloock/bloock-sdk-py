import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="enchaintesdk",
    version="0.0.9.6.5",
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
    install_requires=['numpy>=1.18.0',
                      'requests>=2.24.0',
                      'web3>=5.6.0',
                      'interface>=1.6.0'],
    python_requires='>=3.5',
)

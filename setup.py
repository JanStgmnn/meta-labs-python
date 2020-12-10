import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="metalabs_sdk", # Replace with your own username
    version="0.1.1",
    author="Jeffrey Annaraj",
    author_email="jannaraj@baffled.dev",
    description="SDK for MetaLabs API ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JAnnaraj/meta-labs_sdk",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    keywords='metalabs',
    install_requires=['urllib3']
)
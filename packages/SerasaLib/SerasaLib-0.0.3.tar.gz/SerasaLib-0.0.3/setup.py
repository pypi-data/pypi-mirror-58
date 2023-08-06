import setuptools

with open("README.md", "r") as fh:
	long_description = fh.read()

setuptools.setup(
    name="SerasaLib",
    version="0.0.3",
    author="FastDeploy",
    author_email="fastdeploy@dextra-sw.com",
    description="Transmissao de arquivos (Sandbox)",
    long_description=long_description,
    long_description_content_type="",
    url="",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

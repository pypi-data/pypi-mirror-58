import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="magpy-raz",
    version="1.0.1",
    author="Raz Nitzan",
    author_email="raz.nitzan@gmail.com",
    description="Extract project data from GitLab",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/Razinka/magpy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

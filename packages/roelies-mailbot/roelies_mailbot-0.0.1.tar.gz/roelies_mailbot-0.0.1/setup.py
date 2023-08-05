import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="roelies_mailbot", # Replace with your own username
    version="0.0.1",
    author="Raul Wolters",
    author_email="r.wolters@umail.leidenuniv.nl",
    description="A package that can automatically send emails",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rwolters2000/mailbot",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
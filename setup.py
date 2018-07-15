import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name = 'mypassman',
    version = '0.0.4',
    author = "Sean Pierce",
    author_email = "sumler.sean@gmail.com",
    description = 'A super simple password management app',
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/seanpierce/passman",
    packages = setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Utilities"
    ),
    entry_points = {
        'console_scripts': [
            'passman = passman.passman:main'
        ]
    },
)

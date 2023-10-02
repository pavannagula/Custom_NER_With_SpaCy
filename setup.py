import setuptools

with open("README.MD", 'r', encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "Custom_NER_Model_With_SpaCy"
AUTHOR_USER_NAME = "pavannagula"
SRC_REPO = "Custom_NER_With_SpaCy"
AUTHOR_EMAIL = "npavankumar36@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="This project is about building Custom NER Model using SpaCy for extracting domain specific keywords from the org text data",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)
from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = '-e .'


def get_requirements(file_path: str) -> List[str]:
    """
    This function will return the list of requirements.
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()  # Reads all lines from the requirements file.
        requirements = [req.strip() for req in requirements]  # Removes newline characters.

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)  # Removes the `-e .` entry if present.

    return requirements  # Returns a cleaned list of dependencies.



with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()



REPO_NAME = "Text-Summarization"
AUTHOR_USER_NAME = "ahmed1010ali"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "ahmed938ali@gmail.com"

setup(
    name=SRC_REPO,
    version="0.1.0",
    author=AUTHOR_USER_NAME,  
    author_email=AUTHOR_EMAIL,
    description="A small NLP app for text summarization",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=get_requirements('requirements.txt'),
)

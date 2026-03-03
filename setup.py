from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = "-e ."

def get_requirements(file_path: str) -> List[str]:
    """
    This function returns the list of requirements
    """

    requirements = []

    with open(file_path) as file_obj:
        requirements = file_obj.readlines()# readlines() returns a list of lines in the file, including the newline character at the end of each line
        requirements = [req.replace("\n", "") for req in requirements] 

        # remove -e . from requirements
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements


setup(
    name="mlproject",
    version="0.0.1",
    author="Krishna Mangal",
    author_email="your_email@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)
from setuptools import find_packages, setup
from typing import List

NAME = "sensor"
VERSION = "0.0.2"
AUTHOR = "naveen"
AUTHOR_EMAIL_ID = "naveeneen02@gmail.com"
REQUIREMENTS_FILE_NAME = "requirements.txt"
HYPHEN_E_DOT = "-e ."


def get_requirements(file_path: str = REQUIREMENTS_FILE_NAME) -> List[str]:
    requirements = []

    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

    if HYPHEN_E_DOT in requirements:
        requirements.remove(HYPHEN_E_DOT)

    return requirements


setup(
    name=NAME,
    version=VERSION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL_ID,
    packages=find_packages(exclude=["tests"]),  # Exclude tests directory if present
    install_requires=get_requirements(),
)


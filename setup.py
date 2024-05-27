from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = "-e ."

def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirements.
    '''
    requirements = []
    with open(file_path) as file:
        requirements = file.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements

setup(
    name="ml_project",
    version="1.0.1",
    author="sidhant",
    author_email="sidhanta1989.maharana@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
    entry_points={
        'console_scripts': [
            'ml_project=ml_project.cli:main',
        ],
    },
)

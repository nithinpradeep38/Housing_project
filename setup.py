import re
from setuptools import setup, find_packages
from typing import List

#declaring variables for setup functions

PROJECT_NAME= "Housing-predictor"
VERSION= "0.0.1"
AUTHOR= "NITHIN PRADEEP"
DESCRIPTION= "First end to end ML project"


REQUIREMENT_FILE_NAME= "requirements.txt"

HYPHEN_E_DOT= "-e ."

def get_requirements_list() -> List[str]:
    """
    Description: This function is going to return list of requirement
    mention in requirements.txt file
    return This function is going to return a list which contain name
    of libraries mentioned in requirements.txt file
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        requirement_list = requirement_file.readlines()
        requirement_list= [requirement_name.replace("\n","") for requirement_name in requirement_list]
        if HYPHEN_E_DOT in requirement_list:
            requirement_list.remove(HYPHEN_E_DOT)
        return requirement_list

setup(
name=PROJECT_NAME,
version=VERSION,
author=AUTHOR,
description=DESCRIPTION,
packages=find_packages(), 

install_requires=get_requirements_list()
)
"""
    For packages, instead of ["housing"] we use pre-built find_packages that return list of all folders with __init__.py
    install_requires will install all external packages and for that we use requirements.txt
"""

"""
Run this as python setup.py install
"""
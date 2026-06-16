from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = '-e .'


def get_requiremnt(file_path:str)->List[str]:
    requirments=[]
    with open(file_path) as f:
        requirments=f.readlines()
        requirments=[req.replace("\n","") for req in requirments]

        if HYPEN_E_DOT in requirments:
            requirments.remove(HYPEN_E_DOT)
        
    return requirments

setup(
    name='src',
    version='0.0.1',
    author='aditya',
    author_email='adityasharma32001@gmail.com',
    install_requires=get_requiremnt('requirements.txt'),
    packages=find_packages(),
)
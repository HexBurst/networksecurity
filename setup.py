from os import name
from setuptools import find_packages,setup
from typing import List

def get_requirements()->list[str]:
  """
   this function will return list of requirements 
  """
  requirements_lst:List[str]=[]
  try:
    with open('requirements.txt','r') as file:
      #Read lines from the file
      lines=file.readlines()
      #process each line
      for line in lines:
        requirement=line.strip()
        #ignore emoty lines and -e.
        if requirement and requirement!='-e .':
          requirements_lst.append(requirement)

  except FileNotFoundError:
    print('requirement.txt file  not found error')
  return requirements_lst

setup(
  name="NetworkSecurity",
  version='0.0.1',
  author='Anirudh',
  author_email="anirudhsingh972005@gmail.com",
  packages=find_packages(),
  install_requires=get_requirements()
)
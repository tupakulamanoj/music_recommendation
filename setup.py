from setuptools import find_packages,setup

hypen='-e .'
def get_requirements(file_path:str):
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('/n',"") for req in requirements]
    if hypen in requirements:
        requirements.remove(hypen)
    return requirements
setup(name='music_recommendation',version='0.0.1',author='manoj',packages=find_packages(),requires=get_requirements('requirements.txt'))
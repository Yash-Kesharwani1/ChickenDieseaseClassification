import setuptools
with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = 'ChickenDieseaseClassification'
AUTHOR_USER_NAME = 'Yash-Kesharwani1'
SRC_REPO = 'chicken'
AUTHOR_EMAIL = 'yashkesharwani.india@gmail.com'

setuptools.setup(
    name = SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description='A small python package for cnn app',
    long_description=long_description,
    long_description_content='text/markdown',
    url=f'https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}',
    project_urls={
        'Bug Tracker':f"https:/github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"
    },
    package_dir={"":"src"},
    package=setuptools.find_packages(where="src")
)



# from setuptools import setup, find_packages

# def get_requirements(file_path:str)->list[str]:
#     requirements = []
#     with open(file_path) as file_obj:
#         requirements = file_obj.readlines()
#         requirements = [req.replace('/n','') for req in requirements]

#     if '-e .' in requirements:
#         requirements.remove('-e .')


# setup(
#     name="chicken",
#     version='0.0.1',
#     author='Yash Kesharwani',
#     author_email='yashkesharwani.india@gmial.com',
#     description='This app predicts the chicken disease.',
#     packages=find_packages(),
#     install_requires=get_requirements('requirements.txt')
# )
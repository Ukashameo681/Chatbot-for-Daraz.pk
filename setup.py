from setuptools import setup, find_packages


def get_requirements(filepath):
    with open(filepath) as f:
        return f.read().splitlines()
    

setup(
    name='AIChatbot For Daraz.pk',
    version='0.0.1',
    author="Muhammad Ukasha Atif",
    author_email="ukashaatif123@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),

)    




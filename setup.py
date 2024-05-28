from setuptools import setup, find_packages

setup(
    name='alignfix',
    version='0.1',
    description='CSE185 Project',
    author='Jason Chiu, Manish Sampath, Siddharth Kaipa',
    author_email='jmchiu@ucsd.edu, msampath@ucsd.edu, skaipa@ucsd.edu',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'alignfix=alignfix.main:main'
        ],
    },
}

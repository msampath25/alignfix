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
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/msampath25/alignfix',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
    ],
)

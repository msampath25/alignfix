from setuptools import setup, find_packages

setup(
    name='alignfix',
    version='0.1',
    scripts=['./align/alignfix'],
    description='CSE 185 Project',
    author='Jason Chiu, Manish Sampath, Siddharth Kaipa',
    author_email='jmchiu@ucsd.edu, msampath@ucsd.edu, skaipa@ucsd.edu',
    packages=['lib.alignfix'],
    entry_points={
        'console_scripts': [
            'alignfix=alignfix.alignfix:main'
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

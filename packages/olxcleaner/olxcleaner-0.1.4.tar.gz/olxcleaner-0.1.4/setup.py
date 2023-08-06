# -*- coding: utf-8 -*-
"""
setup.py

Contains setup information for the olxcleaner library.

Run with:
python3 setup.py sdist bdist_wheel
"""
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="olxcleaner",
    version="0.1.4",
    author="Jolyon Bloomfield",
    author_email="jolyon@mit.edu",
    description="Tool to scan edX courses for various errors",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jolyonb/olxcleaner",
    license='LICENSE',
    packages=setuptools.find_packages(exclude=['tests']),
    classifiers=[
        "Intended Audience :: Education",
        "Topic :: Education :: Computer Aided Instruction (CAI)",
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    keywords='edx',
    install_requires=[
       'lxml',
       'python-dateutil',
       'pytz',
       'pylatexenc'
    ],
    python_requires='~=3.6',
    entry_points={
        'console_scripts': [
            'edx-cleaner=olxcleaner.entries.edxcleaner:main',
            'edx-reporter=olxcleaner.entries.edxreporter:main'
        ],
    }
)

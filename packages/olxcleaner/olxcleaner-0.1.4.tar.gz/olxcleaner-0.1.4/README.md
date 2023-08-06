# OLX Cleaner

[![Build Status](https://api.travis-ci.org/jolyonb/olxcleaner.svg?branch=master)](https://travis-ci.org/jolyonb/olxcleaner) [![Coverage Status](https://codecov.io/gh/jolyonb/olxcleaner/branch/master/graphs/badge.svg)](https://codecov.io/gh/jolyonb/olxcleaner)

This library aims to perform two functions:

* Parse the XML code for an edX course, loading it into python objects
* Validate the objects for errors

Based on this, two scripts are provided that leverage the library:

* `edx-cleaner` constructs an error report, course tree and course statistics
* `edx-reporter` constructs a LaTeX file representation of the course structure

Version 0.1.4

Copyright (C) 2018-2019 Jolyon Bloomfield

## Links

* [Error Listing](errors.md)
* [Wishlist](wishlist.md)
* [Vision](vision.md)
* [Changelog](changelog.md)
* [License](LICENSE)

## Installation

This package may be installed from PYPI using `pip install olxcleaner`. It requires python 3.6 or later.

### Repository Installation (advanced) 

Clone this repository, and set up a virtual environment for python 3.6 or later. Run `pip install -r requirements.txt` to install the libraries, followed by `pytest` to ensure that all tests are passing as expected.

## edx-cleaner Usage

Used to validate OLX (edX XML) code. This is a very light wrapper around the olxcleaner library, but exposes all of the functionality thereof.

Basic usage: run `edx-cleaner` in the directory of the course you want to validate.

Command-line options:

```text
edx-cleaner [-h] 
            [-c COURSE]
            [-p {1,2,3,4,5,6,7,8}] 
            [-t TREE] [-l {0,1,2,3,4}]
            [-q] [-e] [-s] [-S]
            [-f {0,1,2,3,4}]
            [-i IGNORE [IGNORE ...]]
```

* `-h`: Display help.
* `-c`: Specify the course file to analyze. If not specified, looks for `course.xml` in the current directory. If given a directory, looks for `course.xml` in that directory.
* `-p`: Specify the validation level you wish analyze the course at:
  * 1: Load the course
  * 2: Load the policy and grading policy
  * 3: Validate url_names
  * 4: Merge policy data with course, ensuring that all references are valid
  * 5: Validate the grading policy
  * 6: Have every object validate itself
  * 7: Parse the course for global errors
  * 8: Parse the course for detailed global errors (default)
* `-t TREE`: Specify a file to output the tree structure to.
* `-l`: Specify the depth level to output the tree structure to. Only used if the `-t` option is set. 0 = Course, 1 = Chapter, 2 = Sequential, 3 = Vertical, 4 = Content. 
* `-q`: Quiet mode. Does not output anything to the screen.
* `-e`: Suppress error listing. Implied by `-q`.
* `-s`: Suppress summary of errors. Implied by `-q`.
* `-S`: Display course statistics (off by default). Overridden by `-q`.
* `-f`: Select the error level at which to exit with an error code. 0 = DEBUG, 1 = INFO, 2 = WARNING, 3 = ERROR (default), 4 = NEVER. Exit code is set to `1` if an error at the specified level or higher is present.
* `-i`: Specify a space-separated list of error names to ignore. See [Error Listing](errors.md).

## edx-reporter Usage

The olxcleaner library includes modules that parse a course into python objects. This can be useful if you want to scan a course to generate a report. We exploit this in `edx-reporter` to generate a LaTeX report of course structure.

Basic usage: run `edx-reporter` in the directory of the course you want to generate a report about.

Command-line options:

```text
edx-reporter.py [-h] 
                [-c COURSE]
                [-u]
                [> latexfile.tex]
```

* `-h`: Display help.
* `-c`: Specify the course file to analyze. If not specified, looks for `course.xml` in the current directory. If given a directory, looks for `course.xml` in that directory.
* `-u`: Include url_names for verticals.
* `> latexfile.tex`: Output the report to a file.

If you get an error like ``Character cannot be encoded into LaTeX: U+FEFF - `'``, then you have some bad unicode in your `display_name` entries. Look through the LaTeX output for `{\bfseries ?}`, which is what that character is converted into.

Once you have generated a latex file, you can compile it into a PDF file by running `pdflatex latexfile.tex`. Note that the latex file can be modified with any text editor; its format should be self-explanatory.

## Library usage

The workhorse of the library is `olxcleaner.validate`, which validates a course in a number of steps.

```python
olxcleaner.validate(filename, steps=8, ignore=None)
```

* `filename`: Pass in either the course directory or the path of `course.xml` for the course you wish to validate.
* `steps`: Choose how many validation steps you wish to perform:
    * 1: Load the course
    * 2: Load the policy and grading policy
    * 3: Validate `url_name`s
    * 4: Merge policy data with course, ensuring that all references are valid
    * 5: Validate the grading policy
    * 6: Have every object validate itself
    * 7: Parse the course for global errors
    * 8: Parse the course for global errors that may be time-consuming to detect
* `ignore`: A list of error names to ignore

Returns `EdxCourse`, `ErrorStore`, `url_names` (dictionary `{'url_name': EdxObject}`, or `None` if `steps < 3`)

See examples of how to use `olxcleaner.validate` and the objects it returns in `olxcleaner.entries`.

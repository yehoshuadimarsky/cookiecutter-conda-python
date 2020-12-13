# cookiecutter-conda-python
A [cookiecutter](https://www.github.com/audreyr/cookiecutter "cookiecutter") template for 
conda packages using Python.

This is my personal preferences for my packages.

## Features
 - Flake8
 - Pytest
 - Black
 - Isort
 - pre-commit
 - Ipython
 - Local Conda environment automatically created 

## Requirements
* conda
* cookiecutter (`conda install cookiecutter`)

## Usage
From the directory you want to creat the project in, run `cookiecutter https://github.com/yehoshuadimarsky/cookiecutter-conda-python.git`.

Once cookiecutter clones the template, you will be asked a series of questions related to your project. After answering the questions asked during installation, a conda Python package will be
created in your current working directory. This will also automatically create a new conda environment for the project.

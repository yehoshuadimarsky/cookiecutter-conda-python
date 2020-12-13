from setuptools import find_packages, setup
from pathlib import Path

setup(
    name='{{ cookiecutter.repo_name }}',
    version='0.1',
    author="{{ cookiecutter.full_name.replace('\"', '\\\"') }}",
    description="{{ cookiecutter.project_short_description }}",
    long_description=Path("./README.md").read_text(),
    long_description_content_type="text/markdown",
    license="{{ cookiecutter.open_source_license }}",
    url='https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}',
    packages=find_packages(),
    install_requires=[],
    python_requires=">={{ cookiecutter.python_min_version }}",
    keywords='{{ cookiecutter.repo_name }}',
)

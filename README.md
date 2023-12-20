# funding-service-design-performance-tests
Performance Tests for the funding service design platform

NOTE: These tests no longer work due to data stores not being exposed in AWS. The ticket below will look into how to get these tests running again in AWS:
https://dluhcdigital.atlassian.net/browse/FS-3950

## Prerequisites
- locust

# Getting started

## Installation

Clone the repository

### Create a Virtual environment

    python3 -m venv .venv

### Enter the virtual environment

...either macOS using bash:

    source .venv/bin/activate

...or if on Windows using Command Prompt:

    .venv\Scripts\activate.bat

### Install dependencies
From the top-level directory enter the command to install pip and the dependencies of the project

    python3 -m pip install --upgrade pip && pip install -r requirements.txt

## How to use
Enter the virtual environment as described above, then:

python -m locust

# Locust config
There is a locust config file in the repository that manages how the tests are run and where they are run against. Change the values in there based on the needs of your performance testing. The host can be changed to point at a local running version of the application.

# Locust HTML report
A html report is produced at the end of a run and is stored in the root of the project. This shows the results of the tests.

# Adding a new performance test
To add a new performance test you need to add a py file to my_locustfiles containing the performance tests and then add an import to the base locustfile.py in the root of the directory.

# Linting
Black (https://black.readthedocs.io/en/stable/), flake8 (https://flake8.pycqa.org/en/latest/) and Bandit (https://bandit.readthedocs.io/en/latest/) have been added to staticly check the code

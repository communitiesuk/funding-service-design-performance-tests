# Funding Service Design Performance Tests
Performance Tests for the funding service design platform

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
Ther is a locust config file in the repository that manages how the tests are run and where they are run against. Change the values in there based on the needs oh your performance testing. The host can be changed to point at a local running version of the application.

# Locust HTML report
A html report is produced at the end of a run and is stored in the root of the project. This shows the results of the tests.


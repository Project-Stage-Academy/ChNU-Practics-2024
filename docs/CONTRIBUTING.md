# Contributing Guide

### Development setup

#### Repository Setup

As a first step, you'll need to clone the repository to your local machine:
```bash
git clone git@github.com:ivtka/Test-ChNU-Practics-2024.github
```

#### Dependency Setup

After you've cloned the repository, you'll need to create and activate a git-ignored virtual env (venv or .venv), e.g.:
```bash
python3 -m venv .venv
source .venv/bin/activate # or .venv\Scripts\activate on Windows
```

Then, you'll need to install the dependencies, we using pyproject.toml for this:
```bash
pip install pip --upgrade
pip install -e .[dev] # Install dev dependencies
```

#### Testing Setup

Run tests:
```bash
pytest
```

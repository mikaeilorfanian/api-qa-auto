# How to Use This Application
## Setup
This project works with Python 3.8.1., so make a Python virtual environment:
`python3.8 -m venv venv`
Then, activate this virtual env and install the required Python packages:
`pip install -r requirements.txt`
Finally, run the tests:
`pytest`
## Development
In addition to the previous steps, install packages that help with developing this project:
`pip install -r dev-requirements.txt`
To check if code follows pep8 guidelines, run
`flake8 --exclude=venv/* --max-line-length=110`
To automatically and uniformly format the code,
`black . --line-length=110 -S --exclude=venv/`
# Assumptions
The API under test makes no assumptions about the attributes of objects like `post`. In real systems, the backend usually checks to see if the provided object has all the required attributes and my tests take this into account.
Below are my specification of what attributes each object must have.
For example, if I try to edit a `post` object with a payload like {'random_attr': 'blah'}, then the backend should return an error such as "400 Bad Request".
## `post` Object Attributes
Create `post` calls must have all these attributes:
- title
- body
- userId

Edit `post` calls must have one or more of these attributes:
- title
- body
- userId
# Analysis and Potential Improvements
## Priorities
Because test code is software code, I like to apply software development best practices to my tests (DRY, KISS, etc.).
But, sometimes goals collide and so there should be a hierarchy of goals so we can decide what's more important.
In this case, the resolution of tests collides with the speed of execution: the finer the resolution, the slower the whole test suite runs.
By resolution I mean the scope of features a test case covers. For example, in the tests here I usually check the server response status code and the payload in the same test case. This means when a test fails someone unfamiliar with the test has to read the test code to understand exactly what is failing. But, if I split the test in two then the only thing you'd need is the name of the test.

## Test Runner
I've picked `pytest` because it's my go-to testing framework. But, depenending on who users of these API tests are another framework may be better fit.
For example, if for BDD tests there are frameworks like `cucumber` or `pytest-bdd`.

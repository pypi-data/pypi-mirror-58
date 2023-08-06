import setuptools
import io
import sys


license = 'Apache License Version 2'

with open("README.md", "r") as fh:
    long_description = fh.read()

install_require = []
with io.open('requirements.txt') as f:
    install_require = [l.strip() for l in f if not l.startswith('#')]


needs_pytest = set(['pytest', 'test']).intersection(sys.argv)
pytest_runner = ['pytest_runner'] if needs_pytest else []
test_require = []
with io.open('requirements-dev.txt') as f:
    test_require = [l.strip() for l in f if not l.startswith('#')]

packages = [
    'python_bootstrap',
]

setuptools.setup(
    name="python-bootstrap",
    version="0.0.4",
    author="Alex Shemshurenko",
    author_email="alexshe@wix.com",
    description="python-bootstrap package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/wix-private/hdc3/tree/master/apps-py/wixfra",
    packages=packages,
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    license=license,
    python_requires='>=3.7',
    tests_require=test_require,
    setup_requires=pytest_runner,
    install_requires=install_require
)




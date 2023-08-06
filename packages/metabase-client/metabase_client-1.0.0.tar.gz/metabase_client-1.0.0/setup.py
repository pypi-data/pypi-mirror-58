from pathlib import Path
from setuptools import find_packages, setup
from metabase_client import __version__ as VERSION
from pip._internal.req import parse_requirements


def _to_list(requires):
    return [str(ir.req) for ir in requires]


install_requires = _to_list(parse_requirements("requirements.txt", session=False))
tests_require = _to_list(parse_requirements("requirements-dev.txt", session=False))
setup(
    name="metabase_client",
    version=VERSION,
    description=(
        "A production-ready metabase client "
        "to spare you from handling HTTP requests directly"
    ),
    long_description=Path("README.md").read_text(),
    long_description_content_type="text/markdown",
    url="https://github.com/Onyo/metabase_client",
    author="Victor Martinez",
    author_email="vcrmartinez@gmail.com",
    license="MIT",
    classifiers=[
        "Intended Audience :: Developers",
        "Topic :: Utilities",
        "License :: Public Domain",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    keywords="metabase client api wrapper",
    packages=find_packages(exclude=["docs", "tests*"]),
    tests_require=tests_require,
    install_requires=install_requires,
    python_requires=">=3.5"
)

# Copyright (C) 2018 Łukasz Langa
from setuptools import setup
import sys
import os

assert sys.version_info >= (3, 6, 0), "black requires Python 3.6+"
from pathlib import Path  # noqa E402

CURRENT_DIR = Path(__file__).parent
sys.path.insert(0, str(CURRENT_DIR))  # for setuptools.build_meta


def get_long_description() -> str:
    readme_md = CURRENT_DIR / "README.md"
    with open(readme_md, encoding="utf8") as ld_file:
        return ld_file.read()


USE_MYPYC = False
# To compile with mypyc, a mypyc checkout must be present on the PYTHONPATH
if len(sys.argv) > 1 and sys.argv[1] == "--use-mypyc":
    sys.argv.pop(1)
    USE_MYPYC = True
if os.getenv("BLACK_USE_MYPYC", None) == "1":
    USE_MYPYC = True

if USE_MYPYC:
    mypyc_targets = [
        "black.py",
        "blib2to3/pytree.py",
        "blib2to3/pygram.py",
        "blib2to3/pgen2/parse.py",
        "blib2to3/pgen2/grammar.py",
        "blib2to3/pgen2/token.py",
        "blib2to3/pgen2/driver.py",
        "blib2to3/pgen2/pgen.py",
    ]

    from mypyc.build import mypycify

    opt_level = os.getenv("MYPYC_OPT_LEVEL", "3")
    ext_modules = mypycify(mypyc_targets, opt_level=opt_level)
else:
    ext_modules = []

setup(
    name="blacker",
    version="0.1.0",
    description="The uncompromising code formatter that respects PEP8.",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    keywords="automation formatter yapf autopep8 pyfmt gofmt rustfmt",
    author="Stefano Borini",
    author_email="stefano.borini@gmail.com",
    url="https://github.com/stefanoborini/blacker",
    license="MIT",
    py_modules=["black", "blackd", "_black_version"],
    ext_modules=ext_modules,
    packages=["blib2to3", "blib2to3.pgen2"],
    package_data={"blib2to3": ["*.txt"]},
    python_requires=">=3.6",
    zip_safe=False,
    install_requires=[
        "click>=6.5",
        "attrs>=18.1.0",
        "appdirs",
        "toml>=0.9.4",
        "typed-ast>=1.4.0",
        "regex!=2019.12.9",
        "pathspec>=0.6, <1",
        "dataclasses>=0.6; python_version < '3.7'",
        "typing_extensions>=3.7.4",
        "mypy_extensions>=0.4.3",
    ],
    extras_require={"d": ["aiohttp>=3.3.2", "aiohttp-cors"]},
    test_suite="tests.test_black",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Quality Assurance",
    ],
    entry_points={
        "console_scripts": [
            "black=black:patched_main",
            "blackd=blackd:patched_main [d]",
        ]
    },
)

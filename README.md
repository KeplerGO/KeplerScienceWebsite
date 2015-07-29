# Kepler Science Website
Website for the Kepler and K2 Science Center

## Usage

Type `make html` to build the website.

## Installation instructions

Before `make html` can be used, you need to ensure that the theme submodule is cloned into the repository
as follows:
```
cd themes
git submodule init
git submodule update
```

You will also need to ensure that `markdown` is installed (e.g. using `conda install markdown`).
If it's not, you will see the cryptic error message:
```
WARNING: No valid files found in content.
```
when running `make html`.

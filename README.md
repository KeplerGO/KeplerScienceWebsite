# Kepler Science Website

***A website for the Kepler/K2 Science Center
that doesn't suck™***

## Usage

Type `make html` to build a static HTML version of the website.

Type `made devserver` to start a development webserver on your local machine,
and the point your browser to `localhost:8000`.

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

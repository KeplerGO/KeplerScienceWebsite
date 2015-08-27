# Kepler Science Website

***A website for the Kepler/K2 Science Center
that doesn't suck™***

Preview: http://keplergo.github.io/KeplerScienceWebsite/

## Usage

* `make html` to build a static HTML version of the website.
* `make devserver` to start a development webserver on your local machine,
and the point your browser to `localhost:8000`.
* `make github` to deploy the website to the preview server.

## Installation instructions

You will need to ensure that `markdown` and `beautifulsoup4` are installed, e.g. using:
```
pip install markdown beautifulsoup4
```

If `markdown` is not installed, you may only see a cryptic warning message (e.g. `No valid files found in content.`) when running `make html`.


# Layout and html elements

The website's theme is based on the `flatly` bootstrap theme.
This means that you can use all the html elements and classes
which are demonstrated here:

    https://bootswatch.com/flatly/

and of course the `bootstrap` css classes can be used as well:

    http://getbootstrap.com/css

The content can be defined in MarkDown (md), ReStructuredText (rst),
or simply html.  There is a useful Markdown cheat sheet here:

    https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet

# Kepler Science Website

***A website for the Kepler/K2 Science Center
that doesn't suck™***

Live URL: http://keplerscience.arc.nasa.gov

Test URL: http://keplergo.github.io/KeplerScienceWebsite/


## Usage

* `make html` to build a static HTML version of the website.
* `make devserver` to start a development webserver on your local machine,
and the point your browser to `localhost:8000`.
* `make github` to deploy the website to the [Test URL](http://keplergo.github.io/KeplerScienceWebsite/).
* `make live` to deploy the website to the [Live URL](http://keplerscience.arc.nasa.gov).


## Installation instructions

You will need to ensure that `pelican`, `markdown` and `beautifulsoup4` are installed, e.g. using:
```
pip install pelican markdown beautifulsoup4
```

If `markdown` is not installed, you may get a very cryptic warning message (`"No valid files found in content."`) when running `make html`.


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


## Authors

Created by Thomas Barclay, Geert Barentsen, and Knicole Colón
for the Kepler/K2 Guest Observer Office at NASA Ames.

Created using the [Pelican package](getpelican.com) and the
[pelican-bootstrap3 theme](https://github.com/DandyDev/pelican-bootstrap3).

# Kepler/K2 Science Website [![DOI](https://zenodo.org/badge/10301/KeplerGO/KeplerScienceWebsite.svg)](https://zenodo.org/badge/latestdoi/10301/KeplerGO/KeplerScienceWebsite)

***The website for astronomers using data from NASA's Kepler/K2 mission.***

Live URL: http://keplerscience.arc.nasa.gov

Test URL: http://keplergo.github.io/KeplerScienceWebsite/


## Usage

* `make quick` for a quick build of pages that have changed.
* `make html` for full local build of the website including the frontpage.
* `make devserver` to start a development webserver on your local machine at `http://localhost:8000`, which will auto-compile a page when you make a change.
* `make github` to deploy the website to the [Test URL](http://keplergo.github.io/KeplerScienceWebsite/).
* `make live` to deploy the website to the [Live URL](http://keplerscience.arc.nasa.gov).

***Note***: `make quick` and `make devserver` both use agressive caching which allows the website to be built quickly, but causes the listing of news items on the front page to be empty.  Use `make html` for a full preview.

## Installation instructions

You will need to ensure that `pelican`, `markdown`, `beautifulsoup4`, and `ghp-import` are installed, e.g. using:
```
pip install pelican markdown beautifulsoup4 ghp-import
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


## Citation

You can cite the Kepler/K2 Science Website in your publications using its [DOI identifier](http://dx.doi.org/10.5281/zenodo.44393)
or using the following BibTex code:
```
@misc{tom_barclay_2016_44393,
  author       = {Tom Barclay and
                  Geert Barentsen and
                  Knicole Colon},
  title        = {KeplerScienceWebsite: 20160106},
  month        = jan,
  year         = 2016,
  doi          = {10.5281/zenodo.44393},
  url          = {http://dx.doi.org/10.5281/zenodo.44393}
}
```

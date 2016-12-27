# Kepler/K2 Science Website [![DOI](https://zenodo.org/badge/10301/KeplerGO/KeplerScienceWebsite.svg)](https://zenodo.org/badge/latestdoi/10301/KeplerGO/KeplerScienceWebsite)

***The website for astronomers using NASA's Kepler/K2 space telescope.***

Live URL: http://keplerscience.arc.nasa.gov

Test URL: http://keplergo.github.io/KeplerScienceWebsite/


### Quickstart

Kepler/K2's Science Center Website can be edited
by modifying the text files in the `content` sub-directory of this repository.
The essential commands for Kepler/K2 staff are:
```
$ git clone git@github.com:KeplerGO/KeplerScienceWebsite.git
$ cd KeplerScienceWebsite
$ make devserver
$ firefox http://localhost:8000

# make changes in the `content` sub-directory
# and preview them at http://localhost:8000

$ git add content/file-you-changed.md
$ git commit -m 'Explain your change'
$ git push
$ make live
```
In what follows these steps are explained in more detail.

## Detailed instructions for website editors

### 1. Cloning the website

The first step to start editing the website is to clone the website's main git repository
onto your local machine, e.g. using:
```
git clone git@github.com:KeplerGO/KeplerScienceWebsite.git
```
If you are going to make changes to the website,
you will need to ask the Kepler GO Office
to give your GitHub account write permissions to this repository.

### 2. Installing the dependencies

Compiling the website requires a working environment of either Python 2 or 3
to be installed, e.g. using the Anaconda Python Distribution.

You will also need to ensure that the `pelican`, `markdown`, `beautifulsoup4`,
and `ghp-import` Python packages are installed,
e.g. using the pip package installer:
```
$ pip install pelican markdown beautifulsoup4 ghp-import
```

Note that if `markdown` is not installed, you will only get a very cryptic warning message (`"No valid files found in content."`) when compiling the website below.

### 3. Editing the website

The website content is stored as a collection of text files
in the `content` sub-directory of this repository,
which is where all changes must be made.

Most of these content files are formatted using the *MarkDown* text format ([see cheat sheet here](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)),
which will automatically be compiled into HTML code using a template (to be explained in step 4).
You may also use HTML tags directly in the content files,
but this should only be necessary in a small number of cases where
very precise control over the layout is required.

Note that the website's template is based on the `flatly` bootstrap theme.
This means that you can use all the html elements and classes
which are demonstrated at [https://bootswatch.com/flatly](https://bootswatch.com/flatly).
In addition, you can also use all the standard [bootstrap css classes](http://getbootstrap.com/css).    

### 4. Compiling and previewing the website

After editing the content, you will usually want to preview your changes
by compiling the website into HTML format and viewing them in your browser.

The easiest way to do this is to type `make devserver` in the root of this
repository, which will start a local server in the background
that will serve the website at `http://localhost:8000`
(type this address in the url bar of your browser to preview the website).
The server is fast and will auto-compile every time you change a content file,
however note that it does not create a full
version of the front page:
you need to perform a full build using `make html` to preview the front page.

When you are done, you can kill the background server process using `make stopserver`.


### 5. Uploading the website

When you are happy with the changes made, you can make them live.
This is a 3-step process.

First, make sure you update the repository to include changes others have made
(and resolve any conflicts), e.g. using
```
$ git pull
```

Second, commit and push your own changes to the KeplerGO git repository
so they are available to others.
For example, if you changed the Helpdesk page, you would type:
```
$ git add content/pages/helpdesk.md`
$ git commit -m 'Changed the helpdesk e-mail address'
$ git push
```

Finally, you can now send the new HTML-compiled version of the website
to the [production webserver](http://keplerscience.arc.nasa.gov).
This is done by typing `make live`.
Note that it may take up to 5-10 minutes for changes to become visible after
`make live` completed, and occasionally you may need to ask the GO Office
to restart the task that keeps the webserver in sync.

If you are no quite ready to make your changes live,
but would to make them available at a test URL,
you can type `make github` which will deploy the website to the [Test URL](http://keplergo.github.io/KeplerScienceWebsite/).


## Makefile summary

The Makefile provides the following useful commands:
* `make html` to compile *all pages* and store them under `output/`.
* `make quick` to compile *only pages that have changed*.  This is faster than `make html` but will cause the front and news pages to be incomplete.
* `make devserver` to start a development webserver on your local machine at `http://localhost:8000`, which will auto-compile a page when you make a change. This too causes the frontpage to be empty unless you call `make html`.
* `make live` to send the compiled HTML files to the [production server](http://keplerscience.arc.nasa.gov) (this is done indirectly by updating the `live` branch).
* `make github` to send the compiled HTML files to the [development server](http://keplergo.github.io/KeplerScienceWebsite/).

Note: `make quick` and `make devserver` both use agressive caching which allows the website to be built quickly, but causes the listing of news items to be missing from the front page (`output/index.html`).  You need to call `make html` if you care about a preview of the front page. Calling `make github` or `make live` automatically triggers `make html`.


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

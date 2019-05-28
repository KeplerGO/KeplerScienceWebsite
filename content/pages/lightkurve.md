Title: Flux time series analysis in Python: Lightkurve v1.0
Save_as: lightkurve/index.html

[Lightkurve v1.0](https://docs.lightkurve.org) is a new Python package
which offers a user-friendly way to work with the pixel and lightcurve
products produced by the Kepler and TESS pipelines.
The package aims to lower the barrier for both students, astronomers,
and citizen scientists interested in analyzing Kepler and K2 data
by providing high-quality tools that are accompanied by tutorials.

Detailed installation instructions are available on the [documentation
webpages](https://docs.lightkurve.org).

The first version of lightkurve is accompanied by the following tutorials:

* [1. Introduction to Lightkurve](https://docs.lightkurve.org/tutorials):
    * [What are Target Pixel File objects?](https://docs.lightkurve.org/tutorials/01-target-pixel-files.html)
    * [What are Light Curve objects?](https://docs.lightkurve.org/tutorials/01-what-are-lightcurves.html)
    * [What are Light Curve File objects?](https://docs.lightkurve.org/tutorials/01-lightcurve-files.html)
    * [What is the Periodogram class?](https://docs.lightkurve.org/tutorials/01-using-the-periodogram-class.html)
* [2. Science examples:](https://docs.lightkurve.org/tutorials)
    * [How to recover a known planet in Kepler data?](https://docs.lightkurve.org/tutorials/02-recover-a-planet.html)
    * [How to recover the first TESS planet candidate with Lightkurve?](https://docs.lightkurve.org/tutorials/02-how-to-recover-the-first-tess-candidate.html)
    * [How to use lightkurve for asteroseismology?](https://docs.lightkurve.org/tutorials/02-how-to-use-lightkurve-for-asteroseismology.html)
    * [How to make a supernova lightcurve?](https://docs.lightkurve.org/tutorials/02-how-to-make-a-supernova-lightcurve.html)
* [3. Extracting light curves:](https://docs.lightkurve.org/tutorials)
    * [How to perform aperture photometry with custom apertures?](https://docs.lightkurve.org/tutorials/03-making-custom-apertures.html)
    * [How to perform PRF photometry?](https://docs.lightkurve.org/tutorials/03-how-to-use-prf-photometry.html)
    * [How to cut out Target Pixel Files from Kepler Superstamps or TESS FFIs?](https://docs.lightkurve.org/tutorials/03-cutting-out-tpfs-from-tess-ffis.html)
    * [How to save a LightCurve in FITS format?
](https://docs.lightkurve.org/tutorials/03-making-fits-files.html)
    * [How to combine lightcurves from different Kepler quarters?](https://docs.lightkurve.org/tutorials/03-appending-lightcurves.html)
* [4. Correcting systematics:](https://docs.lightkurve.org/tutorials/)
    * [Interactively inspecting Target Pixel Files and Lightcurves](https://docs.lightkurve.org/tutorials/04-interact-with-lightcurves-and-tpf.html)
    * [How to remove common systematics using basis vectors (CBVs)](https://docs.lightkurve.org/tutorials/04-removing-cbvs.html)
    * [How to remove K2 motion systematics with SFF?](https://docs.lightkurve.org/tutorials/04-how-to-detrend.html)
    * [How does the SFF method work?](https://docs.lightkurve.org/tutorials/04-replicate-vanderburg-2014-k2sff.html)
    * [Replicating Vanderburg & Johnson 2014 using lightkurve](https://docs.lightkurve.org/tutorials/04-replicate-vanderburg-2014-lightkurve.html)
    * [How to identify time-variable background noise (“rolling bands”)?](https://docs.lightkurve.org/tutorials/04-identify-rolling-band.html)

Additional video tutorials are available on our [YouTube channel](https://www.youtube.com/channel/UCJx_ls4mg5ms9q4Mv_2mYqg).

Lightkurve is an open source community project.
The development [takes place on GitHub](https://github.com/KeplerGO/lightkurve)
and everyone is [invited to contribute](https://docs.lightkurve.org/about/contributing.html).
It replaces the previous [PyKE suite of command-line tools](https://github.com/nasa/Kepler-PyKE).

The animation below illustrates some of the features provided by lightkurve:

<a href="https://docs.lightkurve.org"><img src="https://raw.githubusercontent.com/KeplerGO/lightkurve/master/docs/source/_static/images/lightkurve-teaser.gif" alt="lightkurve animation"></a>

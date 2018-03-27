Title: New Kepler data analysis tools and tutorials: Lightkurve v1.0
Date: 2018-03-18 12:00
Author: Geert Barentsen

[Lightkurve v1.0](http://lightkurve.keplerscience.org) is a new Python package
which offers a user-friendly way to work with the pixel and lightcurve
products produced by the Kepler and TESS pipelines.
The package aims to lower the barrier for both students, astronomers,
and citizen scientists interested in analyzing Kepler and K2 data
by providing high-quality tools that are accompanied by tutorials.

Detailed installation instructions are available on the documentation
webpages at [http://lightkurve.keplerscience.org](http://lightkurve.keplerscience.org).

The first version of lightkurve is accompanied by the following tutorials:

* [Introduction to lightkurve](http://lightkurve.keplerscience.org/tutorials/section1.html):
    * [What are Target Pixel File objects?](http://lightkurve.keplerscience.org/tutorials/1.02-target-pixel-files.html)
    * [What are Light Curve objects?](http://lightkurve.keplerscience.org/tutorials/1.03-what-are-lightcurves.html)
    * [What are Light Curve File objects?](http://lightkurve.keplerscience.org/tutorials/1.04-lightcurve-files.html)
* [Science with lightkurve:](http://lightkurve.keplerscience.org/tutorials/section2.html)
    * [How to recover a known planet in Kepler data](http://lightkurve.keplerscience.org/tutorials/2.02-recover-a-planet.html)
    * [How to combine lightcurves from different Kepler quarters](http://lightkurve.keplerscience.org/tutorials/2.03-appending-lightcurves.html)
    * [How to perform aperture photometry with custom apertures](http://lightkurve.keplerscience.org/tutorials/2.05-making-custom-apertures.html)
    * [How to cut out Target Pixel Files from Kepler Super Stamps or TESS FFIs](http://lightkurve.keplerscience.org/tutorials/cutting-out-tpfs-from-tess-ffis.html)
* [Systematics correction using lightkurve:](http://lightkurve.keplerscience.org/tutorials/section3.html)
    * [How to remove common systematics using basis vectors (CBVs)](http://lightkurve.keplerscience.org/tutorials/2.04-removing-cbvs.html)
    * [How to remove K2 motion systematics with SFF](http://lightkurve.keplerscience.org/tutorials/2.01-how-to-detrend.html)
    * [How does the SFF method work?](http://lightkurve.keplerscience.org/tutorials/motion-correction/replicate-vanderburg-2014-k2sff.html)
    * [Replicating Vanderburg & Johnson 2014 using lightkurve](http://lightkurve.keplerscience.org/tutorials/motion-correction/replicate-vanderburg-2014-lightkurve.html)


Additional video tutorials are available on our [YouTube channel](https://www.youtube.com/channel/UCJx_ls4mg5ms9q4Mv_2mYqg).

Lightkurve is an open source community project owned by the authors.
The development [takes place on GitHub](https://github.com/KeplerGO/lightkurve)
and everyone is [invited to contribute](http://lightkurve.keplerscience.org/contributing.html).
It replaces the existing [PyKE](http://pyke.keplerscience.org) suite of command-line tools, which will slowly be migrated to become the command-line interface for the lightkurve package.

The animation below illustrates some of the features provided by lightkurve:

<a href="http://lightkurve.keplerscience.org/_images/lightkurve-teaser.gif"><img src="http://lightkurve.keplerscience.org/_images/lightkurve-teaser.gif" alt="lightkurve animation"></a>

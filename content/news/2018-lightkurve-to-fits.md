Title: New in lightkurve: saving a lightcurve as a FITS file
Date: 2018-06-13 14:00
Author: Geert Barentsen

The new [lightkurve Python package](http://lightkurve.keplerscience.org)
for Kepler and K2 data analysis, which we [first announced in March](new-kepler-data-analysis-tools-and-tutorials-lightkurve-v10.html),
contains a new feature: `to_fits()`.

The feature solves a common use case for authors of custom lightcurves
who wish to share their lightcurves with collaborators or contribute
them to MAST as a [High Level Science Product](https://archive.stsci.edu/k2/hlsps.html) (HLSP).
Lightkurve now provides a `to_fits()` method on every `LightCurve` object
which enables a lightcurve to be saved as a FITS file in the standard format
adopted by the Kepler and TESS pipelines.

For example, this snippet of code will create a lightcurve file called `output.fits`:

    :::python
    from lightkurve import LightCurve
    llc = LightCurve(time=[1, 2, 3], flux=[1.02, 0.98, 1.01])
    lc.to_fits('output.fits')

A [more comprehensive tutorial](http://lightkurve.keplerscience.org/tutorials/2.08-making-fits-files.html),
which also explains how to include the custom header keywords required by MAST,
is available in the [lightkurve documentation](http://lightkurve.keplerscience.org).

Note that you will need to upgrade your installation of `lightkurve` to the latest version
(v1.0b8) to use this feature. This can be done via the command line as follows:

```
$ pip install lightkurve --upgrade
```

We invite you to try out `to_fits()` today and let us know if you have any problems by [opening a GitHub issue](https://github.com/KeplerGO/lightkurve/issues/new).

Title: New in Lightkurve: the Periodogram class
Date: 2018-10-30 09:00
Author: Christina Hedges

This month in [Lightkurve](http://lightkurve.keplerscience.org/) we have added a Periodogram class, which will help you easily create Lomb-Scargle periodograms from Lightkurve objects. Periodograms can be used to find stellar rotation rates, or the oscillation and pulsation frequencies of stars. They are commonly used in asteroseismology to identify oscillation modes, which can be used to calculate the density of host stars. Below is a quick demonstration of how you can easily obtain the data from mast, create a periodogram and find the oscillation modes of a red giant star in just a few lines.

<p>
<img class="img-responsive" src="images/news/periodogram.gif" alt="New Lightkurve periodogram class" style="max-width:800px;">
</p>


### Usage
To create a periodogram from a light curve you can use the following syntax

```python
from lightkurve import search_lightcurvefile
lcf = search_lightcurvefile('201691589').download()
lc =lcf.PDCSAP_FLUX.remove_nans()
pg = lc.to_periodogram()
```

Periodograms have several useful functions including plotting, smoothing and binning. You can interact with them much the same way you interact with other lightkurve objects.  For example you can use the following syntax to plot a smoothed Lomb-Scargle periodogram.

```python
pg.smooth().plot()
```

The full documentation of the periodogram class is available [here](https://docs.lightkurve.org/api/lightkurve.lightcurve.LightCurve.html#lightkurve.lightcurve.LightCurve.to_periodogram).


You will need to upgrade your installation of `lightkurve` to the latest version (v1.0b17) for this to work. This can be done via the command line as follows:

```
$ pip install lightkurve --upgrade
```

Please consult the [Lightkurve documentation](http://lightkurve.keplerscience.org) for more information.
The documentation includes [a tutorial on the periodogram class](http://lightkurve.keplerscience.org/tutorials/1.06-using-the-periodogram-class.html).

Title: New in Lightkurve: the Periodogram class
Date: 2018-10-29 19:00
Author: Christina Hedges

This month in [Lightkurve](https://docs.lightkurve.org), we have added a Periodogram class, which provides a quick and easy way to create Lomb-Scargle periodograms from LightCurve objects.

Periodograms can be used to find stellar rotation rates, or the oscillation and pulsation frequencies of stars. They are commonly used in asteroseismology to identify oscillation modes, which can be used to calculate the density of stars. 

Below is a quick demonstration of how you can easily obtain the data from the data archive at MAST, create a periodogram, and inspect the oscillation modes of a red giant star in just three lines of Python.

<p>
<img class="img-responsive" src="images/news/toperiodogram.gif" alt="New Lightkurve periodogram class" style="max-width:800px;">
</p>


### Usage
To download a light curve from MAST and create a Periodogram object named `pg`, you can use the following syntax:

```python
from lightkurve import search_lightcurvefile
lcf = search_lightcurvefile('201691589').download()
lc = lcf.PDCSAP_FLUX.remove_nans()
pg = lc.to_periodogram()
```

Periodograms have several useful functions including plotting, smoothing, and binning. You can interact with them much the same way you interact with other Lightkurve objects.  For example you can use the following syntax to plot a smoothed Lomb-Scargle periodogram.

```python
pg.smooth().plot()
```

The full documentation of the periodogram feature [is available here](https://docs.lightkurve.org/api/lightkurve.lightcurve.LightCurve.html#lightkurve.lightcurve.LightCurve.to_periodogram).  This new feature is the work of Kepler visiting scientist [Oliver Hall](https://twitter.com/asteronomer) and summer intern Johnny Zhang.


You will need to upgrade your installation of Lightkurve to the latest version (v1.0b21) for this to work. This can be done via the command line as follows:

```
$ pip install lightkurve --upgrade
```

Please consult the [Lightkurve documentation](https://docs.lightkurve.org) for more information.
The documentation includes [a new tutorial on the Periodogram class](https://docs.lightkurve.org/tutorials/1.06-using-the-periodogram-class.html).

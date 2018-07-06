Title: New in lightkurve: identifying time-variable background noise
Date: 2018-07-04 10:00
Author: Geert Barentsen

The new [lightkurve](http://lightkurve.keplerscience.org) open source Python package
for Kepler and K2 data analysis, which we [first announced in March](new-kepler-data-analysis-tools-and-tutorials-lightkurve-v10.html),
contains a [new data analysis tutorial](http://lightkurve.keplerscience.org/tutorials/2.06-identify-rolling-band.html) which demonstrates how
custom aperture photometry can be used to check your target
for the presence of time-variable background signals.

The background flux level of Kepler pixel data is not static.
In particular, certain CCD channels occasionally experience the 'rolling band' effect,
where the background has a strong time varying component of a 'band' moving up the detector.
You can read more about rolling band in the [Kepler Instrument Handbook](https://archive.stsci.edu/kepler/manuals/KSCI-19033-001.pdf).
An example of the rolling band artifact is shown in the video below.
You can see the band move through the superstamp at the 2 second mark,
leaving the bottom of the screen at the 6 second mark.

The rolling band artifact is small, up to about 20 counts per pixel.
However, this can add up for large apertures containing many pixels or for faint, quiet targets.

Rolling band can often add spurious signals into your data which look like real astrophysical variability. 
The best way to spot rolling band is to vary your aperture size
or make lightcurves of nearby background pixels.
If the signal strength increases as you increase the number of background pixels in the aperture, the effect is likely to be an additive background component.
Our [new data analysis tutorial](http://lightkurve.keplerscience.org/tutorials/2.06-identify-rolling-band.html) demonstrates how lightkurve can be used
to investigate the presence of the noise in your target of choice.

<p style="max-width: 600px;">
<img src="images/news/rollingband.gif"><br>
<i>Animation of the superstamp obtained for the dwarf galaxy IC1613 during K2 Campaign 8.
Around the superstamp you can see smaller Target Pixel Files (TPFs) covering single objects of interest.
You can see a dark band move from the top of the superstamp to the bottom during the movie. This dark band and surrounding artifacts are the so-called "rolling bands".
</i>
</p>


Title: New in lightkurve: interactively select pixel mask
Date: 2018-09-24 09:00
Author: Michael Gully-Santiago

The lifecycle of Kepler data analysis begins with the establishment of which pixels your target of interest occupied, and to what extent artifacts degraded those pixels.  The Kepler/K2 in-house toolkit, [lightkurve](http://lightkurve.keplerscience.org/), offers a new mechanism to witness---in real time---the differential impact of pixel selection on the delivered lightcurve quality.  

The new tool extends lightkurve's existing `.interact()` functionality [introduced in May 2018](https://keplerscience.arc.nasa.gov/new-in-lightkurve-inspecting-pixel-data-using-tpfinteract.html).  What's new is the ability to click on individual pixels in the target pixel file postage stamp window.  The lightcurve on the lefthand side of the plot instantaneously re-renders a lightcurve including all the demarcated pixels.  A user may hold `shift` and mouse-click to select many pixels in sequence, or may click and drag a box to select a rectangular box of pixels.  Pixels may be *de*-selected by clicking the offending pixel while holding shift.

<img class="img-responsive" src="images/news/20180924_interact_HLTau.gif" alt="New Lightkurve tpf.interact() tool" style="margin:2em;">

The seemingly mundane choice of aperture photometry pixels embodies a deep existential phenomenon in statistics, the so-called [bias-variance tradeoff](https://en.wikipedia.org/wiki/Bias%E2%80%93variance_tradeoff).  On one hand, we desire to collect all of a target's photons with a large aperture: more signal is good.  On the other hand, we wish to limit the penalty of adding detector read noise: more noise is bad.  The balance is struck by selecting a problem-specific *optimal aperture mask*.  [The Kepler Pipeline](https://keplerscience.arc.nasa.gov/pipeline.html) provides a mask optimized for finding planets in the near-motion-free Kepler prime data.  It is this ostensibly optimal mask that appears in `.interact()` by default.

The choice of mask became even more problem-specific in the K2 mission, with its heightened spacecraft-induced image motion, and its variegated portfolio of science projects.  Apertures that were acceptable in planet searches of Kepler prime mission will likely underperform in K2.  The interact tool could profoundly help K2 users diagnose and mitigate these K2-specific instrumental artifacts.

You will need two extra packages in order to run interact:

[bokeh](https://bokeh.pydata.org/en/latest/) provides the interactive javascript-based graphics.  
[Jupyter](http://jupyter.org/) is currently the only supported environment for interact.

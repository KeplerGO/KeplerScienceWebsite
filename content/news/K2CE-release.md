Title: Open source release of Kepler/K2 Cadence Events (K2CE) tool
Date: 2019-10-23 15:30
Author: Jeff Coughlin

A new tool for working with short- and long-cadence lightcurves has been released to the public under the NASA Open Source License,
and made available for download via the NASA GitHub repository at [https://github.com/nasa/K2CE](https://github.com/nasa/K2CE).

Kepler/K2 Cadence Events (K2CE) is a Python data visualization and manipulation tool for astronomers to identify and remove cadences (observations) associated with problematic thruster events, thus producing cleaner light curves.  K2CE was designed to work with standard Kepler or K2 data products: long-cadence (30 min) and short-cadence (1 min) light curve files and long-cadence and short-cadence target pixel files.  The tool also works with light curve files and target pixel files from the TESS mission.

K2CE can be used as a stand-alone command-line application, or as part of a Python script.  Documentation and a demo Jupyter notebook is included.  It should be especially useful to those working with short-cadence lightcurves produced as a result of the [K2 global uniform reprocessing effort](k2-uniform-global-reprocessing-underway.html).

Questions can be directed to the author, Kenneth Mighell, at <kenneth.j.mighell@nasa.gov>.

<br>

<div class="thumbnail" style="width: 90%; display: inline-block;">
<div class="caption">
<i>A phased K2 short-cadence lightcurve of an RR Lyr-type variable, before and after being run through K2CE.</i>
</div>
<img style="text-align: center" src="images/news/k2ce-rr-lyr.png" width="100%" align="center"  class="img-responsive">
</div>

<div class="thumbnail" style="width: 90%; display: inline-block;">
<div class="caption">
<i>Example visualization of a short-cadence K2 lightcurve with problematic cadences identified.</i>
</div>
<img style="text-align: center" src="images/news/k2ce-fig.png" width="100%" align="center"  class="img-responsive">
</div>

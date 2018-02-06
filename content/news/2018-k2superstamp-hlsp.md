Title: New K2 superstamp mosaic FITS files available at MAST
Date: 2018-02-05 14:00
Author: Ann Marie Cody

The K2 Guest Observer Office is excited to announce a new
[High Level Science Product (HLSP)](https://archive.stsci.edu/k2/hlsps.html)
available at the MAST archive.
The HLSP – called **[K2Superstamp](https://archive.stsci.edu/prepds/k2superstamp/)** – consists of a series of FITS images for 
four open star clusters observed by K2 using so-called "superstamp" pixel masks:

* **M35**: the ~100 Myr old open cluster observed during Campaign 0.
* **M67**: the solar-age, solar-metallicity benchmark cluster observed during C5.
* **Ruprecht 147**: the ~3 Gyr-old open cluster observed during C7.
* **The Lagoon Nebula (M8)**: the high-mass star-forming region observed during C9.

While the data for these regions have long been served on MAST,
until now they were only available as a disconnected set of smaller Target Pixel Files (TPFs) because the spacecraft stored these observations in small chunks.
As a result, these regions have hitherto been ignored by many lightcurve and planet search pipelines.
With [this new release](https://archive.stsci.edu/prepds/k2superstamp/),
we have stitched these TPFs together into spatially contiguous FITS images
(one per cadence) to make their scientific analysis easier.
In addition, each image has been fit with an accurate WCS solution
so that you may locate any object of interest via its right ascension and declination.
The process of stitching and astrometric calibration is described in a
[companion RNAAS article](http://iopscience.iop.org/article/10.3847/2515-5172/aaac30/meta).

The release of these superstamp FITS images makes the analysis of the open star clusters observed by K2 much easier.
In the future, we expect to release similar products for other superstamp regions observed by K2, including galaxies and globular clusters.

<a href="https://archive.stsci.edu/prepds/k2superstamp/"><img src="images/K2Superstamp.jpg" class="img-responsive" alt="K2 Superstamp regions"></a>

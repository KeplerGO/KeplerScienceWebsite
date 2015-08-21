Title: Photometric performance

[TOC]


### Introduction

Based upon a series of 5-30 day engineering tests carried out between Oct 2013 and Jan 2014, autonomous and programmed spacecraft operations were refined in order to maximize thruster-assisted two-wheel performance from K2. As of Dec 2013, two-wheel testing has demonstrated all of the functionality required for the K2 mission:  pointing and controlling the telescope, aligning the roll angle with the solar balance ridge, tweaking roll with thrusters as required, and pointing the High-Gain Antenna to earth for Ka-Band downlink.  Data were collected to analyze K2 mission performance, confirming the operations concept. The fuel burn rate has been measured for all operational modes for K2.

Field acquisition capabilities and correctional maneuvers for solar-induced drift are being refined in order to minimize the number of pixels required for individual target masks and consequently maximize the number of targets available to each campaign. Photometric precision is dependent primarily upon motion of the spacecraft boresight on jitter timescales shorter than an exposure length and solar-induced drift timescales longer than an exposure. The information below is a photometry status report from a 6-day engineering sequence collected during Dec 2013. 


### Field acquisition

Pre-planned boresight pointings are currently being acquired to a precision of 15 arcsec on the focal plane. Further improvements in absolute pointing using an iterative approach to field acquisition were tested in Jan 2014.


### Reaction wheel jitter

During engineering tests between Oct-Dec 2013, the spacecraft collected data in a coarse-point mode. The measured Full-Width Half Maximum of the coarse-point K2 Point-Spread Function is a measure of spacecraft jitter and is within 5% of the fine-point Kepler Point-Spread Function across the entire field-of-view. The figure below provides a fit of the Kepler fine-point Point-Spread Function to a K2 coarse-point target close to the spacecraft boresight. From top-left to bottom-right: a 30 min observation of a 12th magnitude K2 star, the best-fitting Kepler PSF model, the best-fit model binned over detector pixels, and the fit residual. Spacecraft jitter during two-wheel operation is therefore generally only a few percent larger than the three-wheel Kepler mission and is not a major concern for K2 photometric precision. 

<a href="http://keplerscience.arc.nasa.gov/K2/images/Dec2013PRF.png"><img src="http://keplerscience.arc.nasa.gov/K2/images/Dec2013PRF.png" style="max-width: 640px;"></a>


### Solar pressure-induced drift

Low-frequency motion due to solar pressure and subsequent thruster firings causes targets to drift across detector pixels and is the dominant factor in photometric precision after photon statistics. The frequency of reaction wheel momentum resaturations and thruster-controlled pointing tweaks will be tuned to trade photometric precision with pixel mask size and fuel consumption. During the Dec 2013 test, resaturations occurred on a 48-hour cycle and pointing tweaks every 12 hours. Thruster firings kept targets localized to within three pixels across the duration of the 6-day test run. For the purposes of providing a photometric precision measure that can be compared with the Kepler mission, an uncrowded 12th magnitude target is selected for showcasing and its sensitivity to a 6-hour duration planet transit is measured. After defining a pixel mask to contain the 3-pixel focal-plane drift of the target, motion systematics and stellar astrophysics are removed from the subsequently derived Simple Aperture Photometry time series with a 48-hour Savitzky-Golay filter (a standard method to prepare stellar light curves for transit searches). The subsequent median 6-hr photometric precision of a 12th mag target is 87 ppm (94 &micro;mag). This is within a factor 4 of the fine-point Kepler mission precision for quiet G dwarfs. The blue shaded regions represent times associated with reaction wheel resaturations and engineering tests. The data collected during these intervals were clipped from the time-series. 

<a href="http://keplerscience.arc.nasa.gov/K2/images/Dec2013SAP.png"><img src="http://keplerscience.arc.nasa.gov/K2/images/Dec2013SAP.png" style="max-width: 640px;"></a>

A major activity during ongoing testing is the measurement of thermal alignment changes between star trackers and boresight throughout a campaign. This calibration will allow more precise pointing control, smaller pixel masks and consequently more targets per campaign. There remains room for further improvements in photometric precision by optimizing the frequency of pointing resets and acquiring guide stars for fine-guidance tracking. These capabilities are being tested and optimized in early 2014 before science operations begin. Nevertheless, the photometric capabilities already attained in coarse point provide the community with a powerful scientific observatory.


### Fine-point photometric precision

Fine-point operations were achieved and maintained during the Feb 2014 engineering test. The plot below compares a 12th magnitude target observed during the Dec 2013 coarse-point operations (left) with a 12th magnitude target collected in fine-point (right). The spacecraft pointed in different directions for these two tests and therefore this is a not a like-for-like comparison - the nature and intrinsic variability of both targets is unknown. Nevertheless, in this example, fine-point increases the photometric precision relative to coarse-point by a factor 2. In both plots, the blue curve is 30-min cadence data, the red diamonds are the same data, binned to 6 hours. The dashed line represents the 1-&sigma; standard deviation of the 30-min data. The median 6-hr photometric precision of the 12th magnitude coarse-point target is 82 ppm, while the same measure for the fine-point target is 44 ppm.

<a href="http://keplerscience.arc.nasa.gov/K2/images/Feb2014SAP.png"><img src="http://keplerscience.arc.nasa.gov/K2/images/Feb2014SAP.png" style="max-width: 640px;"></a>

The following plot provides an ensemble comparison of Kepler three-wheel fine-point precision (red), K2 two-wheel coarse-point precision (green) and K2 two-wheel fine-point precision (blue). The red lines are carefully-selected quiet G dwarfs, falling upon arbitrary modules of the Kepler detector. The green points are stars of unknown spectral type and intrinsic variability and therefore the scatter around a power law fit (dashed line) is considerably larger than the Kepler sample. The K2 fine-point ensemble has been extracted from pixels using apertures optimized for signal-to-noise, and systematic, motion-related structure has been calculated and subtracted using singular value deconvolution across the ensemble of light curves. The large scatter demonstrates that the engineering targets display a range of intrinsic astrophysical variability, however the noise floor suggests that K2 fine-point data is a significant improvement upon coarse-point quality and approaches the photometric precision of the Kepler archive. 

<a href="http://keplerscience.arc.nasa.gov/K2/images/Feb2014Precision.png"><img src="http://keplerscience.arc.nasa.gov/K2/images/Feb2014Precision.png" style="max-width: 640px;"></a>

The series of plots below contain the same 11th magnitude target, observed during the Feb 2014 fine-point observations. In each a Mandel-Agol planet transit model has been injected, assuming the star is solar-size and the planet has an orbital period of 1.5 days. In each curve four transits have therefore been injected over a 9-day time series and folded upon the orbital period. Such Jupiters (top-left), Neptunes (top-right) and Super-Earths (bottom-left) will be readily detected by current planet searching algorithms. The 6-hr 5-&sigma; Earth-like transit depth (bottom-right) will be challenging, just as it is in the Kepler time-series, but will becoming increasingly significant with more recorded transits.

<a href="http://keplerscience.arc.nasa.gov/K2/images/Feb2014Injection.png"><img src="http://keplerscience.arc.nasa.gov/K2/images/Feb2014Injection.png" style="max-width: 640px;"></a>

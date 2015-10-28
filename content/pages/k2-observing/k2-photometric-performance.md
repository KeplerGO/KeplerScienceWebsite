Title: K2 technical information
Save_as: k2-photometric-performance.html

[TOC]



## Photometric performance

The photometric precision is dependent primarily 
upon motion of the spacecraft boresight on jitter timescales 
shorter than an exposure length 
and solar-induced drift timescales longer than an exposure. 

### Reaction wheel jitter

During engineering tests between Oct-Dec 2013, 
the spacecraft collected data in a coarse-point mode. 
The measured Full-Width Half Maximum of the coarse-point 
K2 Point-Spread Function is a measure of spacecraft jitter 
and is within 5% of the fine-point Kepler Point-Spread Function 
across the entire field-of-view. 

The figure below provides a fit of the Kepler fine-point Point-Spread Function to a K2 coarse-point target close to the spacecraft boresight. 
From top-left to bottom-right: a 30 min observation of a 12th magnitude K2 star, the best-fitting Kepler PSF model, the best-fit model binned over detector pixels, and the fit residual. Spacecraft jitter during two-wheel operation is therefore generally only a few percent larger than the three-wheel Kepler mission and is not a major concern for K2 photometric precision. 

<br/>

<a href="http://keplerscience.arc.nasa.gov/K2/images/Dec2013PRF.png"><img src="http://keplerscience.arc.nasa.gov/K2/images/Dec2013PRF.png" style="max-width: 640px;"></a>

<br/>


### Solar pressure-induced drift

Low-frequency motion due to solar pressure and subsequent thruster firings cause targets to drift across detector pixels and is the dominant factor in photometric precision after photon statistics. The frequency of reaction wheel momentum resaturations and thruster-controlled pointing tweaks will be tuned to trade photometric precision with pixel mask size and fuel consumption. During the Dec 2013 test, resaturations occurred on a 48-hour cycle and pointing tweaks every 12 hours. Thruster firings kept targets localized to within three pixels across the duration of the 6-day test run. For the purposes of providing a photometric precision measure that can be compared with the Kepler mission, an uncrowded 12th magnitude target is selected for showcasing and its sensitivity to a 6-hour duration planet transit is measured. After defining a pixel mask to contain the 3-pixel focal-plane drift of the target, motion systematics and stellar astrophysics are removed from the subsequently derived Simple Aperture Photometry time series with a 48-hour Savitzky-Golay filter (a standard method to prepare stellar light curves for transit searches). The subsequent median 6-hr photometric precision of a 12th mag target is 87 ppm (94 &micro;mag). This is within a factor of 4 of the fine-point Kepler mission precision for quiet G dwarfs. The blue shaded regions represent times associated with reaction wheel resaturations and engineering tests. The data collected during these intervals were clipped from the time-series. 

<br/>

<a href="http://keplerscience.arc.nasa.gov/K2/images/Dec2013SAP.png"><img src="http://keplerscience.arc.nasa.gov/K2/images/Dec2013SAP.png" style="max-width: 640px;"></a>

<br/>

A major activity during ongoing testing is the measurement of thermal alignment changes between star trackers and boresight throughout a campaign. This calibration will allow more precise pointing control, smaller pixel masks and consequently more targets per Campaign. There remains room for further improvements in photometric precision by optimizing the frequency of pointing resets and acquiring guide stars for fine-guidance tracking. As described in the following section, pointing and guiding optimization has allowed K2 to achieve photometric precisions that rival the Kepler mission.


### Fine-point photometric precision

The following plot below demonstrates the fine-point photometric precision achieved by K2 in Campaign 3 (orange) compared to
Kepler in Quarter 10 (blue) [credit: Andrew Vanderburg, created using the method described in
[Vanderburg (2014)](http://adsabs.harvard.edu/abs/2014arXiv1412.1827V)
and
[Vanderburg & Johnson (2014)](http://adsabs.harvard.edu/abs/2014PASP..126..948V)]. Giant
stars were excluded from the computation of the combined differential
photometric precision (CDPP) to provide a comparison against
photometrically-quiet dwarf stars.  Note that the data from Campaign 3
was taken after applying an increase in pointing control bandwidth, so
data in earlier Campaigns will provide slightly poorer photometric precision.  

<br/>

<img class="img-responsive" style="max-width: 640px;" src="images/k2-kpcdpp-201508.png">

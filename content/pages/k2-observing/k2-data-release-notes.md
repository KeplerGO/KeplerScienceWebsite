Title: K2 Data Release Notes
Save_as: k2-data-release-notes.html

[TOC]

This page details the key features of the K2 data releases,
including a description of technical issues relevant to
the scientific exploitation of the data.

<hr>

# Campaign 4

## At a glance

***Pointing***

* RA: 59.0759116 degrees
* Dec: 18.6605794 degrees
* Roll: -167.6992793 degrees

***Targets***

* 15,853 in long cadence (LC)
* 122 in short cadence (SC)
* Several custom targets (see below)

***Full Frame Images (FFI)***

* <a href="https://archive.stsci.edu/pub/k2/ffi/ktwo2015051131033-c04_ffi-cal.fits">ktwo2015051131033-c04_ffi-cal.fits</a> (389 MB)
* <a href="https://archive.stsci.edu/pub/k2/ffi/ktwo2015092174954-c04_ffi-cal.fits">ktwo2015092174954-c04_ffi-cal.fits</a> (389 MB)

***First cadence***

* Time: 2015-02-08 06:50:09.177 UTC
* Long Cadence Number: 103744
* Short Cadence Number: 2976430

***Last cadence***

* Time: 2015-04-20 04:32:47.045 UTC
* Long Cadence Number: 107213
* Short Cadence Number: 3078009

<div class="thumbnail" style="width: 68%;">
    <div class="caption">
        <i>Figure: Schematic of Kepler's C4 field-of-view with selected targets shown with purple dots.</i>
    </div>
    <a href="images/campaign_selected/C4_selected.png">
        <img src="images/campaign_selected/C4_selected.png" class="img-responsive" alt="C4 field-of-view with selected targets">
    </a>
</div>

<div class="thumbnail" style="width: 68%;">
    <div class="caption">
        <i>Figure: Distribution of the Kepler magnitudes of observed targets in C4. All targets are chosen by Guest Observers. The bimodality is due to how the largest Guest Observer programs were selected for C4.</i>
    </div>
    <a href="images/release-notes/c4/C4_lcDistribution.png">
        <img src="images/release-notes/c4/C4_lcDistribution.png" class="img-responsive" alt="Distribution of the Kepler magnitudes of observed targets in C4.">
    </a>
</div>


## Features and events

<br>
***Pleiades and Hyades***

One Director's Discretionary Target program (GO4901, PI:White) was approved in Campaign 4 which observes the nine 3–5 mag B-stars and red giants in the Pleiades and Hyades open clusters. The targets were observed using circular pixel masks (20 pixels in radius) that cover the wings of the PSF but not the entire saturation bleed.

The two stars in the Hyades are γ Tau and δ1 Tau. The seven stars in the Pleiades are: Alcyone (η Tau), Atlas (27 Tau), Electra (17 Tau), Maia (20 Tau), Merope (23 Tau), Taygeta (19 Tau) and Pleione (28 Tau). These stars are all listed in the EPIC; however, their data are listed by custom aperture number at the MAST in the range 200007765--200007773.

<div class="thumbnail" style="width: 68%;">
    <div class="caption">
        <i>Figure: The Pleiades open cluster as seen on module 15 of the K2 C4 FFI.</i>
    </div>
    <a href="images/release-notes/c4/c4-pleiades-k2-1579.png">
        <img src="images/release-notes/c4/c4-pleiades-k2-1579.png" class="img-responsive" alt="The Pleiades open cluster as seen on module 15 of the K2 C4 FFI.">
    </a>
</div>

<br>
***Trans-Neptunian Object***

The Trans-Neptunian Object 2002 KY14 was observed in Campaign 4 by creating 1340 masks that cover the path of the TNO. The custom aperture numbers range from 200006425 to 200007764. These observations were taken as part of Guest Observer program GO4110 (PI:Schwamb).

<br>
***Background Residuals near Pleiades***

Background removal for channels near the Pleiades has larger than normal residuals. These large residuals occur on mod.outs 10.3 and 15.1 through 15.4 due to the background on these channels being dominated by dust clouds near the Pleiades. The rich spatial structure of the Pleiades' dust clouds is poorly captured by the low order (≤ 4) polynomial model used to fit the background flux, with the best fit for these channels being given by a constant. This fit is done for every cadence, and the result is higher than normal background residuals, with residuals as large as 7 times the standard deviation of the background pixel values. (Normal residuals are typically less than the background standard deviation.)

We recommend caution when using light curves or the background model on these channels. Note that the FLUX column of the target pixel files contains calibrated pixels with the background subtracted. The amount of background that was subtracted per pixel can be found in the <a href="http://keplerscience.arc.nasa.gov/K2/pipelineReleaseNotes.shtml#dr5">FLUX_BKG column</a> and restored, if desired.

Local background estimates per star may produce higher-quality results. The change in the constant background level on these channels over time is in family with the median background change on other channels

<br>
***Lightcurves Created with Non-Optimal Apertures***

Due to an incompatibility between K2 roll motion and the determination of photometric optimal apertures, some light curves may be based on apertures that are too small and therefore have more noise than necessary. In particular, there are 887 stellar targets that are particularly suspect; they are listed <a href="http://keplerscience.arc.nasa.gov/K2/K2drn/C4/C4_reduced_ap_targets.txt">here</a>. The brighter targets in this set may have correct optimal apertures, but stars with Kp > 13 have been shown to have lower photometric precision than non-suspect stars of similar brightness.

<br>
***Stars Show Lower Than Expected Flux***

The comparison of the measured flux to the flux based on their Kepler magnitudes in the EPIC catalog shows that ≈3,752 stars (23.8% of all stellar targets) are too bright by about a magnitude. The EPIC catalog field Kepflag gives the provenance of the Kepler magnitude estimate by listing the catalog magnitudes used to estimate the Kepler magnitude. Stars with Kepflag = “JHK” or “J” have Kepler magnitudes that are generally overestimated. These stars appear at all magnitudes, but predominantly have EPIC Kepler magnitudes dimmer than 14. The optimal apertures used to generate light curves for these “JHK” or “J” targets may be larger than optimal, reducing their photometric precision.

<div class="thumbnail" style="width: 100%;">
    <div class="caption">
        <i>Figure: histograms of the relative flux for C4 stellar targets. Left: the relative flux distribution of stellar targets with EPIC Kepflag values of “gri” or “BV”, showing that their measured flux is consistent with the expected flux. Right: the relative flux distribution of stellar targets with EPIC Kepflag values of “JHK” or “J”, showing that the observed flux is less than half the expected flux.</i>
    </div>
    <a href="images/release-notes/c4/lowfluxJband.png">
        <img src="images/release-notes/c4/lowfluxJband.png" class="img-responsive" alt="histograms of the relative flux for C4 stellar targets">
    </a>
</div>

<br>
***Several Stars Show Higher Than Expected Flux***

There is a group of target stars whose measured flux is more than twice that expected from their EPIC Kepler magnitudes. The figure below shows that these stars fall into spatial groups that are aligned with RA and Dec, rather than focal plane coordinates, strongly indicating that the cause of this anomaly is catalog error. The source of this error is presently unknown and is not correlated with Kepflag values. The optimal apertures used to generate light curves for these targets may be smaller than optimal, reducing their photometric precision.

<div class="thumbnail" style="width: 68%;">
    <div class="caption">
        <i>Figure: all C4 target stars plotted in celestial coordinates, colored by their Kepler magnitude inferred from their observed flux minus their Kepler magnitude from the EPIC catalog. There are two square-like regions and a line of blue markers, indicating stars whose inferred Kepler magnitude is about a magnitude smaller than their catalog magnitude, indicating that these stars are about a magnitude brighter than expected. The randomly distributed red markers are consistent with the population of Kepflag = “JHK” or “J” stars whose brightness is overestimated.</i>
    </div>
    <a href="images/release-notes/c4/C4radecKepMag.png">
        <img src="images/release-notes/c4/C4radecKepMag.png" class="img-responsive" alt="all C4 target stars plotted in celestial coordinates, colored by their Kepler magnitude inferred from their observed flux minus their Kepler magnitude from the EPIC catalog">
    </a>
</div>

<br>
***Stellar Targets with Negative Lightcurve Values***

Seventy-six stellar targets show negative flux values in their SAP_FLUX light curves, which is somewhat more than normally seen. Most of these are very dim, near background level targets at the edge of the focal plane where K2 roll has the largest impact, so it is not surprising that the roll causes negative flux values after background removal. The bright targets with negative flux values either have isolated negative flux outliers or are on the Pleiades channels, where there are large background residuals due to the constant background model on these channels, see above.

<br>
***Light Curve Quality***

The dominant systematic present in K2 simple aperture photometry light curves is a sawtooth shape that is due to the roll of the spacecraft approximately every 6 hours. The PDC module of the Kepler Pipeline uses Principle Component Analysis to remove this signal in addition to other systematics. Below, we examine observed trends and noise levels in the PDC light curves for C4, Data Release 6.

<div class="thumbnail" style="width: 68%;">
    <div class="caption">
        <i>Figure: CDPP measured for all targets as a function of Kepler magnitude. Dim targets have poorer overall photometric precision than bright targets, but can look better because the residual sawtooth falls below the noise floor. The saturated targets tend to have the lowest CDPP, but often show a residual sawtooth. All cadences flagged as having definite thruster firings are gapped.</i>
    </div>
    <a href="images/release-notes/c4/c4-cdpp_kepMag_full_FOV.jpg">
        <img src="images/release-notes/c4/c4-cdpp_kepMag_full_FOV.jpg" class="img-responsive" alt="CDPP measured for all targets as a function of Kepler magnitude">
    </a>
</div>

The photometric precision is generally better near the center of the focal plane where the variations in roll angle produce less pixel motion:

<div class="thumbnail" style="width: 68%;">
    <div class="caption">
        <i>Figure: 10th percentile CDPP of the 12th magnitude targets across the focal plane. The better performance near the center is evident.</i>
    </div>
    <a href="images/release-notes/c4/c4-10pcdpp_12th_mag.jpg">
        <img src="images/release-notes/c4/c4-10pcdpp_12th_mag.jpg" class="img-responsive" alt="10th percentile CDPP of the 12th magnitude targets across the focal plane">
    </a>
</div>


## Release History

The following is the data release history for this campaign. Follow the link for information about some of the features of the software used to reduce and export these data. There will be a new entry each time the data is released by the mission.

* <a href="http://keplerscience.arc.nasa.gov/K2/pipelineReleaseNotes.shtml#dr6">Data Release 6</a>

<br>
***Notes Specific to Data Release 6***

These notes are issues specific to how the data was processed and are likely to change when the data are reprocessed.

*SC PDC Quality Flags*

The PDC quality flags were populated for some of the SC targets even though there are no SC PDC light curves. These flags are: manual exclude (bit 9), SPSD detected (bit 11), and impulsive outlier removed (bit 12). Users may simply ignore these flags.


<hr>

# Campaign 3

TBC


<hr>

# Campaign 2

TBC


<hr>

# Campaign 1

TBC


<hr>

# Campaign 0

TBC

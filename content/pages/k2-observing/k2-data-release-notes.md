Title: K2 Data Release Notes
Save_as: k2-data-release-notes.html

[TOC]

This page details the key features of the K2 data releases,
including information on field pointing, target selection, observation times and cadences, processing version, unique observational features of each campaign, significant events that transpired during each campaign, data quality and processing features, and other descriptions of technical issues relevant to the scientific exploitation of the data.

<hr>


# K2 Campaign 16

<h2>At a glance</h2>

<div class="col-lg-5">
<p>
Campaign 16 was flown in the forward velocity vector direction in order to enable simultaneous K2 and ground-based observations of numerous targets (supernovae, variable stars, exoplanets, etc.) in the C16 field of view.
</p>

<b><i>Pointing</i></b>
<ul>
<li> RA:  133.7099689 degrees</li>
<li> Dec:  18.5253931 degrees</li>
<li> Roll:  -15.0605959 degrees</li>
</ul>

<b><i>Targets</i></b>
<ul>
<li>  35,643 long cadence (LC) targets, including 9,245 galaxy targets.</li>
<li>  131 short cadence (SC) targets.</li>
<li>  20 moving objects were tiled with LC custom strip apertures. 7 bright stars were assigned 24-pixel diameter LC disk apertures to capture the point spread function wings. See the <a href="images/release-notes/c16/kplr2018125112300_c16_caf.csv">csv file that maps</a> the custom aperture number to the target name to find the apertures for a specific target.</li>
</ul>

<b><i>Full Frame Images (FFI)</i></b>
<ul>
<li><a href="https://archive.stsci.edu/pub/k2/ffi/ktwo2017344214411-c16_ffi-cal.fits ">ktwo2017344214411-c16_ffi-cal.fits </a> This FFI, collected on 2017-12-10, has the Earth-Moon system in the field of view on channel 83. There is also a prominent optical ghost on channel 3.</li>
<li><a href="https://archive.stsci.edu/pub/k2/ffi/ktwo2018030100110-c16_ffi-cal.fits">ktwo2018030100110-c16_ffi-cal.fits</a>
</ul>

<b><i>First cadence</i></b>
<ul>
<li>Start Time: 2017-12-07 23:01:18 UTC</li>
<li>Long Cadence Number: 154331</li>
<li>Short Cadence Number: 4618390</li>
</ul>

<b><i>Last cadence</i></b>
<ul>
<li>End Time: 2018-02-25 12:39:52 UTC</li>
<li>Long Cadence Number: 158224</li>
<li>Short Cadence Number: 4735209</li>
</ul>

<b><i>Most Recent Processing Version</i></b>
<ul>
<li> <a href="k2-pipeline-release-notes.html#data-release-23">Data Release 23</a> </li>
</ul>

</div>

<div class="col-lg-7">

<div class="thumbnail">
<div class="caption">
<i>Figure C16-FOV: Schematic of Kepler's C16 field-of-view with high profile objects. </i>
</div>
<a href="images/k2/k2-c16-field.png"><img class="img-responsive" style="padding:0.5em;" src="images/k2/k2-c16-field.png" id="c16fov" alt="C16 field of view with highlights showing the Beehive cluster, M67, and the path of the Earth through the field of view.">
</a>
</div>


<div class="thumbnail">
<div class="caption">
<i>Figure C16-Mag: Distribution of the Kepler magnitudes of observed targets. All targets are chosen by guest observers. The distribution is due to how the largest <a href="k2-approved-programs.html#campaign-16">GO Programs</a>
were selected.</i>
</div>
<a href="images/release-notes/c16/c16_lc_magnitude_distribution.png">
<img src="images/release-notes/c16/c16_lc_magnitude_distribution.png" class="img-responsive" alt="Distribution of the Kepler magnitudes of observed C16 LC targets.">
</a>
</div>

</div>


<h2>Features and Events</h2>

***Earth!***

C16 was a forward velocity vector campaign, so Earth passed through the FOV at the start of the campaign from
2017-12-07 23:01:18 to 2017-12-11 07:27:11 UTC.
Earth traversed channel 67 (long cadence numbers 154331 - 154347) channel 82 (LC 154367 - 154431) and
channel 83 (LC 154429: 154491). The saturated image of Earth resulted in a series of saturated columns from the core
of the image and significant scattered light over the entire focal plane, as evidenced by the background flux
level metric. In addition to the direct image of Earth, there is a optical ghost image on the opposite side of the focal
plane (channels 2, 3, 19) whose core is near saturation. Users are cautioned to check carefully for interference from
Earth in their data during the first three days of the campaign.

<div class="thumbnail" style="width: 100%;display: inline-block;">
<div class="caption">
<i>Figure C16 Earth-at-LC: Earth was on the focal planet at the start of C16 on channel 67
and then passed through channels 82 and 83 before moving off the focal plane.
The saturated image of Earth is seen here passing through the LC target pixel apertures
on channel 82 (left) and 83 (right) in just over three days (~160 cadences).
The saturated columns from the core of the image
extend over all rows in the channel.</i>   
</div>
<table border="0" cellpadding="5px">
<tr>
<td width="75%"><video id="pelican-installation" class="video-js vjs-default-skin" controls loop preload="auto" data-setup="{}">
<source src="images/release-notes/c16/earth_ch82.mp4" type='video/mp4' alt="Movie of Earth transiting across channel 82 as seen through long cadence target apertures">
</video></td>
<td width="75%"><video id="pelican-installation" class="video-js vjs-default-skin" controls loop preload="auto" data-setup="{}">
<source src="images/release-notes/c16/earth_ch83.mp4" type='video/mp4' alt="Movie of Earth transiting across channel 83 as seen through long cadence target apertures">
</video></td>
</tr>
</div>

<div class="thumbnail" style="width: 90%;display: inline-block;">
<div class="caption">
<i>Figure C16-Background Metric: the average background level in electrons/second for each channel plotted
against time. The background level shows significant scattered light from Earth in the first three days of the campaign.</i>
<a href="images/release-notes/c16/c16_background_flux.png">
<img src="images/release-notes/c16/c16_background_flux.png" class="img-responsive" alt="Background flux
plotted versus time for each detector channel. Scattered light from Earth is evident in all channels for
the first three days of C16.">
</a>
</div>
</div>

<br>

***Galaxies***

There are 9,245 galaxies targeted in the C16 field of view; all but three used standard aperture masks. The
three large galaxies were covered with large circular custom masks.

<br>

***Clusters***

The C16 field of view includes the Beehive cluster (M44) and M67. M44 is one of the most nearby open clusters; its members were observed using standard masks.
M67 was tiled with a series of 20 x 20 pixels tiles for a total of 144,000 pixels.

<br>

***Supernovae***

The forward velocity vector orientation during C16 allowed for simultaneous ground-based observations of K2 targets. Numerous supernovae were observed by Kepler and ground-based observatories.
More details of the supernova campaign can be found at the <a href="supernova-experiment/index.html">Supernova Experiment site</a>.

<br>

***Pointing and Roll Performance***

The C16 pointing and roll behavior are well within the limits of that seen
in other K2 campaigns, with no degradation seen due to potentially low fuel levels.
The pipeline-calculated maximum distance between the
derived and nominal positions for any target (the "maximum attitude residual", or MAR)
for C16 is less than 2.3 pixels, well under the 3-pixel limit accommodated by the aperture halos.

As mentioned in the C14 release notes, a change in the on-board fine point fault logging threshold
results in additional cadences being flagged as "Spacecraft is not in fine point"
(QUALITY flag bit #16, decimal=32768). As a reminder, the project recommends that starting with C15,
users look to QUALITY flag bit #3 as an accurate indicator of poor spacecraft pointing.

<div class="thumbnail" style="width: 49%;display: inline-block;">
<div class="caption">
<i>Figure C16-Roll-Error: the roll-error between the photometrically derived attitude (PAD) and the nominal pointing plotted against time for C16.</i>
<a href="images/release-notes/c16/c16_pad_pdq_attitude_roll.png">
<img src="images/release-notes/c16/c16_pad_pdq_attitude_roll.png" class="img-responsive" alt="Pipeline measured roll error for C16.">
</a>
</div>
</div>

<div class="thumbnail" style="width: 49%;display: inline-block;">
<div class="caption">
<i>Figure C16-MAR: the maximum distance between the photometrically derived attitude (PAD) and the nominal position plotted against time for C16.</i>
<a href="images/release-notes/c16/c16_pad_pdq_attitude_mar.png">
<img src="images/release-notes/c16/c16_pad_pdq_attitude_mar.png" class="img-responsive" alt="Maximum residual of the C16 attitude measured with PAD and PDQ.">
</a>
</div>
</div>

<br>


<h2>Data Quality and Processing Notes</h2>

***Light Curve Quality***

As in previous campaigns, the 6-hour spacecraft roll cycle continues
to dominate the systematic errors in C16 simple aperture photometry light curves.
The pipeline CDPP 12th magnitude noise benchmark for C16 is
the lowest seen since C6. It is comparable to that seen in early campaigns with similar
star density (C6, C8, C10), but is well below that seen in C12, also with similar star density.
While we do not have a definitive cause the for the improved precision, it is likely due to a
combination of the relat degreesively low star density, the return to more stable pointing (compared to recent
campaigns), and the updated pipeline version (in-particular the use of the coarse-point flags; see <a href="k2-uniform-global-reprocessing-underway.html">the global reprocessing effort announcement</a> for details).

The magnitude dependence of CDPP and its distribution over the focal
plane are shown below. Other CDPP benchmarks can be found in the
<a href="images/release-notes/c16/c16_bin1.00_sc1.00_CDPP_Summary.png">
table giving 6.5-hr CDPP as a function of magnitude.</a>
<br>
<div class="thumbnail" style="width: 90%;">
<div class="caption">
<i>Figure C16-CDPP: 6.5-hr CDPP measurements for all targets as a function of Kepler magnitude. Dim targets have poorer overall photometric precision than bright targets, but can look better because the residual sawtooth falls below the noise floor. The saturated targets tend to have the lowest CDPP, but often show a residual sawtooth. </i>
</div>
<a href="images/release-notes/c16/c16_logg_CDPP_vs_model.png">
<img src="images/release-notes/c16/c16_logg_CDPP_vs_model.png" class="img-responsive" alt="CDPP measured for all targets as a function of Kepler magnitude.">
</a>
</div>
<div class="thumbnail" style="width: 90%;">
<div class="caption">
<i>Figure C16-CDPP FocalPlane: 6.5-hr CDPP measured as a function of position on the focal plane, for 12th and 14th magnitude dwarf stars. The photometric precision is generally better near the center of the focal plane where the variations in roll angle produce less pixel motion. All cadences coincident with a definite thruster firing are gapped.</i>
<a href="images/release-notes/c16/c16_dwarf_CDPP_by_mod_out.png">
<img src="images/release-notes/c16/c16_dwarf_CDPP_by_mod_out.png" class="img-responsive" alt="CDPP per channel for 12th and 14th magnitude dwarfs">
</a>
</div>
</div>

<br>


***SC Target With no PDC Flux***

The target HD 76333 (EPIC 200200727), a nearby high proper-motion F3V star, failed short-cadence PDC processing due to it being a custom target and the only target on its channel. The short-cadence light curve file includes the (nominal and unaffected) SAP flux, but the PDC_SAP flux is all zeros. Note that the long-cadence data for this target is unaffected and is nominal.

<hr>

<br>


# K2 Campaign 15

<h2>At a glance</h2>

<div class="col-lg-5">

<b><i>Pointing</i></b>
<ul>
<li> RA:  233.6175730 degrees</li>
<li> Dec:  -20.0792397 degrees</li>
<li> Roll:  166.7780778 degrees</li>
</ul>

<b><i>Targets</i></b>
<ul>
<li>  35,150 long cadence (LC) targets, including 3,485 galaxy targets.</li>
<li>  118 short cadence (SC) targets.</li>
<li>  38 moving objects we degreesre tiled with LC custom strip apertures. 13 bright stars were assigned 24-pixel diameter LC disk apertures to capture the point spread function wings. See the <a href="images/release-notes/c15/kplr2017355085300_c15_caf.csv">csv file that maps</a> the custom aperture number to the target name to find the apertures for a specific target.</li>
</ul>

<b><i>Full Frame Images (FFI)</i></b>
<ul>
<li><a href="https://archive.stsci.edu/pub/k2/ffi/ktwo2017246053350-c15_ffi-cal.fits">ktwo2017246053350-c15_ffi-cal.fits</a> Note: only one FFI was collected during C15.</li>
</ul>

<b><i>First cadence</i></b>
<ul>
<li>Start Time: 2017-08-23 22:18:11 UTC</li>
<li>Long Cadence Number: 149142</li>
<li>Short Cadence Number: 4462720</li>
</ul>

<b><i>Last cadence</i></b>
<ul>
<li>End Time: 2017-11-19 22:58:27 UTC</li>
<li>Long Cadence Number: 153449</li>
<li>Short Cadence Number: 4591959</li>
</ul>

<b><i>Most Recent Processing Version</i></b>
<ul>
<li> <a href="k2-pipeline-release-notes.html#data-release-22">Data Release 22</a> </li>
</ul>

</div>

<div class="col-lg-7">

<div class="thumbnail">
<div class="caption">
<i>Figure C15-FOV: Schematic of Kepler's C15 field-of-view with high profile objects. </i>
</div>
<a href="images/k2/k2-c15-field.png"><img class="img-responsive" style="padding:0.5em;" src="images/k2/k2-c15-field.png" id="c15fov" alt="C15 field of view with highlights showing the Upper Sco young star region and the very old globular cluster NGC 5897.">
</a>
</div>


<div class="thumbnail">
<div class="caption">
<i>Figure C15-Mag: Distribution of the Kepler magnitudes of observed targets. All targets are chosen by guest observers. The distribution is due to how the largest <a href="k2-approved-programs.html#campaign-15">GO Programs</a>
were selected.</i>
</div>
<a href="images/release-notes/c15/c15_lc_magnitude_distribution.png">
<img src="images/release-notes/c15/c15_lc_magnitude_distribution.png" class="img-responsive" alt="Distribution of the Kepler magnitudes of observed LC targets.">
</a>
</div>

</div>


<h2>Features and Events</h2>

***Galaxies and Clusters***

There are 3,485 galaxies targeted in the C15 field of view all of which used standard aperture masks.

The C15 field of view overlaps a portion of the young star association Upper Sco.
The FOV also contains the old globular cluster NGC 5897, which was tiled with a
6x6 array of 15x15 pixel tiles for a total of 8100 pixels.

<br>

***Pointing and Roll Performance***

The C15 pointing and roll behavior are well within the limits of that seen
in other K2 campaigns for the majority of the campaign.
The pipeline calculated maximum distance between the
derived and nominal positions for any target (the "maximum attitude residual", or MAR)
for C15 is less than 2.5 pixels, well under the 3-pixel limit accommodated by the aperture halos.
There were far fewer anomalous thruster firing events in C15 than were seen in recent
campaigns prior to C14.

As mentioned in the C14 release notes, a change in the on-board fine point fault logging threshold
results in additional cadences being flagged as "Spacecraft is not in fine point"
(QUALITY flag bit #16, decimal=32768). Starting with C15, the pipeline is now ignoring the
spacecraft not-in-fine-point flag, and instead is using the "Spacecraft is in coarse point" flag (QUALITY
flag bit #3, decimal=4). This flag is set by the project based on the measured pointing error exceeding
1.5 pixels for 4 or more continuous cadences, or exceeding 2.5 pixels for a single cadence. The pipeline will treat
these "coarse-point" cadences just as "not-in-fine-point" cadences were treated in previous campaigns
up to and including C14, i.e., there will be calibrated pixels, but light curve data will be gapped
for the flagged cadences. The project recommends that starting with C15, users look to
QUALITY flag bit #3 as an indicator of poor spacecraft pointing.

<div class="thumbnail" style="width: 49%;display: inline-block;">
<div class="caption">
<i>Figure C15-Roll-Error: the roll-error between the photometrically derived attitude (PAD) and the nominal pointing plotted against time for C15.</i>
<a href="images/release-notes/c15/c15_pad_pdq_attitude_roll.png">
<img src="images/release-notes/c15/c15_pad_pdq_attitude_roll.png" class="img-responsive" alt="Pipeline measured roll error for C15.">
</a>
</div>
</div>

<div class="thumbnail" style="width: 49%;display: inline-block;">
<div class="caption">
<i>Figure C15-MAR: the maximum distance between the photometrically derived attitude (PAD) and the nominal position plotted against time for C15.</i>
<a href="images/release-notes/c15/c15_pad_pdq_attitude_mar.png">
<img src="images/release-notes/c15/c15_pad_pdq_attitude_mar.png" class="img-responsive" alt="Maximum residual of the C15 attitude measured with PAD and PDQ.">
</a>
</div>
</div>

<br>

***Solar Flares and Coronal Mass Ejections (CMEs) During Observations***

From September 6—10, 2017 (during C15 observations) [the Sun emitted 27 M-class and four X-class flares and released several powerful coronal mass ejections, or CMEs](https://www.nasa.gov/feature/goddard/2017/september-2017s-intense-solar-activity-viewed-from-space). The effect of these flares and CMEs is visible in K2 data during C15,
most notably in the measured dark current level for all channels; we provide examples for channels 15 and 25 below.
Peak dark current emission occurred around long cadences 149142 + 675, 901, and 957, respectively, corresponding to BJD 2458003.23, 2458007.85, and 2458009.00.
Uses are urged caution in interpreting astrophysical events in observed targets that have similar timing and duration to these CME events.

<div class="thumbnail" style="width: 49%;display: inline-block;">
<div class="caption">
<i>Figure C15-Dark-Chan15: the dark level measured on channel 15 during C15.</i>
<a href="images/release-notes/c15/C15-Channel15-Dark.png">
<img src="images/release-notes/c15/C15-Channel15-Dark.png" class="img-responsive" alt="Pipeline measured dark current for channel 15 during C15.">
</a>
</div>
</div>

<div class="thumbnail" style="width: 49%;display: inline-block;">
<div class="caption">
<i>Figure C15-Dark-Chan25: the dark level measured on channel 25 during C15.</i>
<a href="images/release-notes/c15/C15-Channel25-Dark.png">
<img src="images/release-notes/c15/C15-Channel25-Dark.png" class="img-responsive" alt="Pipeline measured dark current for channel 25 during C15.">
</a>
</div>
</div>


<br>

<h2>Data Quality and Processing Notes</h2>

***Light Curve Quality***

As in previous campaigns, the 6-hour spacecraft roll cycle continues
to dominate the systematic errors in C15 simple aperture photometry light curves.
The pipeline CDPP 12th magnitude noise benchmark for C15 is
the lowest seen since C6. It is comparable to that seen in early campaigns with similar
star density (C6, C8, C10), but is well below that seen in C12, also with similar star density.
While we do not have a definitive cause the for the improved precision, it is likely due to a
combination of the relatively low star density, the return to more stable pointing (compared to recent
campaigns), and the updated pipeline version (in-particular the use of the coarse-point flags).

The magnitude dependence of CDPP and its distribution over the focal
plane are shown below. Other CDPP benchmarks can be found in the
<a href="images/release-notes/c15/c15_bin1.00_sc1.00_CDPP_Summary_18020113.txt">
table giving 6.5-hr CDPP as a function of magnitude.</a>
<br>
<div class="thumbnail" style="width: 90%;">
<div class="caption">
<i>Figure C15-CDPP: 6.5-hr CDPP measurements for all targets as a function of Kepler magnitude. Dim targets have poorer overall photometric precision than bright targets, but can look better because the residual sawtooth falls below the noise floor. The saturated targets tend to have the lowest CDPP, but often show a residual sawtooth. </i>
</div>
<a href="images/release-notes/c15/c15_logg_CDPP_vs_model.png">
<img src="images/release-notes/c15/c15_logg_CDPP_vs_model.png" class="img-responsive" alt="CDPP measured for all targets as a function of Kepler magnitude.">
</a>
</div>
<div class="thumbnail" style="width: 90%;">
<div class="caption">
<i>Figure C15-CDPP FocalPlane: 6.5-hr CDPP measured as a function of position on the focal plane, for 12th and 14th magnitude dwarf stars. The photometric precision is generally better near the center of the focal plane where the variations in roll angle produce less pixel motion. All cadences coincident with a definite thruster firing are gapped.</i>
<a href="images/release-notes/c15/c15_dwarf__CDPP_by_mod_out.png">
<img src="images/release-notes/c15/c15_dwarf__CDPP_by_mod_out.png" class="img-responsive" alt="CDPP per channel for 12th and 14th magnitude dwarfs">
</a>
</div>
</div>

<br>


***Targets With Incorrect Flux Scaling***

During the analysis of C15 data, the Science Office uncovered an inconsistency in how targets
with high proper motion are handled. We noted that there is a target with an anomalously
high average value for the PDC corrected flux, corresponding to a Kp=7.5 mag star when it should be
a magnitude Kp=12 star. The issue was traced to the fact that the target
EPIC 250111823, (Ross 802) is a high-proper motion star (-448, -624 mas/yr) that is ~12 arcsec
from its J2000 catalog position. The photometric analysis code (PA-COA) was not supplied with
proper motion information and did not find a star at the catalog position. The code correctly reverted
to the flight target aperture (which does account for proper motion), but computed the
flux-fraction in aperture (FFIA~0.03) and crowding metric based on the assumption that the
target was well outside the flight aperture. The low flux-fraction in aperture caused the PDC
flux time series (PDCSAP_FLUX) to be scaled up by a factor of ~1/0.03, or ~33. The time variation of the PDCSAP_FLUX
is correct for the target aperture, only mis-scaled. The SAP_FLUX is unaffected by this bug.

The Science Office is assessing the impact of this issue in K2, but there is a potential mis-scaling for any
targets with accumulated proper motion since J2000 that is larger than ~1.5 pixels (~6 arcseconds).
Users should check for potentially mis-scaled PDCSAP_FLUX for any of the
<a href="images/release-notes/c15/c15_proper_motion_gt_1pix_tgts.csv">
C15 targets with accumulated proper motion ≥ 1 pixel (~4 arcseconds)</a>.

<br>


***Targets Affected by CAL Bug***

Due to a bug in the smear tables, column 928 on channel 33, and column 1008 on channel 47, had both their real and virtual smear values gapped, which resulted in values of "0.0" for the flux along the entire column. This might potentially affect the light curves of the following targets, which contain the affected column in their pixel-stamp image. Users may want conduct custom photometry that excludes or accounts for the affected column.

The EPIC IDs of the affected targets are 249868223, 249921937, 249924613, 249934130, and 249198204.

<br>


***Dynamic Black Correction***

A new feature of the Kepler pipeline that was implemented for K2 processing, starting with C15, is the use of Dynamic Black Correction, or "Dynablack", which is essentially a more sophisticated algorithm to perform the CCD pixel-level calibration that accounts for time varying, instrument-induced artifacts when calibrating the data.

Dynablack uses the full-frame images and collateral pixels to provide two main benefits compared to traditional pixel calibration:

* Correct thermally dependent fine guidance sensor crosstalk pixels.

* Identify rolling-band artifacts (see [§6.7 of the Instrument Handbook](https://archive.stsci.edu/kepler/manuals/KSCI-19033-002.pdf#page=75)) with flags in the target pixel files.

For the latter case, users can use the new RB_LEVEL flags in the FITS files. See [§A.1.1 of the Kepler Data Release 25 Notes](https://archive.stsci.edu/kepler/release_notes/release_notes25/KSCI-19065-002DRN25.pdf#page=11) and [§2.3.2 of the Kepler Archive Manual](https://archive.stsci.edu/kepler/manuals/archive_manual.pdf#page=24) for information on how to interpret and utilize the RB_LEVEL flags. Users should note that the RB_LEVEL test at the shortest duration (3 hours) is overly sensitive to instrument noise and does not offer a reliable indicator of the presence of rolling band pattern noise.  Because the binary "Rolling Band Detected" QUALITY and SAP_QUALITY flags (bits 18, 19) in the target pixel files and light curve files are based on a rolling band detection at any of the test durations, they also do not provide a reliable indicator of the presence of rolling band pattern noise. The RB_LEVEL flags at durations of 6 hours and longer provide the best indication of the presence of rolling band artifacts.


<br>


***Short Cadence Light Curves***

Starting with C15, short-cadence light curves are now produced and available at MAST, though we strongly caution users that no work was done to adapt the Kepler pipeline's detrending module (PDC), developed for Kepler data, to work well on K2 data. *Thruster firings are especially poorly corrected for most short-cadence targets, and other systematic features may not be corrected well.* See Figure  C15-SC-Example-1 below for an example of remaining systematics in short-cadence data around thruster firings. However, some targets do have adequate detrending in short-cadence, and even in the cases of poor detrending, short-term astrophysical variation can be seen for targets where such astrophysical variation exists. See Figure C15-SC-Example-2 below where the ~18 min periodic variations of the AM CVn type binary HP Lip are readily apparent in the C15 short-cadence light curve. The hope is that producing these short-cadence light curves overall benefits the community compared to not producing them, even if they may only be used for initial inspection of the short-cadence data, which might prompt users to perform their own short-cadence detrending, or better adapt the existing long-cadence [Cotrending Basis Vector (CBV) files](https://archive.stsci.edu/k2/cbv.html) for use in detrending the short-cadence data.

<div class="thumbnail" style="width: 49%;display: inline-block;">
<div class="caption">
<i>Figure C15-SC-Example-1: The Exoplanet Host K2-38 / EPIC 204221263.</i>
<a href="images/release-notes/c15/epic_204221263_zoom1.png">
<img src="images/release-notes/c15/epic_204221263_zoom1.png" class="img-responsive" alt="The Exoplanet Host K2-38 / EPIC 204221263.">
</a>
</div>
</div>

<div class="thumbnail" style="width: 49%;display: inline-block;">
<div class="caption">
<i>Figure C15-SC-Example-2: The AM CVn type Binary HP Lip / EPIC 250105131</i>
<a href="images/release-notes/c15/epic_250105131_zoom1.png">
<img src="images/release-notes/c15/epic_250105131_zoom1.png" class="img-responsive" alt="The AM CVn type Binary HP Lip / EPIC 250105131.">
</a>
</div>
</div>

<hr>

<br>


# K2 Campaign 14

<h2>At a glance</h2>

<div class="col-lg-5">

<b><i>Pointing</i></b>
<ul>
<li> RA:  160.6824762 degrees</li>
<li> Dec:  6.8509316 degrees</li>
<li> Roll:  158.7573464 degrees</li>
</ul>

<b><i>Targets</i></b>
<ul>
<li>  39,098 long cadence (LC) targets, including 14,691 galaxy targets</li>
<li>  147 short cadence (SC) targets, with 163 target definitions</li>
<li>  42 moving objects were tiled with LC custom strip apertures. 7 bright stars were assigned 24-pixel diameter LC disk apertures to capture the point spread function wings. See the <a href="images/release-notes/c14/ktwoc14_caf.csv">csv file that maps</a> the custom aperture number to the target name to find the apertures for a specific target.</li>
</ul>

<b><i>Full Frame Images (FFI)</i></b>
<ul>
<li><a href="https://archive.stsci.edu/pub/k2/ffi/ktwo2017162122209-c14_ffi-cal.fits">ktwo2017162122209-c14_ffi-cal.fits</a></li>
<li><a href="https://archive.stsci.edu/pub/k2/ffi/ktwo2017203170143-c14_ffi-cal.fits">ktwo2017203170143-c14_ffi-cal.fits</a></li>
</ul>

<b><i>First cadence</i></b>
<ul>
<li>Start Time: 2017-06-01 05:06:29 UTC</li>
<li>Long Cadence Number: 145045</li>
<li>Short Cadence Number: 4339810</li>
</ul>

<b><i>Last cadence</i></b>
<ul>
<li>End Time: 2017-08-19 22:11:02 UTC</li>
<li>Long Cadence Number: 148945</li>
<li>Short Cadence Number: 4456839</li>
</ul>

<b><i>Most Recent Processing Version</i></b>
<ul>
<li> <a href="k2-pipeline-release-notes.html#data-release-20">Data Release 20</a> </li>
</ul>

</div>

<div class="col-lg-7">


<div class="thumbnail">
<div class="caption">
<i>Figure C14-FOV: Schematic of Kepler's C14 field-of-view with high profile objects. </i>
</div>
 <a href="images/k2/k2-c14-field.png"><img class="img-responsive" style="padding:0.5em;" src="images/k2/k2-c14-field.png" id="c14fov" alt="C14 field of view with highlighted clusters M95, M96, M101 and nearby star Wolf 359, future site of a prominent battle between the UFP and the Borg Collective in Stardate 2367.">
</a>
</div>


<div class="thumbnail">
<div class="caption">
<i>Figure C14-Mag: Distribution of the Kepler magnitudes of observed targets. All targets are chosen by guest observers. The distribution is due to how the largest <a href ="k2-approved-programs.html#campaign-14">GO Programs</a> were selected. The peak in the distribution at faint magnitudes is due to the large number of faint galaxies targeted.</i>
</div>
<a href="images/release-notes/c14/c14_lc_magnitude_distribution.png">
<img src="images/release-notes/c14/c14_lc_magnitude_distribution.png" class="img-responsive" alt="Distribution of the Kepler magnitudes of observed LC targets.">
</a>
</div>

</div>

<h2>Features and Events</h2>

***Galaxies***

The C14 field of view sits at 53º N Galactic latitude in the North Galactic cap.  There are 14,691 galaxies targeted
in the C14 field of view. 47 of the Galaxies with radii > 40 arcseconds were covered with large circular masks.
Twelve galaxies were covered with 15x15 pixel square masks. Six galaxies (M95, M96, M105, NGC3384,
NGC3423, NGC3412) were covered by 40x40 pixel square masks consisting of 16 tiles of 10x10 pixel sub-masks.
The <a href="images/release-notes/c14/ktwoc14_caf.csv">custom aperture file</a> gives the custom EPIC ID for
each of these masks. *This mapping file has changed format with this release and now includes more information.* The
six columns, which are populated according to target type are:

1. custom KepId
2. target type: 1 = star, or quasi-stellar object with an EPIC ID, 2 = engineering data (not used here), 3 = open
cluster or other large patch of the sky with no individual object, 4 = a central object, but with no EPIC ID,
5 = Solar System object
3. the EPIC number, if it exists
4. RA of the center of the sky patch (type 3), or center of the extended object (type 4)
5. Declination of the center of the sky patch (type 3), or center of the extended object (type 4)
6. Object name

In addition to the many galaxies, a number of <a href ="k2-approved-programs.html#campaign-14">notable targets</a>
were observed during C14, including Wolf 359, a nearby late M-dwarf.

<br>

***Pointing and Roll Performance***

The C14 pointing and roll behavior are well within the limits of that seen
in other K2 campaigns for the majority of the campaign.
The pipeline calculated maximum distance between the
derived and nominal positions for any target (the "maximum attitude residual", or MAR)
for C14 is less than 2 pixels, well under the 3-pixel limit accommodated by the aperture halos.
There were far fewer anomalous thruster firing events in C14 than were seen in recent campaigns.

In order to give the flight system engineers an advanced warning of degradation in the pointing
as fuel runs low, the on-board fine point fault logging threshold was lowered from ~103 arcseconds
(0.0005 radians) to ~62 arcseconds (0.0003 radians) on 2017-07-14, mid-way through C14. While
this change does not affect pointing performance, it did have the unintended effect of flagging
more cadences as "Spacecraft is not in fine point" (QUALITY flag bit #16, decimal=32768), which
the pipeline then gaps. The result of this threshold change is that there are 129 long cadences gapped
as not-in-fine-point in C14 versus 48 in C13, with the majority of these falling in the second half of C14,
after the threshold change. The not-in-fine-point cadences have calibrated pixels in the archive TPFs,
but no flux values in the light curve files.

The project has identified a workaround for the flagging resulting from this changed threshold and has
implemented it for future processing starting with C15.

<div class="thumbnail" style="width: 49%;display: inline-block;">
<div class="caption">
<i>Figure C14-Roll-Error: the roll-error between the photometrically derived attitude (PAD) and the nominal pointing plotted against time for C14.</i>
<a href="images/release-notes/c14/c14_pad_pdq_attitude_roll.png">
<img src="images/release-notes/c14/c14_pad_pdq_attitude_roll.png" class="img-responsive" alt="Pipeline measured roll error for C14.">
</a>
</div>
</div>

<div class="thumbnail" style="width: 49%;display: inline-block;">
<div class="caption">
<i>Figure C14-MAR: the maximum distance between the photometrically derived attitude (PAD) and the nominal position plotted against time for C14.</i>
<a href="images/release-notes/c14/c14_pad_pdq_attitude_mar.png">
<img src="images/release-notes/c14/c14_pad_pdq_attitude_mar.png" class="img-responsive" alt="Maximum residual of the C14 attitude measured with PAD and PDQ.">
</a>
</div>
</div>

<br>

<h2>Data Quality and Processing Notes</h2>

***Light Curve Quality***

As in previous campaigns, the 6-hour spacecraft roll cycle continues
to dominate the systematic
errors in C14 simple aperture photometry light curves.
The pipeline CDPP 12th magnitude noise benchmark for C14 is
the lowest seen since C6. It is comparable to that seen in early campaigns with similar
star density (C6, C8, C10), but is well below that seen in C12, also with similar star density.
We do not have a definitive cause the for the improved precision, but it could be in part due
to the relatively low star density and the return to more stable pointing (compared to recent
campaigns).

The magnitude dependence of CDPP and its distribution over the focal
plane are shown below. Other CDPP benchmarks can be found in the
<a href="images/release-notes/c14/c14_bin1.00_sc1.00_CDPP_Summary_17100214.txt">
table giving 6.5-hr CDPP as a function of magnitude.</a>
<br>
<div class="thumbnail" style="width: 90%;">
<div class="caption">
<i>Figure C14-CDPP: 6.5-hr CDPP measurements for all targets as a function of Kepler magnitude. Dim targets have poorer overall photometric precision than bright targets, but can look better because the residual sawtooth falls below the noise floor. The saturated targets tend to have the lowest CDPP, but often show a residual sawtooth. </i>
</div>
<a href="images/release-notes/c14/c14_logg_CDPP_vs_model.png">
<img src="images/release-notes/c14/c14_logg_CDPP_vs_model.png" class="img-responsive" alt="CDPP measured for all targets as a function of Kepler magnitude.">
</a>
</div>
<div class="thumbnail" style="width: 90%;">
<div class="caption">
<i>Figure C14-CDPP FocalPlane: 6.5-hr CDPP measured as a function of position on the focal plane, for 12th and 14th magnitude dwarf stars. The photometric precision is generally better near the center of the focal plane where the variations in roll angle produce less pixel motion. All cadences coincident with a definite thruster firing are gapped.</i>
<a href="images/release-notes/c14/c14_cdpp_benchmark_fov.png">
<img src="images/release-notes/c14/c14_cdpp_benchmark_fov.png" class="img-responsive" alt="CDPP per channel for 12th magnitude dwarfs">
</a>
</div>
</div>

<br>

***Targets Missing from the Archive***

Pipeline errors during the process of exporting the light curve (LCV) and
target pixel (TP) FITS files resulted in two targets (EPIC IDs 248463890 and 248463977)
from C14 having no LCV or TPF files at the archive.

<br>


<hr>

# K2 Campaign 13

<h2>At a glance</h2>

<div class="col-lg-5">

<b><i>Pointing</i></b>
<ul>
<li> RA: 72.7971166 degrees</li>
<li> Dec: 20.7870759 degrees</li>
<li> Roll: -172.7995758 degrees</li>
</ul>

<b><i>Targets</i></b>
<ul>
<li> 26,242 long cadence (LC) targets, including 21,434 standard LC stellar (or point-like) targets</li>
<li> 118 short cadence (SC) targets, with 144 target definitions</li>
<li> 15 moving objects were tiled with LC custom strip apertures. 33 bright stars, including Aldebaran, were assigned 40-pixel diameter LC disk apertures to capture the point spread function wings. Nine bright Hyades cluster stars were assigned 24-pixel diameter SC disk apertures. See the <a href="images/release-notes/c13/ktwoc13_caf.csv">csv file that maps</a> the custom aperture number to the target name.</li>
</ul>

<b><i>Full Frame Image (FFI)</i></b>
<ul>
<li><a href="https://archive.stsci.edu/pub/k2/ffi/ktwo2017079075530-c13_ffi-cal.fits">ktwo2017079075530-c13_ffi-cal.fits</a> Note: only one FFI was collected during C13.</li>
</ul>

<b><i>First cadence</i></b>
<ul>
<li>Start Time: 2017-03-08 01:35:06 UTC</li>
<li>Long Cadence Number: 140878</li>
<li>Short Cadence Number: 4214800</li>
</ul>

<b><i>Last cadence</i></b>
<ul>
<li>End Time: 2017-05-27 15:44:53 UTC</li>
<li>Long Cadence Number: 144821</li>
<li>Short Cadence Number: 4333119</li>
</ul>

<b><i>Most Recent Processing Version</i></b>
<ul>
<li> <a href="k2-pipeline-release-notes.html#data-release-19">Data Release 19</a> </li>
</ul>

</div>

<div class="col-lg-7">

<!---
 <div class="thumbnail">
<div class="caption">
<i>Figure C13-FOV: Schematic of Kepler's C13 field-of-view with observed targets shown with purple dots. REPLACE WITH UPDATED VERSION, OR REMOVE</i>
</div>
<a href="images/release-notes/c13/C13_selected.png">
<img src="images/release-notes/c13/c13_selected.png" class="img-responsive" alt="C13 field-of-view with selected targets plotted in purple.">
</a>
</div>
 --->

<div class="thumbnail">
<div class="caption">
<i>Figure C13-Mag: Distribution of the Kepler magnitudes of observed targets. All targets are chosen by guest observers. The distribution is due to how the largest <a href ="k2-approved-programs.html#campaign-13">GO Programs</a> were selected.</i>
</div>
<a href="images/release-notes/c13/c13_lc_magnitude_distribution.png">
<img src="images/release-notes/c13/c13_lc_magnitude_distribution.png" class="img-responsive" alt="Distribution of the Kepler magnitudes of observed LC targets.">
</a>
</div>

</div>

<h2>Features and Events</h2>

***Clusters and Star Forming Regions***

The C13 field of view encompasses part of the Taurus star forming region,
including the well
known T-Tauri stars HL Tau (EPIC 210690913) and LkCa 15 (EPIC 247520207).
The field of view also covers a portion of the
Hyades star cluster along with the distant clusters
NGC 1647, NGC 1746, and NGC 1817.

<br>

***Galaxies***

There are 33 galaxies targeted in the C13 field of view.


<br>

***Pointing and Roll Performance***

The C13 pointing and roll behavior are within the limits of that seen
in other K2 campaigns for the majority of the campaign.
The pipeline calculated maximum distance between the
derived and nominal positions for any target (the "maximum attitude residual", or MAR)
for C13 is well under the 3-pixel limit accommodated by the aperture halos,
except for three periods with anomalous thruster firings. One is in the first day
of the campaign lasting for 6 hours starting at 2017-03-08 17:46:06 UTC
(cadence numbers 140911-140922).
Two periods of anomalous pointing occur in the final five days
of the campaign: 18 hours starting at 2017-05-23 12:11:44 UTC
(cadence numbers 144619-144654), and 6 hours
starting at 2017-05-25 11:16:28 UTC (cadence numbers 144715-144726).
These anomalous thruster firing events occurring near the start and end of campaigns
are suspected to be due to low fuel levels. The flight team is investigating them in
an effort to understand whether they can be mitigated and how they might
evolve in future campaigns.

<div class="thumbnail" style="width: 49%;display: inline-block;">
<div class="caption">
<i>Figure C13-Roll-Error: the roll-error between the photometrically derived attitude (PAD) and the nominal pointing plotted against time for C13.</i>   
</div>
<a href="images/release-notes/c13/c13_pad_pdq_attitude_roll.png">
<img src="images/release-notes/c13/c13_pad_pdq_attitude_roll.png" class="img-responsive" alt="Pipeline measured roll error for C13.">
</a>
</div>

<div class="thumbnail" style="width: 49%;display: inline-block;">
<div class="caption">
<i>Figure C13-MAR: the maximum distance between the photometrically derived attitude (PAD) and the nominal position plotted against time for C13.</i>
<a href="images/release-notes/c13/c13_pad_pdq_attitude_mar.png">
<img src="images/release-notes/c13/c13_pad_pdq_attitude_mar.png" class="img-responsive" alt="Maximum residual of the C13 attitude measured with PAD and PDQ.">
</a>
</div>
</div>

<br>

***Smear Correction Error on Channel 74***

The presence of the first magnitude star Aldebaran on channel 73 led to an error in
the smear correction for channel 74, which shares the same physical CCD (see figure
Aldebaran).
The saturated charge from Aldebaran spills over all rows of the image and into the
serial register of the CCD, corrupting the first three rows of the masked smear region
in the FFI. While these rows are not used for the smear correction, at times during
C13 the saturation spill covered more rows in the masked smear, extending up to row 15 on
channel 74 (see figure Channel 74 Trailing Black). Trailing black rows 7-18 are fit
with a linear model to estimate the black (bias) level for the masked smear region.

At these times,
the trailing black estimate for the masked smear signal was corrupted, resulting in a
corrupted smear measurement for the affected cadences. Since the smear signal is subtracted
from all the pixels in the channel, all targets on channel 74 were affected for these
cadences. The impact is somewhat mitigated by background correction, but due to the
non-linearity correction during calibration, a residual error remains. The effect is
generally more significant for faint targets; however, users are cautioned
to estimate the impact on their science of using data from the affected cadences.
In addition, due to the rapidly changing background estimate, the argabrightening
detector (see [Kepler Data Characteristics Handbook, Sec 5.8](http://archive.stsci.edu/kepler/manuals/Data_Characteristics.pdf))
was triggered on channel 74 resulting in data gaps in the light curve files for
some targets. Users should treat the channel specific argabrightening indicator
in QUALITY and SAP_QUALITY flags with caution
(bit 13, decimal=4096).

The smear corruption effects were most prominent in the
first 80 cadences of the campaign and again in the period between cadence 1800-3200
(see Figure Channel 74 Trailing Black)
In order to allow users to select the cadences they wish to exclude, the attached
csv file <a href="images/release-notes/c13/c13_ch74_black_for_smear_residuals.csv">c13_ch74_black_for_smear_residuals.csv</a>
contains the residual black level for the masked smear pixels after model fitting for
each LC.
The units of the residual signal are ADU/LC/pixel. The cadences with large negative
residuals (<-200 ADU/LC/pixel) and those showing bimodal behavior are indicative of
a poor model fit and a corrupted smear correction.

<div class="thumbnail">
<div class="caption">
<i>Figure Aldebaran: An image of channels 73 (left) and 74 (right) from the FFI
ktwo2017079075530-c13_ffi-cal shows the bright star on channel 73 with
saturation spilling over all rows (x-axis is CCD columns, y-axis is CCD rows).
In a zoomed image of the first 50 rows of the CCD
(lower panel) the saturation spill along the serial register of both channels shows
up as a white bar in rows 1-3. The readout amplifiers
are located at the lower left corner for channel 73 and lower right corner for
channel 74. The trailing black signal is measured from virtual columns in the center
of this composite image (at the green dashed line).
</i>
</div>
<a href="images/release-notes/c13/ffi_raw_ch73_74_c13.png">
<img src="images/release-notes/c13/ffi_raw_ch73_74_c13.png" class="img-responsive" alt="C13 FFI image of channels 73 and 74 with Aldebaran.">
</a>
</div>
<a href="images/release-notes/c13/ffi_raw_ch73_74_c13_zoom.png">
<img src="images/release-notes/c13/ffi_raw_ch73_74_c13_zoom.png" class="img-responsive" alt="C13 FFI zoomed image of channels 73 and 74 showing collateral data rows.">
</a>
</div>
</div>

<div class="thumbnail">
<div class="caption">
<i>Figure Channel 74 Trailing Black: A time series of the residual trailing
black level for the masked smear pixels after model fitting shows the effect
of the saturation from Aldebaran. The trailing black rows used in estimating
the black correction for the masked smear signal (rows 7:18) show anomalous
values and bimodal behavior during the affected cadences.
</i>
</div>
<a href="images/release-notes/c13/c13_ch74_black_for_ms_residual.png">
<img src="images/release-notes/c13/c13_ch74_black_for_ms_residual.png" class="img-responsive" alt="C13 channel 74 black model residual for masked smear pixels by cadence number.">
</a>
</div>
</div>

<br>

<h2>Data Quality and Processing Notes</h2>

***Light Curve Quality***

As in previous campaigns, the 6-hour spacecraft roll cycle continues
to dominate the systematic
errors in C13 simple aperture photometry light curves.
Similar to C12, the pipeline CDPP 12th magnitude noise
benchmark is 15-20% higher than what was seen in star fields of comparable star
density (e.g. C4, C5). There is tentative evidence that at least part of this increase
is due to the anomalous pointing excursions at the beginning and end of the campaign.
In future campaigns, the processing will exclude such cadences from PDC and from
the CDPP estimates.

The magnitude dependence of CDPP and its distribution over the focal
plane are shown below. Other CDPP benchmarks can be found in the
<a href="images/release-notes/c13/c13_bin1.00_sc1.00_CDPP_Summary_17080715.txt">
table giving 6.5-hr CDPP as a function of magnitude.</a>
<br>
<div class="thumbnail" style="width: 90%;">
<div class="caption">
<i>Figure C13-CDPP: 6.5-hr CDPP measurements for all targets as a function of Kepler magnitude. Dim targets have poorer overall photometric precision than bright targets, but can look better because the residual sawtooth falls below the noise floor. The saturated targets tend to have the lowest CDPP, but often show a residual sawtooth. </i>   
</div>
<a href="images/release-notes/c13/c13_logg_CDPP_vs_model.png">
<img src="images/release-notes/c13/c13_logg_CDPP_vs_model.png" class="img-responsive" alt="CDPP measured for all targets as a function of Kepler magnitude.">
</a>
</div>
<div class="thumbnail" style="width: 90%;">
<div class="caption">
<i>Figure C13-CDPP FocalPlane: 6.5-hr CDPP measured as a function of position on the focal plane, for 12th and 14th magnitude dwarf stars. The photometric precision is generally better near the center of the focal plane where the variations in roll angle produce less pixel motion. All cadences coincident with a definite thruster firing are gapped.</i>
<a href="images/release-notes/c13/c13_dwarf_CDPP_by_mod_out.png">
<img src="images/release-notes/c13/c13_dwarf_CDPP_by_mod_out.png" class="img-responsive" alt="CDPP per channel for 12th magnitude dwarfs">
</a>    
</div>
</div>

<br>

<hr>

# K2 Campaign 12

<h2>At a glance</h2>

<div class="col-lg-5">

<b><i>Pointing</i></b>
<ul>
<li>RA: 351.6588124 degrees</li>
<li>Dec: -5.1023328 degrees</li>
<li>Roll: -156.8808419 degrees</li>
</ul>

<b><i>Targets</i></b>
<ul>
<li> 29,221 standard long cadence (LC) stellar targets, with 46,113 total target definitions</li>
<li> 141 short cadence (SC) stellar targets, with 249 target definitions</li>
<li> 42 unique LC custom targets were selected, along with two SC custom target apertures for Chiron and Trappist-1. See the <a href="images/release-notes/c12/ktwoc12_caf.csv">csv file that maps</a> the custom aperture number to the target name.</li>
</ul>

<b><i>Full Frame Images (FFI)</i></b>
<ul>
<li><a href="https://archive.stsci.edu/pub/k2/ffi/ktwo2016361035629-c12_ffi-cal.fits">ktwo2016361035629-c12_ffi-cal.fits</a></li>
<li><a href="https://archive.stsci.edu/pub/k2/ffi/ktwo2017032102633-c12_ffi-cal.fits">ktwo2017032102633-c12_ffi-cal.fits</a></li>
</ul>

<b><i>First cadence</i></b>
<ul>
<li>Start Time: 2016-12-15 20:40:49 UTC</li>
<li>Long Cadence Number:136855</li>
<li>Short Cadence Number: 4094110 </li>
</ul>

<b><i>Last cadence</i></b>
<ul>
<li>End Time: 2017-03-04 18:37:47 UTC</li>
<li>Long Cadence Number: 140716</li>
<li>Short Cadence Number: 4209969</li>
</ul>

<b><i>Most Recent Processing Version</i></b>
<ul>
<li> <a href="k2-pipeline-release-notes.html#data-release-18">Data Release 18</a> </li>
</ul>

</div>

<div class="col-lg-7">

<div class="thumbnail">
<div class="caption">
<i>Figure C12-FOV: Schematic of Kepler's C12 field-of-view with observed targets shown with purple dots.</i>
</div>
<a href="images/release-notes/c12/C12_selected.png">
<img src="images/release-notes/c12/C12_selected.png" class="img-responsive" alt="C12 field-of-view with selected targets plotted in purple.">
</a>
</div>

<div class="thumbnail">
<div class="caption">
<i>Figure C12-Mag: Distribution of the Kepler magnitudes of observed targets. All targets are chosen by guest observers. The distribution is due to how the largest <a href ="k2-approved-programs.html#campaign-12">GO Programs</a> were selected.</i>
</div>
<a href="images/release-notes/c12/c12_lc_magnitude_distribution.png">
<img src="images/release-notes/c12/c12_lc_magnitude_distribution.png" class="img-responsive" alt="Distribution of the Kepler magnitudes of observed LC targets.">
</a>
</div>

</div>

<h2>Features and Events</h2>

***Mars***

Mars passed through the focal plane during C12, entering active silicon on module
24 output 3 (channel 83) on 2017-01-16 (relative cadence index 1550) and
moving off of module 3 output 4 (dead channel 8) on 2017-02-09
(relative cadence index 2728). The movie *C12-Mars-at-LC* below shows the
direct image of Mars passing over channel 83.
With an average visual magnitude of V ~ -0.2,
the image of Mars is highly saturated, introduces
significant scattered light, and creates a
video crosstalk signal in each of the other three channels of the module on
which it falls. In addition, there is a ghost
image of Mars caused by reflection off of the field-flattener lens and CCD then
off of the Schmidt correcter and back to the focal plane. This ghost image
appears approximately on the opposite side of the boresight from the direct
Mars image. An example of the direct image with crosstalk and the ghost image
is shown in the figures below (*C12-Module-8 Mars FFI Image*,
*C12-Channel-62 Mars Ghost Image*) taken from the second FFI:
ktwo2017032102633-c12_ffi-cal.fits.

<div class="thumbnail" style="width: 90%;">
<div class="caption">
<i>Figure C12-Mars-at-LC: Mars entered the focal plane on channel 83 and is
seen here passing through the LC target pixel apertures on this channel in
just over two days (105 cadences).
The saturated columns from the core of the image
extend over all rows in the channel.</i>   
</div>
<video id="pelican-installation" class="video-js vjs-default-skin" controls loop
preload="auto"  "width="99%"
data-setup="{}">
<source src="images/release-notes/c12/ch83_Mars_movie_c12.mp4" type='video/mp4' alt="Movie of Mars transiting across channel 83 as seen through long cadence target apertures">
</video>
</div>

<div class="thumbnail" style="width: 47%;display: inline-block;">
<div class="caption">
<i>Figure C12-Module-8 Mars FFI Image: the impact of the direct image of Mars from the field-flattener lens ghosts, diffraction spikes, saturated columns, and video crosstalk signals are evident in this stretched image from the calibrated FFI ktwo2017032102633-c12_ffi-cal.fits.</i>   
</div>
<a href="images/release-notes/c12/c12_ffi2_mod8.png">
<img src="images/release-notes/c12/c12_ffi2_mod8.png" class="img-responsive" alt="Module-8 Mars direct image, scattered light, and crosstalk">
</a>
</div>

<div class="thumbnail" style="width: 43%;display: inline-block;">
<div class="caption">
<i>Figure C12-Channel-62 Mars Ghost Image: the large spatial extent and complex structure of the Schmidt corrector ghost image of Mars is striking in this stretched image from the calibrated FFI ktwo2017032102633-c12_ffi-cal.fits.</i>
</div>
<a href="images/release-notes/c12/c12_ffi2_mod18.png">
<img src="images/release-notes/c12/c12_ffi2_mod18.png" class="img-responsive" alt="Module-18 Schmidt corrector ghost image of Mars.">
</a>
</div>


A more quantitative understanding of
the signals from Mars can be gained from the raw flux profiles below of
Mars and its ghost image, taken from the same FFI. The profile shows a
slice through the direct image for a rough guide to the
azimuthally-averaged part of the image. Note that the saturation
spills across all CCD rows for the central columns of the Mars image
and the diffraction spikes extend over multiple channels.
Spikes in the profile plot are caused by
stray stars. Users should also note that the median rate of motion of
Mars is 11 pixels per Long Cadence.


<div class="thumbnail" style="width: 90%;">
<div class="caption">
<i>Figure C12 Mars Flux Profile: </i>   
</div>
<a href="images/release-notes/c12/c12_mars_and_ghost_profile.png">
<img src="images/release-notes/c12/c12_mars_and_ghost_profile.png" class="img-responsive" alt="Flux distribution profile for Mars direct image and Mars Schmidt corrector ghost image.">
</a>
</div>


For users wishing to have a better idea when Mars may have affected the data from
particular targets, pipe-delimited text files for the path of Mars
<a href="images/release-notes/c12/c12_mars_direct.txt">c12_mars_direct.txt</a>
and its ghost <a href="images/release-notes/c12/c12_mars_ghost.txt">
c12_mars_ghost.txt</a> during the middle of C12 have been generated using the
<a href="https://ssd.jpl.nasa.gov/?horizons">JPL Horizons website</a>.
The location of Mars was calculated from the Kepler-o-centric (NAIF Id = -227)
RA and DEC. The location of Mars and its ghost in the FFI are in the
headers of the respective files.

The location of the ghost was calculated by rotating the
RA and DEC of Mars around the boresight by 180 degrees and is approximate due to
variations of the CCD and field-flattener lens positions and orientations
from the ideal focal plane. Based on the FFI and the long cadence pixel data,
the ghost can vary in position by up to ~100 pixels from the locations given in
the table. Given this variation and the large size of the ghost image,
users might be advised to use caution if their target is within
200 pixels from the (predicted) ghost
image and 350 pixels from the direct image of Mars.  


<br>

***Galaxies***

There are 2576 galaxies targeted in the high Galactic latitude (-60º) C12 field of view.


<br>

***Pointing and Roll Performance***

The C12 pointing and roll behavior are within the limits of that seen
in other K2 campaigns for the majority of the campaign.
The pipeline calculated maximum distance between the
derived and nominal positions for any target (the "maximum attitude residual", or MAR)
for C12 is well under the 3-pixel limit accommodated by the aperture halos,
except for one 6-hour period starting at 2017-03-03 19:05:24 near the end
of the campaign. Cadence numbers 140670-140681 have a roll error of more than
-50 arcseconds, though roll performance returned to normal at the
subsequent thruster firing
and remained nominal for the rest of the campaign.

<div class="thumbnail" style="width: 49%;display: inline-block;">
<div class="caption">
<i>Figure C12-Roll-Error: the roll-error between the photometrically derived attitude (PAD) and the nominal pointing plotted against time for C12.</i>   
</div>
<a href="images/release-notes/c12/c12_pad_pdq_attitude_roll.png">
<img src="images/release-notes/c12/c12_pad_pdq_attitude_roll.png" class="img-responsive" alt="Pipeline measured roll error for C12.">
</a>
</div>

<div class="thumbnail" style="width: 49%;display: inline-block;">
<div class="caption">
<i>Figure C12-MAR: the maximum distance between the photometrically derived attitude (PAD) and the nominal position plotted against time for C12.</i>
<a href="images/release-notes/c12/c12_pad_pdq_attitude_mar.png">
<img src="images/release-notes/c12/c12_pad_pdq_attitude_mar.png" class="img-responsive" alt="Maximum residual of the C12 attitude measured with PAD and PDQ.">
</a>
</div>
</div>


<br>

***Safe Mode and Loss of Engineering Data***
On 2017-02-01 15:06 UTC the spacecraft entered safe mode. The safe mode was
likely due to a flight software reset, which has occurred several times during the
Kepler/K2 mission. The recovery from this safe mode was routine and the spacecraft
resumed science data collection at 2017-02-06 20:47 UTC. The total time lost to this
safe mode was 5.3 days.

In order to minimize the science data loss, the project decided not to downlink
stored engineering data during during the safe mode recovery. This decision resulted
in the loss of ~10 days of engineering data, starting 2017-01-25 08:16 UTC and
extending into the safe mode. No stored science data were lost. The engineering
data includes the thruster firing data, so there is no thruster firing
information from the spacecraft for this time period. In order to fill in the
thruster firing information in the archive data files, we used the short cadence
pointing history to detect likely thruster firings during the data gap. If the
thruster firing could be unambiguously identified within a SC interval, a thruster
firing was flagged in the QUALITY and SAP_QUALITY fields (bit 21). If the thruster
firing appeared to span SC intervals, both intervals would be flagged with a
possible thruster firing (bit 20). Users should be alert to possible missed
thruster firings in the interval from 2017-01-25 08:16 UTC to the start of the
safe mode at 2017-02-01 15:06 UTC.

<br>

<h2>Data Quality and Processing Notes</h2>

***Light Curve Quality***

As in previous campaigns, the 6-hour spacecraft roll cycle continues
to dominate the systematic
errors in C12 simple aperture photometry light curves. In spite of the sparse
nature of the C12 field of view, the pipeline CDPP 12th magnitude noise
benchmark is 20% higher than what was seen in star fields of comparable star
density (55 ppm in C12 vs 42 ppm in C6 and 47 ppm in C8). The passage of Mars
most significantly affected CDPP on the channels with the
direct and ghost images; however, excluding these channels does not lower
the 12th magnitude CDPP benchmark value. The project is investigating this
performance change to better understand the change in CDPP as a function
of magnitude, position, color, etc., and to see if it can be traced
to a spacecraft, or a pipeline processing change.

The magnitude dependence of CDPP and its distribution over the focal
plane are shown below. Other CDPP benchmarks can be found in the
<a href="images/release-notes/c12/c12_bin1.00_sc1.00_CDPP_Summary_17070516.txt">
table giving 6.5-hr CDPP as a function of magnitude.</a>
<br>
<div class="thumbnail" style="width: 90%;">
<div class="caption">
<i>Figure C12-CDPP: 6.5-hr CDPP measurements for all targets as a function of Kepler magnitude. Dim targets have poorer overall photometric precision than bright targets, but can look better because the residual sawtooth falls below the noise floor. The saturated targets tend to have the lowest CDPP, but often show a residual sawtooth. </i>   
</div>
<a href="images/release-notes/c12/c12_logg_CDPP_vs_model.png">
<img src="images/release-notes/c12/c12_logg_CDPP_vs_model.png" class="img-responsive" alt="CDPP measured for all targets as a function of Kepler magnitude.">
</a>
</div>
<div class="thumbnail" style="width: 90%;">
<div class="caption">
<i>Figure C12-CDPP FocalPlane: 6.5-hr CDPP measured as a function of position on the focal plane, for 12th and 14th magnitude dwarf stars. The photometric precision is generally better near the center of the focal plane where the variations in roll angle produce less pixel motion. All cadences coincident with a definite thruster firing are gapped.</i>
<a href="images/release-notes/c12/c12_dwarf_CDPP_by_mod_out.png">
<img src="images/release-notes/c12/c12_dwarf_CDPP_by_mod_out.png" class="img-responsive" alt="CDPP per channel for 12th magnitude dwarfs">
</a>    
</div>
</div>

<br>

<hr>


# K2 Campaign 11

<h2>At a glance</h2>

<div class="col-lg-5">

<p>
Campaign 11 was operationally separated into two segments as a result of an
error in the initial roll-angle used to minimize solar torque on the spacecraft.
The larger than expected roll motion seen at the start of the campaign meant
that the targets would be rolling out of their pixel apertures by the end of the
campaign. The excess roll motion was corrected twenty-three days into the campaign
by applying a -0.32º roll offset. The size of this correction meant
that new target aperture definitions
had to be used for the second part of the campaign.
The two segments are identified in the
archive products as C111 and C112, respectively.
</p>

<b><i>C11a Pointing</i></b>
<ul>
<li>RA: 260.3880064 degrees</li>
<li>Dec: -23.9759578 degrees</li>
<li>Roll: 176.7437075 degrees</li>
</ul>

<b><i>C11b Pointing</i></b>
<ul>
<li>RA: 260.3880064 degrees</li>
<li>Dec: -23.9759578 degrees</li>
<li>Roll: 176.4237075 degrees</li>
</ul>

<b><i>C11b pointing offset from C11a</i></b>
<ul>
<li>delta-RA: 0.0 degrees</li>
<li>delta-Dec: 0.0 degrees</li>
<li>delta-Roll: -0.32 degrees</li>
</ul>

<b><i>C11a First cadence</i></b>
<ul>
<li>Time: 2016-09-24 19:12:30 UTC</li>
<li>Long Cadence Number: 132839</li>
<li>Short Cadence Number: 3973630</li>
</ul>

<b><i>C11a Last cadence</i></b>
<ul>
<li>Time: 2016-10-18 02:16:19 UTC</li>
<li>Long Cadence Number: 133979</li>
<li>Short Cadence Number: 4007859</li>
</ul>

<b><i>C11b First cadence</i></b>
<ul>
<li>Time: 2016-10-21 06:17:05 UTC</li>
<li>Long Cadence Number: 134134</li>
<li>Short Cadence Number: 4012480</li>
</ul>

<b><i>C11b Last cadence</i></b>
<ul>
<li>Time: 2016-12-07 23:23:03 UTC</li>
<li>Long Cadence Number: 136469</li>
<li>Short Cadence Number: 4082559</li>
</ul>

<b><i>C11 Targets</i></b>
<ul>
<li> 32884 (32580 in C11b) in long cadence (LC)</li>
<li> 67 (66 in C11b) in short cadence (SC)</li>
<li> 72 Custom targets include 64 Solar System moving objects tiled with multiple apertures, featuring Titan and Enceladus, 9 bright stars covered with disk apertures to capture the PSF wings, 22 late microlensing targets, and 5 galaxy targets. See the <a href="images/release-notes/c11/ktwoc111_caf.csv">C11a csv file</a> and <a href="images/release-notes/c11/ktwoc112_caf.csv">C11b csv file</a> to map the Solar system object custom aperture numbers to the target names.</li>
<li> No new targets were added for C11b. Because of the change in roll attitude, the positions of all the target apertures on the focal plane were changed, causing some targets to move to a different detector channel and some to fall off active silicon. 304 long cadence targets and 1 short cadence target were dropped in C11b.
</ul>

<b><i>Full Frame Images (FFI)</i></b>
<p>
The two C11 FFIs were taken at the C11a and C11b pointings respectively. The -0.32 degree roll offset
is evident when comparing the two images.
</p>
<ul>
<li><a href="https://archive.stsci.edu/pub/k2/ffi/ktwo2016279022810-c111_ffi-cal.fits">ktwo2016279022810-c111_ffi-cal.fits</a></li>
<li><a href="https://archive.stsci.edu/pub/k2/ffi/ktwo2016307123729-c112_ffi-cal.fits">ktwo2016307123729-c112_ffi-cal.fits</a></li>
</ul>

<b><i>Most Recent Processing Version</i></b>
<ul>
<li> <a href="k2-pipeline-release-notes.html#data-release-17">Data Release 17</a> </li>
</ul>

</div>


<div class="col-lg-7">

<div class="thumbnail">
<div class="caption">
<i>Figure C11-FOV: Schematic of Kepler's C11 field-of-view with observed targets shown with purple dots. The galactic plane passes through modules 2 and 6.</i>
</div>
<a href="images/release-notes/c11/C11_selected.png">
<img src="images/release-notes/c11/C11_selected.png" class="img-responsive" alt="C11 field-of-view with selected targets plotted in purple. The galactic plane passes through modules 2 and 6.">
</a>
</div>
<div class="thumbnail">
<div class="caption">
<i>Figure C11-Mag: Distribution of the Kepler magnitudes of observed targets. All targets are chosen by guest observers. The distribution is due to the <a href="k2-approved-programs.html#campaign-11">GO  programs</a> that were selected.</i>
</div>
<a href="images/release-notes/c10/c10LcMagDistribution.png">
<img src="images/release-notes/c10/c10LcMagDistribution.png" class="img-responsive" alt="Distribution of the Kepler magnitudes of observed C11 targets.">
</a>
</div>

</div>

<br style="clear:both;">

<h2>Features and Events</h2>

***Galactic Bulge***

The C11 field of view is the densest star field for which pipeline light curves have been created.
The average density of stars with magnitude 11.5 < Kp < 14.5 over the field of view is
6959 stars/deg^2. Detector channels covering the galactic bulge have densities as high
as 25,000 stars/deg^2. For comparison the average density of stars in this magnitude range
for the Kepler field of view is 900 stars/deg^2. As a result of the high star density, many
of the pipeline algorithms are operating outside of their design range. Users are cautioned
to treat the pipeline background, centroid, and aperture photometry results with care, especially
on channels covering the Galactic Bulge.
<div class="thumbnail">
<div class="caption">
<i>Figure C11-Star Density: The average density of stars with 11.5 < Kp < 14.5 for each channel
ranges from a few thousand to over 20,000 stars/deg^2.  The galactic plane passes through
modules 2 and 6. The numbers indicate the detector module and output number.</i>
</div>
<a href="images/release-notes/c11/k2_c11_star_density.jpg">
<img src="images/release-notes/c11/k2_c11_star_density.jpg" class="img-responsive" alt="C11 star
density ranges from a few thousand to over 20000 stars/deg^2.">
</a>
</div>

<br>

***Saturn***

Saturn (V = +1) and its bright moons Titan (V = +9), and Enceladus (V = +12) entered
channel 84 near the end of the campaign (Dec 3, ~12h UT) allowing ~4.5 days of observations.
Titan is ~18 pixels away from Saturn, while Enceladus is only 2-4 pixels from Saturn and
regularly passed through Saturn's saturated charge spill columns. Both Titan and Enceladus
were tiled with custom aperture masks.

<br>

***Attitude Offset and Segmenting of C11 Data***

The spacecraft attitude was adjusted by -0.32º in roll on 2016-10-21 to correct
the initial roll-offset error. Because this attitude offset was large enough to
require new target pixel apertures, the C11 data were processed through the
pipeline in two separate parts:
<ul>
<li>the first 23 days of data, dubbed C11a  
<li>the remaining 48 days of the campaign, dubbed C11b.
</ul>
The C11a files are found in the archive under Campaign number 111. The C11b
files have Campaign number 112. A search for Campaign 11 will return both sets of files.
Users should take care when combining data from C11a and C11b for targets. Because the
targets have changed pixels -and in some cases detectors- there is no guarantee that the
C11a and C11b fluxes will match in absolute value, or even slope across the C11a-C11b boundary.
The C11a and C11b data may need to be treated as coming from two separate campaigns.
The figures below give some examples of the behavior of SAP flux over C11.

In some cases, the updated C11b target apertures extended off the edge of the active
CCD and included rows of collateral smear, or columns of collateral black data. These
collateral data are evident in the TPFs and should not be used when doing photometry on
the target.
<div class="caption">
<i>Figure C11 SAP Flux: The C11a (red) and C11b (blue) SAP flux for four sample targets.
Because of the change of target pixel apertures between C11a and C11b, the fluxes can
differ in absolute value and in behavior with the K2 roll motion.</i>   
</div>
<div class="thumbnail" style="width: 49%;display: inline-block;">
<a href="images/release-notes/c11/epic221115664.png">
<img src="images/release-notes/c11/epic221115664.png" class="img-responsive" alt="C11 SAP flux for EPIC-221115664.">
</a>
</div>
<div class="thumbnail" style="width: 49%;display: inline-block;">
<a href="images/release-notes/c11/epic221326895.png">
<img src="images/release-notes/c11/epic221326895.png" class="img-responsive" alt="C11 SAP flux for EPIC-221326895.">
</a>
</div>
<br>
<div class="thumbnail" style="width: 49%;display: inline-block;">
<a href="images/release-notes/c11/epic221391462.png">
<img src="images/release-notes/c11/epic221391462.png" class="img-responsive" alt="C11 SAP flux for EPIC-221391462.">
</a>
</div>
<div class="thumbnail" style="width: 49%;display: inline-block;">
<a href="images/release-notes/c11/epic221597630.png">
<img src="images/release-notes/c11/epic221597630.png" class="img-responsive" alt="C11 SAP flux for EPIC-221597630.">
</a>
</div>


<br>

***Pointing and Roll Performance***

The C11a and C11b pointing and
roll behavior are within the limits of that seen in other K2 campaigns.
The pipeline calculated maximum distance between the
derived and nominal positions for any target (the "maximum attitude residual", or MAR)
for C11 is well under the 3-pixel limit accommodated by the aperture halos.  
The C11a attitude error started at a relatively high value and large roll amplitude,
due in part to the initial roll offset error. The negative going roll offsets
along with the large negative roll rate at the start of C11a indicated that,
without correction, the roll would have been unacceptably large in the 6-hours
between thruster firing windows by the end of the campaign. The large roll would have
caused targets at the edge of the focal plane to roll out of their apertures.
The roll offset was corrected during the gap starting
around 2016-10-16 seen in the C11-Pointing History figure, resulting in a roll profile
for C11b that is more typical of past campaigns.
Similarly, the C11a maximum attitude residual was
somewhat high -though well within the aperture limits- while the C11b
starting maximum attitude
residual was more typical of K2 behavior.

There was a smaller related change in roll behavior during C11a when the spacecraft
X-band communications were switched from low gain antenna 2(LGA-2) to LGA-1. The
antenna switch resulted in different thermal torque on the spacecraft and somewhat
mitigated the initial C11a roll pointing error. The improvement is most evident in the
roll rate at a solar elongation angle of -35º (top right panel below), but can be
seen in the roll error at around 2016-10-02 (top left panel below).

<div class="thumbnail" style="width: 45%;display: inline-block;">
<div class="caption">
<i>Figure C11-Pointing History: pointing performance for C11 was consistent with that of previous campaigns. The C11a-C11b transition occured at the gap around 2016-10-16.</i>
</div>
<a href="images/release-notes/c11/c11_roll_error.png">
<img src="images/release-notes/c11/c11_roll_error.png" class="img-responsive" alt="Roll amplitude for C11 matched that of previous campaigns."></a>
</a>
</div>

<div class="thumbnail" style="width: 49%;display: inline-block;">
<div class="caption">
<i>Figure C11-Roll Rate: the C11 roll rate as a function of solar elevation angle
clearly shows the impact of the roll offset error (C3 is shown here for comparison). The large
negative roll rate during C11a was corrected with the roll offset change in C11b.</i>
<a href="images/release-notes/c11/c11_roll_rate.jpg">
<img src="images/release-notes/c11/c11_roll_rate.jpg" class="img-responsive" alt="Roll Drift rates for C11 indicate the improvement in performance with the corrected roll offset in C11b.">
</a>
</div>
</div>

<div class="thumbnail" style="width: 49%;display: inline-block;">
<div class="caption">
<i>Figure C11a-MAR: The maximum distance between the photometrically derived attitude (PAD) and the nominal position plotted against time for C11a.</i>
<a href="images/release-notes/c11/c11a_pad_pdq_attitude_mar.png">
<img src="images/release-notes/c11/c11a_pad_pdq_attitude_mar.png" class="img-responsive" alt="Maximum residual of the C11a attitude measured with PAD and PDQ.">
</a>
</div>
</div>

<div class="thumbnail" style="width: 49%;display: inline-block;">
<div class="caption">
<i>Figure C11b-MAR: The maximum attitude residual for C11b shows the pointing improvement at the
start of the sub-campaign.</i>
<a href="images/release-notes/c11/c11b_pad_pdq_attitude_mar.png">
<img src="images/release-notes/c11/c11b_pad_pdq_attitude_mar.png" class="img-responsive" alt="Maximum residual of the attitude measured with PAD and PDQ.">
</a>
</div>
</div>

<br>

<h2>Data Quality and Processing Notes</h2>

***Light Curve Quality***

We consider the C11a and C11b pipeline-generated light curves separately
for noise analysis and comparison with previous campaigns.
As in previous campaigns, the 6-hour spacecraft roll cycle
continues to dominate the systematic
errors in C11 simple aperture photometry light curves.

The magnitude dependence of CDPP and its distribution over the focal plane
are shown below. Other CDPP benchmarks can be found in the
<a href="images/release-notes/c11/c11a_bin1.00_sc1.00_CDPP_Summary_17042811.txt">
table giving C11a 6.5-hr CDPP as a function of magnitude</a> and
<a href="images/release-notes/c11/c11b_bin1.00_sc1.00_CDPP_Summary_17051815.txt">
the C11b 6.5-hr CDPP table.</a>
The stellar properties
for each target, available from the
<a href="http://archive.stsci.edu/k2/epic/search.php">EPIC catalog</a>,
were used to distinguish dwarf and giant stars. The C11
CDPP values are in family with C7, the next most crowded K2 FOV for which
pipeline light curves were generated.
<br>

<div class="caption">
<i>Figure C11-CDPP: 6.5-hr CDPP measurements for C11a targets (left) and C11b targets (right) as a function of Kepler magnitude. Dim targets have poorer overall photometric precision than bright targets, but can look better because the residual sawtooth falls below the noise floor. The saturated targets tend to have the lowest CDPP, but often show a residual sawtooth. </i>   
</div>
<div class="thumbnail" style="width: 49%;display: inline-block;">
<a href="images/release-notes/c11/c11a_logg_CDPP_vs_model.png">
<img src="images/release-notes/c11/c11a_logg_CDPP_vs_model.png" class="img-responsive" alt="CDPP measured for all targets as a function of Kepler magnitude.">
</a>
</div>

<div class="thumbnail" style="width: 49%;display: inline-block;">
<a href="images/release-notes/c11/c11b_logg_CDPP_vs_model.png">
<img src="images/release-notes/c11/c11b_logg_CDPP_vs_model.png" class="img-responsive" alt="CDPP measured for all targets as a function of Kepler magnitude.">
</a>
</div>

<div class="caption">
<i>Figure C11-CDPP Focal Plane: 6.5-hr CDPP for C11a (left) and C11b (right) dwarf targets across the focal plane. Panels show the 10th percentile (left) and median (right) CDPP metric for all dwarf targets in the 12th (top) and 14th (bottom) magnitude range. The photometric precision is generally better near the center of the focal plane where the variations in roll angle produce less pixel motion. All cadences coincident with a definite thruster firing are gapped.</i>
</div>
<div class="thumbnail" style="width: 49%;display: inline-block;">
<a href="images/release-notes/c11/c11a_dwarf_CDPP_by_channel.png">
<img src="images/release-notes/c11/c11a_dwarf_CDPP_by_channel.png" class="img-responsive" alt="CDPP per channel for all 12th magnitude stars">
</a>    
</div>

<div class="thumbnail" style="width: 49%;display: inline-block;">
<a href="images/release-notes/c11/c11b_dwarf_CDPP_by_mod_out.png">
<img src="images/release-notes/c11/c11b_dwarf_CDPP_by_mod_out.png" class="img-responsive" alt="CDPP per channel for all 12th magnitude stars">
</a>    
</div>

***Targets Missing from the Archive***

Pipeline errors during the process of exporting the light curve (LCV) and
target pixel (TP) FITS files resulted in targets from both C11a and C11b
having no LCV or TP files at the archive.
There are <a href="images/release-notes/c11/c11a_missing_export_target_epic_ids.txt">194
missing targets for C11a</a> (15 are non-custom targets) and
<a href="images/release-notes/c11/c11b_missing_export_target_epic_ids.txt">3
missing custom-aperture targets for C11b</a>. There is no overlap between the C11a
and C11b missing target lists. The project is investigating options
for delivering these targets in the future.
<br>

***Poor Smear Correction - Bright Stars***

There were several very bright stars observed in C11 with saturation spilling
over all rows of the array on *three* channels, corrupting the smear measurement
for the affected columns. For these columns
the virtual smear measurement is used for smear correction,
though it is known that this value is invalid and will corrupt data on the
affected columns. Given the normal motion of the stars in K2 due to roll and
differential velocity aberration, it is likely
that adjacent columns will be corrupted at some times during the campaign. The
smear corruption is complicated in C11 due to the roll offset: stars at the edge
of the array moved up to 30 pixels from C11a to C11b, while stars in the center
modules moved only slightly. The channels and affected columns in C11a and C11b
are given below.

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;}
.tg th{font-family:Arial, sans-serif;font-size:14px;font-weight:normal;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;}
.tg .tg-baqh{text-align:center;vertical-align:top}
.tg .tg-25al{font-size:10px;vertical-align:top}
.tg .tg-yw4l{vertical-align:top}
</style>
<table class="tg">
<div class="caption">
<i>Channels with corrupt smear measurments due to saturating stars on the specified
columns for C11a and C11b</i>
</div>
<tr>
<th class="tg-yw4l">Channel</th>
<th class="tg-yw4l">C11a columns</th>
<th class="tg-yw4l">C11b columns</th>
</tr>
<tr>
<td class="tg-yw4l">35</td>
<td class="tg-baqh">888-892</td>
<td class="tg-baqh">858-861</td>
</tr>
<tr>
<td class="tg-yw4l">43</td>
<td class="tg-baqh">162-165</td>
<td class="tg-baqh">160-162</td>
</tr>
<tr>
<td class="tg-yw4l">58</td>
<td class="tg-baqh">167-169</td>
<td class="tg-baqh">154-158</td>
</tr>
</table>
<br>

***LDE Flags***

During the last three days of C11b we experienced a large number of parity errors coming from the photometer's local detector electronics (LDE). These LDE parity errors can occur when a very bright object saturates and spills charge into the CCD serial readout register, causing an overflow at the input to the analog-to-digital converter. The LDE parity errors were likely caused by the image of Saturn on the focal plane. These errors do not affect the quality of data from pixels on the active focal plane.

The LDE parity error triggers a flag (bit 15, decimal=16384) in the QUALITY column of the target pixel files. Most of the cadences from long cadence number 136276 (2016-12-4 00:58 UTC) to LC 136426 (2016-12-7 02:32 UTC) have the parity error flag set.

<br>

<hr>


# K2 Campaign 10

<h2>At a glance</h2>

<div class="col-lg-5">

<p>
Campaign 10 was operationally separated into two segments as a result of a 3.5-pixel
initial pointing error at the start of the campaign. The offset was corrected
six days into the campaign. The two segments are identified in the
archive products as C101 and C102, respectively.
</p>

<b><i>C10 Pointing</i></b>
<ul>
<li>RA: 186.7794430 degrees</li>
<li>Dec: -4.0271572 degrees</li>
<li>Roll: 157.6280500 degrees</li>
</ul>

The C10a offset from the desired pointing (nominal - measured) was
<ul>
<li>delta-RA: 12.12951918 arcsec</li>
<li>delta-Dec: -4.12973550 arcsec</li>
<li>delta-Roll: -8.00606815 arcsec</li>
</ul>

<b><i>C10a First cadence</i></b>
<ul>
<li>Time: 2016-07-06 19:45:29 UTC</li>
<li>Long Cadence Number: 128925</li>
<li>Short Cadence Number: 3856210</li>
</ul>

<b><i>C10a Last cadence</i></b>
<ul>
<li>Time: 2016-07-13 01:19:55 UTC</li>
<li>Long Cadence Number: 129230</li>
<li>Short Cadence Number: 3865389</li>
</ul>

<br>

<b><i>C10b First cadence</i></b>
<ul>
<li>Time: 2016-07-13 01:49:21 UTC</li>
<li>Long Cadence Number: 129231</li>
<li>Short Cadence Number: 3865390</li>
</ul>

<b><i>C10b Last cadence before 14-day gap due to Mod-4 failure</i></b>
<ul>
<li>Time: 2016-07-20 06:26:44 UTC</li>
<li>Long Cadence Number: 129583</li>
<li>Short Cadence Number: 3875979</li>
</ul>

<b><i>C10b First cadence after gap</i></b>
<ul>
<li>Time: 2016-08-03 06:51:51 UTC</li>
<li>Long Cadence Number: 130269</li>
<li>Short Cadence Number: 3896530</li>
</ul>

<b><i>C10b Last cadence</i></b>
<ul>
<li>Time: 2016-09-20 04:52:03 UTC</li>
<li>Long Cadence Number: 132614</li>
<li>Short Cadence Number: 3966909</li>
</ul>

<b><i>C10 Targets</i></b>
<ul>
<li>  41,607 in long cadence (LC)</li>
<li>  138 in short cadence (SC)</li>
<li>  Custom targets include 16 Solar System moving objects tiled with multiple apertures, 8 bright stars covered with disk apertures to capture the PSF wings, and 27 large galaxies. See the <a href="images/release-notes/c10/ktwoc10_caf.csv">csv file that maps</a> the Solar system object custom aperture numbers to the target names.</li>
</ul>

<b><i>Full Frame Images (FFI)</i></b>
<p>
Both C10 FFIs were taken at the C10b pointing.
The first includes data from module~4,
the second does not.
</p>
<ul>
<li><a href="https://archive.stsci.edu/pub/k2/ffi/ktwo2016199030108-c102_ffi-cal.fits">ktwo2016199030108-c102_ffi-cal.fits</a></li>
<li><a href="https://archive.stsci.edu/pub/k2/ffi/ktwo2016240074042-c102_ffi-cal.fits">ktwo2016240074042-c102_ffi-cal.fits</a></li>
</ul>

<b><i>Most Recent Processing Version</i></b>
<ul>
<li> <a href="k2-pipeline-release-notes.html#data-release-15">Data Release 15</a> </li>
</ul>

</div>

<div class="col-lg-7">

<div class="thumbnail">
<div class="caption">
<i>Figure C10-FOV: Schematic of Kepler's C10 field-of-view with observed targets shown with purple dots. Note that module 4, centered near RA = 193º, Dec = -2º, failed seven days into C10b, so targets on channels 9--12 have truncated data sets.</i>
</div>
<a href="images/release-notes/c10/c10_selected.png">
<img src="images/release-notes/c10/c10_selected.png" class="img-responsive" alt="C10 field-of-view with selected targets plotted in purple.">
</a>
</div>
<div class="thumbnail">
<div class="caption">
<i>Figure C10-Mag: Distribution of the Kepler magnitudes of observed targets. All targets are chosen by guest observers. The distribution is due to the <a href="k2-approved-programs.html#campaign-10">GO  programs</a> that were selected.</i>
</div>
<a href="images/release-notes/c10/c10LcMagDistribution.png">
<img src="images/release-notes/c10/c10LcMagDistribution.png" class="img-responsive" alt="Distribution of the Kepler magnitudes of observed C10 targets.">
</a>
</div>

</div>

<br style="clear:both;">

<h2>Features and Events</h2>

***Galaxies***

With its high Galactic latitude, Campaign 10 observed 4,977 galaxies,
over 2,000 more than in C8. Twenty-seven large galaxies were each
covered using 1,500 pixel custom masks. The extragalactic targets
include the well-known quasar 3C 273 (EPIC 229151988).

<br>

***Comet 67P: Churyumov-Gerasimenko***

Comet 67P was observed in C10b from September 7 through September 20 as it crossed
channels 69 and 70. The comet was observed using 2200 custom aperture tiles.

<br>

***Segmenting of C10 Data***

The C10 data were processed through the pipeline in two separate sets:
<ul>
<li>The first six days of data, dubbed C10a, were collected with a pointing error of 3.5 pixels from the nominal field-of-view, so they were only processed through CAL to make Type 1 target pixel files and collateral data files.
<li>The remainder of the campaign, dubbed C10b, was processed through the entire photometry pipeline, creating Type 2 target pixel files, long-cadence light curves, and collateral data files.
</ul>
The C10a files are found in the archive under Campaign number 101, and the C10b
files have Campaign number 102. A search for Campaign 10 will return both sets of files.

**Attitude Offset in C10a**

C10a data collection started with a pointing error from the intended C10 attitude of
3.5 pixels. This pointing offset potentially invalidates
many of the target pixel apertures. The apertures for data collection
include the pixels needed for photometry plus additional halos to allow
for pointing errors or target catalog errors. Two halos are used in the center of
the array and three halos are used in the outer portions to account
for the increased roll-induced motion of targets further from the center
of the array. Since the C10a initial pointing error
was 3.5 pixels, it is likely that significant flux from target stars fell outside
their aperture during the K2 roll cycle. Users should check the validity of the
aperture for their particular target in C10a before interpreting the flux measurements.

The spacecraft attitude was adjusted at 2016-07-13 01:49:21 UTC to correct
the pointing error, marking the start of C10b.

<br>

**Loss of Module 4**

An additional complication arises in the C10b data due to the loss of
module 4 seven days into C10b (around 2017-07-20 07:00 UT), which powered off the
photometer resulting in a 14-day data gap. The cause of the module 4 failure is
not known, but the sequence of telemetry faults leading up to the failure and the
post-recovery behavior of the focal plane are similar to those seen around the failures
of module 7 (January 2014) and module 3 (January 2010). These failures were
attributed to a blown fuse in the focal plane local detector electronics (LDE) driver
boards, likely due to the failure of an upstream component creating an
over-current load.

The C10b spacecraft pointing on either side of this data gap was consistent
and at the correct C10 attitude, so flux values should be consistent
across the gap. Note that PDC corrected fluxes may show inconsistent
systematic error corrections across the 14-day gap, as the cotrending
basis vectors can be dominated by systematics present on one side of the gap
but not the other side.

<br>


***Pointing and Roll Performance***

Apart from the initial pointing error in C10a, the C10a and C10b pointing and
roll behavior were typical of K2 campaigns. The cross-boresight pointing was
well behaved outside of the coarse point portion caused by the failure of
module 4 (see Figure C10-Pointing History). However, the photometer was off during
this time, so no coarse-point science data were collected. The roll behavior during
C10 was also nominal. The pipeline calculated maximum distance between the
derived and nominal positions for any target (the "maximum attitude residual", or MAR)
for C10b was well under the 3-pixel limit accommodated by the aperture halos.


<div class="thumbnail" style="width: 45%;display: inline-block;">
<div class="caption">
<i>Figure C10-Pointing History: pointing performance for C10 was consistent with that of previous campaigns. </i>
</div>
<a href="images/release-notes/c10/c10_pointing_history.png">
<img src="images/release-notes/c10/c10_pointing_history.png" class="img-responsive" alt="Roll amplitude for C10 matched that of previous campaigns."></a>
</a>
</div>

<div class="thumbnail" style="width: 49%;display: inline-block;">
<div class="caption">
<i>Figure C10-MAR: The maximum distance between the photometrically derived attitude (PAD) and the nominal position plotted against time for C10b.</i>
<a href="images/release-notes/c10/pad_pdq_attitude_mar.png">
<img src="images/release-notes/c10/pad_pdq_attitude_mar.png" class="img-responsive" alt="Maximum residual of the attitude measured with PAD and PDQ.">
</a>
</div>
</div>

<br>

<h2>Data Quality and Processing Notes</h2>

***Calibrated Target Pixel Files***

This data release consists of calibrated target pixel files (TPFs) and supporting
calibration files for C10a, as well as a full set of archive files (TPFs, calibration
files, and light curve files) for C10b.
The two separate sets of calibrated TPFs for C10a and C10b
have filenames that contain "C101" and "C102" respectively.

Because the full pipeline was not run, the C10a TPFs are Type-1 files.
The C10b TPFs are Type-2 and contain all the nominal calibration information.
See [Type-1 vs Type-2 TPFs](#type1v2) for details on the contents of the Type-1
versus Type-2 files.

Since the thruster firing flags are not populated in FITS quality flags for the
C10a Type-1 TPFs, they are delivered as separate
long-cadence <a href="http://archive.stsci.edu/missions/k2/thruster_firings/thruster_firing_flags_c10_lc.csv">(thruster_firing_flags_C10_lc.csv)</a>
and short-cadence <a href="http://archive.stsci.edu/missions/k2/thruster_firings/thruster_firing_flags_c10_sc.csv">(thruster_firing_flags_C10_sc.csv)</a>
thruster firing tables for the combined C10a + C10b campaign. Thruster firing
flags are populated in the FITS quality flag in the C10b Type-2 TPFs.


<br>

***Light Curve Quality***

We consider only the C10b pipeline-generated light curves
for noise analysis and comparison with previous campaigns.
As in previous campaigns, the 6-hour spacecraft roll cycle
continues to dominate the systematic
errors in C10 simple aperture photometry light curves.

The magnitude dependence of CDPP and its distribution over the focal plane
are shown below. Other CDPP benchmarks can be found in the
<a href="images/release-notes/c10/c10-postDQAU-PMD_2487_bin1.00_sc1.04_CDPP_Summary.txt">
table giving 6.5-hr CDPP as a function of magnitude.</a> The stellar properties
for each target, available from the
<a href="http://archive.stsci.edu/k2/epic/search.php">EPIC catalog</a>,
were used to distinguish dwarf and giant stars. The C10b
CDPP values compare favorably with those from C8 and other nominal K2 campaigns.
<br>

<div class="thumbnail" style="width: 90%;">
<div class="caption">
<i>Figure C10b-CDPP: 6.5-hr CDPP measurements for all targets as a function of Kepler magnitude. Dim targets have poorer overall photometric precision than bright targets, but can look better because the residual sawtooth falls below the noise floor. The saturated targets tend to have the lowest CDPP, but often show a residual sawtooth. </i>   
</div>
<a href="images/release-notes/c10/c10-postDQAU_PMD_2487_logg_TMCDPP_vs_model.jpg">
<img src="images/release-notes/c10/c10-postDQAU_PMD_2487_logg_TMCDPP_vs_model.jpg" class="img-responsive" alt="CDPP measured for all targets as a function of Kepler magnitude.">
</a>
</div>
<div class="thumbnail" style="width: 90%;">
<div class="caption">
<i>Figure C10b-CDPP Focal Plane: 6.5-hr CDPP for dwarf targets. Panels show the 10th percentile (left) and median (right) CDPP metric for all dwarf targets in the 12th (top) and 14th (bottom) magnitude range. The photometric precision is generally better near the center of the focal plane where the variations in roll angle produce less pixel motion. All cadences coincident with a definite thruster firing are gapped.</i>
<a href="images/release-notes/c10/c10-postDQAU_dwarfs__TMCDPP_by_channel.png">
<img src="images/release-notes/c10/c10-postDQAU_dwarfs__TMCDPP_by_channel.png" class="img-responsive" alt="CDPP per channel for all 12th magnitude stars">
</a>    
</div>
</div>

<br>

***Poor Smear Correction - Bright Stars***

There are two channels in C10 containing very bright stars with saturation spilling
over all rows of the array, corrupting the smear measurement.
On channel 28 (mod.out 9.4) saturated charge from HD 110380 (V=3.5) spills across all
rows of columns 829 & 830 in C10a and 831 & 832 in C10b.
On channel 65 (19.1) saturated charge from HD 107259 (V=3.9) spills across all rows
of columns 961 & 962 in C10a and 962 & 963 in C10b.
In both cases, the virtual smear measurement is used for smear correction,
though it is known that this value is invalid and will corrupt data on
these columns. Given the normal motion of the stars in K2 due to roll and
differential velocity aberration, it is likely
that adjacent columns will be corrupted at some times during the campaign.


<br>

<hr>


# K2 Campaign 9

<h2>At a glance</h2>

<div class="col-lg-5">

<p>
Campaign 9 was flown in the forward velocity vector direction to observe the
star-rich region around the Galactic bulge in search of microlensing events. In
order to maximize data collection capabilities, the campaign was conducted in
two parts with a mid-campaign data downlink and a ~0.6 pixel offset between the
two subfields known as C9a and C9b, identified in the archive products as C91
and C92, respectively.
</p>

<b><i>C9a Pointing</i></b>
<ul>
<li>RA: 270.3544823 degrees</li>
<li>Dec: -21.7798098 degrees</li>
<li>Roll: 0.4673417 degrees</li>
</ul>

<b><i>C9a Targets</i></b>
<ul>
<li>3,481 in long cadence (LC)</li>
<li>12 in short cadence (SC)</li>
<li>76 unique custom targets were selected in C9. Three million of the total 3.3 million C9 target pixels were used to construct microlensing super apertures on 5 channels around the Galactic bulge. See the <a href="images/release-notes/c9/ktwoc91_caf.csv">csv file that maps</a> the custom aperture number to the target name.</li>
</ul>

<b><i>C9a First cadence</i></b>
<ul>
<li>Time: 2016-04-22 14:04:59 UTC</li>
<li>Long Cadence Number: 125243</li>
<li>Short Cadence Number: 3745750</li>
</ul>

<b><i>C9a Last cadence</i></b>
<ul>
<li>Time:  2016-05-18 22:42:26 UTC</li>
<li>Long Cadence Number: 126532</li>
<li>Short Cadence Number: 3784449</li>
</ul>

<br>

<b><i>C9b Pointing</i></b>
<ul>
<li>RA: 270.3543824 degrees</li>
<li>Dec: -21.7804700 degrees</li>
<li>Roll: 0.4673417 degrees</li>
</ul>

<b><i>C9b Targets</i></b>
<ul>
<li>3,614 in long cadence (LC)</li>
<li>13 in short cadence (SC)</li>
<li>132 additional long-cadence  microlensing targets and 1 short-cadence target were added to the C9a target list for C9b. See the <a href="images/release-notes/c9/ktwoc92_caf.csv">csv file that maps</a> the custom aperture number to the target name.</li>
</ul>

<b><i>C9b First cadence</i></b>
<ul>
<li>Time: 2016-05-22 14:58:45 UTC</li>
<li>Long Cadence Number: 126713</li>
<li>Short Cadence Number: 3789850 </li>
</ul>

<b><i>C9b Last cadence</i></b>
<ul>
<li>Time: 2016-07-02 22:34:52 UTC</li>
<li>Long Cadence Number: 128734 </li>
<li>Short Cadence Number: 3850509 </li>
</ul>

<b><i>Full Frame Images (FFI)</i></b>
<ul>
<li><a href="https://archive.stsci.edu/pub/k2/ffi/ktwo2016119231109-c91_ffi-cal.fits">ktwo2016119231109-c91_ffi-cal.fits</a></li>
<li><a href="https://archive.stsci.edu/pub/k2/ffi/ktwo2016153221424-c92_ffi-cal.fits">ktwo2016153221424-c92_ffi-cal.fits</a></li>
</ul>

<b><i>Most Recent Processing Version</i></b>
<ul>
<li> <a href="k2-pipeline-release-notes.html#data-release-12">Data Release 12</a> </li>
</ul>

</div>

<div class="col-lg-7">

<div class="thumbnail">
<div class="caption">
<i>Figure C9-FOV: Schematic of Kepler's C9 field-of-view with observed targets shown with purple dots.</i>
</div>
<a href="images/release-notes/c9/C9_selected.png">
<img src="images/release-notes/c9/C9_selected.png" class="img-responsive" alt="C9 field-of-view with selected targets plotted in purple.">
</a>
</div>
<div class="thumbnail">
<div class="caption">
<i>Figure C9-Mag: Distribution of the Kepler magnitudes of observed targets. All targets are chosen by guest observers. The distribution is due to the <a href="k2-approved-programs.html#campaign-9">GO  programs</a> that were selected. Note that the small number of targets is due to the fact that the majority of pixels were in the microlensing super apertures.</i>
</div>
<a href="images/release-notes/c9/c9LcMagDistribution.png">
<img src="images/release-notes/c9/c9LcMagDistribution.png" class="img-responsive" alt="Distribution of the Kepler magnitudes of observed targets.">
</a>
</div>

</div>

<br style="clear:both;">

<h2>Features and Events</h2>

***Microlensing Toward the Galactic Bulge***

The <a href="k2-c9.html">C9 campaign</a> was dedicated
to a microlensing study of targets in the direction of the Galactic Bulge. As
such, there were a number of unique aspects to the campaign:
<ul>
<li> The spacecraft observed in the forward velocity vector direction to allow for simultaneous observations of targets from Earth.
<li> Three million of the 3.3 million pixels were in dedicated super apertures around the Galactic Bulge. Because these pixels do not have traditional star target apertures, light curves were not generated by the pipeline and we are delivering calibrated pixels only. In addition, there were a number of individual targets outside the super apertures that were added late as they showed microlensing signatures detected by ground-based surveys.
<li> The campaign was split into two parts in order to double the available on-board data storage, enabling coverage of the entire high-priority bulge region. This also accomodated the addition of late high-value microlensing targets and allowed for a mid-campaign subpixel pointing offset.
</ul>

<div class="thumbnail">
<div class="caption">
<i>Figure C9 Microlensing super apertures: the super apertures (highlighted in green) were comprised of 3 million pixels on five CCD channels.  Together they combined to cover the near-contiguous region in the sky in the C9 footprint where the highest number of microlensing events were expected. The numbers annotate the CCD channel identifiers in both module.output notation (e.g. 10.3) and channel number notation (e.g. #31). The super apertures were unchanged between C9a and C9b.
</i>
</div>
<a href="images/release-notes/c9/c9-microlensing-superstamp.png">
<img src="images/release-notes/c9/c9-microlensing-superstamp.png" class="img-responsive" alt="C9 microlensing super apertures on 5 channels around the Galactic bulge.">
</a>
</div>

<br>

***Emergency Mode***

Prior to the start of C9a, the spacecraft entered Safemode on 2016-04-07
00:05:06 UTC following a glitch on a data bus that left the spacecraft in an
unstable configuration. As a result of this misconfiguration, large attitude
excursions during Safemode led to a
Sun-avoidance fault that caused the spacecraft to enter Emergency mode
approximately two hours later.

In Emergency mode the spacecraft computer is
powered off, resetting all configurations and emptying stored science and
engineering data. The spacecraft is operated by a low-level controller that
maintains a Sun-safe attitude using thrusters. Since Kepler had never been in
Emergency mode, the operations team was careful in restoring the spacecraft
first to Safemode, which uses significantly less fuel, and then to normal
operations. The recovery was completed and C9a observations began on
2016-04-22, 14 days after the planned 2016-04-08 start, shortening the C9a
portion of the campaign by two weeks.

During Emergency mode the spacecraft clock was reset, so an updated time was loaded to the clock
prior to the start of C9a data collection. Subsequent timing observations on the ground determined that there
was a 4 second error in the uploaded spacecraft time. The Mission Operations Center made a
retroactive clock kernel update after C9a data collection was
completed, changing the time on-board the spacecraft by 4.2 seconds and allowing the
C9a data to be correctly time stamped once it hit the ground. As a result, both the C9a
and C9b data have the nominal 50 msec absolute accuracy, but the two
sets of cadences have an offset of 4.2 sec relative to each other.
The C9a data were collected 4.2 seconds later than expected based on
a uniform cadence interval across C9a and C9b.

<br>

***Pointing and Roll Performance***

The C9a and C9b pointing and roll behavior were typical of K2 campaigns despite
the forward velocity vector orientation. There were two notable pointing
excursions during the campaign: a commanded pointing offset for C9b, and an
uncommanded impulsive roll offset observed during C9b.


<div class="thumbnail" style="width: 45%;display: inline-block;">
<div class="caption">
<i>Figure C9-Pointing History: pointing performance for C9 was consistent with that of previous campaigns. The roll amplitude and roll rate were in family with previous campaigns.</i>
</div>
<a href="images/release-notes/c9/c9_pointing_history.png">
<img src="images/release-notes/c9/c9_pointing_history.png" class="img-responsive" alt="Roll amplitude for C9 matched that of previous campaigns despite the forward velocity vector orientation"></a>
</a>
</div>

<div class="thumbnail" style="width: 49%;display: inline-block;">
<div class="caption">
<i>Figure C9-Roll Rate: the C9 roll rate as a function of solar elevation angle
is consistent with previous campaigns (C4 is shown here for comparison) despite
the reversed motion of the Sun as seen by the spacecraft due to the forward facing
orientation.</i>
<a href="images/release-notes/c9/c9_roll_rate.png">
<img src="images/release-notes/c9/c9_roll_rate.png" class="img-responsive" alt="Roll Drift rates for C9 matched t
hat of previous campaigns despite the forward velocity vector orientation.">
</a>
</div>
</div>

**Commanded Pointing Offset for C9b**

The Microlensing Science Team (MST) requested that a subpixel pointing offset
be introduced between C9a and C9b. The intent of the offset was to move the
star images 0.64 pixels (2.4 arc seconds) perpendicular to the K2 roll-induced
image motion in the microlensing super apertures. The offset causes the image
motion in the combined C9a + C9b campaign to better span the subpixel space,
facilitating image reconstruction photometry. Based on preliminary pointing
measurements collected from the spacecraft, the C9b offset met the intended goal.

<div class="thumbnail">
<div class="caption">
<i>Figure C9a-C9b Pointing Offset: the position of a model star on CCD channel
31 in the microlensing super aperture demonstrates that the C9b offset
amplitude and direction were as expected. The pre-flight planned postion was
centered on CCD row=50, column=500 in C9a (black circle) with the commanded C9b
offset expected to put the target at row=50.6, column=499.8 (black asterisk).
At the start of C9a the position measured by the Photometer Data Quality (PDQ)
pipeline (red circle) was ~0.3 pixels from the planned position, well within
operating limits. A later C9a measure (green circle) put the star
along the expected line of roll-motion (red x's). The measured C9b position (green
asterisk) is consistent with the predicted position (red asterisk) based on
the initial C9a pointing measure and meets the desired goal of a ~0.6 pixel
offset perpendicular to the roll motion.
</i>
</div>
<a href="images/release-notes/c9/c9b_initial_pointing.png">
<img src="images/release-notes/c9/c9b_initial_pointing.png" class="img-responsive" alt="Offset achieved between C9a and C9b was 0.6 pixels as commanded.">
</a>
</div>

**Impulsive Roll offset in C9b**

A small uncommanded movement of the spacecraft of about -20 arc seconds in roll
was observed at 2016-06-18 02:17:30, during long-cadence number 128008. The
movement appears to have been due to a short impulse applied to the spacecraft
that the reaction wheel momentum nulled out over a period of 2 minutes,
resulting in the -20 arc second roll offset. The roll offset was corrected 22.5
hours later by thrusters as part of the normal K2 roll management cycle.

<div class="thumbnail">
<div class="caption">
<i>Figure C9b Roll Impulse: the centroid column of a target (EPIC 223254456) on
CCD channel 50 shows the impulsive pointing offset on cadence number 128008. The
centroid behavior of this target for 4 days around the jump shows that the
impulsive offset did not introduce target motions that were out-of-family with
normal roll-induced motion.
</i>
</div>
<a href="images/release-notes/c9/c9b_pointing_jump.png">
<img src="images/release-notes/c9/c9b_pointing_jump.png" class="img-responsive" alt="Impulsive offset in C9b did not result in excessive target motion.">
</a>
</div>


<br>

<h2>Data Quality and Processing Notes</h2>

***Calibrated Target Pixel Files***

This data release consists of calibrated target pixel files (TPFs) and supporting
calibration files. With
the use of large super apertures to collect the vast majority of the pixels and
the resulting small number of standard targets, no light curve files were
generated for the C9 data. These calibrated TPFs are intended to replace the
raw uncalibrated cadence pixel files currently available at the MAST. These
raw files
<ul>
<li>long cadence target data - lcs-targ
<li>long cadence collateral data - lcs-col
<li>long cadence processing history - lcs-history
</ul>
were delivered to facilitate rapid follow-up of possible microlensing events.
There are two separate sets of calibrated TPFs for C9a and C9b
whose filenames contain "c91" and "c92" respectively. The TPFs are available
through the normal K2 archive source page at MAST, whereas the cadence
pixel files are available on the
<a href="http://archive.stsci.edu/missions/k2/c9_raw_cadence_data/">MAST FTP site</a>.

We recommend that the calibrated TPFs delivered in Data Release 12 be used
in place of these raw files for scientific publications. The raw data will
continue to be available at the MAST until Jan 1, 2017, three months after
the delivery of Data Release 12, after which point it will no longer be
available.

<a name="type1v2"></a>
**Type-1 vs Type-2 TPFs**

In normal K2 processing, later stages of the pipeline are used to reconstruct
the pointing history and associate thruster firings with specific long- and
short-cadence numbers. These products are then included in the exported target
pixel and light curve FITS files. Because the C9 processing only used the pipeline
pixel-level calibration, these products are not available in the usual format.

The C9 TPFs, known as "Type-1 TPFs" are like those released early in K2
for C0 (DR2), C1 (DR3), and C2 (DR4).
These TPFs have world coordinate system (WCS) coordinates
based on the ra_dec_2_pix focal plane model and commanded pointing,
rather than using a reconstructed pointing history. We expect that the Type-1 WCS
coordinates can be wrong by up to ~1 pixel given the unmodeled roll motion
and discrete pointing offsets.

The standard Type-2 TPFs (campaigns C3-C8) contain WCS coordinates based on
the reconstructed pointing determined from the measured PRF centroid motion of a
number of bright unsaturated stars across each channel. The "motion polynomial"
model tracks the roll drift and any impulsive pointing offsets, resulting in
position errors at or below 0.1 pixel.

Since the thruster firing flags are not populated in FITS quality flags for the
Type-1 TPFs, they are being delivered in separate
long-cadence <a href="http://archive.stsci.edu/missions/k2/thruster_firings/thruster_firing_flags_c91_lc.csv">(thruster_firing_flags_c91_lc.csv</a>, <a href="http://archive.stsci.edu/missions/k2/thruster_firings/thruster_firing_flags_c92_lc.csv">thruster_firing_flags_c92_lc.csv)</a>
and short-cadence <a href="http://archive.stsci.edu/missions/k2/thruster_firings/thruster_firing_flags_c91_sc.csv">(thruster_firing_flags_c91_sc.csv</a>, <a href="http://archive.stsci.edu/missions/k2/thruster_firings/thruster_firing_flags_c92_sc.csv">thruster_firing_flags_c92_sc.csv)</a>
thruster firing tables.
<br>

**Large Target Pixel Files**

Note that due to an oddly-shaped aperture, the target pixel files for EPIC-200070438
contain 795x411 pixels for each cadence, despite the fact that only ~800 of these
pixels were actually observed. Users are cautioned that these target pixel files
are quite large and may cause memory problems when accessed:
<ul>
<li>ktwo200070438-c91_lpd-targ.fits = 10GB
<li>ktwo200070438-c92_lpd-targ.fits = 15GB.
</ul>

<br>

<hr>



# K2 Campaign 8

<h2>At a glance</h2>

<div class="col-lg-5">

<b><i>Pointing</i></b>
<ul>
<li>RA: 16.3379975 degrees</li>
<li>Dec: 5.2623459 degrees</li>
<li>Roll: -157.3538761 degrees</li>
</ul>

<b><i>Targets</i></b>
<ul>
<li> 24,187 in long cadence (LC)</li>
<li> 55 in short cadence (SC) including Uranus</li>
<li>26 unique LC custom targets were selected. See the <a href="images/release-notes/c8/ktwoc08_caf.csv">csv file that maps</a> the custom aperture number to the target name.</li>
</ul>

<b><i>Full Frame Images (FFI)</i></b>
<ul>
<li><a href="https://archive.stsci.edu/pub/k2/ffi/ktwo2016014203204-c08_ffi-cal.fits">ktwo2016014203204-c08_ffi-cal.fits</a></li>
<li><a href="https://archive.stsci.edu/pub/k2/ffi/ktwo2016056011138-c08_ffi-cal.fits">ktwo2016056011138-c08_ffi-cal.fits</a></li>
</ul>

<b><i>First cadence</i></b>
<ul>
<li>Time: 2016-01-04 13:16:25 UTC</li>
<li>Long Cadence Number:119907</li>
<li>Short Cadence Number: 3585670</li>
</ul>

<b><i>Last cadence</i></b>
<ul>
<li>Time: 2016-03-23 06:48:35 UTC</li>
<li>Long Cadence Number: 123759</li>
<li>Short Cadence Number: 3701259</li>
</ul>

<b><i>Most Recent Processing Version</i></b>
<ul>
<li> <a href="k2-pipeline-release-notes.html#data-release-11">Data Release 11</a> </li>
</ul>

</div>

<div class="col-lg-7">

<div class="thumbnail">
<div class="caption">
<i>Figure C8-FOV: Schematic of Kepler's C8 field-of-view with observed targets shown with purple dots.</i>
</div>
<a href="images/release-notes/c8/C8_selected.png">
<img src="images/release-notes/c8/C8_selected.png" class="img-responsive" alt="C8 field-of-view with selected targets plotted in purple.">
</a>
</div>

<div class="thumbnail">
<div class="caption">
<i>Figure C8-Mag: Distribution of the Kepler magnitudes of observed targets. All targets are chosen by guest observers. The distribution is due to how the largest <a href="k2-approved-programs.html#campaign-8">GO  programs</a> were selected.</i>
</div>
<a href="images/release-notes/c8/c8LcMagDistribution.png">
<img src="images/release-notes/c8/c8LcMagDistribution.png" class="img-responsive" alt="Distribution of the Kepler magnitudes of observed targets.">
</a>
</div>

</div>

<h2>Features and Events</h2>

***Uranus***

Uranus and four of its moons were observed with custom masks during Campaign 8. The path of Uranus was tiled with 245 single column target definitions at long cadence and with nine 9 x 307 trapezoidal masks at short cadence. The moons Caliban, Prospero, Setebos, and Sycorax were observed with separate custom masks. Uranus is the brightest moving object yet observed by K2.


<!-- The animated gif below shows Pluto as observed by K2.
<div class"thumbnail" style="width:65%;">
<div class="caption"><i>Figure C7-Pluto: An animated gif of a portion of the custom apertures that contain Pluto during C7. </i>
</div>
<a href="images/release-notes/c7/k2c7-pluto.gif"><img src="images/release-notes/c7/k2c7-pluto.gif" class="img-responsive" alt="Movie of Pluto moving through the K2 field of view."></a>
</div> -->


<br>

***Galaxies***

With its high Galactic latitude, Campaign 8 was ideal for observing galaxies. There were 2750 galaxies targeted, including IC 1613 (Caldwell 51), an irregular dwarf galaxy in the Local Group. IC 1613 was tiled with 48 20 x 20 pixel masks for a total of 19,200 pixels.


<br>

***Roll Drift Returns to _Normal_***

Based on the C7 degraded roll performance, the Mission Operations Center switched back to low-gain antenna LGA1 for spacecraft communication during most of C8. The switch resulted in a return to nominal K2 roll performance and drift rates. The campaign was started using LGA2, as was used in C7, and then starting around 23 Jan 2016 23:50 UTC operations were switched to LGA1. The antenna swap can be seen in the roll drift attitude error.

<div class="thumbnail" style="width: 90%">
 <div class="caption">
 <i>Figure C8-Pointing History: With the change back to using low-gain antenna LGA1 for communications, the roll drift (or x-axis attitude error) returned to nominal K2 behavior after the anomalous C7 roll drifts. Several larger than normal thruster firing tweaks affected C8 pointing. One of these, on 2016-02-01, resulted in a loss of fine pointing control for 30 hours (ADFFINEPTLK Fault).</i>   
 </div>
<a href="images/release-notes/c8/c8_pointing_history.png">
<img src="images/release-notes/c8/c8_pointing_history.png" class="img-responsive" alt="Roll Drift for C8 returns to nominal K2 behavior"></a>
</div>


<br>

***Loss of Fine Point***
On 2016-02-01 16:40 UTC the spacecraft dropped out of fine point control. Observations continued in coarse point, with much degraded pointing performance, until 2016-02-02 22:27:26 UTC when the spacecraft reacquired fine point during a resat period. This resulted in 29:47:53 of coarse point data collection. These cadences are flagged as "spacecraft is not in fine point" using bit 16 in the data quality flags. The loss of fine point occured following a thruster firing fine tweak that resulted in the spacecraft rolling in the wrong direction. The next tweak was unable to correct the attitude before the loss of fine point fault was triggered, but fine pointing control was restored automatically at the next momentum wheel resaturation. There were several other instances of anomalous thruster firing tweaks in C8, none of which resulted in loss of fine point. Their cause is under investigation.

<br>

<h2>Data Quality and Processing Notes</h2>

***Light Curve Quality***

The dominant systematic present in K2 simple aperture photometry light curves is a sawtooth shape that is due to the roll of the spacecraft, which is corrected approximately every 6 hours. With the return to more nominal K2 roll performance in C8, we find CDPP values have improved noticeably over those from C7. Below, we examine observed noise levels in the PDC light curves for C8, Data Release 11.

Analysis of the light curve quality reveals that CDPP values are decreased by roughly 20% from C7, from 59.2 ppm in C7 to 47.0 ppm in C8, as measured by the tenth percentile of 12th magnitude dwarfs. The values are comparable to those from C4-C6.

The magnitude dependence of CDPP and its distribution over the focal plane are shown below. Other CDPP benchmarks can be found in the <a href="images/release-notes/c8/C8_bin1.00_sc1.00_CDPP_Summary_16052411.txt">table giving 6.5-hr CDPP as a function of magnitude.</a>
<br>
<div class="thumbnail" style="width: 90%;">
<div class="caption">
<i>Figure C8-CDPP: 6.5-hr CDPP measurements for all targets as a function of Kepler magnitude. Dim targets have poorer overall photometric precision than bright targets, but can look better because the residual sawtooth falls below the noise floor. The saturated targets tend to have the lowest CDPP, but often show a residual sawtooth. </i>   
</div>
<a href="images/release-notes/c8/C8_logg_CDPP_vs_model.png">
<img src="images/release-notes/c8/C8_logg_CDPP_vs_model.png" class="img-responsive" alt="CDPP measured for all targets as a function of Kepler magnitude.">
</a>
</div>
<div class="thumbnail" style="width: 90%;">
<div class="caption">
<i>Figure C8-CDPP FocalPlane: 6.5-hr CDPP measured as a function of position on the focal plane, for 12th and 14th magnitude dwarf stars. The photometric precision is generally better near the center of the focal plane where the variations in roll angle produce less pixel motion. All cadences coincident with a definite thruster firing are gapped.</i>
<a href="images/release-notes/c8/C8_dwarf__CDPP_by_mod_out.png">
<img src="images/release-notes/c8/C8_dwarf__CDPP_by_mod_out.png" class="img-responsive" alt="CDPP per channel for 12th magnitude dwarfs">
</a>    
</div>
</div>

***Poor Smear Correction***

*Bright Stars*

There are 2 channels in C8 for which the saturation spill due to very bright stars corrupts both the masked and virtual smear measurements for one or more columns. The affected channels are 23 (columns 500-507 and 1055-1059) and channel 45 (columns 162-166). In these cases, in order to allow the pipeline calibration to complete, we flag the masked smear as bad and process the data with only the virtual smear. As a result, the smear correction will be poor for the channel/column combinations listed above and will be suspect for the same columns on other outputs of the same module due to video crosstalk.

We identified 5 individual targets whose light curves are clearly affected by the poor smear correction: EPIC-220519545 and 220549392 (ch 23); EPIC-220530070 and 220539101 (ch 45), and EPIC-220566642 (ch 48). During this smear investigation, we identified one additional target, EPIC-220498268 on channel 65, that is within the saturation spill of a very bright star and has a similarly corrupted light curve.

*Intermittent Streaks*

There are episodic smear correction errors on channel 42 (mod.out 13.2), the channel containing the Uranus supermask. Nearly every long cadence in the supermask appears to contain between 2 and 20 columns which are brightened by 10 to 80 counts. The brightening of a column lasts only for a single cadence, with no obvious patterns as to which columns are affected in a given cadence. Two example cadences which are particularly affected are 119980 and 119982.

Preliminary investigation indicates that this streaking is caused by false cosmic ray detections in the smear collateral data. Because we do not see similar streaking in the supermask for IC 1613, located on channel 58, we believe that the poor cosmic ray detector performance is due to the bright signal from Uranus moving across columns and altering the cosmic ray detector's dynamic threshold. When false cosmic rays are removed from the smear signal, the pixel data in that column is under-corrected, resulting in a brightening of that column for a given cadence. The streaks are not in the raw data, so users may wish to do their own smear correction on this channel.

The extent of the problem in time and CCD columns can be seen in the figure *C8-Channel 42 Calibrated Smear*. The long cadence data were calibrated in three segments of ~1284 cadences each. The false cosmic ray detections are present in columns where Uranus appeared at any time during the set of cadences being processed. In the figure, the false detections are seen to be confined primarily to the first segment (relative cadence 1-1285, LC number 119907-121191) and third segment (relative cadence 2570-3853, LC number 122476-123759) and to columns above 500. Targets on channel 42 below column 500 should be relatively unaffected by this anomaly.

<div class="thumbnail" style="width: 45%;display: inline-block;">
<div class="caption">
<i>Figure C8-Channel-42a: Uranus supermask smear anomaly, Cadence 119980. </i>   
</div>
<a href="images/release-notes/c8/c8-channel42-cadence119980.png">
<img src="images/release-notes/c8/c8-channel42-cadence119980.png" class="img-responsive" alt="Uranus supermask cadence 119980 smear streaks.">
</a>
</div>

<div class="thumbnail" style="width: 45%;display: inline-block;">
<div class="caption">
<i>Figure C8-Channel-42b: Uranus supermask smear anomaly, Cadence 119982.  </i>
</div>
<a href="images/release-notes/c8/c8-channel42-cadence119982.png">
<img src="images/release-notes/c8/c8-channel42-cadence119982.png" class="img-responsive" alt="Uranus supermask cadence 119982 smear streaks.">
</a>
</div>

<div class="thumbnail" style="width: 90%;">
<div class="caption">
<i>Figure C8-Channel 42 Calibrated Smear: The smear measurement for channel 42 consists of a row vector with 1100 columns for each of the 3853 long cadences. All of the smear measurements are shown with column number on the x-axis and relative cadence number on the y-axis. Time is increasing downward. The gray scale indicates the smear level in e-/sec, with black indicating higher levels. The retrograde path of Uranus across the columns is clearly visible as a strong signal in the smear. The false cosmic ray detections are visible as white spots (a single column for a single cadence) scattered throughout the right half of the figure. The white vertical streak corresponds to a bad column; the white horizontal streaks are excluded cadences. Dark vertical streaks indicate a bright star somewhere in that column.</i>   
</div>
<a href="images/release-notes/c8/c8_calibrated_smear_m13o2.png">
<img src="images/release-notes/c8/c8_calibrated_smear_m13o2.png" class="img-responsive" alt="Calibrated smear values for channel 42 showing excessive false cosmic ray detections.">
</a>
</div>

<br>

<hr>



# K2 Campaign 7

<h2>At a glance</h2>

<div class="col-lg-5">

    <b><i>Pointing</i></b>
    <ul>
        <li>RA: 287.82850661 degrees</li>
        <li>Dec: -23.36001815 degrees</li>
        <li>Roll: -172.78037532 degrees</li>
    </ul>

    <b><i>Targets</i></b>
    <ul>
        <li> 13,469 in long cadence (LC)</li>
        <li> 72 in short cadence (SC)</li>
        <li>Several custom targets were selected. See the <a href="images/release-notes/c7/ktwoc07_caf.csv">csv file that maps</a> the custom aperture number to the target name.</li>
    </ul>

    <b><i>Full Frame Images (FFI)</i></b>
    <ul>
        <li><a href="https://archive.stsci.edu/pub/k2/ffi/ktwo2015290001304-c07_ffi-cal.fits">ktwo2015290001304-c07_ffi-cal.fits</a></li>
        <li><a href="https://archive.stsci.edu/pub/k2/ffi/ktwo2015331045232-c07_ffi-cal.fits">ktwo2015331045232-c07_ffi-cal.fits</a></li>
    </ul>

    <b><i>First cadence</i></b>
    <ul>
        <li>Time: 2015-10-04 17:52:39 UTC</li>
        <li>Long Cadence Number:115414</li>
        <li>Short Cadence Number: 3450880</li>
    </ul>

    <b><i>Last cadence</i></b>
    <ul>
        <li>Time: 2015-12-26 08:35:28 </li>
        <li>Long Cadence Number: 119456</li>
        <li>Short Cadence Number: 3572169</li>
    </ul>

    <b><i>Most Recent Processing Version</i></b>
    <ul>
    <li> <a href="k2-pipeline-release-notes.html#data-release-9">Data Release 9</a> </li>
    </ul>

</div>

<div class="col-lg-7">

    <div class="thumbnail">
        <div class="caption">
            <i>Figure C7-FOV: Schematic of Kepler's C7 field-of-view with observed targets shown with purple dots.</i>
        </div>
        <a href="images/release-notes/c7/C7_selected.png">
            <img src="images/release-notes/c7/C7_selected.png" class="img-responsive" alt="C7 field-of-view with selected targets plotted in purple.">
        </a>
    </div>

    <div class="thumbnail">
        <div class="caption">
            <i>Figure C7-Mag: Distribution of the Kepler magnitudes of observed targets. All targets are chosen by guest observers. The distribution is due to how the largest <a href="k2-approved-programs.html#campaign-7">GO  programs</a> were selected.</i>
        </div>
        <a href="images/release-notes/c7/c7LcMagDistribution.png">
            <img src="images/release-notes/c7/c7LcMagDistribution.png" class="img-responsive" alt="Distribution of the Kepler magnitudes of observed targets.">
        </a>
    </div>

</div>

<h2>Features and Events</h2>

***Pluto***

Pluto, one of the largest trans-Neptunian objects, previously known as the ninth planet in our solar system, was observed during Campaign 7. The path of Pluto was tiled with 1 x n pixel target definitions, where n ranges from 1 to 217. The range of custom aperture numbers for Pluto is 200062954 -- 200062827. The animated gif below shows Pluto as observed by K2.
<div class"thumbnail" style="width:65%;">
    <div class="caption"><i>Figure C7-Pluto: An animated gif of a portion of the custom apertures that contain Pluto during C7. </i>
    </div>
    <a href="images/release-notes/c7/k2c7-pluto.gif"><img src="images/release-notes/c7/k2c7-pluto.gif" class="img-responsive" alt="Movie of Pluto moving through the K2 field of view."></a>
</div>


<br>

***Ruprecht 47***

Ruprecht 47 is an open cluster observed with K2 during Campaign 7.  It was observed using a super-aperture, tiled with 60 51 x 51 masks, totalling 156,060 pixels. The custom aperture numbers range from 200062524 -- 200062583.


<br>

***Increase in Roll Drift***

For C7, an alternate low-gain antenna was active during science data collection. The previously used LGA1 was replaced by LGA2 (see [KIH Figure 2](http://archive.stsci.edu/kepler/manuals/KSCI-19033-001.pdf)), as the latter is slightly better oriented with respect to earth. (This partially compensates for the increasing distance to the spacecraft in its earth-trailing orbit, now at 0.8 AU.)  Since the two antennas are mounted on opposite sides of the spacecraft, this antenna swap produced a change in radiation pressure that placed an additional (unbalanced) torque about the boresight on the spacecraft.  The resulting increase in roll drift is illustrated in Figure *C7-RollDrift*, which compares the drift rates for C4, C6, and C7. Consequently, the maximum excursion of any pixel from its nominal position is significantly larger for C7 than for previous campaigns (see Figure *C7-MAR*).

<div class="thumbnail" style="width: 45%;display: inline-block;">
    <div class="caption">
    <i>Figure C7-Roll Drift: The roll of the Kepler spacecraft around the boresight during campaigns 4, 6 and 7. The C7 drift rate is significantly out of family, being negative throughout the entire campaign.</i>   
    </div>
    <a href="images/release-notes/c7/c7-rolldrift.png">
        <img src="images/release-notes/c7/c7-rolldrift.png" class="img-responsive" alt="Roll Drift for C7 is larger than it was for C4 and C6.">
    </a>
</div>

<div class="thumbnail" style="width: 49%;display: inline-block;">
    <div class="caption">
    <i>Figure C7-MAR: The maximum distance between the photometrically derived attitude (PAD) and the nominal position plotted against time for C7.  </i>
    <a href="images/release-notes/c7/c7-mar.png">
        <img src="images/release-notes/c7/c7-mar.png" class="img-responsive" alt="Maximum residual of the attitude measured with PAD and PDQ.">
    </a>

    </div>
</div>


Given this unanticipated result, LGA1 will be used for C8, C9, and C10, while the fields of view for C11, C12, and C13 were tweaked by 0.12° – 0.16° (<a href="/minor-changes-in-the-fields-of-campaigns-11-12-and-13.html">see GO blog</a>) so that a subsequent return to LGA2 should have no adverse effects on data quality.


<br>

***Effect of Roll on Photometry***

The unusually large roll motion in C7, combined with an extremely crowded field, had a strong impact on photometry, particularly on targets near the edge of the focal plane. This impact has several components:
<ul>
<li>
In some cases target stars came close to the edge of their aperture masks. In such cases the photometric precision will be low.
</li>
<li>
Background estimates based on background polynomials were strongly polluted by stars rolling in and out of the background apertures. This is especially true for channels near the edge of the focal plane (more roll) and near the Galactic plane (more stars). As a result, the background is strongly over-corrected, with short-time background variations strongly correlated with roll motion. These background variations have been subtracted from all pixels on the channel.
</li>
<li>
The peaks of the roll motion in the background pixels were often incorrectly identified as cosmic rays and removed. The resulting change in background is minor in magnitude, but potentially diminishes the correlation between background variations and roll motion.
</li>
</ul>

The motion polynomials generally did a reasonable job tracking the large roll motion, and this enabled the computation of photometric apertures that significantly reduced the impact of roll motion in many cases. In other cases, however, the roll motion was too large for the recovery of high-quality photometry using the standard pipeline processing.

In addition to the issues with unusually large roll and crowding, stars selected for observation were unusually distributed in C7, with some channels having many targets and other channels having relatively few targets. The result was that some channels had few target stars in the range of magnitudes used to characterize field motion via motion polynomials. A particularly dramatic example is channel 24.4, where all the targets used to create the motion polynomial for this channel are in one corner, resulting in a very inaccurate motion polynomial. Because motion polynomials are used in the creation of the photometric aperture, photometry for some targets on 24.4 may be particularly poor.

<br>

<h2>Data Quality and Processing Notes</h2>

***Light Curve Quality***

The dominant systematic present in K2 simple aperture photometry light curves is a sawtooth shape that is due to the roll of the spacecraft approximately every 6 hours. The PDC module of the Kepler Pipeline uses Principle Component Analysis to remove this signal in addition to other systematics. Below, we examine observed noise levels in the PDC light curves for C7, Data Release 9.

Since two halos were used for targets near the center of the focal plane and three halos were used for targets around the periphery, the requisite pixels were captured, but the increased roll motion has severely challenged the data processing pipeline’s ability to perform high-precision photometry. Analysis of the light curve quality reveals that CDPP values are increased by roughly 35% above the benchmark value (tenth percentile of 12th magnitude dwarfs) compared to C4-C6.

<a href="images/release-notes/c7/C7_bin1.00_sc1.00_CDPP_Summary_16033014.txt">Table giving 6.5-hr CDPP as a function of magnitude.</a>
<br>
<div class="thumbnail" style="width: 70%;">
    <div class="caption">
    <i>Figure C7-CDPP: 6.5-hr CDPP measurements for all targets as a function of Kepler magnitude. Dim targets have poorer overall photometric precision than bright targets, but can look better because the residual sawtooth falls below the noise floor. The saturated targets tend to have the lowest CDPP, but often show a residual sawtooth. </i>   
    </div>
    <a href="images/release-notes/c7/C7_logg_CDPP_vs_model.png">
        <img src="images/release-notes/c7/C7_logg_CDPP_vs_model.png" class="img-responsive" alt="CDPP measured for all targets as a function of Kepler magnitude.">
    </a>
</div>
<div class="thumbnail" style="width: 80%;">
    <div class="caption">
    <i>Figure C7-CDPPFocalPlane: 6.5-hr CDPP measured as a function of position on
the focal plane for 12th and 14th magnitude dwarf stars. The photometric precision
is generally better near the center of the focal plane where the variations in roll
angle produce less pixel motion. All cadences coincident with a definite thruster
firing are gapped.</i>
    <a href="images/release-notes/c7/C7_dwarf__CDPP_by_mod_out.png">
        <img src="images/release-notes/c7/C7_dwarf__CDPP_by_mod_out.png" class="img-responsive" alt="CDPP per channel for 12th magnitude dwarfs">
    </a>    
    </div>
</div>

<br>

***Poor Smear Correction***

There are 4 channels in C7 for which the saturation spill due to very bright stars spans all CCD rows for one or more columns, corrupting both the masked and virtual smear measurements for these columns. In these cases, in order to allow the pipeline calibration to complete, we flag the masked smear as bad and process the data with only the virtual smear. As a result, the smear correction will be poor for the channel/column combinations listed below and will be suspect for the same columns on other outputs on the same module as the indicated channel due to video crosstalk.

<ul>
<li style="list-style-type:none">Channel | Columns</li>
<li style="list-style-type:none">&emsp;&emsp;45 | 685:691</li>
<li style="list-style-type:none">&emsp;&emsp;53 | 42:51</li>
<li style="list-style-type:none">&emsp;&emsp;65 | 819:828</li>
<li style="list-style-type:none">&emsp;&emsp;67 | 234:242</li>
</ul>

<br>

<hr>


# K2 Campaign 6

<h2>At a glance</h2>

<div class="col-lg-5">

    <b><i>Pointing</i></b>
    <ul>
        <li>RA: 204.8650344 degrees</li>
        <li>Dec: -11.2953585 degrees</li>
        <li>Roll: 159.6356000 degrees</li>
    </ul>

    <b><i>Targets</i></b>
    <ul>
        <li> 28,289 in long cadence (LC)</li>
        <li> 84 in short cadence (SC)</li>
        <li>Several custom targets (see below)</li>
    </ul>

    <b><i>Full Frame Images (FFI)</i></b>
    <ul>
        <li><a href="https://archive.stsci.edu/pub/k2/ffi/ktwo22015207050529-c06_ffi-cal.fits">ktwo2015207050529-c06_ffi-cal.fits</a></li>
        <li><a href="https://archive.stsci.edu/pub/k2/ffi/ktwo2015246104018-c06_ffi-cal.fits">ktwo2015246104018-c06_ffi-cal.fits</a></li>
    </ul>

    <b><i>First cadence</i></b>
    <ul>
        <li>Time: 2015-07-13 22:45:04 UTC</li>
        <li>Long Cadence Number: 111362</li>
        <li>Short Cadence Number: 3329320</li>
    </ul>

    <b><i>Last cadence</i></b>
    <ul>
        <li>Time: 2015-09-30 21:11:29 UTC</li>
        <li>Long Cadence Number: 115224</li>
        <li>Short Cadence Number: 3445209 </li>
    </ul>

    <b><i>Most Recent Processing Version</i></b>
    <ul>
    <li> <a href="k2-pipeline-release-notes.html#data-release-8">Data Release 8</a> </li>
    </ul>

</div>

<div class="col-lg-7">

    <div class="thumbnail">
        <div class="caption">
            <i>Figure: Schematic of Kepler's C6 field-of-view with observed targets shown with purple dots.</i>
        </div>
        <a href="images/campaign_selected/C6_selected.png">
            <img src="images/campaign_selected/C6_selected.png" class="img-responsive" alt="C6 field-of-view with selected targets">
        </a>
    </div>

    <div class="thumbnail">
        <div class="caption">
            <i>Figure: Distribution of the Kepler magnitudes of observed targets. All targets are chosen by guest observers. The bimodality is due to how the largest <a href="k2-approved-programs.html#campaign-6">GO  programs</a> were selected.</i>
        </div>
        <a href="images/release-notes/c6/c6LcMagDistribution.png">
            <img src="images/release-notes/c6/c6LcMagDistribution.png" class="img-responsive" alt="Distribution of the Kepler magnitudes of observed targets.">
        </a>
    </div>
</div>

<h2>Features and Events</h2>

***Spica***

The star Spica (α Virginis, [EPIC 212573842](http://archive.stsci.edu/k2/epic/search.php?id=212573842&action=Search)) the 15th brightest star in the sky, is on silcon during Campaign 6. As can be seen on the FFI below, Spica is on mod.out 18.3 (channel 63) and its Schmidt-corrector reflection lies on mod.out 8.3. The star bleeds into both smear regions, preventing proper smear correction on columns 805-816 on channel 63.  Also, because of cross-talk, the Spica signal appears on all channels of module 18 at the same row and column position, but to a lesser degree.  For more information on cross-talk, see the [Instrument Handbook](http://archive.stsci.edu/kepler/manuals/KSCI-19033-001.pdf).

<div class="thumbnail" style="width: 52%;">
    <div class="caption">
        <i>Figure: The FFI taken during Campaign 6 showing the bright star Spica and its reflection.</i>
    </div>
    <a href="images/release-notes/c6/spica.png">
        <img src="images/release-notes/c6/spica.png" class="img-responsive" alt="The FFI taken during Campaign 6 showing the bright star Spica and its reflection.">
    </a>
</div>

<br>

***Observed Trojans***

During Campaign 6, K2 observed 65 Trojan asteroids. Each was tiled with 1 x n pixel target definitions, where n ranges from 1 to 217. The tiled regions for three examples are shown in the figure below.  The range of custom aperture numbers given to the Trojans is 200041889 -- 200061149. A mapping of the minor planet designation numbers to the custom aperture numbers can be <a href="images/release-notes/c6/trojanCustomApertureC6.csv">downloaded here.</a>

<div class="thumbnail" style="width: 52%;">
    <div class="caption">
        <i>Figure: The selected pixels are highlighted in green to show the paths of three Trojans captured during C6.</i>
    </div>
    <a href="images/release-notes/c6/exTrojanPath.png">
        <img src="images/release-notes/c6/exTrojanPath.png" class="img-responsive" alt="The path of three trojans are shown on one channel.">
    </a>
</div>

<br>

***Variable Guide Star***

The star on Module 25 used for guiding during C6 was highly variable. No adverse effects of this variability were detected in the data collection or spacecraft operations.  

****Update -- February 18, 2016****
<p> The signal seen in the guide star on module 25 appears to be that of a contact binary with a period of 14.5 hours and a depth of approximately 40 percent. A signal with the same period and phase is seen in a large number of long cadence, PDC, light curves with an amplitude as large as 0.1 per cent.  See the folded light curve, and normalized BLS spectra below.  The mechanism by which this signal is propagating into the K2 data is still under investigation.

<p>To help users understand and mitigate the effects of this guide star, we make available the <a href="images/release-notes/c6/C6fgsFlux-mod25.csv"> module 25 guide star fluxes </a> in a csv file.  The guide star was selected from the USNO catalog and has an RA of 200.6867 degrees, Dec of -6.0353 degrees, and R magnitude of 9.51. </p>

<div class="thumbnail" style="width: 56%;">
    <div class="caption">
<i>Figure C6-GuideStar: The folded light curve of one long cadence target (top) and the module 25 guide star (bottom). Both are folded at a period of 0.6046 days, the approximate period of the guide star.  
</i></div>
    <a href="images/release-notes/c6/fgsCompareC6to212668671.png">
        <img src="images/release-notes/c6/fgsCompareC6to212668671.png" class="img-responsive" alt="The folded light curve of the guide star and an example C6 LC target.">
    </a>
</div>

<div class="thumbnail" style="width: 56%;">
    <div class="caption">
<i>Figure C6-BLS: The normalized BLS (box-least squares) spectra for 400 long cadence targets on channel 42, sorted by magnitude (with the brightest at the top).  The 14.5-hour period and a series of peaks every ~7 hours show-up as yellow vertical lines on this figure. The majority of targets on this channel have a significant signal at this period.   
</i></div>
    <a href="images/release-notes/c6/ch42blsSpectrumC6.png">
        <img src="images/release-notes/c6/ch42blsSpectrumC6.png" class="img-responsive" alt="The Bls spectrum for 400 targets on channel 42.">
    </a>
</div>

****Update -- April 2016****
<p>See this [addendum](images/release-notes/c6/var_fgs_kso-391_drnC6_addendum_16040722.pdf) for a thorough description of the pointing and photometric errors induced by the variable guide star in C6.</p>

<br>

<h2>Data Quality and Processing Notes</h2>

***Light Curve Quality***

The dominant systematic present in K2 simple aperture photometry light curves is a sawtooth shape that is due to the roll of the spacecraft approximately every 6 hours. The PDC module of the Kepler Pipeline uses Principle Component Analysis to remove this signal in addition to other systematics. Below, we examine observed noise levels in the PDC light curves for C6, Data Release 8.

<a href="images/release-notes/c6/K2-C06_bin1.00_sc1.00_CDPP_Summary.txt">Table giving 6.5-hr CDPP as a function of magnitude.</a>

<div class="thumbnail" style="width: 70%;">
    <div class="caption">
    <i>Figure C6-CDPP: CDPP measured for all targets as a function of Kepler magnitude. Dim targets have poorer overall photometric precision than bright targets, but can look better because the residual sawtooth falls below the noise floor. The saturated targets tend to have the lowest CDPP, but often show a residual sawtooth. Also, the photometric precision is generally better near the center of the focal plane where the variations in roll angle produce less pixel motion. <a href="images/release-notes/c6/K2-C6_dwarf__CDPP_by_mod_out.eps">See here for CDPP as a function of position on the focal plane.</a> All cadences coincident with a definite thruster firing are gapped.</i>
    </div>
    <a href="images/release-notes/c6/K2-C06_logg_CDPP_vs_model.png">
        <img src="images/release-notes/c6/K2-C6_logg_CDPP_vs_model.png " class="img-responsive" alt="CDPP measured for all targets as a function of Kepler magnitude.">
    </a>
</div>

<br>

<hr>



# K2 Campaign 5

<h2>At a glance</h2>

<div class="col-lg-5">

    <b><i>Pointing</i></b>
    <ul>
        <li>RA: 130.1576478 degrees</li>
        <li>Dec: 16.8296140 degrees</li>
        <li>Roll: 166.0591297 degrees</li>
    </ul>

    <b><i>Targets</i></b>
    <ul>
        <li>25,850 in long cadence (LC)</li>
        <li>204 in short cadence (SC)</li>
        <li>Several custom targets (see below)</li>
    </ul>

    <b><i>Full Frame Images (FFI)</i></b>
    <ul>
        <li><a href="https://archive.stsci.edu/pub/k2/ffi/ktwo2015127093352-c05_ffi-cal.fits">ktwo2015127093352-c05_ffi-cal.fits</a></li>
        <li><a href="https://archive.stsci.edu/pub/k2/ffi/ktwo2015170131810-c05_ffi-cal.fits">ktwo2015170131810-c05_ffi-cal.fits</a></li>
    </ul>

    <b><i>First cadence</i></b>
    <ul>
        <li>Time: 2015-04-27 02:18:11.949 UTC</li>
        <li>Long Cadence Number: 107552</li>
        <li>Short Cadence Number: 3215020</li>
    </ul>

    <b><i>Last cadence</i></b>
    <ul>
        <li>Time: 2015-07-10 22:39:43.571 UTC</li>
        <li>Long Cadence Number: 111214</li>
        <li>Short Cadence Number: 3324909</li>
    </ul>

    <b><i>Most Recent Processing Version</i></b>
    <ul>
    <li> <a href="k2-pipeline-release-notes.html#data-release-10">Data Release 10</a> </li>
    </ul>

</div>

<div class="col-lg-7">

    <div class="thumbnail">
        <div class="caption">
            <i>Figure: Schematic of Kepler's C5 field-of-view with observed targets shown with purple dots.</i>
        </div>
        <a href="images/campaign_selected/C5_selected.png">
            <img src="images/campaign_selected/C5_selected.png" class="img-responsive" alt="C5 field-of-view with selected targets">
        </a>
    </div>

    <div class="thumbnail">
        <div class="caption">
            <i>Figure: Distribution of the Kepler magnitudes of observed targets in C5. All targets are chosen by Guest Observers. The bimodality is due to how the largest <a href="k2-approved-programs.html#campaign-5">Guest Observer programs</a> were selected.</i>
        </div>
        <a href="images/release-notes/c5/C5LcMagDistribution.png">
            <img src="images/release-notes/c5/C5LcMagDistribution.png" class="img-responsive" alt="Distribution of the Kepler magnitudes of observed targets in C5.">
        </a>
    </div>

</div>

<h2>Features and Events</h2>

***M67***

The open cluster M67 was observed by collecting a 400x400 region of sky near the core of the cluster in modules 6.1 and 6.2. See the image below. These data are grouped into 72 custom apertures, each with a 50x50 pixel mask or smaller. Their data are listed by custom aperture number at the MAST in the range 200008644--200008715.

<div class="thumbnail" style="width: 68%;">
    <div class="caption">
        <i>Figure: The tiling of the M67 open cluster is shown in green on mod.outs 6.1 and 6.2 of C5.</i>
    </div>
    <a href="images/release-notes/c5/M67Tiling.png">
        <img src="images/release-notes/c5/M67Tiling.png" class="img-responsive" alt="The tiling of the M67 open cluster is shown in green on mod.outs 6.1 and 6.2 of C5.">
    </a>
</div>

<br>

***Trans-Neptunian Object***

The Trans-Neptunian Object TNO (126154) 2001 YH140 was observed in Campaign 5 by creating 565 1 x n pixel target definitions (where n ranges from 4 to 21) that cover the path of the TNO. The custom aperture numbers range from 200008716 to 200009280.

<br>

***Noted Data Anomalies***

Approximately 55.5 days after the start of C5, we note a small (~4000 electrons per cadence) increase in the median dark level that lasts approximately a day. The event is likely caused by a Coronal Mass Ejection, and its size is small compared to other normal variations seen in the dark level. This change in dark level is part of the normal calibration process that occurs in the CAL module.

One Argabrightening event was seen in the observed background level approximately 38 days into the campaign and affects a majority of the channels. This event is flagged on bit 13 in the QUALITY column of the light curve and target pixel files for those targets on the affected channels.

<br>

<h2>Data Quality and Processing Notes</h2>

***Light Curve Quality***

The dominant systematic present in K2 simple aperture photometry light curves is a sawtooth shape that is due to the roll of the spacecraft approximately every 6 hours. The PDC module of the Kepler Pipeline uses Principle Component Analysis to remove this signal in addition to other systematics. Below, we examine observed noise levels in the PDC light curves for C5, Data Release 7.

<a href="images/release-notes/c5/K2-C05_CDPP_Summary.txt">Table giving 6.5-hr CDPP as a function of magnitude.</a>

<div class="thumbnail" style="width: 68%;">
    <div class="caption">
        <i>Figure: CDPP measured for all targets as a function of Kepler magnitude. Dim targets have poorer overall photometric precision than bright targets, but can look better because the residual sawtooth falls below the noise floor. The saturated targets tend to have the lowest CDPP, but often show a residual sawtooth. Also, the photometric precision is generally better near the center of the focal plane where the variations in roll angle produce less pixel motion. All cadences coincident with a definite thruster firing are gapped.</i>
    </div>
    <a href="images/release-notes/c5/K2-C05_logg_CDPP_vs_model.png">
        <img src="images/release-notes/c5/K2-C05_logg_CDPP_vs_model.png" class="img-responsive" alt="CDPP measured for all targets as a function of Kepler magnitude.">
    </a>
</div>

<br>

<hr>



# K2 Campaign 4

<h2>At a glance</h2>

<div class="col-lg-5">

    <b><i>Pointing</i></b>
    <ul>
        <li>RA: 59.0759116 degrees</li>
        <li>Dec: 18.6605794 degrees</li>
        <li>Roll: -167.6992793 degrees</li>
    </ul>

    <b><i>Targets</i></b>
    <ul>
        <li>15,847 in long cadence (LC)</li>
        <li>122 in short cadence (SC)</li>
        <li>Several custom targets (see below)</li>
    </ul>

    <b><i>Full Frame Images (FFI)</i></b>
    <ul>
        <li><a href="https://archive.stsci.edu/pub/k2/ffi/ktwo2015051131033-c04_ffi-cal.fits">ktwo2015051131033-c04_ffi-cal.fits</a></li>
        <li><a href="https://archive.stsci.edu/pub/k2/ffi/ktwo2015092174954-c04_ffi-cal.fits">ktwo2015092174954-c04_ffi-cal.fits</a></li>
    </ul>

    <b><i>First cadence</i></b>
    <ul>
        <li>Time: 2015-02-08 06:50:09.177 UTC</li>
        <li>Long Cadence Number: 103744</li>
        <li>Short Cadence Number: 3100780</li>
    </ul>

    <b><i>Last cadence</i></b>
    <ul>
        <li>Time: 2015-04-20 04:32:47.045 UTC</li>
        <li>Long Cadence Number: 107213</li>
        <li>Short Cadence Number: 3204879</li>
    </ul>

    <b><i>Most Recent Processing Version</i></b>
    <ul>
    <li> <a href="k2-pipeline-release-notes.html#data-release-10">Data Release 10</a> </li>
    </ul>

</div>

<div class="col-lg-7">

    <div class="thumbnail">
        <div class="caption">
            <i>Figure: C4 field-of-view with selected targets shown as purple dots.</i>
        </div>
        <a href="images/campaign_selected/C4_selected.png">
            <img src="images/campaign_selected/C4_selected.png" class="img-responsive" alt="C4 field-of-view with selected targets">
        </a>
    </div>

    <div class="thumbnail">
        <div class="caption">
            <i>Figure: Distribution of the Kepler magnitudes of observed targets in C4. All targets are chosen by Guest Observers. The bimodality is due to how the largest Guest Observer programs were selected for C4.</i>
        </div>
        <a href="images/release-notes/c4/C4_lcDistribution.png">
            <img src="images/release-notes/c4/C4_lcDistribution.png" class="img-responsive" alt="Distribution of the Kepler magnitudes of observed targets in C4.">
        </a>
    </div>

</div>

<h2>Features and Events</h2>

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

<h2>Data Quality and Processing Notes</h2>

***Background Residuals near Pleiades***

Background removal for channels near the Pleiades has larger than normal residuals. These large residuals occur on mod.outs 10.3 and 15.1 through 15.4 due to the background on these channels being dominated by dust clouds near the Pleiades. The rich spatial structure of the Pleiades' dust clouds is poorly captured by the low order (≤ 4) polynomial model used to fit the background flux, with the best fit for these channels being given by a constant. This fit is done for every cadence, and the result is higher than normal background residuals, with residuals as large as 7 times the standard deviation of the background pixel values. (Normal residuals are typically less than the background standard deviation.)

We recommend caution when using light curves or the background model on these channels. Note that the FLUX column of the target pixel files contains calibrated pixels with the background subtracted. The amount of background that was subtracted per pixel can be found in the <a href="/K2/pipelineReleaseNotes.shtml#dr5">FLUX_BKG column</a> and restored, if desired.

Local background estimates per star may produce higher-quality results. The change in the constant background level on these channels over time is in family with the median background change on other channels

<br>

***Lightcurves Created with Non-Optimal Apertures***

Due to an incompatibility between K2 roll motion and the determination of photometric optimal apertures, some light curves may be based on apertures that are too small and therefore have more noise than necessary. In particular, there are 887 stellar targets that are particularly suspect; they are listed <a href="/K2/K2drn/C4/C4_reduced_ap_targets.txt">here</a>. The brighter targets in this set may have correct optimal apertures, but stars with Kp > 13 have been shown to have lower photometric precision than non-suspect stars of similar brightness.

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

<a href="images/release-notes/c4/K2-C04_CDPP_Summary.txt">Table giving 6.5-hr CDPP as a function of magnitude.</a>

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


*SC PDC Quality Flags*

The PDC quality flags were populated for some of the SC targets even though there are no SC PDC light curves. These flags are: manual exclude (bit 9), SPSD detected (bit 11), and impulsive outlier removed (bit 12). Users may simply ignore these flags.

<br>

<hr>



# K2 Campaign 3

<h2>At a glance</h2>

<div class="col-lg-5">

    <b><i>Pointing</i></b>
    <ul>
        <li>RA: 336.66534641439 degrees</li>
        <li>Dec: -11.096663792177 degrees</li>
        <li>Roll: -158.494818065985 degrees</li>
    </ul>

    <b><i>Targets</i></b>
    <ul>
        <li>16,375 in long cadence (LC)</li>
        <li>55 in short cadence (SC)</li>
        <li>Several custom targets (see below)</li>
    </ul>

    <b><i>Full Frame Images (FFI)</i></b>
    <ul>
        <li><a href="https://archive.stsci.edu/pub/k2/ffi/ktwo2014331202630-c03_ffi-cal.fits">ktwo2014331202630-c03_ffi-cal.fits</a></li>
        <li><a href="https://archive.stsci.edu/pub/k2/ffi/ktwo2015008010551-c03_ffi-cal.fits">ktwo2015008010551-c03_ffi-cal.fits</a></li>
    </ul>

    <b><i>First cadence</i></b>
    <ul>
        <li>Time: 2014-11-15 14:06:05.515 UTC</li>
        <li>Long Cadence Number: 99599</li>
        <li>Short Cadence Number: 2976430</li>
    </ul>

    <b><i>Last cadence</i></b>
    <ul>
        <li>Time: 2015-01-23 18:37:04.488 UTC</li>
        <li>Long Cadence Number: 102984</li>
        <li>Short Cadence Number: 3078009</li>
    </ul>

    <b><i>Most Recent Processing Version</i></b>
    <ul>
    <li> <a href="k2-pipeline-release-notes.html#data-release-10">Data Release 10</a> </li>
    </ul>

</div>

<div class="col-lg-7">

    <div class="thumbnail">
        <div class="caption">
            <i>Figure: Schematic of Kepler's C3 field-of-view with selected targets shown with purple dots. Note, the use of an incorrect rotation angle in software used by Guest Observers to select targets has resulted in obvious variations in target density across the focal plane.</i>
        </div>
        <a href="images/campaign_selected/C3_selected.png">
            <img src="images/campaign_selected/C3_selected.png" class="img-responsive" alt="C3 field-of-view with selected targets">
        </a>
    </div>

    <div class="thumbnail">
        <div class="caption">
            <i>Figure: Distribution of the Kepler magnitudes of observed targets in C3. The bimodality is due to the large Guest Observer programs selected for C3.</i>
        </div>
        <a href="images/release-notes/c3/magnitudeDist.png">
            <img src="images/release-notes/c3/magnitudeDist.png" class="img-responsive" alt="Distribution of the Kepler magnitudes of observed targets in C3.">
        </a>
    </div>

</div>

<h2>Features and Events</h2>

***Neptune***

Neptune moved across the field of view during C3 and K2 observed it in both long and short cadence. Short cadence data were obtained approximately 20 days either side of the stationary point of Neptune. See this time lapse <a href="https://www.youtube.com/watch?v=Tw-q3uM_5_0">movie</a> created by Jason Rowe that clearly shows Neptune and its moons, Titan and Nereid. The custom aperture numbers associated with Neptune are 200004468--200004923. These observations were taken as part of Guest Observer Programs GO3060 (PI:Rowe) and GO3057 (PI:Gaulme).

<br>

***Trans-Neptunian Object***

The Trans-Neptunian Object (225088) 2007 OR10 was observed with 2 masks and given custom aperture numbers 200004466 and 200004467. This target was observed as part of Guest Observer Program GO3053 (PI:Szabo).

<br>

***Premature End***

Campaign 3 had a nominal duration of 80 days, but an actual duration of only 69.2 days. The campaign ended earlier than expected because the on-board storage filled up faster than anticipated due to unusually poor data compression.


<br>

<h2>Data Quality and Processing Notes</h2>

***Highlights of Pipeline Improvements***

Campaign 3 (Data Release 5) data were the first K2 data processed with the SOC 9.3 pipeline. With this data release comes the higher-level data products. A detailed list of the pipeline developments that accompany this data release is listed on the [pipeline release page](k2-pipeline-release-notes.html#data-release-5). A few highlights are listed here:

* Quality flags now indicate which cadences were obtained during thruster firings.
* Background pixels were observerd and used to model the background level across the field of view. The calibrated pixels available in the target pixel files now have this background level removed.
* Simple Aperture Photometry (SAP_FLUX) and cotrended (PDCSAP_FLUX) light curves are available for long cadence data.
* The FFIs now contain a World Coordinate Solution.

<br>

***Light Curve Quality***

The dominant systematic present in K2 simple aperture photometry light curves is a sawtooth shape that is due to the roll of the spacecraft approximately every 6 hours. The PDC module of the Kepler Pipeline uses Principle Component Analysis to remove this signal in addition to other systematics. Below, we examine observed trends and noise levels in the PDC light curves for C3 (as measured using Data Release 5).

<div class="thumbnail" style="width: 68%;">
    <div class="caption">
        <i>Figure: CDPP measured for all targets as a function of Kepler magnitude. Dim targets have poorer overall photometric precision than bright targets, but can look better because the residual sawtooth falls below the noise floor. The saturated targets tend to have the lowest CDPP but often show a residual sawtooth. All cadences flagged as having definite thruster firings are gapped.</i>
    </div>
    <a href="images/release-notes/c3/cdpp_vs_mag.png">
        <img src="images/release-notes/c3/cdpp_vs_mag.png" class="img-responsive" alt="CDPP measured for all targets as a function of Kepler magnitude">
    </a>
</div>

<div class="thumbnail" style="width: 68%;">
    <div class="caption">
        <i>Figure: The photometric precision is generally better near the center of the focal plane where the variations in roll angle produce less pixel motion. This figure shows the 10th percentile CDPP of the 12th magnitude targets across the focal plane. The better performance near the center is evident.</i>
    </div>
    <a href="images/release-notes/c3/tenth_prctile_cdpp.png">
        <img src="images/release-notes/c3/tenth_prctile_cdpp.png" class="img-responsive" alt="10th percentile CDPP of the 12th magnitude targets across the focal plane">
    </a>
</div>

<div class="thumbnail" style="width: 68%;">
    <div class="caption">
        <i>Figure: Tests show that stellar signals are well preserved out to a period of about 20 days. However sometimes the stellar signals are partially masked by residual sawtooth.
</i>
    </div>
    <a href="images/release-notes/c3/amplitude_study_1_6379_amp.png">
        <img src="images/release-notes/c3/amplitude_study_1_6379_amp.png" class="img-responsive" alt="Tests show that stellar signals are well preserved out to a period of about 20 days.">
    </a>
</div>

The short cadence light curves produced by the Kepler pipeline are inadequate for scientific research and are not being released at this time.


<br>

***Reduced Noise from Change in Bandwidth***

The change in bandwidth for pointing control (from 50 to 20 seconds) for C3 resulted in an increase in SNR for short cadence by a factor of roughly 4--9, with the larger improvement seen at the higher frequency end. Note, the bandwidth pointing control parameter was set to 10 seconds for the original Kepler Mission.

<br>

<hr>



# K2 Campaign 2

These release notes are for the C2 data currently available at MAST in the nominal K2 data locations, which have been processed with the final version of the K2 pipeline as part of the <a href="k2-uniform-global-reprocessing-underway.html">K2 global uniform reprocessing effort</a>. The original release notes corresponding to the previous version(s) of C2 data can be found in the <a href="archived-k2-data-release-notes.html#k2-campaign-2">archived data release notes page</a>.

<h2>At a glance</h2>

<div class="col-lg-5">

<b><i>Pointing</i></b>
<ul>
<li> RA: 246.1264 degrees</li>
<li> Dec: -22.4473 degrees</li>
<li> Roll: 171.2284 degrees</li>
</ul>

<b><i>Targets</i></b>
<ul>
<li>13,399 in long cadence (LC)</li>
<li>54 in short cadence (SC)</li>
<li>Several custom targets (see below)</li>
</ul>

<b><i>Full Frame Images (FFI)</i></b>
<ul>
<li><a href="https://archive.stsci.edu/pub/k2/ffi/ktwo2014240042843-c02_ffi-cal.fits">ktwo2014240042843-c02_ffi-cal.fits</a></li>
<li><a href="https://archive.stsci.edu/pub/k2/ffi/ktwo2014294030900-c02_ffi-cal.fits">ktwo2014294030900-c02_ffi-cal.fits</a></li>
</ul>

<b><i>First cadence</i></b>
<ul>
<li>Time: 2014-08-23 18:27:16 UTC</li>
<li>Long Cadence Number: 95497</li>
<li>Short Cadence Number: 2853370</li>
</ul>

<b><i>Last cadence</i></b>
<ul>
<li>Time: 2014-11-10 13:27:43 UTC</li>
<li>Long Cadence Number: 99352</li>
<li>Short Cadence Number: 2969049</li>
</ul>

<b><i>Most Recent Processing Version</i></b>
<ul>
<li> <a href="k2-pipeline-release-notes.html#data-release-21">Data Release 21</a> </li>
</ul>

</div>

<div class="col-lg-7">

    <div class="thumbnail">
        <div class="caption">
            <i>Figure C2-FOV: Schematic of Kepler's C2 field-of-view with with high profile objects.</i>
        </div>
        <a href="images/k2/k2-c02-field.png">
            <img src="images/k2/k2-c02-field.png" class="img-responsive" alt="C2 field-of-view with high profile objects.">
        </a>
    </div>

    <div class="thumbnail">
        <div class="caption">
            <i>Figure C2-Mag: Distribution of the Kepler magnitudes of observed targets in C2.  All targets are chosen by guest observers. The distribution is due to how the largest <a href="k2-approved-programs.html#campaign-2">GO Programs</a>
            were selected. </i>
        </div>
        <a href="images/release-notes/c2/C2_lc_kp.png">
            <img src="images/release-notes/c2/C2_lc_kp.png" class="img-responsive" alt="Distribution of the Kepler magnitudes of observed targets in C2.">
        </a>
    </div>
</div>

</div>

<div class="thumbnail">
    <div class="caption">
        <i>Figure C2-FFI: Full Frame Image Highlights: A processed FFI image from C2 highlighting several extended source features in the field.</i>
    </div>
    <a href="images/release-notes/c2/K2-new-litho_2015.png">
        <img src="images/release-notes/c2/K2-new-litho_2015.png" class="img-responsive" alt="Campaign 2 Full Frame Image Highlights.">
    </a>
</div>

<br>


<h2>Features and Events</h2>

***Solar Activity***

During C2 Kepler experienced two energetic particle events of note, likely caused by solar activity. Both events affected all channels as can be seen in the dark current metric plot for the first 26 days of C2 (see Figure K2-Dark below). The first was a broad peak lasting approximately from cadence 95924&ndash;96335 (01-Sep-2014 11:51:30 Z [MJD: 56901.4941] to 09-Sep-2014 21:24:55 Z [MJD: 56909.8923]). The second was a stronger, sharper peaked event lasting approximately from cadence 96357&ndash;96551 (10-Sep-2014 17:01:54 Z [56910.7096] to 14-Sep-2014 07:20:35 Z [56914.30596]). At the peak of the 10-Sep-2014 event the average dark current increased by a factor of ~7 over the quiescent level. The GOES X-ray flux plot for this time shows an increased X-ray flux at Earth, though an independent measure of the exact timing and magnitude at the location of Kepler is not available. The impact to the data will be in the form of increased background level and increased photometric noise &mdash; the impact will be largest for faint targets.

<div class="thumbnail">
    <div class="caption">
        <i>Figure C20-Dark: The Dark Current Metric plotted against time for C2.</i>
    </div>
    <a href="images/release-notes/c2/c2_dark_current_metric.png">
        <img src="images/release-notes/c2/c2_dark_current_metric.png" class="img-responsive" alt="Dark Current Metric plotted against time.">
    </a>
</div>

<br>

***Mars***

Mars passed across the field of view between October 1 and October 23, 2014. See Figure C2-Mars below for a prediction of where Mars is on the focal plane during Campaign 2. Mars is a bright object that saturates the CCD causing significant bleeding along the columns it falls on as it passes through the field. Both its image and its reflection will likely contaminate nearby stars.

<div class="thumbnail">
    <div class="caption">
        <i>Figure C2-Mars: Schematic of Kepler's C2 field of view (outlined in blue) with the positions of Mars shown as small red squares.</i>
    </div>
    <a href="images/release-notes/c2/f2-fov.png">
        <img src="images/release-notes/c2/f2-fov.png" class="img-responsive" alt="Schematic of Kepler's C2 field of view.">
    </a>
</div>


<br>

***Two Globular Clusters***

The clusters M4 and M80 were observed in C2 by collecting all the pixels in 50x50 pixel masks. For M4, 16 of these custom apertures were collected and for M80, 4 were collected. The data files for M4 range from 200004370&ndash;200004385. The data files for M80 range from 200004386&ndash;200004389. The target pixel files may be found by using the Object Type field on the <a href="http://archive.stsci.edu/k2/data_search/search.php">MAST K2 data search</a> page.

<br>

***Two Solar System Objects***

Comet C/2013 A1 (Siding Spring) was observed by obtaining 2583, 25x1 pixel, masks across module.outputs 2.3, 4.2, 4.3 and 4.4 (channels 3, 10, 11, and 12 respectively) as shown in Figure C2-Comet below. These apertures were given custom aperture numbers ranging from 200001787&ndash;200004369. This target was observed as part of the Guest Observer Programs GO2030 (PI:Kelley) and GO2046 (PI:Lisse).

The Trans-Neptunian Object (268361) 2007 JJ43 was observed with 661 pixel masks, each one with size of either 11x1 or 13x1 pixels, and given custom aperture numbers ranging from 200001126&ndash;200001786. The pixel masks are shown below in Figure C2-TNO. This target was observed as part of Guest Observer Program GO2066 (PI:Schwamb).

These data sets can be found at the <a href="http://archive.stsci.edu/k2/data_search/search.php">MAST</a> by entering the Investigation ID on the search form. The Investigation ID matches the GO Program number that requested the observations.

<div class="thumbnail" style="width: 49%;display: inline-block;">
    <div class="caption">
        <i>Figure C2-Comet: The path (shown in blue) of C/2013 A1 (Siding Spring) runs along modules 2 and 4 during C2.</i>
    </div>
    <a href="images/release-notes/c2/comet-path.png">
        <img src="images/release-notes/c2/comet-path.png" class="img-responsive" alt="Path of comet Siding Spring.">
    </a>
</div>

<div class="thumbnail" style="width: 49%;display: inline-block;">
    <div class="caption">
        <i>Figure C2-TNO: The masks selected for mod.out 17.3 are shown in green. Those selected to capture the TNO 2007 JJ43 are shown as a green arc in the lower right-hand corner of this figure.</i>
    </div>
    <a href="images/release-notes/c2/jj43_path.png">
        <img src="images/release-notes/c2/jj43_path.png" class="img-responsive" alt="Masks selected to capture TNO 2007 JJ43.">
    </a>
</div>

<br>


***Attitude Tweak***

The pointing of the spacecraft was adjusted by approximately 10" on 2014-Aug-25, during cadence 95546, in order to ensure that the observed targets were centered in their masks. This event is flagged in the QUALITY column of the target pixel files with bit 1 (decimal=1). The data collected before the tweak may fall close to the edge of the collected mask and some of the object's flux may have been lost. Users are warned to use these cadences with caution.

<br>


<h2>Data Quality and Processing Notes</h2>

***Unflagged Large Pointing Excursion Towards Start of Campaign***

As part of the <a href="k2-uniform-global-reprocessing-underway.html">K2 global uniform reprocessing effort</a>, cadences are no longer automatically gapped based on the "Spacecraft is not in fine point" (QUALITY flag bit #16, decimal=32768) flag. Instead, the Kepler/K2 Science Office sets the "Spacecraft is in coarse point" flag (QUALITY flag bit #3, decimal=4) flag based on inspection of the actual pointing data for the campaign using high-frequency sub-cadence telemetry. For C2, the spacecraft was technically in 'coarse point' for LC cadences 95687&ndash;95696, which are early on in the campaign. However, the pointing was stable to ~2 pixels during this time period, which given the large size of the collected pixel-stamps for each target in C2 (3&ndash;4 pixels in a 'halo' around every target were collected), the decision was made to not set the "Spacecraft is in coarse point" flag (QUALITY flag bit #3, decimal=4) for these cadences.

While the targets did remain on downloaded pixels during this cadence range, a significant fraction of their flux came in and out of the pipeline-computed optimal photometric apertures. For the PA and PDC lightcurves, this results in some significant outliers during this cadence range, including some negative flux values. Consequently the CDPP (a measure of the detrended lightcurve scatter) is higher due both to the outliers themselves, and the PDC module likely wasting some of its 'detrending power' on trying to correct outliers instead of broader systematic features.

If users are utilizing the PA or PDC lightcurves, it is recommended that they discard the cadences in this range. However, if users are producing their own light curves, as long as their own photometric apertures are sufficiently large to capture each target's flux given the extra motion, or if their light-curve production/detrending technique utilizes all the pixels in the image, then these cadences should still be usable and result in good data.

<br>


***KIC 204241221 Short-Cadence Dynablack Bug***

KIC 204241221 is a V=8.7, A9V star with potentially observable asteroseismic signatures. Due to a bug in the K2 pipeline, Dynablack (<a href="k2-uniform-global-reprocessing-underway.html">see news post here</a>) was not run on the short-cadence pixel-level data for this target &mdash; the pipeline defaulted to the original CAL module. (Note that the long-cadence data did have Dynablack successfully run for this target.) The end result is minor, namely that the short-cadence TPF and lightcurve files for 204241221 will not have the benefits of Dynablack, e.g., the correction of potential cross-talk from the fine guidance sensors and rolling-band flags.

<br>


***LDE Flags***

During the latter half of C2 a large number of 'parity errors' were observed from the photometer's local detector electronics (LDE). These LDE parity errors can occur when a very bright star saturates and spills charge into the CCD serial readout register, causing an overflow at the input to the analog-to-digital converter. While these errors were rare in Kepler, the very bright stars, or solar system planets, on the focal plane in K2 can cause frequent parity errors. For example, stars on channels 67 and 75 were the source of many of the parity errors during C2. These errors do not affect the quality of data from pixels on the active focal plane.

The LDE parity error triggers a flag (bit 15, decimal=16384) in the QUALITY column of the target pixel files. This flag is set for the majority of cadences in the second half of the campaign.

Note that the pipeline does not utilize the LDE parity flag and thus the delivered data is unaffected by this flagging &mdash; it is mentioned here for users who may do their own processing and it is recommended that cadences with this flag set are not discarded as they contain good quality data.

<br>

<hr>



# K2 Campaign 1

<h2>At a glance</h2>

<div class="row">
<div class="col-lg-5">

    <b><i>Pointing</i></b>
    <ul>
        <li>RA: 173.939610 degrees</li>
        <li>Dec: 1.4172989 degrees</li>
        <li>Roll: 157.641206 degrees</li>
    </ul>

    <b><i>C1 Targets</i></b>
    <ul>
    <li>  21,732 in long cadence (LC)</li>
    <li>  56 in short cadence (SC)</li>
<li>  1 custom target was selected in C1: TNO 2002 GV31, which was assigned EPIC ID 200001049</li>
    </ul>

    <b><i>Full Frame Images (FFI)</i></b>
    <ul>
        <li><a href="https://archive.stsci.edu/pub/k2/ffi/ktwo2014157010055-c01_ffi-cal.fits">ktwo2014157010055-c01_ffi-cal.fits</a></li>
        <li><a href="https://archive.stsci.edu/pub/k2/ffi/ktwo2014203150825-c01_ffi-cal.fits">ktwo2014203150825-c01_ffi-cal.fits</a></li>
    </ul>

    <b><i>First cadence</i></b>
    <ul>
        <li>Time: 2014-05-30 15:54:44 UTC</li>
        <li>Long Cadence Number: 91332</li>
        <li>Short Cadence Number: 2728420</li>
    </ul>

    <b><i>Last cadence</i></b>
    <ul>
        <li>Time: 2014-08-20 20:19:37 UTC</li>
        <li>Long Cadence Number: 95353</li>
        <li>Short Cadence Number: 2849079</li>
    </ul>

    <b><i>Most Recent Processing Version</i></b>
    <ul>
    <li> <a href="k2-pipeline-release-notes.html#data-release-14">Data Release 14</a> </li>
    </ul>

</div>

<div class="col-lg-7">

    <div class="thumbnail">
        <div class="caption">
            <i>Figure: Schematic of Kepler's C1 field-of-view with selected targets shown with purple dots.</i>
        </div>
        <a href="images/campaign_selected/C1_selected.png">
            <img src="images/campaign_selected/C1_selected.png" class="img-responsive" alt="C1 field-of-view with selected targets">
        </a>
    </div>

</div>

</div>


<h2>Features and Events</h2>

***Operational Considerations***

Campaign 1 (C1) is the first full length observing campaign for K2 where the targets were
selected by peer review. The project was uncertain of the pointing precision and compression
efficiency that could be achieved in early K2 operations and took steps to miminimize the risk
of losing science data. In order to
allow for the potential of coarse point operations, all target apertures included six halo rings.
The oversized apertures and uncertain compression performance led the project to
include a mid-campaign break lasting 2.9 days in order to downlink data.

<br>

***Attitude Tweak***

The attitude of the spacecraft was tweaked by 3.3 pixels at cadence 91433 to better
position the targets in the centers of their apertures. All cadences in the first
2 days of C1 prior to this event have the first bit in the QUALITY column set
(integer value = 1) to indicate that they were taken prior to the tweak.

When creating light curves, the pipeline uses PA-COA to determine the optimal photometric
aperture that maximizes the signal-to-noise ratio for each target over the full
campaign. This static optimal aperture is determined from a robust average of
the achieved pointing, so relatively short segments of off-nominal pointing
tend to be excluded from the aperture calculation. In the case of C1, the optimal
apertures generally do not contain the target star in the pre-attitude tweak
cadences. Accordingly, the SAP-Flux and PDC-Flux values found in the light curve
files are gapped for the pre-tweak cadences (where the QUALITY flag=1). In
addition, neither background flux (FLUX_BKG, FLUX_BKG_ERR) nor motion
polynomial values (POS_CORR1, POS_CORR2) were computed for the
pre-tweak cadences.

Because of the large C1 apertures, the TPFs do fully contain the target in
the full set of pixels collected from the spacecraft. However, for the
pre-tweak cadences incorrect
background flux values were subtracted from the TPF pixel fluxes given
in the FLUX column of the TPF. Users wishing to recover photometry from these
cadences should add the per-cadence pixel background values (TPF column FLUX_BKG)
back into the pixel flux values and then compute their own background levels.
The position offset columns (POS_CORR1, POS_CORR2) should likewise be ignored
for these cadences.

Finally, in the pre-tweak cadences a small number of targets may have incorrect
smear calibrations due to bright saturating stars spilling charge into the
detector smear regions. Such affects are flagged and excluded from smear calibration
for the post-tweak cadences, but the pre-tweak positions of the bright stars
were not used to flag bad smear corrections. Only about 0.2% of the
focal plane columns were affected in this way, so the number of potentially
affected targets is small.

<br>

***Trans-Neptunian Object***

A long-cadence custom aperture was constructed in order to collect data on
trans-Neptunian Object 2002 GV31. Note, this target is very faint (V=22) and
falls in its 23x22 pixel custom aperture for only about 10 days. This custom
aperture can be found by searching the MAST for EPIC ID 200001049.

<br>

***EPIC Catalog Assignment***

For this Campaign, a number of targets were proposed without EPIC IDs.
If a target was observed, it was either 1) given an EPIC ID from the regular
catalog if that target matched a target in the catalog, or
2) assigned a new EPIC ID. We created EPIC IDs for 28 targets, ranging from
210282464 to 210282491. The remaining C1 targets have EPIC IDs ranging
from 201000001 to 202059065.

<br>

<h2>Data Quality and Processing Notes</h2>

***Light Curve Quality***

C1 long cadence light curves have been delivered with [Data Release 14](k2-pipeline-release-notes.html#data-release-14).
The dominant noise contributors in the C1 data are the saw-tooth roll signal inherent in
K2 data and an increased (over Kepler and later K2 campaigns) cross-boresight pointing motion
due to the lower bandwidth for the attitude determination and control system (ADCS)
used in K2 campaigns C0, C1, and C2. The low ADCS bandwidth was particularly
problematic for short cadence data, as it meant that the spacecraft pointing errors are on the
same time scale as the SC exposure, so that the pointing induced noise is correlated from
cadence to cadence. See notes under [C0](#k2-campaign-0) for details.

Analysis of the light curve quality reveals that long cadence CDPP values for dwarf stars are
in family with the values from subsequent campaigns.
The magnitude dependence of CDPP and its distribution over the focal plane are shown below.
Other CDPP benchmarks can be found in the
[table giving 6.5-hr CDPP as a function of magnitude](images/release-notes/c1/K2-C1_CDPP_Summary_16102111.txt).
<br>
<div class="thumbnail" style="width: 90%;">
<div class="caption">
<i>Figure C1-CDPP: 6.5-hr CDPP measurements for all targets as a function of Kepler magnitude. Dim targets have poorer overall photometric precision than bright targets, but can look better because the residual sawtooth falls below the noise floor. The saturated targets tend to have the lowest CDPP, but often show a residual sawtooth. </i>   
</div>
<a href="images/release-notes/c1/K2-C1_logg_CDPP_vs_model.png">
<img src="images/release-notes/c1/K2-C1_logg_CDPP_vs_model.png" class="img-responsive" alt="CDPP measured for all targets as a function of Kepler magnitude.">
</a>
</div>
<div class="thumbnail" style="width: 90%;">
<div class="caption">
<i>Figure C1-CDPP FocalPlane: 6.5-hr CDPP measured as a function of position on the focal plane for 12th and 14th magnitude dwarf stars. The photometric precision is generally better near the center of the focal plane where the variations in roll angle produce less pixel motion. All cadences coincident with a definite thruster firing are gapped.</i>
<a href="images/release-notes/c1/K2-C1_dwarf__CDPP_by_mod_out.jpg">
<img src="images/release-notes/c1/K2-C1_dwarf__CDPP_by_mod_out.jpg" class="img-responsive" alt="CDPP per channel for 12th magnitude dwarfs">
</a>    
</div>
</div>

<br>

<hr>



# K2 Campaign 0

Campaign 0 (C0) was implemented as a full-length engineering test to prove that K2 was a viable mission. It observed sources "at risk" from a community-provided target list.

<h2>At a glance</h2>

<div class="row">
<div class="col-lg-5">

    <b><i>Pointing</i></b>
    <ul>
        <li>RA: 98.2985439 degrees</li>
        <li>Dec: 21.5904167 degrees</li>
        <li>Roll: 177.4754730 degrees</li>
    </ul>

    <b><i>Full Frame Images (FFI)</i></b>
    <ul>
        <li><a href="https://archive.stsci.edu/pub/k2/ffi/ktwo2014070234206-c00_ffi-cal.fits">ktwo2014070234206-c00_ffi-cal.fits</a></li>
        <li><a href="https://archive.stsci.edu/pub/k2/ffi/ktwo2014074233223-c00_ffi-cal.fits">ktwo2014074233223-c00_ffi-cal.fits</a></li>
        <li><a href="https://archive.stsci.edu/pub/k2/ffi/ktwo2014110010101-c00_ffi-cal.fits">ktwo2014110010101-c00_ffi-cal.fits</a></li>
    </ul>

    <b><i>First cadence</i></b>
    <ul>
        <li>Time: 2014-03-12 00:18:30 UTC</li>
        <li>Long Cadence Number: 87434</li>
        <li>Short Cadence Number: 2611480</li>
    </ul>

    <b><i>Last cadence</i></b>
    <ul>
        <li>Time: 2014-05-27 16:48:13 UTC</li>
        <li>Long Cadence Number: 91186</li>
        <li>Short Cadence Number: 2724069</li>
    </ul>

    <b><i>Most Recent Processing Version</i></b>
    <ul>
    <li> <a href="k2-pipeline-release-notes.html#data-release-2">Data Release 2</a> </li>
    </ul>

</div>

<div class="col-lg-7">

    <div class="thumbnail">
        <div class="caption">
            <i>Figure: Schematic of Kepler's C0 field-of-view with selected targets shown with purple dots.</i>
        </div>
        <a href="images/campaign_selected/C0_selected.png">
            <img src="images/campaign_selected/C0_selected.png" class="img-responsive" alt="C0 field-of-view">
        </a>
    </div>

</div>

</div>

<h2>Features and Events</h2>

***Not In Fine Point Data***

The second half of the C0 data is more indicative of the quality of data users should expect from K2. The Kepler spacecraft was not in fine point for the first part of C0, causing large photometric scatter. The data quality is much improved in the second half of the campaign, beginning on cadence 89347 after the safe mode, when compared to the first half of the campaign. See the QUALITY flag (bit 16) to determine when the spacecraft was in fine point.

<br>

***Safe Mode***

The Kepler Spacecraft was in safe mode between cadences 88198 and 89346. Data is flagged in the QUALITY column with bit 2. The project used this time to fix large attitude errors that were occuring during resaturation events.

<br>

***Module 7 Failure***

Prior to the start of C0, on January 21, 2014, the photometer was autonomously powered off by an under voltage fault in the Local Detector Electronics Power Supply. Since that time, module 7 (i.e., channels 17 to 20) has yielded no star data or charge injection signal. The subsequent behavior of this module is very similar to that of module 3 after it failed on January 19, 2010. K2 continues to operate and collect simultaneous data from sources falling upon the remaining 19 detector modules over 105 square degrees. There is no indication of any accelerated degradation on these other modules.

<br>


***Large Pixel Masks***

When planning C0 observations, the pointing performance of K2 was not accurately known. The worst case scenario was that a star at the edge of the focal plane could move as much as 40" from its nominal position. Therefore each star was assigned a large pixel mask by first computing a Kepler-style optimal aperture and then adding 10 rings of pixels to account for a potential 40" pointing offset. During the second half of C0, the pointing performance was excellent and the pointing drifts were no more than 6" for any target star. Care will be needed when performing photometry on C0 data. Simply including all collected pixels for a given target will not create a high signal-to-noise light curve. For tools to help choose your photometric aperture, see for example, <a href="http://keplergo.arc.nasa.gov/PyKE.shtml">PyKE contributed software</a>.

<br>

***Jupiter's Reflection***

Because K2 points along the ecliptic, its field of view will occasionally contain bright solar system objects. Jupiter was in the K2 field of view during C0 from 2014-03-14 through 2014-05-12, but fell on dead module 3. It creates a bright antipodal ghost on module 23, channel 79, and impacts all the targets observed in this region. See the FFI ktwo2014074233223-c00, extension 79, for an image of the reflection.

While Jupiter was on the focal plane, the background level was increased over its nominal value for nearly half the channels, with the largest impact seen in channels 53 -- 84. In addition, as Jupiter moved on and off the focal plane, a specular reflection lasting approximately 6 hours was seen in these channels. The relative background levels as measured in the smear signal from channel 83 are shown below as Jupiter enters the focal plane (near cadence no. 87525) and leaves the focal plane (cadence no. 90375). The specular bump resulted in an increase in background level of 25-30% for the affected channels, while the quasi-static background increase for the time Jupiter was on the focal plane was 3-5%.

<div class="thumbnail" style="width: 68%;">
    <div class="caption">
        <i>Figure: FFI showing the reflection of Jupiter as seen on channel 79.</i>
    </div>
    <a href="images/release-notes/c0/Jupiter-ghost3.png">
        <img src="images/release-notes/c0/Jupiter-ghost3.png" class="img-responsive" alt="FFI showing the reflection of Jupiter as seen on channel 79.">
    </a>
</div>

<div class="thumbnail" style="width: 68%;">
    <div class="caption">
        <i>Figure: The background level on channel 83 as Jupiter enters (left) and leaves (right) the focal plane.</i>
    </div>
    <a href="images/release-notes/c0/ch83_jupiter_on_smear.png">
        <img src="images/release-notes/c0/ch83_jupiter_on_smear.png" class="img-responsive" alt="The background level on channel 83 as Jupiter enters (left) and leaves (right) the focal plane.">
    </a>
</div>

<br>

***Observations of M35 and NGC 2158***

The open clusters M35 (NGC 2168) and NGC 2158 were observed during this campaign by placing 154 separate 50x50 pixel masks over the densest portion of these two adjacent clusters. Each mask was given a custom aperture number to act as the unique identifier found in the file name. The target pixel files for these clusters have custom aperture numbers ranging from 200,000,811 to 200,000,964.

<div class="thumbnail" style="width: 68%;">
    <div class="caption">
        <i>Figure: Individual masks when tiled together cover the field of view containing M35 and NGC 2158.</i>
    </div>
    <a href="images/release-notes/c0/M35_im1.png">
        <img src="images/release-notes/c0/M35_im1.png" class="img-responsive" alt="Individual masks when tiled together cover the field of view containing M35 and NGC 2158.">
    </a>
</div>

<br>

<h2>Data Quality and Processing Notes</h2>

***Photometric Jitter Caused by Lower Bandwidth***

During the development of the K2 Mission, the number of guide stars per fine-guidance sensor (FGS) was changed from ten (for Kepler) to one (for K2). This change was demanded by the need for increased aperture sizes given the uncertainties in the star-tracker to boresight alignment and the need to acquire an entirely new field-of-view every 80 to 90 days. To compensate for the increased sensor noise and assure that fine-point lock could be achieved, the attitude control bandwidth was decreased from 0.1 Hz (for Kepler) to 0.02 Hz (for K2). This change in bandwidth means that the cross-boresight attitude (i.e., RA and Dec) has a time constant of 50 seconds, comparable to the short-cadence duration. Engineering studies have shown that the photometric precision of the long-cadence data is also compromised by the larger pointing jitter associated with the lower bandwidth. The project has approved a change in bandwidth to 0.05 Hz (20 seconds) starting with Campaign 3.

<br>

***Channel 10 Black Correction***

The black correction on Channel 10, mod.out 4.2, has problems because a bright star bleeds into the black region. For data release 1, the affected regions of the black are excluded from the fit of the black, so the fit is poorly constrained and we see chatter in the residuals. This mostly affects stars in the last 200 rows of the channel.

<br>

***Image Artifacts in K2***

The thermal environment is changing more rapidly in K2 than it did for the Kepler Mission. As a result the number of channels with significant rolling band (changes in the black level that are both time and spatial dependent) is larger for K2. The channels observed to be most impacted by rolling band in C0 are 1, 2, 10, 11, 14, 25-28, 36, 44, 58, 62, 74 and 79. Other known image artifacts, such as Moiré patterns and undershoot from bright stars, are also likely to be enhanced in K2 data as compared to Kepler. See the <a href="http://archtest.stsci.edu/kepler/manuals/KSCI-19033-001.pdf">Kepler Instrument Handbook</a>.

<br>

***Thruster Firing Flags***

Since the thruster firing flags are not populated in FITS quality flags for the
C0 Type-1 TPFs, they are delivered as separate
long-cadence <a href="http://archive.stsci.edu/missions/k2/thruster_firings/thruster_firing_flags_c0_lc.csv">(thruster_firing_flags_c0_lc.csv)</a>
and short-cadence <a href="http://archive.stsci.edu/missions/k2/thruster_firings/thruster_firing_flags_c0_sc.csv">(thruster_firing_flags_c0_sc.csv)</a>
thruster firing tables for the C0 campaign.

<br>

<hr>


# Two-wheel Concept Engineering Test


<h2>At a glance</h2>

Before the official start of the K2 Mission, the spacecraft executed a 9-day test to demonstrate the two-wheel mission concept. While this engineering test is not an officially-supported Campaign, the pixel data were made public to help the community appraise the characteristics of K2 data.  Extensive data release notes are not available for this test, but support is offered on a best-effort basis via the Kepler Science Center helpdesk. Please refer to this data set as the "Two-wheel Concept Engineering Test" in all publications.

<div class="row">
<div class="col-lg-5">

    <b><i>Pointing</i></b>
    <ul>
        <li>RA: 358.6492374 degrees</li>
        <li>Dec: -2.1523890 degrees</li>
        <li>Roll: -156.4440683 degrees</li>
    </ul>

    <b><i>First cadence</i></b>
    <ul>
        <li>Time: 2014-02-04 12:57:46 UTC</li>
        <li>Long Cadence Number: 85698</li>
        <li>Short Cadence Number: 2559400</li>
    </ul>

    <b><i>Last cadence</i></b>
    <ul>
        <li>Time: 2014-02-13 12:44:30 UTC</li>
        <li>Long Cadence Number: 86137</li>
        <li>Short Cadence Number: 2572599</li>
    </ul>

</div>

</div>

<hr>
<br>
Page last updated on:
<script>
document.write(document.lastModified);
</script>

Title: K2 Data Release Notes
Save_as: k2-data-release-notes.html

[TOC]

This page details the key features of the K2 data releases,
including information on field pointing, target selection, observation times and cadences, processing version, unique observational features of each campaign, significant events that transpired during each campaign, data quality and processing features, and other descriptions of technical issues relevant to the scientific exploitation of the data.

<hr>

# K2 Campaign 19

<h2>At a glance</h2>

<div class="col-lg-5">

<b><i>Pointing</i></b>
<ul>
<li> RA: 347.2590265 degrees</li>
<li> Dec: -4.2027029 degrees</li>
<li> Roll: 22.8818335 degrees</li>
</ul>

<b><i>Targets With Data Available at MAST</i></b>
<ul>
<li>44,152 EPIC IDs in long cadence (LC).</li>
<li>222 EPIC IDs in short cadence (LC).</li>
<li>31 moving objects (including Neptune) were tiled with LC custom strip apertures (see below for details).</li>
</ul>

<b><i>Full Frame Images (FFI)</i></b>
<ul>
<li><a href="https://archive.stsci.edu/missions/k2/ffi/kplr2018268151041-c19_ffi-orig.fits">kplr2018268151041-c19_ffi-orig.fits</a>
<li><a href="https://archive.stsci.edu/missions/k2/ffi/kplr2018249002316-c19_ffi-orig.fits">kplr2018249002316-c19_ffi-orig.fits</a>
</ul>

<b><i>First cadence</i></b>
<ul>
<li>Start Time: 2018-08-30 15:17:05 UTC</li>
<li>Long Cadence Number: 167333</li>
<li>Short Cadence Number: 5008450</li>
</ul>

<b><i>Last cadence<sup>†</sup></i></b>
<ul>
<li>End Time: 2018-09-26 00:23:59 UTC</li>
<li>Long Cadence Number: 168623</li>
<li>Short Cadence Number: 5047179</li>
</ul>

<sup>†</sup>The last collected long cadence was 168624 (and corresponding short cadences 5047180&ndash;5047209), but were discarded in processing due to quality issues.<br><br>

<b><i>Most Recent Processing Version</i></b>
<ul>
<li> <a href="k2-pipeline-release-notes.html#data-release-29">Data Release 29</a> </li>
</ul>

<div class="thumbnail">
<div class="caption">
<i>Figure C19-Mag: Distribution of the Kepler magnitudes of observed LC targets. All targets are chosen by guest observers. The distribution is due to how the largest <a href="k2-approved-programs.html#campaign-19">GO Programs</a>
were selected.</i>
</div>
<a href="images/release-notes/c19/c19_lc_magnitude_distribution.png">
<img src="images/release-notes/c19/c19_lc_magnitude_distribution.png" class="img-responsive" alt="Distribution of the Kepler magnitudes of observed C19 LC targets.">
</a>
</div>

</div>

<div class="col-lg-7">

<div class="thumbnail">
<div class="caption">
<i>Figure C19-FOV: Schematic of Kepler's C19 field-of-view with high profile objects. </i>
</div>
<a href="images/k2/k2-c19-field.png"><img class="img-responsive" style="padding:0.5em;" src="images/k2/k2-c19-field.png" id="c19fov" alt="C19 field of view with highlights, such as known planet hosts and the path of Neptune and 2P Encke.">
</a>
</div>

<div class="thumbnail">
    <div class="caption">
    <i>Figure: Figure C19-FFI: A gif of the two full frame images (FFIs) taken during C19, with a flux scaling designed to highlight features of interest.</i>
</div>
<a href="images/release-notes/c9/C19-FFIs.gif">
    <img src="images/release-notes/c19/C19-FFIs.gif" class="img-responsive" alt="The C19 FFIs">
    </a>
</div>

</div>

<br>

<br>

<h2>Features and Events</h2>

***Overlap with C3, C12, and the Engineering Test Run***

As shown in Figure C19-FOV, C19 field significantly overlaps with Campaign 12 and the Engineering Test Run, and partially overlaps with Campaign 3. Many targets observed in C19 were also observed in C3 and/or C12, thus establishing a several year temporal baseline that provides unique science opportunities.

<br>

***Custom Targets***

There were 11,495 galaxies targeted in the C19 field of view; all but six used standard aperture masks. The six large galaxies were covered with 35-pixel diameter large circular custom masks.

There were 15 bright stars that were assigned 24-pixel diameter LC disk apertures to capture the wings of the point spread function.

The C19 field of view includes 31 moving objects composed of 9 Asteroids, 20 faint Trans-Neptunian Objects, the planet Neptune, and the periodic comet [2P/Encke](https://en.wikipedia.org/wiki/Comet_Encke), all observed in long cadence. Neptune was also observed in short cadence approximately 20 days on each side of the stationary point of Neptune. Just as when Neptune was observed in [Campaign 3](k2-approved-programs.html#campaign-3), Neptune is expected to saturate the detector, resulting in spikes in the column direction as Neptune moves across the detector. The custom aperture numbers associated with Neptune are 200262135&ndash;200262467 for long cadence and 200262489&mdash;200262493 for short cadence. These observations were taken as part of Guest Observer Programs GO19009 (PI:Garcıa-Munoz), GO19061 (PI:Trafton), and GO19069 (PI:Smith).

See the <a href="images/release-notes/c19/kplr2018316185300_c19_caf.csv">csv file that maps</a> the custom aperture number to the target name to find the apertures for a specific target.

<br>

***Erratic Pointing Due to Fuel Exhaustion***

Due to an anomalous drop in fuel pressure, the Kepler team [paused the science observations for K2 Campaign 18](kepler-fuel-status-update-faq.html) about 50 days into the campaign and then a month later [successfully downloaded the C18 data](k2-campaign-18-downlink-successful.html). At the start of Campaign 19 the spacecraft configuration was [modified in order to adapt to a change in thruster performance](k2-campaign-19-status-update.html) due to the low fuel pressure. Observations for C19 were collected for about a month, at which point the Kepler team received data showing that the spacecraft no longer had sufficient remaining fuel to point precisely enough to gather useful scientific data, and [observations were again paused](k2-campaign-19-ended-to-downlink-data.html) and then later [successfully downloaded](k2-campaign-19-raw-data-available.html). While [an attempt was made to start Campaign 20](kepler-spacecraft-update.html), without sufficient fuel [end-of-flight was declared and the spacecraft was retired](https://www.nasa.gov/press-release/nasa-retires-kepler-space-telescope-passes-planet-hunting-torch). Thus Campaign 19 is the final campaign for which scientific data is available.

Figure C19-Pointing-1 shows the pointing performance of the spacecraft over the duration of Campaign 19 via the observed deviation of targets from their expected location as a function of long cadence number &mdash; the blue line shows the deviation affecting all targets from displacement of the spacecraft boresight, while the red line shows the maximum deviation at the edge of the field of view due to the roll angle. Figure C19-Pointing-2 similarly shows the combined motion of a target at the edge of the field of view in science pixels, as well as some important data quality flags. Note that neither FFI was captured while in Fine Point and have noticeably different pointings (see Figure C19-FFI above).

As can be seen in these figures, for the first ~8.5 days (long cadences 167333&ndash;167742; short cadences 5008450&ndash;5020749), the spacecraft boresight was significantly off-nominal, and as a result nearly all targets were completely outside their observed pixel stamps, which had only 2- or 3-pixel halos &mdash; it is not expected that useable photometric data can be obtained for this time region for the pre-selected Campagin 19 targets. For the next ~7 days (long cadences 167743&ndash;168097; short cadences 5020750&ndash;5031399) the pointing due to boresight and roll was nominal compared to other K2 campaigns, and thus this ~7 day region should provide K2 data of quality comparable to other campaigns. For the final ~11 days (long cadences 168098&ndash;168623; short cadences 5031400&ndash;5047179) the boresight and roll fluctuated erratically &mdash; the 'well-behaved' portions of this timespan should provide useable photometric data for most targets, though careful analysis is encouraged --- the last likely useable long cadence is 168481.


<div class="thumbnail" style="width: 100%;">
<div class="caption">
<i>Figure C19-Pointing-1: The C19 pointing history, shown by the motion of the boresight and the roll motion at the edge in science pixels.</i>
</div>
<a href="images/release-notes/c19/c19_pointing_history.png">
<img src="images/release-notes/c19/c19_pointing_history.png" class="img-responsive" alt="The pointing history for C19">
</a>
</div>
</div>

<div class="thumbnail" style="width: 100%;">
<div class="caption">
<i>Figure C19-Poining-2: The C19 pointing history, shown by the motion of experienced by a target at the edge of the field of view in science pixels.</i>
</div>
<a href="images/release-notes/c19/c19_pointing_flags.png">
<img src="images/release-notes/c19/c19_pointing_flags.png" class="img-responsive" alt="The pointing-related flags for C19">
</a>
</div>
</div>

<br>

***Pointing and Roll Performance During the Central ~7 days***

Examining only the central ~7 days of continuously nominal pointing (long cadences 167743&ndash;168097; short cadences 5020750&ndash;5031399), the C19 pointing and roll behavior are very well behaved compared to most other K2 campaigns. The pipeline-calculated maximum distance between the derived and nominal positions for any target (the "maximum attitude residual", or MAR) for C19 in this time period is under 1.5 pixels, well under the 3-pixel limit accommodated by the aperture halos.

<div class="thumbnail" style="width: 49%;display: inline-block;">
<div class="caption">
<i>Figure C19-Roll-Error: the roll-error between the photometrically derived attitude (PAD) and the nominal pointing plotted against time for the central ~7 days of C19.</i>
<a href="images/release-notes/c19/c19_pad_pdq_attitude_roll.png">
<img src="images/release-notes/c19/c19_pad_pdq_attitude_roll.png" class="img-responsive" alt="Pipeline measured roll error for C19.">
</a>
</div>
</div>

<div class="thumbnail" style="width: 49%;display: inline-block;">
<div class="caption">
<i>Figure C19-MAR: the maximum distance between the photometrically derived attitude (PAD) and the nominal position plotted against time for the central ~7 days C19.</i>
<a href="images/release-notes/c19/c19_pad_pdq_attitude_mar.png">
<img src="images/release-notes/c19/c19_pad_pdq_attitude_mar.png" class="img-responsive" alt="Maximum residual of the C19 attitude measured with PAD and PDQ.">
</a>
</div>
</div>

<br>


<h2>Data Quality and Processing Notes</h2>

***Special Processing Parameters***

In order to successfully process this unique campaign with the Kepler pipeline, and produce useful data of sufficient quality, the following approach was taken:

<ul>

<li> The final long cadence observed by the spacecraft (168624) and the corresponding short cadences (5047180&ndash;5047209) were discarded due to data quality issues.<br>

<br>

<li> For the rest of the campaign (long cadences 167333&ndash;168623 and short cadences 5008450&ndash;5047179), instead of the "Dynablack" calibration method that has been used for all other campaigns processed as part of the <a href="k2-uniform-global-reprocessing-underway.html">global uniform reprocessing effort</a>, the simpler CAL method was used to calibrate pixels, due to the short duration of the observations. Rolling band flags (see the <a href="k2-uniform-global-reprocessing-underway.html">news post on global reprocessing</a>) were still able to be computed and provided.<br>

<br>

<li> When producing the raw / simple aperture (PA) lightcurves, unlike all other campaigns processed as part of the <a href="k2-uniform-global-reprocessing-underway.html">global uniform reprocessing effort</a>, cadences marked as "Spacecraft is not in fine point" (QUALITY flag bit #16, decimal=32768) were discarded. This is illustrated in Figure C19-Pointing-2. The resulting PA cadence range is thus 167742&ndash;168481 (note that while 167742 is included, it is flagged as COARSE_POINT, i.e., QUALITY flag bit #4.)  <br>

<br>

<li> When producing the systematic-corrected (PDC) lightcurves, the cadence range was restricted to the central ~7 days of continuously stable pointing (long cadences 167743&ndash;168097 and short cadences 5020750&ndash;5031399). This is illustrated in Figure C19-Pointing-1. The corresponding time range is 2018-09-08 00:24:52 UTC to 2018-09-15 06:32:00 UTC.<br>


</ul>

As a result, users will have calibrated pixels for nearly the entire campaign, raw / simple aperture lightcurves (called PA or SAP_FLUX) for the last ~2/3 of the campaign during times when the spacecraft was in fine point, and systematic-corrected lightcurves (called PDC or PDCSAP_FLUX) for the central ~7 days of continuously good pointing.

Users producing their own lightcurves will likely want to make use of the "Spacecraft is not in fine point" (QUALITY flag bit #16, decimal=32768) and "Spacecraft is in coarse point" (QUALITY flag bit #3, decimal=4) to remove cadences with significant pointing deviations from nominal, while accounting for the location of their target on the focal plane (and thus observed motion due to spacecraft roll) and aperture size.

<br>


***Light Curve Quality***

Examining only the central ~7 days of continuously nominal pointing (long cadences 167743&ndash;168097; short cadences 5020750&ndash;5031399), the 6-hour spacecraft roll cycle dominates the systematic errors in the C19 simple aperture photometry light curves, similar to other campaigns.
The pipeline CDPP 12th magnitude noise benchmark for C19 is technically the lowest of any campaign observed to-date &mdash; however, it is not necessarily correct to compare it to other campaigns, as there is only ~7 days of data analyzed here, compared to other campaigns that normally have ~50&ndash;80 days. It is likely that the PDC module is over-fitting the data to some extent. Users are cautioned that astrophysical variations, particularly those of long (~several days or more) period may be artificially suppressed in the PDCSAP_FLUX data. Users can examine the C19 [cotrending basis vectors](https://archive.stsci.edu/missions/k2/cbv/) to check and see if they contain data trends that resemble astrophysical signals of interest.

The magnitude dependence of CDPP for the central ~7 days, and its distribution over the focal plane, are shown below in Figure C19-CDPP. Other CDPP benchmarks can be found in the
<a href="images/release-notes/c19/c19_bin1.00_sc1.00_CDPP_Summary_19040216.txt">
table giving 6.5-hr CDPP as a function of magnitude.</a>

<br>

<div class="thumbnail" style="width: 90%;">
<div class="caption">
<i>Figure C19-CDPP: 6.5-hr CDPP measurements for all targets as a function of Kepler magnitude. Dim targets have poorer overall photometric precision than bright targets, but can look better because the residual sawtooth falls below the noise floor. The saturated targets tend to have the lowest CDPP, but often show a residual sawtooth. </i>
</div>
<a href="images/release-notes/c19/c19_logg_CDPP_vs_model.png">
<img src="images/release-notes/c19/c19_logg_CDPP_vs_model.png" class="img-responsive" alt="CDPP measured for all targets as a function of Kepler magnitude.">
</a>
</div>
</div>

<div class="thumbnail" style="width: 90%;">
<div class="caption">
<i>Figure C19-CDPP FocalPlane: 6.5-hr CDPP measured as a function of position on the focal plane, for 12th and 14th magnitude dwarf stars. The photometric precision is generally better near the center of the focal plane where the variations in roll angle produce less pixel motion. All cadences coincident with a definite thruster firing are gapped.</i>
<a href="images/release-notes/c19/c19_dwarf_CDPP_by_mod_out.png">
<img src="images/release-notes/c19/c19_dwarf_CDPP_by_mod_out.png" class="img-responsive" alt="CDPP per channel for 12th and 14th magnitude dwarfs">
</a>
</div>
</div>


<hr>

<br>

# K2 Campaign 18

<h2>At a glance</h2>

<div class="col-lg-5">

<b><i>Pointing</i></b>
<ul>
<li> RA: 130.1610170 degrees</li>
<li> Dec: 16.8278629  degrees</li>
<li> Roll: 165.8977388 degrees</li>
</ul>

<b><i>Targets With Data Available at MAST</i></b>
<ul>
<li>36,909 EPIC IDs in long cadence (LC).</li>
<li>237 EPIC IDs in short cadence (LC).</li>
<li>27 moving objects were tiled with LC custom strip apertures. 11 bright stars were assigned 24-pixel diameter LC disk apertures to capture the point spread function wings. See the <a href="images/release-notes/c18/kplr2018254082100_c18_caf.csv">csv file that maps</a> the custom aperture number to the target name to find the apertures for a specific target.</li>
</ul>

<b><i>Full Frame Images (FFI)</i></b>
<ul>
<li><a href="https://archive.stsci.edu/missions/k2/ffi/ktwo2018143080022-c18_ffi-cal.fits">ktwo2018143080022-c18_ffi-cal.fits</a>
</ul>

<b><i>First cadence</i></b>
<ul>
<li>Start Time: 2018-05-13 00:44:43 UTC</li>
<li>Long Cadence Number: 161969</li>
<li>Short Cadence Number: 4847530</li>
</ul>

<b><i>Last cadence</i></b>
<ul>
<li>End Time: 2018-07-02 21:51:26 UTC</li>
<li>Long Cadence Number: 164458</li>
<li>Short Cadence Number: 4922229</li>
</ul>

<b><i>Most Recent Processing Version</i></b>
<ul>
<li> <a href="k2-pipeline-release-notes.html#data-release-27">Data Release 27</a> </li>
</ul>

</div>

<div class="col-lg-7">

<div class="thumbnail">
<div class="caption">
<i>Figure C18-FOV: Schematic of Kepler's C18 field-of-view with high profile objects. </i>
</div>
<a href="images/k2/k2-c18-field.png"><img class="img-responsive" style="padding:0.5em;" src="images/k2/k2-c18-field.png" id="c18fov" alt="C18 field of view with highlights, such as the Beehive and M67 clusters, and the path of the asteroid Apophis.">
</a>
</div>

<div class="thumbnail">
<div class="caption">
<i>Figure C18-Mag: Distribution of the Kepler magnitudes of observed LC targets. All targets are chosen by guest observers. The distribution is due to how the largest <a href="k2-approved-programs.html#campaign-18">GO Programs</a>
were selected.</i>
</div>
<a href="images/release-notes/c18/c18_lc_magnitude_distribution.png">
<img src="images/release-notes/c18/c18_lc_magnitude_distribution.png" class="img-responsive" alt="Distribution of the Kepler magnitudes of observed C18 LC targets.">
</a>
</div>

</div>

<h2>Features and Events</h2>

***Overlap with C5 and C16***

The C18 field is almost identical to that observed during Campaign 5, and overlaps substantially with Campaign 16. Many targets observed in C18 were also observed in C5 and C16, establishing a 3 year temporal baseline with an 8 month duty cycle that provides unique science opportunities.

<br>

***Galaxies***

There are 2,193 galaxies targeted in the C18 field of view; all but five used standard aperture masks. The five large galaxies were covered with 35-pixel diameter large circular custom masks.

<br>

***Clusters***

The C18 field of view includes the Beehive cluster (M44) and M67. M44 is one of the most nearby open clusters; its members were observed using standard masks.
M67 was tiled with a series of 441 20 x 20 pixel tiles for a total of 176,400 pixels.

<br>

***Solar System Objects***

The C18 field of view includes 22 comets and trojan Asteroids, 9 faint Trans-Neptunian Objects, and the formerly potentially hazardous asteroid [99942 Apophis](https://en.wikipedia.org/wiki/99942_Apophis), all observed in long cadence.

<br>

***Early End to Campaign 18***

Due to indications that the spacecraft fuel tank was running very low ~50 days into Campaign 18, [collection of science data was terminated on July 2, 2018](https://www.nasa.gov/feature/ames/nasa-s-kepler-spacecraft-pauses-science-observations-to-download-science-data) and the spacecraft was put in a hibernation-like state until the data was downloaded at the regularly scheduled time in early August. As a result, only one FFI was collected.

<br>

***Pointing and Roll Performance***

The C18 pointing and roll behavior are well within the limits of that seen in other K2 campaigns, with no degradation seen due to potentially low fuel levels.
The pipeline-calculated maximum distance between the derived and nominal positions for any target (the "maximum attitude residual", or MAR)
for C18 is less than 1.9 pixels for nearly the entire campaign, well under the 3-pixel limit accommodated by the aperture halos.

The exception is about a dozen long cadences just prior to BKJD 3432 / MJD 58264.5, where the pointing temporarily exceeded 4 pixels, as clearly seen in the plots below. Users are encouraged to discard long cadences 162613 &ndash; 162627 (short cadences 4866897 &ndash; 4867246) due to this pointing excursion. These cadences are flagged using QUALITY flag bit #3. Similarly, while not visible in the plots below, the very last long cadence of the campaign, 164458 (short cadences 4922216 &ndash; 4922230) had a very large pointing excursion and are also flagged using QUALITY flag bit #3.

As mentioned in the C14 release notes, a change in the on-board fine point fault logging threshold
results in additional cadences being flagged as "Spacecraft is not in fine point"
(QUALITY flag bit #16, decimal=32768). As a reminder, the project recommends that starting with C15,
users look to QUALITY flag bit #3 as an accurate indicator of poor spacecraft pointing.

<div class="thumbnail" style="width: 50%;display: inline-block;">
<div class="caption">
<i>Figure C18-Roll-Error: the roll-error between the photometrically derived attitude (PAD) and the nominal pointing plotted against time for C18.</i>
<a href="images/release-notes/c18/c18_pad_pdq_attitude_roll.png">
<img src="images/release-notes/c18/c18_pad_pdq_attitude_roll.png" class="img-responsive" alt="Pipeline measured roll error for C18.">
</a>
</div>
</div>

<div class="thumbnail" style="width: 48%;display: inline-block;">
<div class="caption">
<i>Figure C18-MAR: the maximum distance between the photometrically derived attitude (PAD) and the nominal position plotted against time for C18.</i>
<a href="images/release-notes/c18/c18_pad_pdq_attitude_mar.png">
<img src="images/release-notes/c18/c18_pad_pdq_attitude_mar.png" class="img-responsive" alt="Maximum residual of the C18 attitude measured with PAD and PDQ.">
</a>
</div>
</div>

<br>

<h2>Data Quality and Processing Notes</h2>

***Light Curve Quality***

As in previous campaigns, the 6-hour spacecraft roll cycle continues
to dominate the systematic errors in C18 simple aperture photometry light curves.
The pipeline CDPP 12th magnitude noise benchmark for C18 is
the second-lowest ever seen (just higher C5) at the time of this processing.
The improved precision compared to most other campaigns is likely due to a combination of lower star density,
stable pointing (compared to most other campaigns), and the updated pipeline version (in-particular the use of the coarse-point flags; see <a href="k2-uniform-global-reprocessing-underway.html">the global reprocessing effort announcement</a> for details).

The magnitude dependence of CDPP and its distribution over the focal plane are shown below. Other CDPP benchmarks can be found in the
<a href="images/release-notes/c18/c18_bin1.00_sc1.00_CDPP_Summary_18101501.txt">
table giving 6.5-hr CDPP as a function of magnitude.</a>

<br>

<div class="thumbnail" style="width: 90%;">
<div class="caption">
<i>Figure C18-CDPP: 6.5-hr CDPP measurements for all targets as a function of Kepler magnitude. Dim targets have poorer overall photometric precision than bright targets, but can look better because the residual sawtooth falls below the noise floor. The saturated targets tend to have the lowest CDPP, but often show a residual sawtooth. </i>
</div>
<a href="images/release-notes/c18/c18_logg_CDPP_vs_model.png">
<img src="images/release-notes/c18/c18_logg_CDPP_vs_model.png" class="img-responsive" alt="CDPP measured for all targets as a function of Kepler magnitude.">
</a>
</div>
</div>

<div class="thumbnail" style="width: 90%;">
<div class="caption">
<i>Figure C18-CDPP FocalPlane: 6.5-hr CDPP measured as a function of position on the focal plane, for 12th and 14th magnitude dwarf stars. The photometric precision is generally better near the center of the focal plane where the variations in roll angle produce less pixel motion. All cadences coincident with a definite thruster firing are gapped.</i>
<a href="images/release-notes/c18/c18_dwarf_CDPP_by_mod_out.png">
<img src="images/release-notes/c18/c18_dwarf_CDPP_by_mod_out.png" class="img-responsive" alt="CDPP per channel for 12th and 14th magnitude dwarfs">
</a>
</div>
</div>

<br>

***Target With Incomplete FITS Header: EPIC 200233235***

The custom target EPIC 200233235 is missing centroid information and values for the following FITS headers in its target pixel and lightcurve files: RA_OBJ, DEC_OBJ, 1CRVL4, 2CRVL4, 1CRVL5, 2CRVL5, 1CRVL6, 2CRVL6, 1CRVL7, 2CRVL7, 1CRVL8, 2CRVL8, 1CRVL9, 2CRVL9, EXPOSURE, TELAPSE, LIVETIME, TSTART, TSTOP, CRVAL1, and CRVAL2. This was a custom target for which the entire 20x20 pixel stamp was selected as the aperture by the pipeline. As a result there were no background pixels available to compute the centroid information, and thus the values for the listed FITS headers. This issue appears unique to this custom target and no other targets are affected. Users wanting to analyze this target are encourage to create their own lightcurve using software such as the [lightkurve Python package](https://docs.lightkurve.org), [PyKE software tool suite](http://pyke.keplerscience.org), or [other packages](https://archive.stsci.edu/missions-and-data/kepler/related-software-1).


<hr>

<br>



# K2 Campaign 17

<h2>At a glance</h2>

<div class="col-lg-5">
<p>
Campaign 17 was flown in the forward velocity vector direction in order to enable simultaneous K2 and ground-based observations of numerous targets (supernovae, variable stars, exoplanets, etc.) in the C17 field of view.
</p>

<b><i>Pointing</i></b>
<ul>
<li> RA:  202.5496152 degrees</li>
<li> Dec: -7.7210759 degrees</li>
<li> Roll:  -20.7870925 degrees</li>
</ul>

<b><i>Targets With Data Available at MAST</i></b>
<ul>
<li>46,230 EPIC IDs in long cadence (LC).</li>
<li>179 EPIC IDs in short cadence (LC).</li>
<li>24 moving objects were tiled with LC custom strip apertures. 6 bright stars were assigned 24-pixel diameter LC disk apertures to capture the point spread function wings. See the <a href="images/release-notes/c17/kplr2018190145900_c17_caf.csv">csv file that maps</a> the custom aperture number to the target name to find the apertures for a specific target.</li>
</ul>

<b><i>Full Frame Images (FFI)</i></b>
<ul>
<li><a href="https://archive.stsci.edu/missions/k2/ffi/ktwo2018073065336-c17_ffi-cal.fits">ktwo2018073065336-c17_ffi-cal.fits</a>
<li><a href="https://archive.stsci.edu/missions/k2/ffi/ktwo2018112122825-c17_ffi-cal.fits">ktwo2018112122825-c17_ffi-cal.fits</a>
</ul>

<b><i>First cadence</i></b>
<ul>
<li>Start Time: 2018-03-02 00:33:12 UTC</li>
<li>Long Cadence Number: 158445</li>
<li>Short Cadence Number: 4741810</li>
</ul>

<b><i>Last cadence</i></b>
<ul>
<li>End Time: 2018-05-08 02:33:28 UTC</li>
<li>Long Cadence Number: 161727</li>
<li>Short Cadence Number: 4840299</li>
</ul>

<b><i>Most Recent Processing Version</i></b>
<ul>
<li> <a href="k2-pipeline-release-notes.html#data-release-25">Data Release 25</a> </li>
</ul>

</div>

<div class="col-lg-7">

<div class="thumbnail">
<div class="caption">
<i>Figure C17-FOV: Schematic of Kepler's C17 field-of-view with high profile objects. </i>
</div>
<a href="images/k2/k2-c17-field.png"><img class="img-responsive" style="padding:0.5em;" src="images/k2/k2-c17-field.png" id="c17fov" alt="C17 field of view with highlights showing numerous supernovae detected during campaign 17 and the first magnitude star Spica.">
</a>
</div>

<div class="thumbnail">
<div class="caption">
<i>Figure C17-Mag: Distribution of the Kepler magnitudes of observed LC targets. All targets are chosen by guest observers. The distribution is due to how the largest <a href="k2-approved-programs.html#campaign-17">GO Programs</a>
were selected.</i>
</div>
<a href="images/release-notes/c17/c17_lc_magnitude_distribution.png">
<img src="images/release-notes/c17/c17_lc_magnitude_distribution.png" class="img-responsive" alt="Distribution of the Kepler magnitudes of observed C17 LC targets.">
</a>
</div>

</div>

<h2>Features and Events</h2>

***Galaxies***

There are 14,314 galaxies targeted in the C17 field of view; all but eight used standard aperture masks. The eight large galaxies were covered with large circular custom masks. The very large number of galaxies observed was due in part to the K2 Supernova Experiment (see below).

<br>

***Supernovae***

The forward velocity vector orientation during C17 allowed for simultaneous ground-based observations of K2 targets. As shown in Figure C17-FOV, numerous supernovae were observed by Kepler and ground-based observatories during C17. More details of the supernova campaign can be found at the <a href="supernova-experiment/index.html">Supernova Experiment site</a>.

<br>

***Spica***

The first magnitude star Spica fell on channel 48 for the entirety of campaign 17. Spica's optical ghost (due to reflection off the telescope's Schmidt corrector plate) is seen on the opposite side of the focal plane on channel 40. (See <a href="images/kepler_focal_plane_layout_channels_color.png">this schematic of the Kepler detector layout</a> for the positions of channels 40 and 48.) As can be seen in the FFI images below, the light from both Spica and its ghost cover a large portion of channels 48 and 40. As well Spica bleeds along its central columns, resulting in poor CCD calibration along those columns. Users with targets near Spica or its ghost are encouraged to take this information into account when interpreting observations of those targets, or if performing their own data reduction.

<div class="thumbnail" style="width: 49%;display: inline-block;">
<div class="caption">
<i>Figure C17-Spica: Spica as seen in an FFI on channel 48. The central columns are saturated along the entire detector, resulting in poor CCD calibration for those columns, thus causing them to appear dark.</i>
<a href="images/release-notes/c17/c17_spica.png">
<img src="images/release-notes/c17/c17_spica.png" class="img-responsive" alt="Spica as seen in an FFI on channel 48.">
</a>
</div>
</div>

<div class="thumbnail" style="width: 49%;display: inline-block;">
<div class="caption">
<i>Figure C17-Spica-Ghost: the ghost image of Spica as seen in an FFI on channel 40 due to reflection off the Schmidt corrector plate. The ghost is equidistant and opposite the field of view center from Spica.</i>
<a href="images/release-notes/c17/c17_spica_ghost.png">
<img src="images/release-notes/c17/c17_spica_ghost.png" class="img-responsive" alt="the ghost image of Spica as seen in an FFI on channel 40.">
</a>
</div>
</div>

<br>

***Pointing and Roll Performance***

The C17 pointing and roll behavior are well within the limits of that seen
in other K2 campaigns, with no degradation seen due to potentially low fuel levels.
The pipeline-calculated maximum distance between the
derived and nominal positions for any target (the "maximum attitude residual", or MAR)
for C17 is less than 2.0 pixels, well under the 3-pixel limit accommodated by the aperture halos.

As mentioned in the C14 release notes, a change in the on-board fine point fault logging threshold
results in additional cadences being flagged as "Spacecraft is not in fine point"
(QUALITY flag bit #16, decimal=32768). As a reminder, the project recommends that starting with C15,
users look to QUALITY flag bit #3 as an accurate indicator of poor spacecraft pointing.

<div class="thumbnail" style="width: 49%;display: inline-block;">
<div class="caption">
<i>Figure C17-Roll-Error: the roll-error between the photometrically derived attitude (PAD) and the nominal pointing plotted against time for C17.</i>
<a href="images/release-notes/c17/c17_pad_pdq_attitude_roll.png">
<img src="images/release-notes/c17/c17_pad_pdq_attitude_roll.png" class="img-responsive" alt="Pipeline measured roll error for C17.">
</a>
</div>
</div>

<div class="thumbnail" style="width: 49%;display: inline-block;">
<div class="caption">
<i>Figure C17-MAR: the maximum distance between the photometrically derived attitude (PAD) and the nominal position plotted against time for C17.</i>
<a href="images/release-notes/c17/c17_pad_pdq_attitude_mar.png">
<img src="images/release-notes/c17/c17_pad_pdq_attitude_mar.png" class="img-responsive" alt="Maximum residual of the C17 attitude measured with PAD and PDQ.">
</a>
</div>
</div>

<br>

<h2>Data Quality and Processing Notes</h2>

***Light Curve Quality***

As in previous campaigns, the 6-hour spacecraft roll cycle continues
to dominate the systematic errors in C17 simple aperture photometry light curves.
The pipeline CDPP 12th magnitude noise benchmark for C17 is
the lowest seen since C6 and the third-lowest overall (just higher than C6 and C5) at the time of this processing.
The improved precision compared to most other campaigns is likely due to a combination of lower star density,
stable pointing (compared to most other campaigns), and the updated pipeline version (in-particular the use of the coarse-point flags; see <a href="k2-uniform-global-reprocessing-underway.html">the global reprocessing effort announcement</a> for details).

The magnitude dependence of CDPP and its distribution over the focal plane are shown below. Other CDPP benchmarks can be found in the
<a href="images/release-notes/c17/c17_bin1.00_sc1.00_CDPP_Summary_18051614.txt">
table giving 6.5-hr CDPP as a function of magnitude.</a>
<br>
<div class="thumbnail" style="width: 90%;">
<div class="caption">
<i>Figure C17-CDPP: 6.5-hr CDPP measurements for all targets as a function of Kepler magnitude. Dim targets have poorer overall photometric precision than bright targets, but can look better because the residual sawtooth falls below the noise floor. The saturated targets tend to have the lowest CDPP, but often show a residual sawtooth. </i>
</div>
<a href="images/release-notes/c17/c17_logg_CDPP_vs_model.png">
<img src="images/release-notes/c17/c17_logg_CDPP_vs_model.png" class="img-responsive" alt="CDPP measured for all targets as a function of Kepler magnitude.">
</a>
</div>
<div class="thumbnail" style="width: 90%;">
<div class="caption">
<i>Figure C17-CDPP FocalPlane: 6.5-hr CDPP measured as a function of position on the focal plane, for 12th and 14th magnitude dwarf stars. The photometric precision is generally better near the center of the focal plane where the variations in roll angle produce less pixel motion. All cadences coincident with a definite thruster firing are gapped.</i>
<a href="images/release-notes/c17/c17_dwarf_CDPP_by_mod_out.png">
<img src="images/release-notes/c17/c17_dwarf_CDPP_by_mod_out.png" class="img-responsive" alt="CDPP per channel for 12th and 14th magnitude dwarfs">
</a>
</div>


<hr>

<br>



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

<b><i>Targets With Data Available at MAST</i></b>
<ul>
<li>35,571 EPIC IDs in long cadence (LC).</li>
<li>131 EPIC IDs in short cadence (LC).</li>
<li>20 moving objects were tiled with LC custom strip apertures. 7 bright stars were assigned 24-pixel diameter LC disk apertures to capture the point spread function wings. See the <a href="images/release-notes/c16/kplr2018125112300_c16_caf.csv">csv file that maps</a> the custom aperture number to the target name to find the apertures for a specific target.</li>
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
<i>Figure C16-Mag: Distribution of the Kepler magnitudes of observed LC targets. All targets are chosen by guest observers. The distribution is due to how the largest <a href="k2-approved-programs.html#campaign-16">GO Programs</a>
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
combination of the relatively low star density, the return to more stable pointing (compared to recent
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


***Short-Cadence Target With no PDC Flux***

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

<b><i>Targets With Data Available at MAST</i></b>
<ul>
<li>35,078 EPIC IDs in long cadence (LC).</li>
<li>118 EPIC IDs in short cadence (LC).</li>
<li>38 moving objects were tiled with LC custom strip apertures. 13 bright stars were assigned 24-pixel diameter LC disk apertures to capture the point spread function wings. See the <a href="images/release-notes/c15/kplr2017355085300_c15_caf.csv">csv file that maps</a> the custom aperture number to the target name to find the apertures for a specific target.</li>
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
<i>Figure C15-Mag: Distribution of the Kepler magnitudes of observed LC targets. All targets are chosen by guest observers. The distribution is due to how the largest <a href="k2-approved-programs.html#campaign-15">GO Programs</a>
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

These release notes are for the C14 data currently available at MAST (Data Release 40) in the nominal K2 data locations, which have been processed with the final version of the K2 pipeline as part of the <a href="k2-uniform-global-reprocessing-underway.html">K2 global uniform reprocessing effort</a>. The original release notes corresponding to the previous versions of C14 data (Data Release 20) can be found in the <a href="archived-k2-data-release-notes.html#k2-campaign-14">archived data release notes page</a>.

<h2>At a glance</h2>

<div class="col-lg-5">

<b><i>Pointing</i></b>
<ul>
<li> RA:  160.6824762 degrees</li>
<li> Dec:  6.8509316 degrees</li>
<li> Roll:  158.7573464 degrees</li>
</ul>

<b><i>Targets With Data Available at MAST</i></b>
<ul>
<li>39,024 EPIC IDs in long cadence (LC).</li>
<li>147 EPIC IDs in short cadence (LC).</li>
<li>42 moving objects were tiled with LC custom strip apertures. 7 bright stars were assigned 24-pixel diameter LC disk apertures to capture the point spread function wings. See the <a href="images/release-notes/c14/ktwoc14_caf.csv">csv file that maps</a> the custom aperture number to the target name to find the apertures for a specific target.</li>
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
<li> <a href="k2-pipeline-release-notes.html#data-release-40">Data Release 40</a> </li>
</ul>

<br>

<div class="thumbnail">
<div class="caption">
<i>Figure C14-Mag: Distribution of the Kepler magnitudes of observed LC targets. All targets are chosen by guest observers. The distribution is due to how the largest <a href ="k2-approved-programs.html#campaign-14">GO Programs</a> were selected. The peak in the distribution at faint magnitudes is due to the large number of faint galaxies targeted.</i>
</div>
<a href="images/release-notes/c14/c14_lc_magnitude_distribution.png">
<img src="images/release-notes/c14/c14_lc_magnitude_distribution.png" class="img-responsive" alt="Distribution of the Kepler magnitudes of observed LC targets.">
</a>
</div>

</div>


<div class="col-lg-7">

<div class="thumbnail">
<div class="caption">
<i>Figure C14-FOV: Schematic of Kepler's C14 field-of-view with high profile objects. </i>
</div>
  <a href="images/k2/k2-c14-field.png">
    <img src="images/k2/k2-c14-field.png" class="img-responsive" alt="C14 field-of-view with selected targets">
  </a>
</div>

<div class="thumbnail">
  <div class="caption">
    <i>Figure: Figure C14-FFI: A full frame image (FFI) taken during C14, with a flux scaling designed to highlight features of interest.</i>
  </div>
  <a href="images/release-notes/c14/C14R-FFI.png">
    <img src="images/release-notes/c14/C14R-FFI.png" class="img-responsive" alt="A C14 FFI">
  </a>
</div>

</div>

</div>

<h2>Features and Events</h2>

***Galaxies***

The C14 field of view sits at 53&deg; N Galactic latitude in the North Galactic cap.  There are 14,691 galaxies targeted
in the C14 field of view.  47 of the Galaxies with radii > 40 arcseconds were covered with large circular masks.
Twelve galaxies were covered with 15x15 pixel square masks.  Six galaxies (M95, M96, M105, NGC3384,
NGC3423, NGC3412) were covered by 40x40 pixel square masks consisting of 16 tiles of 10x10 pixel sub-masks.

The MAST [K2 Data Search and Retreival Page](http://dx.doi.org/10.17909/t9-6zdf-eh42) has an option to select data by Object Type, including a section for Galaxies, which includes all the large galaxies mentioned above.  The corresponding custom EPIC IDs for the masks can also be found in the [custom aperture file](http://dx.doi.org/10.17909/t9-dw50-3e97) hosted at MAST.

In addition to the many galaxies, a number of <a href ="k2-approved-programs.html#campaign-14">notable targets</a>
were observed during C14, including Wolf 359, a nearby late M-dwarf.

<br>

***Pointing and Roll Performance***

The C14 pointing and roll behavior are well within the limits of that seen in other K2 campaigns for the majority of the campaign.
The pipeline calculated maximum distance between the
derived and nominal positions for any target (the "maximum attitude residual", or MAR) for C14 is less than 1.8 pixels, well under the 3-pixel limit accommodated by the aperture halos.  There were far fewer anomalous thruster firing events in C14 than were seen in other campaigns.

<div class="thumbnail" style="width: 49%;display: inline-block;">
<div class="caption">
<i>Figure C14-Roll-Error: the roll-error between the photometrically derived attitude (PAD) and the nominal pointing plotted against time for C14.</i>
</div>
<a href="images/release-notes/c14/c14_pad_pdq_attitude_roll_dr40.png">
<img src="images/release-notes/c14/c14_pad_pdq_attitude_roll_dr40.png" class="img-responsive" alt="Pipeline measured roll error for C14.">
</a>
</div>


<div class="thumbnail" style="width: 49%;display: inline-block;">
<div class="caption">
<i>Figure C14-MAR: the maximum distance between the photometrically derived attitude (PAD) and the nominal position plotted against time for C14.</i>
</div>
<a href="images/release-notes/c14/c14_pad_pdq_attitude_mar_dr40.png">
<img src="images/release-notes/c14/c14_pad_pdq_attitude_mar_dr40.png" class="img-responsive" alt="Maximum residual of the C14 attitude measured with PAD and PDQ.">
</a>
</div>


<br>

<h2>Data Quality and Processing Notes</h2>

***Light Curve Quality***

As in other campaigns, the 6-hour spacecraft roll cycle dominates the systematic errors in C14 simple aperture photometry light curves.
The pipeline CDPP 12th magnitude noise benchmark for C14 (DR40) is comparable to that seen in other campaigns with similar star density.

The magnitude dependence of CDPP and its distribution over the focal
plane are shown below. Other CDPP benchmarks can be found in the
<a href="images/release-notes/c14/c14_bin1.00_sc1.00_CDPP_Summary_20031320.txt">
table giving 6.5-hr CDPP as a function of magnitude.</a>

<br>

<div class="thumbnail" style="width: 90%;">
<div class="caption">
<i>Figure C14-CDPP: 6.5-hr CDPP measurements for all targets as a function of Kepler magnitude. Dim targets have poorer overall photometric precision than bright targets, but can look better because the residual sawtooth falls below the noise floor. The saturated targets tend to have the lowest CDPP, but often show a residual sawtooth. </i>
</div>
<a href="images/release-notes/c14/c14_logg_CDPP_vs_model_dr40.png">
<img src="images/release-notes/c14/c14_logg_CDPP_vs_model_dr40.png" class="img-responsive" alt="CDPP measured for all targets as a function of Kepler magnitude.">
</a>
</div>

<div class="thumbnail" style="width: 90%;">
<div class="caption">
<i>Figure C14-CDPP FocalPlane: 6.5-hr CDPP measured as a function of position on the focal plane, for 12th and 14th magnitude dwarf stars. The photometric precision is generally better near the center of the focal plane where the variations in roll angle produce less pixel motion. All cadences coincident with a definite thruster firing are gapped.</i>
<a href="images/release-notes/c14/c14_dwarf_CDPP_by_mod_out_dr40.png">
<img src="images/release-notes/c14/c14_dwarf_CDPP_by_mod_out_dr40.png" class="img-responsive" alt="CDPP per channel for 12th magnitude dwarfs">
</a>
</div>
</div>

<br>

***No Lightcurve Files for Wolf 359***

Due to an error in pipeline configuration for the data release 40 processing, the proper motion of Wolf 359 (~4.7 arcseconds/yr, or >1 Kepler pixel per year) was not taken into account.  As a result, there was no optimal aperture generated for the target, and thus no long- or short-cadence lightcurve files were produced.  The target pixel files, aside from not having any pixels identified as belonging to an optimal aperture, were not affected.

Users are encouraged to create their own lightcurves for this object from target pixel files using software such as the [lightkurve Python package](https://docs.lightkurve.org), [PyKE software tool suite](http://pyke.keplerscience.org), or [other packages](https://archive.stsci.edu/missions-and-data/kepler/related-software-1).

<br>

***Improper Smear Correction for Channel 74***

For data release 40, channel 74 in campaign 14 had an improper smear correction that results in an additive effect at the pixel-level, with two step-wise discontinuities.

The cause of this improper correction appears to be unexpected behavior from the Dynablack pixel-level calibration algorithim (<a href="k2-uniform-global-reprocessing-underway.html">see news post here</a>) that was used for data release 40.  Outliers unique to this channel and campaign caused Dynablack to improperly bias-correct the smear calibration region, which in turn led to an improper smear correction for the entire channel.

As shown in Figure C14-DR40-Smear, this results in an additive effect of ~5E4 electrons per cadence per pixel, with a step discontinuity at cadences ~510 and ~2600 (MJD ~57905 and ~57958) of an extra ~1.5E4 electrons per cadence per pixel.  The discontinuities correspond to when the spacecraft crossed the roll pointing zero-points.  This effect is for every pixel in channel 74.  As it is an additive effect, only faint targets should be significantly affected, depending on the number of pixels used for the photometric aperture relative to the target's flux.  Users are cautioned to be aware of this effect when interpreting any signals for their science.

Note that, at some level, this effect influences the creation of the CBVs for all channels in the same PDC unit of work as channel 74 (channels 73&ndash;84).  If the CBVs have this signal present, then all PDC lightcurves for all targets on those channels could have it present.  However, inspection of PDC lightcurves on these channels did not reveal any significantly visible effect, and thus users should not have to worry about this signal being present in lightcurves for channels other than 74.

<div class="thumbnail" style="width: 90%;">
<div class="caption">
<i>Figure C14-DR40-Smear: The measured smear signal per-channel for Campaign 14, Data Release 40.  The smear correction for channel 74 is noticeably out of family, off by ~5E4 electrons per cadence per pixel, with a step discontinuity at cadences ~510 and ~2600 (MJD ~57905 and ~57958) of an extra ~1.5E4 electrons per cadence per pixel, when the spacecraft crossed the roll zero-points.</i>
<a href="images/release-notes/c14/C14R-PAD-Smear-Level.png">
<img src="images/release-notes/c14/C14R-PAD-Smear-Level.png" class="img-responsive" alt="Smear level per channel for C14 DR40">
</a>
</div>
</div>


<br>


<hr>

# K2 Campaign 13

These release notes are for the C13 data currently available at MAST in the nominal K2 data locations, which have been processed with the final version of the K2 pipeline as part of the <a href="k2-uniform-global-reprocessing-underway.html">K2 global uniform reprocessing effort</a>. The original release notes corresponding to the previous version(s) of C13 data can be found in the <a href="archived-k2-data-release-notes.html#k2-campaign-13">archived data release notes page</a>.


<h2>At a glance</h2>

<div class="col-lg-5">

<b><i>Pointing</i></b>
<ul>
<li> RA: 72.7971166 degrees</li>
<li> Dec: 20.7870759 degrees</li>
<li> Roll: -172.7995758 degrees</li>
</ul>

<b><i>Targets With Data Available at MAST</i></b>
<ul>
<li>26,170 EPIC IDs in long cadence (LC).</li>
<li>118 EPIC IDs in short cadence (LC).</li>
<li>15 moving objects were tiled with LC custom strip apertures. 33 bright stars, including Aldebaran, were assigned 40-pixel diameter LC disk apertures to capture the point spread function wings. Nine bright Hyades cluster stars were assigned 24-pixel diameter SC disk apertures. See the <a href="images/release-notes/c13/ktwoc13_caf.csv">csv file that maps</a> the custom aperture number to the target name.</li>
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
<li> <a href="k2-pipeline-release-notes.html#data-release-24">Data Release 24</a> </li>
</ul>

</div>

<div class="col-lg-7">


<div class="thumbnail">
<div class="caption">
<i>Figure C13-FOV: Schematic of Kepler's C13 field-of-view with high profile objects.</i>
</div>
<a href="images/k2/k2-c13-field.png">
<img src="images/k2/k2-c13-field.png" class="img-responsive" alt="C13 field-of-view with selected targets plotted in purple.">
</a>
</div>


<div class="thumbnail">
<div class="caption">
<i>Figure C13-Mag: Distribution of the Kepler magnitudes of observed LC targets. All targets are chosen by guest observers. The distribution is due to how the largest <a href ="k2-approved-programs.html#campaign-13">GO Programs</a> were selected.</i>
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

<div class="thumbnail" style="width: 49%;display: inline-block;">
<div class="caption">
<i>Figure C13-Roll-Error: the roll-error between the photometrically derived attitude (PAD) and the nominal pointing plotted against time for C13.</i>   
</div>
<a href="images/release-notes/c13/c13_pad_pdq_attitude_roll_reprocessing_drn24.png">
<img src="images/release-notes/c13/c13_pad_pdq_attitude_roll_reprocessing_drn24.png" class="img-responsive" alt="Pipeline measured roll error for C13.">
</a>
</div>

<div class="thumbnail" style="width: 49%;display: inline-block;">
<div class="caption">
<i>Figure C13-MAR: the maximum distance between the photometrically derived attitude (PAD) and the nominal position plotted against time for C13.</i>
<a href="images/release-notes/c13/c13_pad_pdq_attitude_mar_reprocessing_drn24.png">
<img src="images/release-notes/c13/c13_pad_pdq_attitude_mar_reprocessing_drn24.png" class="img-responsive" alt="Maximum residual of the C13 attitude measured with PAD and PDQ.">
</a>
</div>
</div>

<br>

<h2>Data Quality and Processing Notes</h2>

***Light Curve Quality***

As in previous campaigns, the 6-hour spacecraft roll cycle continues to dominate the systematic errors in C13 simple aperture photometry light curves.
The pipeline CDPP 12th magnitude noise benchmark is similar to star fields of comparable star density (e.g., C4, C5, C16).


The magnitude dependence of CDPP and its distribution over the focal
plane are shown below. Other CDPP benchmarks can be found in the
<a href="images/release-notes/c13/c13_bin1.00_sc1.00_CDPP_Summary_reprocessing_drn24.txt">
table giving 6.5-hr CDPP as a function of magnitude.</a>
<br>
<div class="thumbnail" style="width: 90%;">
<div class="caption">
<i>Figure C13-CDPP: 6.5-hr CDPP measurements for all targets as a function of Kepler magnitude. Dim targets have poorer overall photometric precision than bright targets, but can look better because the residual sawtooth falls below the noise floor. The saturated targets tend to have the lowest CDPP, but often show a residual sawtooth. </i>   
</div>
<a href="images/release-notes/c13/c13_logg_CDPP_vs_model_reprocessing_drn24.png">
<img src="images/release-notes/c13/c13_logg_CDPP_vs_model_reprocessing_drn24.png" class="img-responsive" alt="CDPP measured for all targets as a function of Kepler magnitude.">
</a>
</div>
<div class="thumbnail" style="width: 90%;">
<div class="caption">
<i>Figure C13-CDPP FocalPlane: 6.5-hr CDPP measured as a function of position on the focal plane, for 12th and 14th magnitude dwarf stars. The photometric precision is generally better near the center of the focal plane where the variations in roll angle produce less pixel motion. All cadences coincident with a definite thruster firing are gapped.</i>
<a href="images/release-notes/c13/c13_dwarf_CDPP_by_mod_out_reprocessing_drn24.png">
<img src="images/release-notes/c13/c13_dwarf_CDPP_by_mod_out_reprocessing_drn24.png" class="img-responsive" alt="CDPP per channel for 12th magnitude dwarfs">
</a>    
</div>
</div>

<br>

***Short-Cadence Targets With no PDC Flux***

The following four targets failed short-cadence PDC processing due to them being custom targets and the only targets on their channel. The short-cadence light curve files include the (nominal and unaffected) SAP flux, but the PDC_SAP flux is all zeros. Note that the long-cadence data for these targets are unaffected and are nominal.

<ul>
<li>200173880
<li>200173881
<li>200173884
<li>200173885
</ul>



<br>

<hr>

# K2 Campaign 12

These release notes are for the C12 data currently available at MAST (Data Release 39) in the nominal K2 data locations, which have been processed with the final version of the K2 pipeline as part of the <a href="k2-uniform-global-reprocessing-underway.html">K2 global uniform reprocessing effort</a>. The original release notes corresponding to the previous versions of C12 data (Data Release 18) can be found in the <a href="archived-k2-data-release-notes.html#k2-campaign-12">archived data release notes page</a>.


<h2>At a glance</h2>

<div class="col-lg-5">

<b><i>Pointing</i></b>
<ul>
<li>RA: 351.6588124 degrees</li>
<li>Dec: -5.1023328 degrees</li>
<li>Roll: -156.8808419 degrees</li>
</ul>

<b><i>Targets With Data Available at MAST</i></b>
<ul>
<li>45,951 EPIC IDs in long cadence (LC).</li>
<li>234 EPIC IDs in short cadence (LC).</li>
<li>42 unique LC custom targets were selected, along with two SC custom target apertures for Chiron and Trappist-1. See the <a href="images/release-notes/c12/ktwoc12_caf.csv">csv file that maps</a> the custom aperture number to the target name.</li>
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
<li> <a href="k2-pipeline-release-notes.html#data-release-39">Data Release 39</a> </li>
</ul>

    <br>

    <div class="thumbnail">
        <div class="caption">
            <i>Figure C12-Mag: Distribution of the Kepler magnitudes of observed LC targets in C12. All targets are chosen by Guest Observers. The shape is due to how the largest <a href="k2-approved-programs.html#campaign-12">Guest Observer programs</a> were selected.</i>
        </div>
        <a href="images/release-notes/c12/c12_lc_magnitude_distribution.png">
            <img src="images/release-notes/c12/c12_lc_magnitude_distribution.png" class="img-responsive" alt="Distribution of the Kepler magnitudes of observed LC targets in C12.">
        </a>
    </div>

</div>


<div class="col-lg-7">

<div class="thumbnail">
  <div class="caption">
    <i>Figure: Figure C12-FOV: Schematic of Kepler's C12 field-of-view with high profile objects.</i>
  </div>
  <a href="images/k2/k2-c12-field.png">
    <img src="images/k2/k2-c12-field.png" class="img-responsive" alt="C12 field-of-view with selected targets">
  </a>
</div>

<div class="thumbnail">
  <div class="caption">
    <i>Figure: Figure C12-FFI: A full frame image (FFI) taken during C12, with a flux scaling designed to highlight features of interest.</i>
  </div>
  <a href="images/release-notes/c12/C12R-FFI.png">
    <img src="images/release-notes/c12/C12R-FFI.png" class="img-responsive" alt="A C12 FFI">
  </a>
</div>

</div>

</div>

<h2>Features and Events</h2>

***Mars***

Mars passed through the focal plane during C12, entering active silicon on module 24 output 3 (channel 83) on 2017-01-16 (relative cadence index 1550) and moving off of module 3 output 4 (dead channel 8) on 2017-02-09 (relative cadence index 2728).  In order, Mars fell on the active channels 83, 82, 67, 66, 41, 42, 22, and 23 (see [this figure](/images/kepler_focal_plane_layout_channels_color.png) for the detector channel layout).  The movie *C12-Mars-at-LC* below shows the
direct image of Mars passing over channel 83.
With an average visual magnitude of V ~ -0.2,
the image of Mars is highly saturated and introduces
significant scattered light.  It also creates a
video crosstalk signal in each of the other three channels of each module on
which it falls.  In addition, there is a ghost
image of Mars caused by reflection off of the field-flattener lens and CCD then
off of the Schmidt correcter and back to the focal plane.  This ghost image appears approximately on the opposite side of the boresight from the direct Mars image. An example of the direct image with crosstalk and the ghost image
is shown in the figures below (*C12-Module-8 Mars FFI Image*,
*C12-Channel-62 Mars Ghost Image*) taken from the second FFI: <a href="https://archive.stsci.edu/pub/k2/ffi/ktwo2017032102633-c12_ffi-cal.fits">ktwo2017032102633-c12_ffi-cal.fits</a>.

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
in other K2 campaigns for the majority of the campaign.  The pipeline calculated maximum distance between the derived and nominal positions for any target (the "maximum attitude residual", or MAR) for C12 is less than 2.0 pixels for nearly the entire campaign, well under the 3-pixel limit accommodated by the aperture halos.  The exception is one 6-hour period starting at 2017-03-03 19:05:24 (MJD 57815.79542) right near the end of the campaign, as can be seen in Figures C12-Roll-Error and C12-MAR.  Cadence numbers 140670&ndash;140681 have a roll error of more than -50 arcseconds, though roll performance returned to normal at the subsequent thruster firing and remained nominal for the rest of the campaign.

<div class="thumbnail" style="width: 49%;display: inline-block;">
<div class="caption">
<i>
Figure C12-Roll-Error: the roll-error between the photometrically derived attitude (PAD) and the nominal pointing plotted against time for C12.
</i>   
</div>
<a href="images/release-notes/c12/c12_pad_pdq_attitude_roll_dr39.png">
<img src="images/release-notes/c12/c12_pad_pdq_attitude_roll_dr39.png" class="img-responsive" alt="Pipeline measured roll error for C12.">
</a>
</div>

<div class="thumbnail" style="width: 49%;display: inline-block;">
<div class="caption">
  <i>
    Figure C12-MAR: the maximum distance between the photometrically derived attitude (PAD) and the nominal position plotted against time for C12.
  </i>
  </div>
  <a href="images/release-notes/c12/c12_pad_pdq_attitude_mar_dr39.png">
    <img src="images/release-notes/c12/c12_pad_pdq_attitude_mar_dr39.png" class="img-responsive" alt="Maximum residual of the C12 attitude measured with PAD and PDQ.">
  </a>
</div>

<br>

***Safe Mode and Loss of Engineering Data***
On 2017-02-01 15:06 UTC (MJD 57785.62917) the spacecraft entered safe mode. The safe mode was likely due to a flight software reset, which occurred several times during the Kepler/K2 mission. The recovery from this safe mode was routine and the spacecraft resumed science data collection at 2017-02-06 20:47 UTC (MJD 57790.86597). The total time lost to this safe mode was 5.25 days.

In order to minimize the science data loss, the project decided not to downlink
stored engineering data during during the safe mode recovery. This decision resulted
in the loss of ~10 days of engineering data, starting 2017-01-25 08:16 UTC (MJD 57778.344) and
extending into the safe mode. No stored science data were lost. The engineering
data includes the thruster firing data, so there is no thruster firing
information from the spacecraft for this time period. In order to fill in the
thruster firing information in the archive data files, the short cadence
pointing history was used to detect likely thruster firings during the data gap. If the
thruster firing could be unambiguously identified within a SC interval, a thruster
firing was flagged in the QUALITY and SAP_QUALITY fields (bit 21). If the thruster
firing appeared to span SC intervals, both intervals would be flagged with a
possible thruster firing (bit 20). Users should be alert to possible missed
thruster firings in the interval from 2017-01-25 08:16 UTC (MJD 57778.344) to the start of the
safe mode at 2017-02-01 15:06 UTC (MJD 57785.62917).

<br>

<h2>Data Quality and Processing Notes</h2>

***Light Curve Quality***

As in other campaigns, the 6-hour spacecraft roll cycle continues
to dominate the systematic errors in C12 simple aperture photometry light curves. In spite of the sparse nature of the C12 field of view, the pipeline CDPP 12th magnitude noise benchmark is a bit higher than what was seen in star fields of comparable star density (53 ppm in C12 vs 42 ppm in C6 and 47 ppm in C8). The passage of Mars
most significantly affected CDPP on the channels with the
direct and ghost images; however, excluding these channels does not significantly lower the 12th magnitude CDPP benchmark value.  It is unknown exactly why the noise benchmark is higher.

The magnitude dependence of CDPP and its distribution over the focal
plane are shown below. Other CDPP benchmarks can be found in the
<a href="images/release-notes/c12/c12_bin1.00_sc1.00_CDPP_Summary_20031318.txt">
table giving 6.5-hr CDPP as a function of magnitude.</a>
<br>
<div class="thumbnail" style="width: 90%;">
<div class="caption">
<i>Figure C12-CDPP: 6.5-hr CDPP measurements for all targets as a function of Kepler magnitude. Dim targets have poorer overall photometric precision than bright targets, but can look better because the residual sawtooth falls below the noise floor. The saturated targets tend to have the lowest CDPP, but often show a residual sawtooth. </i>   
</div>
<a href="images/release-notes/c12/c12_logg_CDPP_vs_model_dr39.png">
<img src="images/release-notes/c12/c12_logg_CDPP_vs_model_dr39.png" class="img-responsive" alt="CDPP measured for all targets as a function of Kepler magnitude.">
</a>
</div>
<div class="thumbnail" style="width: 90%;">
<div class="caption">
<i>Figure C12-CDPP FocalPlane: 6.5-hr CDPP measured as a function of position on the focal plane, for 12th and 14th magnitude dwarf stars. The photometric precision is generally better near the center of the focal plane where the variations in roll angle produce less pixel motion. All cadences coincident with a definite thruster firing are gapped.</i>
<a href="images/release-notes/c12/c12_dwarf_CDPP_by_mod_out_dr39.png">
<img src="images/release-notes/c12/c12_dwarf_CDPP_by_mod_out_dr39.png" class="img-responsive" alt="CDPP per channel for 12th magnitude dwarfs">
</a>    
</div>
</div>

<br>

<hr>


# K2 Campaign 11

These release notes are for the C11 data currently available at MAST (Data Release 30) in the nominal K2 data locations, which have been processed with the final version of the K2 pipeline as part of the <a href="k2-uniform-global-reprocessing-underway.html">K2 global uniform reprocessing effort</a>. The original release notes corresponding to the previous version(s) of C11 data (Data Release 17) can be found in the <a href="archived-k2-data-release-notes.html#k2-campaign-11">archived data release notes page</a>.


<h2>At a glance</h2>

<div class="col-lg-5">

<p>
Campaign 11 was operationally separated into two segments as a result of an
error in the initial roll-angle used to minimize solar torque on the spacecraft.
The larger than expected roll motion seen at the start of the campaign meant
that the targets would be rolling out of their pixel apertures by the end of the
campaign. The excess roll motion was corrected twenty-three days into the campaign
by applying a -0.32º roll offset. The size of this correction meant
that new target aperture definitions had to be used for the second part of the campaign.
The two segments, colloquially called C11a and C11b, are identified in the
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

<b><i>C11a Targets With Data Available at MAST</i></b>
<ul>
<li>32,812 EPIC IDs in long cadence (LC).</li>
<li>67 EPIC IDs in short cadence (LC).</li>
<li>72 Custom targets (see below).</li>
</ul>

<b><i>C11b Targets With Data Available at MAST</i></b>
<ul>
<li>32,508 EPIC IDs in long cadence (LC).</li>
<li>66 EPIC IDs in short cadence (LC).</li>
<li>72 Custom targets (see below).</li>
<li>No new targets were added for C11b. Because of the change in pointing, 304 long cadence targets and 1 short cadence target fell off active silicon and thus were dropped in C11b.</li>
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

<b><i>Most Recent Processing Version</i></b>
<ul>
<li> <a href="k2-pipeline-release-notes.html#data-release-30">Data Release 30</a> </li>
</ul>

</div>

<div class="col-lg-7">

    <div class="thumbnail">
        <div class="caption">
        <i>Figure: Figure C11-FOV: Schematic of Kepler's C11 field-of-view with high profile objects.</i>
    </div>
    <a href="images/k2/k2-c11-field.png">
        <img src="images/k2/k2-c11-field.png" class="img-responsive" alt="C11 field-of-view with selected targets">
        </a>
    </div>

    <div class="thumbnail">
        <div class="caption">
        <i>Figure: Figure C11-FFI: A full frame image (FFI) taken during C11a, with a flux scaling designed to highlight features of interest.</i>
    </div>
    <a href="images/release-notes/c11/C11aR-FFI.png">
        <img src="images/release-notes/c11/C11aR-FFI.png" class="img-responsive" alt="The C11a FFI">
        </a>
    </div>

    <div class="thumbnail">
        <div class="caption">
            <i>Figure C11-Mag: Distribution of the Kepler magnitudes of observed LC targets in C11. All targets are chosen by Guest Observers. The bimodality is due to how the largest <a href="k2-approved-programs.html#campaign-11">Guest Observer programs</a> were selected.</i>
        </div>
        <a href="images/release-notes/c11/C11MagDist.png">
            <img src="images/release-notes/c11/C11MagDist.png" class="img-responsive" alt="Distribution of the Kepler magnitudes of observed LC targets in C11.">
        </a>
    </div>

<br>

  </div>

</div>

<br>


<h2>Features and Events</h2>

***Galactic Bulge***

The C11 field of view is the densest star field for which pipeline light curves have been created.
The average density of stars with magnitude 11.5 < Kp < 14.5 over the field of view is
6,959 stars/deg<sup>2</sup>. Detector channels covering the galactic bulge have densities as high
as 25,000 stars/deg<sup>2</sup>. For comparison the average density of stars in this magnitude range
for the Kepler field of view is 900 stars/deg<sup>2</sup>. As a result of the high star density, many
of the pipeline algorithms are operating outside of their design range. Users are cautioned
to treat the pipeline background, centroid, and aperture photometry results with care, especially
on channels covering the Galactic Bulge.

<div class="thumbnail" style="width: 75%;">
  <div class="caption">
  <i>Figure C11-StarDensity: The average density of stars with 11.5 < Kp < 14.5 for each channel. As shown by the legend, the density ranges from a few thousand to over 20,000 stars/deg<sup>2</sup>. The galactic plane passes through modules 2 and 6 for the detector layout). The numbers indicate the detector module and output number (see figures on <a href="the-kepler-space-telescope.html">the telescope overview page</a> for more images describing the detector layout).</i>
  </div>
  <a href="images/release-notes/c11/k2_c11_star_density.jpg">
    <img src="images/release-notes/c11/k2_c11_star_density.jpg" class="img-responsive" alt="C11 star
    density ranges from a few thousand to over 20000 stars/deg<sup>2</sup>.">
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


***Custom targets***

Many custom targets were selected, composed of:

* 64 Solar System moving objects tiled with multiple apertures, featuring Titan and Enceladus
* 9 bright stars covered with disk apertures to capture the PSF wings
* 22 late microlensing targets
* 5 galaxy targets

See the <a href="images/release-notes/c11/ktwoc111_caf.csv">C11a csv file</a> and <a href="images/release-notes/c11/ktwoc112_caf.csv">C11b csv file</a> to map the Solar system object custom aperture numbers to the target names.

<br>


***Attitude Offset and Segmenting of C11 Data***

The spacecraft attitude was adjusted by -0.32º in roll on 2016-10-21 to correct
the initial roll-offset error. Because this attitude offset was large enough to
require new target pixel apertures, the C11 data were processed through the
pipeline in two separate parts:

* C11a: the first 23 days of the campaign
* C11b: the remaining 48 days of the campaign

The C11a files are found in the archive under Campaign number 111. The C11b
files have Campaign number 112. A search for Campaign 11 will return both sets of files.
Users should take care when combining data from C11a and C11b. Because the
targets have changed pixels &mdash; and in some cases detectors &mdash; there is no guarantee that the C11a and C11b fluxes will match in absolute value, or even slope across the C11a&ndash;C11b boundary. The C11a and C11b data likely need to be treated as coming from two separate campaigns. The figures below give some examples of the behavior of SAP flux over C11.

In some cases, the updated C11b target apertures extended off the edge of the active
CCD and included rows of collateral smear, or columns of collateral black data. These
collateral data are evident in the TPFs and should not be used when doing photometry on
the target.

<div class="thumbnail" style="width: 100%;">
    <div class="caption">
        <i>Figure C11 SAP Flux: The C11a (red) and C11b (blue) SAP flux for four sample targets.
        Because of the change of target pixel apertures between C11a and C11b, the fluxes can
        differ in absolute value and in behavior with the K2 roll motion.</i>
    </div>
    <a href="images/release-notes/c11/c11_stiched_examples.png">
        <img src="images/release-notes/c11/c11_stiched_examples.png" class="img-responsive" alt="C11 SAP flux for EPICs 221115664, 221326895, 221391462, and 221597630.">
    </a>
</div>

<br>

***Pointing and Roll Performance***

The C11a and C11b pointing and roll behavior are within the limits of that seen in other K2 campaigns. The pipeline calculated maximum distance between the
derived and nominal positions for any target (the "maximum attitude residual", or MAR)
for C11 never exceeds 2.2 pixels &mdash; well under the 3-pixel limit accommodated by the aperture halos. See Figures C11a-MAR and C11b-MAR.

The C11a attitude error started at a relatively high value and large roll amplitude,
due in part to the initial roll offset error. The negative going roll offsets
along with the large negative roll rate at the start of C11a indicated that,
without correction, the roll would have been unacceptably large in the 6-hours
between thruster firing windows by the end of the campaign. The large roll would have
caused targets at the edge of the focal plane to roll out of their apertures.
The roll offset was corrected during the gap starting around 2016-10-16 seen in Figure C11-Pointing-History, resulting in a roll profile for C11b that is more typical of past campaigns. Similarly, the C11a maximum attitude residual was somewhat high &mdash; though well within the aperture limits &mdash; while the C11b starting maximum attitude residual was more typical of K2 behavior.

There was a smaller related change in roll behavior during C11a when the spacecraft
X-band communications were switched from low gain antenna 2(LGA-2) to LGA-1. The
antenna switch resulted in different thermal torque on the spacecraft and somewhat
mitigated the initial C11a roll pointing error. The improvement is most evident in the
roll rate at a solar elongation angle of -35º (see Figure C11-Roll-Rate), but can be
seen in the roll error at around 2016-10-02 (see Figure C11-Pointing-History).


<div class="thumbnail" style="width: 49%;display: inline-block;">
<div class="caption">
<i>Figure C11-Pointing-History: the pointing performance for C11 was consistent with that of previous campaigns. The C11a&ndash;C11b transition occurred at the gap around 2016-10-16.</i>
</div>
<a href="images/release-notes/c11/c11_roll_error.png">
<img src="images/release-notes/c11/c11_roll_error.png" class="img-responsive" alt="Roll amplitude for C11 matched that of previous campaigns."></a>
</a>
</div>

<div class="thumbnail" style="width: 49%;display: inline-block;">
<div class="caption">
<i>Figure C11-Roll-Rate: the C11 roll rate as a function of solar elevation angle
clearly shows the impact of the roll offset error (C3 is shown here for comparison). The large
negative roll rate during C11a was corrected with the roll offset change in C11b.</i>
<a href="images/release-notes/c11/c11_roll_rate.jpg">
<img src="images/release-notes/c11/c11_roll_rate.jpg" class="img-responsive" alt="Roll Drift rates for C11 indicate the improvement in performance with the corrected roll offset in C11b.">
</a>
</div>
</div>

<div class="thumbnail" style="width: 49%;display: inline-block;">
<div class="caption">
<i>Figure C11a-Roll-Error: the roll-error between the photometrically derived attitude (PAD) and the nominal pointing plotted against time for C11a.</i>
<a href="images/release-notes/c11/C11a-Roll.png">
<img src="images/release-notes/c11/C11a-Roll.png" class="img-responsive" alt="Pipeline measured roll error for C11a.">
</a>
</div>
</div>

<div class="thumbnail" style="width: 49%;display: inline-block;">
<div class="caption">
<i>Figure C11b-Roll-Error: the roll-error between the photometrically derived attitude (PAD) and the nominal pointing plotted against time for C11b. Note an atypically large pointing excursion at day 26.</i>
<a href="images/release-notes/c11/C11b-Roll.png">
<img src="images/release-notes/c11/C11b-Roll.png" class="img-responsive" alt="Pipeline measured roll error for C11b.">
</a>
</div>
</div>

<div class="thumbnail" style="width: 49%;display: inline-block;">
<div class="caption">
<i>Figure C11a-MAR: The maximum distance between the photometrically derived attitude (PAD) and the nominal position plotted against time for C11a.</i>
<a href="images/release-notes/c11/C11a-Mar.png">
<img src="images/release-notes/c11/C11a-Mar.png" class="img-responsive" alt="Maximum residual of the C11a attitude measured with PAD and PDQ.">
</a>
</div>
</div>

<div class="thumbnail" style="width: 49%;display: inline-block;">
<div class="caption">
<i>Figure C11b-MAR: The maximum distance between PAD and the nominal position plotted against time for C11b. Note the pointing the pointing improvement at the start of the sub-campaign.</i>
<a href="images/release-notes/c11/C11b-Mar.png">
<img src="images/release-notes/c11/C11b-Mar.png" class="img-responsive" alt="Maximum residual of the C11b attitude measured with PAD and PDQ.">
</a>
</div>
</div>

<br>

<h2>Data Quality and Processing Notes</h2>

***Light Curve Quality***

We consider the C11a and C11b pipeline-generated light curves separately for noise analysis and comparison with previous campaigns.
As in previous campaigns, the 6-hour spacecraft roll cycle continues to dominate the systematic
errors in C11 simple aperture photometry light curves.

The magnitude dependence of CDPP and its distribution over the focal plane
are shown below. Other CDPP benchmarks can be found in the
<a href="images/release-notes/c11/c11a_bin1.00_sc1.00_CDPP_Summary_19032701.txt">
table giving C11a 6.5-hr CDPP as a function of magnitude</a> and
<a href="images/release-notes/c11/c11b_bin1.00_sc1.00_CDPP_Summary_19032702.txt">
the C11b 6.5-hr CDPP table.</a>

The stellar properties for each target, available from the <a href="http://archive.stsci.edu/k2/epic/search.php">EPIC catalog</a>,
were used to distinguish dwarf and giant stars. The C11 CDPP values are in family with C7, the next most crowded K2 FOV for which pipeline light curves were generated.

<br>

<div class="thumbnail" style="width: 90%;">
<div class="caption">
<i>Figure C11a-CDPP: 6.5-hr CDPP measurements for C11a targets as a function of Kepler magnitude. Dim targets have poorer overall photometric precision than bright targets, but can look better because the residual sawtooth falls below the noise floor. The saturated targets tend to have the lowest CDPP, but often show a residual sawtooth.</i>   
</div>
<a href="images/release-notes/c11/c11Ra_logg_CDPP_vs_model.png">
<img src="images/release-notes/c11/c11Ra_logg_CDPP_vs_model.png" class="img-responsive" alt="CDPP measured for all C11a targets as a function of Kepler magnitude.">
</a>
</div>

<div class="thumbnail" style="width: 90%;">
<div class="caption">
<i>Figure C11b-CDPP: 6.5-hr CDPP measurements for C11b targets as a function of Kepler magnitude. Dim targets have poorer overall photometric precision than bright targets, but can look better because the residual sawtooth falls below the noise floor. The saturated targets tend to have the lowest CDPP, but often show a residual sawtooth.</i>   
</div>
<a href="images/release-notes/c11/c11Rb_logg_CDPP_vs_model.png">
<img src="images/release-notes/c11/c11Rb_logg_CDPP_vs_model.png" class="img-responsive" alt="CDPP measured for all C11b targets as a function of Kepler magnitude.">
</a>
</div>

<div class="thumbnail" style="width: 90%;">
<div class="caption">
<i>Figure C11a-CDPP Focal Plane: 6.5-hr CDPP for C11a dwarf targets across the focal plane. Panels show the 10th percentile (left) and median (right) CDPP metric for all dwarf targets in the 12th (top) and 14th (bottom) magnitude range. The photometric precision is generally better near the center of the focal plane where the variations in roll angle produce less pixel motion. All cadences coincident with a definite thruster firing are gapped.</i>
</div>
<a href="images/release-notes/c11/c11Ra_dwarf_CDPP_by_channel.png">
<img src="images/release-notes/c11/c11Ra_dwarf_CDPP_by_channel.png" class="img-responsive" alt="C11a CDPP per channel for all 12th magnitude stars">
</a>    
</div>

<div class="thumbnail" style="width: 90%;">
<div class="caption">
<i>Figure C11b-CDPP Focal Plane: 6.5-hr CDPP for C11b dwarf targets across the focal plane. Panels show the 10th percentile (left) and median (right) CDPP metric for all dwarf targets in the 12th (top) and 14th (bottom) magnitude range. The photometric precision is generally better near the center of the focal plane where the variations in roll angle produce less pixel motion. All cadences coincident with a definite thruster firing are gapped.</i>
</div>
<a href="images/release-notes/c11/c11Rb_dwarf_CDPP_by_channel.png">
<img src="images/release-notes/c11/c11Rb_dwarf_CDPP_by_channel.png" class="img-responsive" alt="C11b CDPP per channel for all 12th magnitude stars">
</a>    
</div>

<br>

***Short-Cadence Target With No PDC Flux***

The target EPIC 200147465 (36 Ophiuchi; a bright, nearby triple star system) failed short-cadence PDC processing due to it being a custom target and the only target on its channel. The short-cadence light curve file includes the (nominal and unaffected) SAP flux, but the PDC_SAP flux is all zeros. Note that the long-cadence data for this target is unaffected and is nominal.

<br>

***Targets With Incomplete FITS Header***

There are 13 custom targets in C11a and 3 in C11b (see list below) that are missing centroid information and values for the following FITS headers in thier target pixel and lightcurve files: RA_OBJ, DEC_OBJ, 1CRVL4, 2CRVL4, 1CRVL5, 2CRVL5, 1CRVL6, 2CRVL6, 1CRVL7, 2CRVL7, 1CRVL8, 2CRVL8, 1CRVL9, 2CRVL9, EXPOSURE, TELAPSE, LIVETIME, TSTART, TSTOP, CRVAL1, and CRVAL2. This situation typically for a very small fraction of custom targets, where the entire pixel stamp is erroneously selected as the aperture. As a result there are no background pixels available to compute the centroid information, and thus the values for the listed FITS headers. Users wanting to analyze this target are encouraged to create their own lightcurve using software such as the [lightkurve Python package](https://docs.lightkurve.org), [PyKE software tool suite](http://pyke.keplerscience.org), or [other packages](https://archive.stsci.edu/missions-and-data/kepler/related-software-1).

The list of the affected targets are:

C11a
<ul>
<li>200108002
<li>200109390
<li>200109391
<li>200111995
<li>200112045
<li>200112066
<li>200117957
<li>200121136
<li>200121176
<li>200121179
<li>200122458
<li>200124751
<li>200125354
</ul>
<br>
C11b
<ul>
<li>200134507
<li>200136321
<li>200129342
</ul>

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
<i>Channels with corrupt smear measurements due to saturating stars on the specified
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

During the last three days of C11b the detector experienced a large number of parity errors coming from the photometer's local detector electronics (LDE). These LDE parity errors can occur when a very bright object saturates and spills charge into the CCD serial readout register, causing an overflow at the input to the analog-to-digital converter. The LDE parity errors were likely caused by the image of Saturn on the focal plane. These errors do not affect the quality of data from pixels on the active focal plane, and the pipeline as run in this most recent processing does ***not*** discard data based on this flag.

The LDE parity error triggers a flag (bit 15, decimal=16384) in the QUALITY column of the target pixel files. Most of the cadences from long cadence number 136276 (2016-12-4 00:58 UTC) to LC 136426 (2016-12-7 02:32 UTC) have the parity error flag set.

<hr>

<br>


# K2 Campaign 10

These release notes are for the C10 data currently available at MAST (Data Release 37) in the nominal K2 data locations, which have been processed with the final version of the K2 pipeline as part of the <a href="k2-uniform-global-reprocessing-underway.html">K2 global uniform reprocessing effort</a>. The original release notes corresponding to the previous versions of C10 data (Data Release 15) can be found in the <a href="archived-k2-data-release-notes.html#k2-campaign-10">archived data release notes page</a>.

<h2>At a glance</h2>

<div class="col-lg-5">

<p>
Campaign 10 was operationally separated into two segments as a result of a 3.5-pixel
initial pointing error at the start of the campaign. The offset was corrected
six days into the campaign. The two segments are identified in the
archive products as c101 and c102, respectively.
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

<b><i>Targets With Data Available at MAST</i></b>
<ul>
<li>41,531 EPIC IDs in long cadence (LC).</li>
<li>138 EPIC IDs in short cadence (LC).</li>
<li>Custom targets include 16 Solar System moving objects tiled with multiple apertures, 8 bright stars covered with disk apertures to capture the PSF wings, and 27 large galaxies. See the <a href="images/release-notes/c10/ktwoc10_caf.csv">csv file that maps</a> the Solar system object custom aperture numbers to the target names.</li>
</ul>

<b><i>Full Frame Images (FFI)</i></b>
<p>
Both C10 FFIs were taken at the C10b pointing.
The first includes data from module 4,
the second does not.
</p>
<ul>
<li><a href="https://archive.stsci.edu/pub/k2/ffi/ktwo2016199030108-c102_ffi-cal.fits">ktwo2016199030108-c102_ffi-cal.fits</a></li>
<li><a href="https://archive.stsci.edu/pub/k2/ffi/ktwo2016240074042-c102_ffi-cal.fits">ktwo2016240074042-c102_ffi-cal.fits</a></li>
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

<b><i>Most Recent Processing Version</i></b>
<ul>
<li> <a href="k2-pipeline-release-notes.html#data-release-37">Data Release 37</a> </li>
</ul>



</div>

<div class="col-lg-7">

<div class="thumbnail">
  <div class="caption">
    <i>Figure: Figure C10-FOV: Schematic of Kepler's C10 field-of-view with high profile objects.</i>
  </div>
  <a href="images/k2/k2-c10-field.png">
    <img src="images/k2/k2-c10-field.png" class="img-responsive" alt="C10 field-of-view with selected targets">
  </a>
</div>

<div class="thumbnail">
  <div class="caption">
    <i>Figure: Figure C10-FFI: A full frame image (FFI) taken during C10 (before the failure of Mod 4), with a flux scaling designed to highlight features of interest.</i>
  </div>
  <a href="images/release-notes/c10/C10R-FFI.png">
    <img src="images/release-notes/c10/C10R-FFI.png" class="img-responsive" alt="A C10 FFI">
  </a>
</div>

    <div class="thumbnail">
        <div class="caption">
            <i>Figure C10-Mag: Distribution of the Kepler magnitudes of observed LC targets in C10. All targets are chosen by Guest Observers. The shape is due to how the largest <a href="k2-approved-programs.html#campaign-10">Guest Observer programs</a> were selected.</i>
        </div>
        <a href="images/release-notes/c10/c10LcMagDistribution.png">
            <img src="images/release-notes/c10/c10LcMagDistribution.png" class="img-responsive" alt="Distribution of the Kepler magnitudes of observed LC targets in C10.">
        </a>
    </div>

</div>

</div>

<!--
Figure C10-FOV: Schematic of Kepler's C10 field-of-view with observed targets shown with purple dots. Note that module 4, centered near RA = 193º, Dec = -2º, failed seven days into C10b, so targets on channels 9--12 have truncated data sets.
-->



<h2>Features and Events</h2>

***Galaxies***

With its high Galactic latitude, Campaign 10 observed 4,977 galaxies. Twenty-seven large galaxies were each covered using 1,500 pixel custom masks. The extragalactic targets include the well-known quasar 3C 273 (EPIC 229151988).

<br>

***Comet 67P: Churyumov-Gerasimenko***

Comet 67P was observed in C10b from September 7 through September 20 2016 as it crossed
channels 69 and 70. The comet was observed using 2200 custom aperture tiles.

<br>

***Segmenting of C10 Data***

The C10 data were processed through the pipeline in two separate sets:

<ul>
<li>The first six days of data, dubbed C10a, were collected with a pointing error of 3.5 pixels from the nominal field-of-view, so they were only processed through CAL to make Type 1 target pixel files and collateral data files.
<br>
<li>The remainder of the campaign, dubbed C10b, was processed through the entire pipeline, creating Type 2 target pixel files, light curves, and collateral data files.
</ul>

The C10a files are found in the archive under Campaign number 101, and the C10b
files have Campaign number 102. A search for Campaign 10 will return both sets of files.

<br>

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
roll behavior were typical of K2 campaigns. The cross-boresight pointing during C10b was well-behaved outside of the coarse point portion caused by the failure of
module 4 &mdash; since the photometer was off during the coarse point portion, no coarse-point science data were collected. The roll behavior during
C10a and C10b was also nominal. The pipeline calculated maximum distance between the
derived and nominal positions for any target (the "maximum attitude residual", or MAR)
for C10b was well under the 3-pixel limit accommodated by the aperture halos.


<div class="thumbnail" style="width: 49%; display: inline-block;">
  <div class="caption">
    <i>
    Figure C10b-Roll-Error: the roll-error between the photometrically derived attitude (PAD) and the nominal pointing plotted against time for C10b.
    </i>
  </div>
  <a href="images/release-notes/c10/c10_pad_pdq_attitude_roll.png">
    <img src="images/release-notes/c10/c10_pad_pdq_attitude_roll.png" class="img-responsive" alt="Pipeline measured roll error for C10b.">
  </a>
</div>

<div class="thumbnail" style="width: 49%; display: inline-block;">
  <div class="caption">
    <i>
    Figure C10b-MAR: the maximum distance between the photometrically derived attitude (PAD) and the nominal position plotted against time for C10b.
    </i>
  </div>
  <a href="images/release-notes/c10/c10_pad_pdq_attitude_mar.png">
    <img src="images/release-notes/c10/c10_pad_pdq_attitude_mar.png" class="img-responsive" alt="Maximum residual of the C10b attitude measured with PAD and PDQ.">
  </a>
</div>


<br>

<h2>Data Quality and Processing Notes</h2>

***Calibrated Target Pixel Files***

This data release consists of calibrated target pixel files (TPFs) and supporting
calibration files for C10a, as well as a full set of archive files (TPFs, calibration
files, and light curve files) for C10b.
The two separate sets of calibrated TPFs for C10a and C10b
have filenames that contain "c101" and "c102" respectively.

Because the full pipeline was not run, the C10a TPFs are Type-1 files.
The C10b TPFs are Type-2 and contain all the nominal calibration information.
See section 2.4 of the [K2 Handbook](https://archive.stsci.edu/files/live/sites/mast/files/home/missions-and-data/kepler/_documents/KSCI-19116-002.pdf) for details on the contents of the Type-1
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
errors in C10b simple aperture photometry light curves.

The magnitude dependence of CDPP and its distribution over the focal
plane are shown below. Other CDPP benchmarks can be found in the
<a href="images/release-notes/c10/c10_bin1.00_sc1.00_CDPP_Summary_19112610.txt">
table giving 6.5-hr CDPP as a function of magnitude.</a>

<br>
<div class="thumbnail" style="width: 90%;">
<div class="caption">
<i>Figure C10b-CDPP: 6.5-hr CDPP measurements for all targets as a function of Kepler magnitude. Dim targets have poorer overall photometric precision than bright targets, but can look better because the residual sawtooth falls below the noise floor. The saturated targets tend to have the lowest CDPP, but often show a residual sawtooth. </i>
</div>
<a href="images/release-notes/c10/cdpp_vs_mag_dr37.png">
<img src="images/release-notes/c10/cdpp_vs_mag_dr37.png" class="img-responsive" alt="CDPP measured for all targets as a function of Kepler magnitude.">
</a>
</div>

<div class="thumbnail" style="width: 90%;">
<div class="caption">
<i>Figure C10b-CDPP FocalPlane: 6.5-hr CDPP measured as a function of position on the focal plane, for 12th and 14th magnitude dwarf stars. The photometric precision is generally better near the center of the focal plane where the variations in roll angle produce less pixel motion. All cadences coincident with a definite thruster firing are gapped.</i>
</div>
<a href="images/release-notes/c10/c10_dwarf_CDPP_by_mod_out_dr37.png">
<img src="images/release-notes/c10/c10_dwarf_CDPP_by_mod_out_dr37.png" class="img-responsive" alt="CDPP per channel for 12th and 14th magnitude dwarfs">
</a>
</div>


<br>

***Targets With No Lightcurve Files***

The following three targets do not have lightcurve files available for data release 37. All three targets are faint M dwafs with significant proper motion, which appears to have resulted in corner cases where the pipeline selected an optimal aperture that was just outside the observed pixels.  As a result neither SAP_FLUX nor PDC_SAPFLUX were able to be computed for these targets, and thus no lightcurve files exist for them. Users are encouraged to produce their own lightcurves for these objects from the target pixel files.

<ul>
<li>201288233
<li>201482905
<li>228849156
</ul>

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
differential velocity aberration, it is likely that adjacent columns will be corrupted at some times during the campaign.

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

<b><i>C9b Pointing</i></b>
<ul>
<li>RA: 270.3543824 degrees</li>
<li>Dec: -21.7804700 degrees</li>
<li>Roll: 0.4673417 degrees</li>
</ul>

<b><i>C9a Targets With Data Available at MAST</i></b>
<ul>
<li>3,417 EPIC IDs in long cadence (LC)</li>
<li>12 EPIC IDs in short cadence (SC)</li>
<li>76 unique custom targets were selected in C9. Three million of the total 3.3 million C9 target pixels were used to construct microlensing super apertures on 5 channels around the Galactic bulge. See the <a href="images/release-notes/c9/ktwoc91_caf.csv">csv file that maps</a> the custom aperture number to the target name.</li>
</ul>

<b><i>C9b Targets With Data Available at MAST</i></b>
<ul>
<li>3,550 EPIC IDs in long cadence (LC)</li>
<li>13 EPIC IDs in short cadence (SC)</li>
<li>132 additional long-cadence  microlensing targets and 1 short-cadence target were added to the C9a target list for C9b. See the <a href="images/release-notes/c9/ktwoc92_caf.csv">csv file that maps</a> the custom aperture number to the target name.</li>
</ul>

<b><i>Full Frame Images (FFI)</i></b>
<ul>
<li><a href="https://archive.stsci.edu/pub/k2/ffi/ktwo2016119231109-c91_ffi-cal.fits">ktwo2016119231109-c91_ffi-cal.fits</a></li>
<li><a href="https://archive.stsci.edu/pub/k2/ffi/ktwo2016153221424-c92_ffi-cal.fits">ktwo2016153221424-c92_ffi-cal.fits</a></li>
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
<i>Figure C9-Mag: Distribution of the Kepler magnitudes of observed LC targets. All targets are chosen by guest observers. The distribution is due to the <a href="k2-approved-programs.html#campaign-9">GO  programs</a> that were selected. Note that the small number of targets is due to the fact that the majority of pixels were in the microlensing super apertures.</i>
</div>
<a href="images/release-notes/c9/c9LcMagDistribution.png">
<img src="images/release-notes/c9/c9LcMagDistribution.png" class="img-responsive" alt="Distribution of the Kepler magnitudes of observed LC targets.">
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

These release notes are for the C8 data currently available at MAST (Data Release 38) in the nominal K2 data locations, which have been processed with the final version of the K2 pipeline as part of the <a href="k2-uniform-global-reprocessing-underway.html">K2 global uniform reprocessing effort</a>. The original release notes corresponding to the previous versions of C8 data (Data Release 11) can be found in the <a href="archived-k2-data-release-notes.html#k2-campaign-8">archived data release notes page</a>.


<h2>At a glance</h2>

<div class="col-lg-5">

<b><i>Pointing</i></b>
<ul>
<li>RA: 16.3379975 degrees</li>
<li>Dec: 5.2623459 degrees</li>
<li>Roll: -157.3538761 degrees</li>
</ul>

<b><i>Targets With Data Available at MAST</i></b>
<ul>
<li>29,939 EPIC IDs in long cadence (LC).</li>
<li>63 EPIC IDs in short cadence (LC).</li>
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
<li> <a href="k2-pipeline-release-notes.html#data-release-11">Data Release 38</a> </li>
</ul>


    <br>

    <div class="thumbnail">
        <div class="caption">
            <i>Figure C8-Mag: Distribution of the Kepler magnitudes of observed LC targets in C8. All targets are chosen by Guest Observers. The shape is due to how the largest <a href="k2-approved-programs.html#campaign-8">Guest Observer programs</a> were selected.</i>
        </div>
        <a href="images/release-notes/c8/c8LcMagDistribution.png">
            <img src="images/release-notes/c8/c8LcMagDistribution.png" class="img-responsive" alt="Distribution of the Kepler magnitudes of observed LC targets in C8.">
        </a>
    </div>

</div>



<div class="col-lg-7">

<div class="thumbnail">
  <div class="caption">
    <i>Figure: Figure C8-FOV: Schematic of Kepler's C8 field-of-view with high profile objects.</i>
  </div>
  <a href="images/k2/k2-c08-field.png">
    <img src="images/k2/k2-c08-field.png" class="img-responsive" alt="C8 field-of-view with selected targets">
  </a>
</div>

<div class="thumbnail">
  <div class="caption">
    <i>Figure: Figure C8-FFI: A full frame image (FFI) taken during C8, with a flux scaling designed to highlight features of interest.</i>
  </div>
  <a href="images/release-notes/c8/C8R-FFI.png">
    <img src="images/release-notes/c8/C8R-FFI.png" class="img-responsive" alt="A C8 FFI">
  </a>
</div>

</div>

</div>

<h2>Features and Events</h2>

***Uranus***

Uranus and four of its moons were observed with custom masks during Campaign 8. The path of Uranus was tiled with 245 single column target definitions at long cadence and with nine 9 x 307 trapezoidal masks at short cadence. The moons Caliban, Prospero, Setebos, and Sycorax were observed with separate custom masks.  Uranus is one of the brightest moving objects observed by K2.

<br>

***Galaxies***

With its high Galactic latitude, Campaign 8 was ideal for observing galaxies. There were 2750 galaxies targeted, including IC 1613 (Caldwell 51), an irregular dwarf galaxy in the Local Group.  IC 1613 was tiled with 48 20 x 20 pixel masks for a total of 19,200 pixels.

<br>

***Pointing and Roll Performance***

Based on the C7 degraded roll performance, the Mission Operations Center switched back to low-gain antenna LGA1 for spacecraft communication during most of C8. The switch resulted in a return to nominal K2 roll performance and drift rates. The campaign was started using LGA2, as was used in C7, and then starting around 23 Jan 2016 23:50 UTC (MJD 57410.99) operations were switched to LGA1. The antenna swap can be seen in the roll drift attitude error.

On 2016-02-01 16:40 UTC (MJD	57419.69) the spacecraft dropped out of fine point control. Observations continued in coarse point, with much degraded pointing performance, until 2016-02-02 22:27 UTC (MJD 57420.94) when the spacecraft reacquired fine point during a resat period. This resulted in 29 hours and 48 minutes of coarse point data collection. These cadences (121284&mdash;121344) are flagged as both "spacecraft is not in fine point" (QUALITY flag bit #16, decimal=32768) and "spacecraft is in coarse point" flag (QUALITY flag bit #3, decimal=4).  The loss of fine point occurred following a thruster firing fine tweak that resulted in the spacecraft rolling in the wrong direction. The next tweak was unable to correct the attitude before the loss of fine point fault was triggered, but fine pointing control was restored automatically at the next momentum wheel resaturation. There were several other instances of anomalous thruster firing tweaks in C8, none of which resulted in loss of fine point.

<div class="thumbnail" style="width: 49%; display: inline-block;">
  <div class="caption">
    <i>
    Figure C8-Roll-Error: the roll-error between the photometrically derived attitude (PAD) and the nominal pointing plotted against time for C8.
    </i>
  </div>
  <a href="images/release-notes/c8/c8_pad_pdq_attitude_roll.png">
    <img src="images/release-notes/c8/c8_pad_pdq_attitude_roll.png" class="img-responsive" alt="Pipeline measured roll error for C8.">
  </a>
</div>

<div class="thumbnail" style="width: 49%; display: inline-block;">
  <div class="caption">
    <i>
    Figure C8-MAR: the maximum distance between the photometrically derived attitude (PAD) and the nominal position plotted against time for C8.
    </i>
  </div>
  <a href="images/release-notes/c8/c8_pad_pdq_attitude_mar.png">
    <img src="images/release-notes/c8/c8_pad_pdq_attitude_mar.png" class="img-responsive" alt="Maximum residual of the C8 attitude measured with PAD and PDQ.">
  </a>
</div>


<div class="thumbnail" style="width: 90%">
 <div class="caption">
 <i>Figure C8-Pointing History: With the change back to using low-gain antenna LGA1 for communications, the roll drift (or x-axis attitude error) returned to nominal K2 behavior after the anomalous C7 roll drifts. Several larger than normal thruster firing tweaks affected C8 pointing. One of these, on 2016-02-01, resulted in a loss of fine pointing control for 30 hours (ADFFINEPTLK Fault).</i>   
 </div>
<a href="images/release-notes/c8/c8_pointing_history.png">
<img src="images/release-notes/c8/c8_pointing_history.png" class="img-responsive" alt="Roll Drift for C8 returns to nominal K2 behavior"></a>
</div>


<br>

<h2>Data Quality and Processing Notes</h2>

***Light Curve Quality***

As in other campaigns, the 6-hour spacecraft roll cycle dominates the systematic errors in C8 simple aperture photometry light curves.
The pipeline CDPP 12th magnitude noise benchmark for C8 (DR38) is comparable to that seen in other campaigns with similar star density.

The magnitude dependence of CDPP and its distribution over the focal
plane are shown below. Other CDPP benchmarks can be found in the
<a href="images/release-notes/c8/c8_bin1.00_sc1.00_CDPP_Summary_19121101.txt">
table giving 6.5-hr CDPP as a function of magnitude.</a>

<br>

<div class="thumbnail" style="width: 90%;">
<div class="caption">
<i>Figure C8-CDPP: 6.5-hr CDPP measurements for all targets as a function of Kepler magnitude. Dim targets have poorer overall photometric precision than bright targets, but can look better because the residual sawtooth falls below the noise floor. The saturated targets tend to have the lowest CDPP, but often show a residual sawtooth. </i>
</div>
<a href="images/release-notes/c8/cdpp_vs_mag_dr38.png">
<img src="images/release-notes/c8/cdpp_vs_mag_dr38.png" class="img-responsive" alt="CDPP measured for all targets as a function of Kepler magnitude.">
</a>
</div>

<div class="thumbnail" style="width: 90%;">
<div class="caption">
<i>Figure C8-CDPP FocalPlane: 6.5-hr CDPP measured as a function of position on the focal plane, for 12th and 14th magnitude dwarf stars. The photometric precision is generally better near the center of the focal plane where the variations in roll angle produce less pixel motion. All cadences coincident with a definite thruster firing are gapped.</i>
</div>
<a href="images/release-notes/c8/c8_dwarf_CDPP_by_mod_out_dr38.png">
<img src="images/release-notes/c8/c8_dwarf_CDPP_by_mod_out_dr38.png" class="img-responsive" alt="CDPP per channel for 12th and 14th magnitude dwarfs">
</a>
</div>

<br>

***Short-Cadence Targets With no PDC Flux***

The following nine targets failed short-cadence PDC processing due to them being custom targets and the only targets on their channel. The short-cadence light curve files include the (nominal and unaffected) SAP flux, but the PDC_SAP flux is all zeros. Note that the long-cadence data for these targets are unaffected and are nominal.

<ul>
<li>200068647
<li>200068648
<li>200068649
<li>200068650
<li>200068651
<li>200068652
<li>200068653
<li>200068654
<li>200068655
</ul>

<br>

***Poor Smear Correction on Channel 42***

In the original C8 processing (data release 11), it was noted that there were episodic smear correction errors on channel 42 (mod.out 13.2) &mdash; the channel containing the Uranus supermask. Nearly every long cadence in the supermask appeared to contain between 2 and 20 columns which were brightened by 10&ndash;20 counts. The brightening of a column lasted only for a single cadence, with no obvious patterns as to which columns are affected in a given cadence. Two example cadences which are particularly affected are 119980 and 119982 (see Figures C8-Ch42-DR11-Cad119980 and C8-Ch42-DR11-Cad119982) below.

Preliminary investigation indicated that the streaking was caused by false cosmic ray detections in the smear collateral data. Because similar streaking was not seen in the supermask for IC 1613, located on channel 58, it was believed that the poor cosmic ray detector performance was due to the bright signal from Uranus moving across columns and altering the cosmic ray detector's dynamic threshold. When false cosmic rays are removed from the smear signal, the pixel data in that column is under-corrected, resulting in a brightening of that column for a given cadence.

For the final processing of C8 (data relase 38), as for all reprocessed campaigns, the detection threshold of the cosmic ray detector was increased (see the <a href="k2-uniform-global-reprocessing-underway.html">news post on global reprocessing</a>).  While this did reduce the number of false cosmic ray detections for nearly all campaigns and channels, it did not appear to help for channel 42 in C8.  In fact, the situation appears worse for channel 42 in C8 for DR38 than DR11.  The maximum value of the smear offsets appear to range up to 60 counts in DR38, compared to 20 counts in DR11, and with perhaps a higher frequency of occurrence (see Figures C8-Ch42-DR11-Smear and C8-Ch42-DR38-Smear below.)  While the exact cause of the worsening of the false cosmic ray flagging is not yet known, possibilities include the use of Dynablack as well as processing the entire campaign through the CAL module of the pipeline at once for DR38, whereas Dynablack was not used for DR11 and CAL was run in three separate time chunks &mdash; regardless, the root cause remains Uranus' bright, moving signal.

Just as was advised for DR11, for DR38, since the streaks are not in the raw data, users may wish to do their own smear correction on this channel, or at least use the data release 11 version of the files [available here](https://archive.stsci.edu/missions/k2/target_pixel_files/old_release_bundles/c8/).

<div class="thumbnail" style="width: 45%;display: inline-block;">
<div class="caption">
<i>Figure C8-Ch42-DR11-Cad119980: Uranus supermask smear anomaly, Cadence 119980, Data Release 11. </i>   
</div>
<a href="images/release-notes/c8/c8-channel42-cadence119980.png">
<img src="images/release-notes/c8/c8-channel42-cadence119980.png" class="img-responsive" alt="Uranus supermask cadence 119980 smear streaks.">
</a>
</div>

<div class="thumbnail" style="width: 45%;display: inline-block;">
<div class="caption">
<i>Figure C8-Ch42-DR11-Cad119982: Uranus supermask smear anomaly, Cadence 119982 Data Release 11.  </i>
</div>
<a href="images/release-notes/c8/c8-channel42-cadence119982.png">
<img src="images/release-notes/c8/c8-channel42-cadence119982.png" class="img-responsive" alt="Uranus supermask cadence 119982 smear streaks.">
</a>
</div>

<div class="thumbnail" style="width: 90%;">
<div class="caption">
<i>Figure C8-Ch42-DR11-Smear: The masked minus virtual smear measured for Channel 42 for the first 30 days of C8, for Data Release 11.  The measurement is shown as a function of both column and cadence on the left, and then just cadence for all columns combined on the right.</i>
</div>
<a href="images/release-notes/c8/c8_ch42_dr11_smear.png">
<img src="images/release-notes/c8/c8_ch42_dr11_smear.png" class="img-responsive" alt="Masked minus virtual smear measurement for channel 42, C8, DR 11.">
</a>
</div>

<div class="thumbnail" style="width: 90%;">
<div class="caption">
<i>Figure C8-Ch42-DR38-Smear: The masked minus virtual smear measured for Channel 42 for the first 30 days of C8, for Data Release 38.  The measurement is shown as a function of both column and cadence on the left, and then just cadence for all columns combined on the right.</i>
</div>
<a href="images/release-notes/c8/c8_ch42_dr38_smear.png">
<img src="images/release-notes/c8/c8_ch42_dr38_smear.png" class="img-responsive" alt="Masked minus virtual smear measurement for channel 42, C8, DR 38.">
</a>
</div>


<br>

<hr>



# K2 Campaign 7

These release notes are for the C7 data currently available at MAST (Data Release 36) in the nominal K2 data locations, which have been processed with the final version of the K2 pipeline as part of the <a href="k2-uniform-global-reprocessing-underway.html">K2 global uniform reprocessing effort</a>. The original release notes corresponding to the previous versions of C7 data (Data Release 9) can be found in the <a href="archived-k2-data-release-notes.html#k2-campaign-7">archived data release notes page</a>.


<h2>At a glance</h2>

<div class="col-lg-5">

    <b><i>Pointing</i></b>
    <ul>
        <li>RA: 287.82850661 degrees</li>
        <li>Dec: -23.36001815 degrees</li>
        <li>Roll: -172.78037532 degrees</li>
    </ul>

    <b><i>Targets With Data Available at MAST</i></b>
    <ul>
        <li>15,085 EPIC IDs in long cadence (LC).</li>
        <li>72 EPIC IDs in short cadence (LC).</li>
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
    <li> <a href="k2-pipeline-release-notes.html#data-release-36">Data Release 36</a> </li>
    </ul>

    <br>

    <div class="thumbnail">
        <div class="caption">
            <i>Figure C7-Mag: Distribution of the Kepler magnitudes of observed LC targets in C7. All targets are chosen by Guest Observers. The shape is due to how the largest <a href="k2-approved-programs.html#campaign-7">Guest Observer programs</a> were selected.</i>
        </div>
        <a href="images/release-notes/c7/c7LcMagDistribution.png">
            <img src="images/release-notes/c7/c7LcMagDistribution.png" class="img-responsive" alt="Distribution of the Kepler magnitudes of observed LC targets in C7.">
        </a>
    </div>

</div>

<div class="col-lg-7">

<div class="thumbnail">
  <div class="caption">
    <i>Figure: Figure C7-FOV: Schematic of Kepler's C7 field-of-view with high profile objects.</i>
  </div>
  <a href="images/k2/k2-c07-field.png">
    <img src="images/k2/k2-c07-field.png" class="img-responsive" alt="C7 field-of-view with selected targets">
  </a>
</div>

<div class="thumbnail">
  <div class="caption">
    <i>Figure: Figure C7-FFI: A full frame image (FFI) taken during C7, with a flux scaling designed to highlight features of interest.</i>
  </div>
  <a href="images/release-notes/c7/C7R-FFI.png">
    <img src="images/release-notes/c7/C7R-FFI.png" class="img-responsive" alt="A C7 FFI">
  </a>
</div>

</div>

</div>

<h2>Features and Events</h2>

***Pluto***

Pluto, a dwarf planet in the Kuiper belt, and one of the largest trans-Neptunian objects, was observed during Campaign 7. The path of Pluto was tiled with 1 x n pixel target definitions, where n ranges from 1 to 217. The range of custom aperture numbers for Pluto is 200062954 &ndash; 200062827. The animated gif below shows Pluto as observed by K2.
<div class"thumbnail" style="width:65%;">
    <div class="caption"><i>Figure C7-Pluto: An animated gif of a portion of the custom apertures that contain Pluto during C7. </i>
    </div>
    <a href="images/release-notes/c7/k2c7-pluto.gif"><img src="images/release-notes/c7/k2c7-pluto.gif" class="img-responsive" alt="Movie of Pluto moving through the K2 field of view."></a>
</div>

<br>

***Ruprecht 47***

Ruprecht 47 is an open cluster observed with K2 during Campaign 7.  It was observed using a super-aperture, tiled with 60 51 x 51 masks, totaling 156,060 pixels. The custom aperture numbers range from 200062524 &ndash; 200062583.

<br>

***Pointing and Roll Performance***

For the first ~30 hours of the campaign, the telescope was in coarse point &mdash; one of the guide stars was brighter than expected, preventing fine point lock, and an update to the fine guidance sensor was issued to accommodate the higher signal count. The span of coarse point is long cadences 115414 &ndash; 115474 (corresponding short cadences 3450880 &ndash; 3452680. See Figure C7-MAR below.

The C7 roll behavior is worse than typically seen in other K2 campaigns. For C7, an alternate low-gain antenna was active during science data collection. The previously used LGA1 was replaced by LGA2 (see [Figure 2 of the Kepler Instrument Handbook](http://archive.stsci.edu/kepler/manuals/KSCI-19033-002.pdf)), as the latter was slightly better oriented with respect to earth. (This partially compensated for the increasing distance to the spacecraft in its Earth-trailing orbit, then at 0.8 AU.)  Since the two antennas are mounted on opposite sides of the spacecraft, this antenna swap produced a change in radiation pressure that placed an additional (unbalanced) torque about the boresight on the spacecraft.  The resulting increase in roll drift is illustrated in Figure C7-RollDrift, which compares the drift rates for C4, C6, and C7.

<div class="thumbnail" style="width: 50%;display: inline-block;">
  <div class="caption">
    <i>Figure C7-Roll Drift: The roll of the Kepler spacecraft around the boresight during campaigns 4, 6 and 7. The C7 drift rate is significantly out of family, being negative throughout the entire campaign.</i>
  </div>
  <a href="images/release-notes/c7/c7-rolldrift.png">
    <img src="images/release-notes/c7/c7-rolldrift.png" class="img-responsive" alt="Roll Drift for C7 is larger than it was for C4 and C6.">
  </a>
</div>

As a result of this increased roll drift (see Figure C7-Roll-Error), the maximum excursion of any pixel from its nominal position is significantly larger for C7 than for other campaigns. The pipeline-calculated maximum distance between the derived and nominal positions for any target (the "maximum attitude residual", or MAR) for C7 is as large as 3.4 pixels, as shown in Figure C7-MAR &mdash; most campaigns have a MAR of ~2. As described below, since target apertures were designed with a maximum 3-pixel halo, this results in lost light for some targets.

<div class="thumbnail" style="width: 49%; display: inline-block;">
  <div class="caption">
    <i>
    Figure C7-Roll-Error: the roll-error between the photometrically derived attitude (PAD) and the nominal pointing plotted against time for C7.
    </i>
  </div>
  <a href="images/release-notes/c7/c7_pad_pdq_attitude_roll.png">
    <img src="images/release-notes/c7/c7_pad_pdq_attitude_roll.png" class="img-responsive" alt="Pipeline measured roll error for C7.">
  </a>
</div>

<div class="thumbnail" style="width: 49%; display: inline-block;">
  <div class="caption">
    <i>
    Figure C7-MAR: the maximum distance between the photometrically derived attitude (PAD) and the nominal position plotted against time for C7.
    </i>
  </div>
  <a href="images/release-notes/c7/c7_pad_pdq_attitude_mar.png">
    <img src="images/release-notes/c7/c7_pad_pdq_attitude_mar.png" class="img-responsive" alt="Maximum residual of the C7 attitude measured with PAD and PDQ.">
  </a>
</div>

<br>



<h2>Data Quality and Processing Notes</h2>

***Light Curve Quality***

For the first ~30 hours of the campaign when the spacecraft was in coarse point, most stars are expected to be significantly outside of their optimal aperture.  While the raw light curve (PA / SAP_FLUX) is processed and provided in the lightcurve FITS files for these cadences, the data was excluded from the PDC detrending module in order to improve performance across the campaign, and thus there is no PDC_SAPFLUX values in the provided lightcurve FITS files.  Users wishing to attempt to utilize these ~30 days of coarse point should also note that the black level in the target-pixel files will be off by a constant value compared to the rest of the campaign &mdash; subtraction or addition of a flux constant will likely be required if combining with data from the rest of the campaign.

As in other campaigns, the 6-hour spacecraft roll cycle dominates the systematic errors in C7 simple aperture photometry light curves.  The unusually large roll motion in C7, combined with an extremely crowded field, had a particularly strong impact on photometry compared to other campaigns, especially for targets near the edge of the focal plane &mdash; such targets have lower photometric precision.  Also, background estimates based on background polynomials were strongly polluted by stars rolling in and out of the background apertures. This is especially true for channels near the edge of the focal plane (more roll) and near the Galactic plane (more stars). As a result, the background is strongly over-corrected, with short-time background variations strongly correlated with roll motion. These background variations have been subtracted from all pixels on the channel.

Despite the extra roll motion, the motion polynomials generally did a reasonable job tracking the large roll motion, and this enabled the computation of photometric apertures that significantly reduced the impact of roll motion in many cases. In other cases though, the roll motion was too large for the recovery of high-quality photometry using the standard pipeline processing.  As part of the <a href="k2-uniform-global-reprocessing-underway.html">K2 global uniform reprocessing effort</a> the spacecraft telemetry was used to identify pointing outliers and remove associated cadences from the PDC detrending module.  This resulted in significantly better common basis vectors and PDC detrended lightcurves (PDC_SAPFLUX) than the previous processing.  

While the <a href="archived-k2-data-release-notes.html#k2-campaign-7">previous processing</a> resulted in a CDPP dwarf 12th magnitude noise benchmark that was increased by ~30% compared to the median value for all campaigns, as a result of reprocessing the benchmark is only ~15% higher, i.e., now within the normal range of campaign-to-campaign variation.  The magnitude dependence of CDPP and its distribution over the focal plane are shown below. Other CDPP benchmarks can be found in the
<a href="images/release-notes/c7/c7_bin1.00_sc1.00_CDPP_Summary_19100123.txt">
table giving 6.5-hr CDPP as a function of magnitude.</a>

<br>
<div class="thumbnail" style="width: 90%;">
<div class="caption">
<i>Figure C7-CDPP: 6.5-hr CDPP measurements for all targets as a function of Kepler magnitude. Dim targets have poorer overall photometric precision than bright targets, but can look better because the residual sawtooth falls below the noise floor. The saturated targets tend to have the lowest CDPP, but often show a residual sawtooth. </i>
</div>
<a href="images/release-notes/c7/cdpp_vs_mag_dr36.png">
<img src="images/release-notes/c7/cdpp_vs_mag_dr36.png" class="img-responsive" alt="CDPP measured for all targets as a function of Kepler magnitude.">
</a>
</div>

<div class="thumbnail" style="width: 90%;">
<div class="caption">
<i>Figure C7-CDPP FocalPlane: 6.5-hr CDPP measured as a function of position on the focal plane, for 12th and 14th magnitude dwarf stars. The photometric precision is generally better near the center of the focal plane where the variations in roll angle produce less pixel motion. All cadences coincident with a definite thruster firing are gapped.</i>
</div>
<a href="images/release-notes/c7/c7_dwarf_CDPP_by_mod_out_dr36.png">
<img src="images/release-notes/c7/c7_dwarf_CDPP_by_mod_out_dr36.png" class="img-responsive" alt="CDPP per channel for 12th and 14th magnitude dwarfs">
</a>
</div>

In addition to the issues with unusually large roll and crowding, stars selected for observation were unusually distributed in C7, with some channels having many targets and other channels having relatively few targets (see Figure C7-FOV-Targets). The result was that some channels had few target stars in the range of magnitudes used to characterize field motion via motion polynomials. A particularly dramatic example is channel 24.4, where all the targets used to create the motion polynomial for this channel are in one corner, resulting in a very inaccurate motion polynomial.  Because motion polynomials are used in the creation of the photometric aperture, photometry for some targets on Mod.Out 24.4, and to a lesser extent 12.3, may be particularly poor.

<div class="thumbnail"  style="width: 90%;">
  <div class="caption">
    <i>Figure C7-FOV-Targets: Schematic of Kepler's C7 field-of-view with observed targets shown with purple dots.</i>
  </div>
  <a href="images/release-notes/c7/C7_selected.png">
    <img src="images/release-notes/c7/C7_selected.png" class="img-responsive" alt="C7 field-of-view with selected targets plotted in purple.">
  </a>
</div>

<br>

***Poor Smear Correction***

There are 4 channels in C7 for which the saturation spill due to very bright stars spans all CCD rows for one or more columns, corrupting both the masked and virtual smear measurements for these columns. In these cases, in order to allow the pipeline calibration to complete, we flag the masked smear as bad and process the data with only the virtual smear. As a result, the smear correction will be poor for the channel/column combinations listed below, and will be suspect for the same columns on other outputs on the same module as the indicated channel due to video crosstalk.

<table>
<tr><th>Channel&emsp;</th><th>Columns</th></tr>
<tr><td>45</td><td>685:691</td></tr>
<tr><td>53</td><td>42:51</td></tr>
<tr><td>65</td><td>819:828</td></tr>
<tr><td>67</td><td>234:242</td></tr>
</table>


<br>

<hr>


# K2 Campaign 6

These release notes are for the C6 data currently available at MAST (Data Release 35) in the nominal K2 data locations, which have been processed with the final version of the K2 pipeline as part of the <a href="k2-uniform-global-reprocessing-underway.html">K2 global uniform reprocessing effort</a>. The original release notes corresponding to the previous versions of C6 data (Data Release 8) can be found in the <a href="archived-k2-data-release-notes.html#k2-campaign-6">archived data release notes page</a>.


<h2>At a glance</h2>

<div class="row">
<div class="col-lg-5">

    <b><i>Pointing</i></b>
    <ul>
        <li>RA: 204.8650344 degrees</li>
        <li>Dec: -11.2953585 degrees</li>
        <li>Roll: 159.6356000 degrees</li>
    </ul>

    <b><i>Targets With Data Available at MAST</i></b>
    <ul>
        <li>47,550 EPIC IDs in long cadence (LC).</li>
        <li>84 EPIC IDs in short cadence (LC).</li>
        <li>Several custom targets (see below)</li>
    </ul>

    <b><i>Full Frame Images (FFI)</i></b>
    <ul>
        <li><a href="https://archive.stsci.edu/pub/k2/ffi/ktwo2015207050529-c06_ffi-cal.fits">ktwo2015207050529-c06_ffi-cal.fits</a></li>
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
    <li> <a href="k2-pipeline-release-notes.html#data-release-35">Data Release 35</a> </li>
    </ul>

    <br>

    <div class="thumbnail">
        <div class="caption">
            <i>Figure C6-Mag: Distribution of the Kepler magnitudes of observed LC targets in C6. All targets are chosen by Guest Observers. The shape is due to how the largest <a href="k2-approved-programs.html#campaign-6">Guest Observer programs</a> were selected.</i>
        </div>
        <a href="images/release-notes/c6/c6LcMagDistribution.png">
            <img src="images/release-notes/c6/c6LcMagDistribution.png" class="img-responsive" alt="Distribution of the Kepler magnitudes of observed LC targets in C6.">
        </a>
    </div>

</div>

<div class="col-lg-7">

<div class="thumbnail">
  <div class="caption">
    <i>Figure: Figure C6-FOV: Schematic of Kepler's C6 field-of-view with high profile objects.</i>
  </div>
  <a href="images/k2/k2-c06-field.png">
    <img src="images/k2/k2-c06-field.png" class="img-responsive" alt="C6 field-of-view with selected targets">
  </a>
</div>

<div class="thumbnail">
  <div class="caption">
    <i>Figure: Figure C6-FFI: A full frame image (FFI) taken during C6, with a flux scaling designed to highlight features of interest.</i>
  </div>
  <a href="images/release-notes/c6/C6R-FFI.png">
    <img src="images/release-notes/c6/C6R-FFI.png" class="img-responsive" alt="A C6 FFI">
  </a>
</div>

</div>

</div>



<h2>Features and Events</h2>

***Spica***

The star Spica (α Virginis, [EPIC 212573842](http://archive.stsci.edu/k2/epic/search.php?id=212573842&action=Search)), the 15th brightest star in the sky, is on silcon during Campaign 6. As can be seen on the FFI above, Spica is on mod.out 18.3 (channel 63) and its Schmidt-corrector reflection lies on mod.out 8.3. (See [this image](/images/kepler_focal_plane_layout_channels_color.png) for the module/channel layout.) The star bleeds into both smear regions, preventing proper smear correction on columns 805&ndash;816 on channel 63.  Also, because of cross-talk, the Spica signal appears on all channels of module 18 at the same row and column position, but to a lesser degree.  For more information on cross-talk, see the [Instrument Handbook](https://archive.stsci.edu/kepler/manuals/KSCI-19033-002.pdf).

<br>

***Observed Trojans***

During Campaign 6, K2 observed 65 Trojan asteroids. Each was tiled with 1 x n pixel target definitions, where n ranges from 1 to 217. The tiled regions for three examples are shown in the figure below.  The range of custom aperture numbers given to the Trojans is 200041889 &ndash; 200061149. A mapping of the minor planet designation numbers to the custom aperture numbers can be <a href="images/release-notes/c6/trojanCustomApertureC6.csv">downloaded here.</a>

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

The star on Module 25 used for guiding during C6 was highly variable, appearing to be a contact binary with a period of 14.5 hours and a depth of approximately 40 percent. A signal with the same period and phase is seen in a large number of long cadence, PDC light curves with an amplitude as large as 0.1 per cent. Please see the folded light curve and normalized BLS spectra below, and [read this document](images/release-notes/c6/var_fgs_kso-391_drnC6_addendum_16040722.pdf), written for the previous processing release, for a detailed explanation. In short, the variable guide star caused periodic pointing errors of &#177;10 mas in RA and Dec, resulting in photometric variations in all targets and PDC cotrending basis vectors.  Note that we expect the current data release (35) to be affected in the same way as the previous data release (8).

To help users understand and mitigate the effects of this guide star, we make available the <a href="images/release-notes/c6/C6fgsFlux-mod25.csv">module 25 guide star fluxes</a> in a csv file.  [This data can also be found as part of the K2 Fine guidance sensor delivery](https://keplerscience.arc.nasa.gov/final-release-of-k2-high-cadence-guide-star-photometry.html).  The guide star was selected from the USNO catalog and has an RA of 200.6867 degrees, Dec of -6.0353 degrees, and R magnitude of 9.51.

<div class="thumbnail" style="width: 49%;display: inline-block;">
  <div class="caption">
    <i>
    Figure C6-GuideStar: The folded light curve of one long cadence target (top) and the module 25 guide star (bottom). Both are folded at a period of 0.6046 days, the approximate period of the variability of the guide star.
    </i>
  </div>
  <a href="images/release-notes/c6/fgsCompareC6to212668671.png">
    <img src="images/release-notes/c6/fgsCompareC6to212668671.png" class="img-responsive" alt="The folded light curve of the guide star and an example C6 LC target.">
  </a>
</div>

<div class="thumbnail" style="width: 49%;display: inline-block;">
  <div class="caption">
    <i>
    Figure C6-BLS: The normalized BLS (box-least squares) spectra for 400 long cadence targets on channel 42, sorted by magnitude (with the brightest at the top).  The 14.5-hour period and a series of peaks every ~7 hours show-up as yellow vertical lines on this figure. The majority of targets on this channel have a significant signal at this period.
    </i>
  </div>
  <a href="images/release-notes/c6/ch42blsSpectrumC6.png">
    <img src="images/release-notes/c6/ch42blsSpectrumC6.png" class="img-responsive" alt="The Bls spectrum for 400 targets on channel 42.">
  </a>
</div>

<br>

***Pointing and Roll Performance***

The C6 pointing and roll behavior are well within the limits of that seen in other K2 campaigns. The pipeline-calculated maximum distance between the derived and nominal positions for any target (the "maximum attitude residual", or MAR) for C6 is less than 2.2 pixels for nearly the entire campaign, well under the 3-pixel limit accommodated by the C6 aperture halos.

Users should note a significant ~6.5-hour pointing excursion that occurred just after mid-campaign, which encompasses long cadences 113663 &ndash; 113676 (short cadences 3398351 &ndash; 3398711).  While these cadences are gapped in the delivered PDC lightcurve data, they are intentionally not gapped in the PA lightcurve data.

<div class="thumbnail" style="width: 49%; display: inline-block;">
  <div class="caption">
    <i>
    Figure C6-Roll-Error: the roll-error between the photometrically derived attitude (PAD) and the nominal pointing plotted against time for C6.
    </i>
  </div>
  <a href="images/release-notes/c6/c6_pad_pdq_attitude_roll.png">
    <img src="images/release-notes/c6/c6_pad_pdq_attitude_roll.png" class="img-responsive" alt="Pipeline measured roll error for C6.">
  </a>
</div>

<div class="thumbnail" style="width: 49%; display: inline-block;">
  <div class="caption">
    <i>
    Figure C6-MAR: the maximum distance between the photometrically derived attitude (PAD) and the nominal position plotted against time for C6.
    </i>
  </div>
  <a href="images/release-notes/c6/c6_pad_pdq_attitude_mar.png">
    <img src="images/release-notes/c6/c6_pad_pdq_attitude_mar.png" class="img-responsive" alt="Maximum residual of the C6 attitude measured with PAD and PDQ.">
  </a>
</div>

<br>

<h2>Data Quality and Processing Notes</h2>

***Light Curve Quality***

As in other campaigns, the 6-hour spacecraft roll cycle dominates the systematic errors in C6 simple aperture photometry light curves.
The pipeline CDPP 12th magnitude noise benchmark for C6 (DR35) is comparable to that seen in other campaigns with similar star density.

The magnitude dependence of CDPP and its distribution over the focal
plane are shown below. Other CDPP benchmarks can be found in the
<a href="images/release-notes/c6/c6_bin1.00_sc1.00_CDPP_Summary_19091816.txt">
table giving 6.5-hr CDPP as a function of magnitude.</a>

<br>
<div class="thumbnail" style="width: 90%;">
<div class="caption">
<i>Figure C6-CDPP: 6.5-hr CDPP measurements for all targets as a function of Kepler magnitude. Dim targets have poorer overall photometric precision than bright targets, but can look better because the residual sawtooth falls below the noise floor. The saturated targets tend to have the lowest CDPP, but often show a residual sawtooth. </i>
</div>
<a href="images/release-notes/c6/cdpp_vs_mag_dr35.png">
<img src="images/release-notes/c6/cdpp_vs_mag_dr35.png" class="img-responsive" alt="CDPP measured for all targets as a function of Kepler magnitude.">
</a>
</div>

<div class="thumbnail" style="width: 90%;">
<div class="caption">
<i>Figure C6-CDPP FocalPlane: 6.5-hr CDPP measured as a function of position on the focal plane, for 12th and 14th magnitude dwarf stars. The photometric precision is generally better near the center of the focal plane where the variations in roll angle produce less pixel motion. All cadences coincident with a definite thruster firing are gapped.</i>
</div>
<a href="images/release-notes/c6/c6_dwarf_CDPP_by_mod_out_dr35.png">
<img src="images/release-notes/c6/c6_dwarf_CDPP_by_mod_out_dr35.png" class="img-responsive" alt="CDPP per channel for 12th and 14th magnitude dwarfs">
</a>
</div>


***Missing PDC Data for Short-Cadence Lightcurves***

Due to a processing bug, in this data release there is no PDC (PDCSAP_FLUX) data for all short-cadence lightcurves starting with short cadence 3345210 until the end of the campaign, i.e., the last ~86% of the PDCSAP_FLUX values are NaN.  This bug only affected this campaign and only the short-cadence PDC data &mdash; the long-cadence data is unaffected, and the PA (SAP_FLUX) lightcurve data for short-cadence is unaffected.

Users of the short-cadence lightcurve data are encouraged to do their own detrending, starting with the PA (SAP_FLUX) photometric data.  For example, see [https://docs.lightkurve.org/api/correctors.html#module-lightkurve.correctors](https://docs.lightkurve.org/api/correctors.html#module-lightkurve.correctors).

<br>

<hr>


# K2 Campaign 5

These release notes are for the C5 data currently available at MAST (Data Release 31) in the nominal K2 data locations, which have been processed with the final version of the K2 pipeline as part of the <a href="k2-uniform-global-reprocessing-underway.html">K2 global uniform reprocessing effort</a>. The original release notes corresponding to the previous version(s) of C5 data (Data Releases 5 and 7) can be found in the <a href="archived-k2-data-release-notes.html#k2-campaign-5">archived data release notes page</a>.


<h2>At a glance</h2>

<div class="col-lg-5">

    <b><i>Pointing</i></b>
    <ul>
        <li>RA: 130.1576478 degrees</li>
        <li>Dec: 16.8296140 degrees</li>
        <li>Roll: 166.0591297 degrees</li>
    </ul>

    <b><i>Targets With Data Available at MAST</i></b>
    <ul>
        <li>25,774 EPIC IDs in long cadence (LC).</li>
        <li>204 EPIC IDs in short cadence (LC).</li>
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
    <li> <a href="k2-pipeline-release-notes.html#data-release-31">Data Release 31</a> </li>
    </ul>

<br>

    <div class="thumbnail">
        <div class="caption">
            <i>Figure C5-Mag: Distribution of the Kepler magnitudes of observed LC targets in C5. All targets are chosen by Guest Observers. The bimodality is due to how the largest <a href="k2-approved-programs.html#campaign-5">Guest Observer programs</a> were selected.</i>
        </div>
        <a href="images/release-notes/c5/C5LcMagDistribution.png">
            <img src="images/release-notes/c5/C5LcMagDistribution.png" class="img-responsive" alt="Distribution of the Kepler magnitudes of observed LC targets in C5.">
        </a>
    </div>

</div>

<div class="col-lg-7">

    <div class="thumbnail">
        <div class="caption">
        <i>Figure: Figure C5-FOV: Schematic of Kepler's C5 field-of-view with high profile objects.</i>
    </div>
    <a href="images/k2/k2-c05-field.png">
        <img src="images/k2/k2-c05-field.png" class="img-responsive" alt="C5 field-of-view with selected targets">
        </a>
    </div>


    <div class="thumbnail">
        <div class="caption">
        <i>Figure: Figure C5-FFI: A full frame image (FFI) taken during C5, with a flux scaling designed to highlight features of interest.</i>
    </div>
    <a href="images/release-notes/c5/C5R-FFI.png">
        <img src="images/release-notes/c5/C5R-FFI.png" class="img-responsive" alt="A C5 FFI">
        </a>
    </div>

</div>

<br>

<h2>Features and Events</h2>

***M67***

The open cluster M67 was observed by collecting a 400x400 region of sky near the core of the cluster in modules 6.1 and 6.2. See Figures M67-Tile and M67-FFI below. These data are grouped into 72 custom apertures, each with a 50x50 pixel mask or smaller. Their data are listed by custom aperture number at the MAST in the range 200008644&ndash;200008715.

<div class="thumbnail" style="width: 100%;">
    <div class="caption">
        <i>Figure M67-Tile: The tiling of the M67 open cluster is shown in green on mod.outs 6.1 and 6.2 of C5.</i>
    </div>
    <a href="images/release-notes/c5/M67Tiling.png">
        <img src="images/release-notes/c5/M67Tiling.png" class="img-responsive" alt="The tiling of the M67 open cluster is shown in green on mod.outs 6.1 and 6.2 of C5.">
    </a>
</div>

<div class="thumbnail" style="width: 100%;">
    <div class="caption">
        <i>Figure M67-FFI: The FFI image of M67 during C5, oriented to match Figure M67-Tile above and scaled to highlight features of interest.</i>
    </div>
    <a href="images/release-notes/c5/C5R-M67.png">
        <img src="images/release-notes/c5/C5R-M67.png" class="img-responsive" alt="The FFI of the two channels that M67 spans during C5.">
    </a>
</div>



<br>

***Trans-Neptunian Object***

The Trans-Neptunian Object TNO (126154) 2001 YH140 was observed in Campaign 5 by creating 565 1xn pixel target definitions (where n ranges from 4 to 21) that cover the path of the TNO. The custom aperture numbers range from 200008716 to 200009280.

<br>

***Noted Data Anomalies***

Approximately 55.5 days after the start of C5, we note a small (~4000 electrons per cadence) increase in the median dark level that lasts approximately a day. The event is likely caused by a Coronal Mass Ejection, and its size is small compared to other normal variations seen in the dark level. This change in dark level is part of the normal calibration process that occurs in the CAL module.

One Argabrightening event was seen in the observed background level approximately 38 days into the campaign and affects a majority of the channels. This event is flagged on bit 13 in the QUALITY column of the light curve and target pixel files for those targets on the affected channels.

<br>

<h2>Data Quality and Processing Notes</h2>

***Light Curve Quality***

As in other campaigns, the 6-hour spacecraft roll cycle dominates the systematic errors in C5 simple aperture photometry light curves.
The pipeline CDPP 12th magnitude noise benchmark for C5 (DR31) is comparable to that seen in other campaigns with similar star density.

The magnitude dependence of CDPP and its distribution over the focal
plane are shown below. Other CDPP benchmarks can be found in the
<a href="images/release-notes/c5/c5_bin1.00_sc1.00_CDPP_Summary_19021916.txt">
table giving 6.5-hr CDPP as a function of magnitude.</a>

<br>
<div class="thumbnail" style="width: 90%;">
<div class="caption">
<i>Figure C5-CDPP: 6.5-hr CDPP measurements for all targets as a function of Kepler magnitude. Dim targets have poorer overall photometric precision than bright targets, but can look better because the residual sawtooth falls below the noise floor. The saturated targets tend to have the lowest CDPP, but often show a residual sawtooth. </i>
</div>
<a href="images/release-notes/c5/cdpp_vs_mag_dr31.png">
<img src="images/release-notes/c5/cdpp_vs_mag_dr31.png" class="img-responsive" alt="CDPP measured for all targets as a function of Kepler magnitude.">
</a>
</div>

<br>

***Incorrect pixel-level calibration of some short-cadence TPFs***

Due to a processing error in <a href="k2-pipeline-release-notes.html#data-release-31">Data Release 31</a>, there are 74 C5 short-cadence targets that had incorrect calibration of their short-cadence pixel-level data. (Long cadence data is unaffected.) The list of affected C5 targets is below. Although it is estimated that only ~25% of them are affected at a non-negligible level, users are strongly encouraged to examine their target, if it is on the list below, to check the severity level and evaluate potential science impact. For a more detailed description of this issue, along with per-target diagnostics and a link to short-cadence TPFs from a previous processing that was not affected by this error, [please read this news post](incorrect-pixel-level-calibration-of-short-cadence-tpfs-for-some-c2r-c3r-and-c5r-targets.html).

211383343&emsp;&emsp;211401610&emsp;&emsp;211403555&emsp;&emsp;211407836&emsp;&emsp;211408116&emsp;&emsp;211408138&emsp;&emsp;211408522<br>
211408990&emsp;&emsp;211409011&emsp;&emsp;211409345&emsp;&emsp;211409348&emsp;&emsp;211409376&emsp;&emsp;211409644&emsp;&emsp;211410664<br>
211410931&emsp;&emsp;211412077&emsp;&emsp;211412252&emsp;&emsp;211414203&emsp;&emsp;211416577&emsp;&emsp;211417812&emsp;&emsp;211427749<br>
211429653&emsp;&emsp;211480655&emsp;&emsp;211529191&emsp;&emsp;211565467&emsp;&emsp;211569404&emsp;&emsp;211596649&emsp;&emsp;211623711<br>
211630249&emsp;&emsp;211642294&emsp;&emsp;211686003&emsp;&emsp;211696659&emsp;&emsp;211708181&emsp;&emsp;211730342&emsp;&emsp;211765471<br>
211779126&emsp;&emsp;211808853&emsp;&emsp;211846489&emsp;&emsp;211888384&emsp;&emsp;211892034&emsp;&emsp;211902739&emsp;&emsp;211909987<br>
211912407&emsp;&emsp;211916015&emsp;&emsp;211918335&emsp;&emsp;211918500&emsp;&emsp;211920612&emsp;&emsp;211927867&emsp;&emsp;211929178<br>
211931736&emsp;&emsp;211934173&emsp;&emsp;211936827&emsp;&emsp;211948678&emsp;&emsp;211950227&emsp;&emsp;211950703&emsp;&emsp;211951863<br>
211952381&emsp;&emsp;211954226&emsp;&emsp;211954550&emsp;&emsp;211957988&emsp;&emsp;211972627&emsp;&emsp;211975006&emsp;&emsp;211979334<br>
211980170&emsp;&emsp;211980688&emsp;&emsp;211988287&emsp;&emsp;211992776&emsp;&emsp;211995547&emsp;&emsp;212001099&emsp;&emsp;212100422<br>
212104541&emsp;&emsp;212160442&emsp;&emsp;212173112&emsp;&emsp;228682517

<br>


<!--

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
-->



<hr>



# K2 Campaign 4

These release notes are for the C4 data currently available at MAST (Data Release 33) in the nominal K2 data locations, which have been processed with the final version of the K2 pipeline as part of the <a href="k2-uniform-global-reprocessing-underway.html">K2 global uniform reprocessing effort</a>. The original release notes corresponding to the previous versions of C4 data (Data Releases 6 and 10) can be found in the <a href="archived-k2-data-release-notes.html#k2-campaign-4">archived data release notes page</a>.

<h2>At a glance</h2>

<div class="row">
<div class="col-lg-5">

    <b><i>Pointing</i></b>
    <ul>
        <li>RA: 59.0759116 degrees</li>
        <li>Dec: 18.6605794 degrees</li>
        <li>Roll: -167.6992793 degrees</li>
    </ul>

    <b><i>Targets With Data Available at MAST</i></b>
    <ul>
        <li>15,847 EPIC IDs in long cadence (LC).</li>
        <li>122 EPIC IDs in short cadence (LC).</li>
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
    <li> <a href="k2-pipeline-release-notes.html#data-release-33">Data Release 33</a> </li>
    </ul>

    <br>

    <div class="thumbnail">
        <div class="caption">
            <i>Figure C4-Mag: Distribution of the Kepler magnitudes of observed LC targets in C4. All targets are chosen by Guest Observers. The shape is due to how the largest <a href="k2-approved-programs.html#campaign-4">Guest Observer programs</a> were selected.</i>
        </div>
        <a href="images/release-notes/c4/C4_lcDistribution.png">
            <img src="images/release-notes/c4/C4_lcDistribution.png" class="img-responsive" alt="Distribution of the Kepler magnitudes of observed LC targets in C4.">
        </a>
    </div>

</div>

<div class="col-lg-7">

<div class="thumbnail">
  <div class="caption">
    <i>Figure: Figure C4-FOV: Schematic of Kepler's C4 field-of-view with high profile objects.</i>
  </div>
  <a href="images/k2/k2-c04-field.png">
    <img src="images/k2/k2-c04-field.png" class="img-responsive" alt="C4 field-of-view with selected targets">
  </a>
</div>

<div class="thumbnail">
  <div class="caption">
    <i>Figure: Figure C4-FFI: A full frame image (FFI) taken during C4, with a flux scaling designed to highlight features of interest.</i>
  </div>
  <a href="images/release-notes/c4/C4R-FFI.png">
    <img src="images/release-notes/c4/C4R-FFI.png" class="img-responsive" alt="A C4 FFI">
  </a>
</div>

</div>

</div>


<h2>Features and Events</h2>

***Pleiades and Hyades***

The Pleidaes and Hyades are notable features in Campaign 4, and include several bright stars that significantly saturate the detector.

One Director's Discretionary Target program (GO4901, PI:White) was approved in Campaign 4 which observes the nine 3&ndash;5 mag B-stars and red giants in the Pleiades and Hyades open clusters. The targets were observed using circular pixel masks (20 pixels in radius) that cover the wings of the PSF but not the entire saturation bleed.

The two stars in the Hyades are γ Tau and δ1 Tau. The seven stars in the Pleiades are: Alcyone (η Tau), Atlas (27 Tau), Electra (17 Tau), Maia (20 Tau), Merope (23 Tau), Taygeta (19 Tau) and Pleione (28 Tau). These stars are all listed in the EPIC, however their data are listed by custom aperture number at the MAST in the range 200007765&ndash;200007773.

The Figures C4-Pleiades and C4-Pleiades-Inv below show an FFI of module 15, which covers the Pleiades cluster, in two different flux scalings.

<div class="thumbnail" style="width: 65%;display: inline-block;">
    <div class="caption">
        <i>Figure C4-Pleiades: The Pleiades open cluster as seen on module 15 of the K2 C4 FFI.</i>
    </div>
    <a href="images/release-notes/c4/c4-pleiades-k2-1579.png">
        <img src="images/release-notes/c4/c4-pleiades-k2-1579.png" class="img-responsive" alt="The Pleiades open cluster as seen on module 15 of the K2 C4 FFI.">
    </a>
</div>

<div class="thumbnail" style="width: 34%;display: inline-block;">
    <div class="caption">
        <i>Figure C4-Pleiades-Inv: A flux scaling of the C4 module 15 FFI that matches Figure C4-FFI.</i>
    </div>
    <a href="images/release-notes/c4/c4-pleiades-ffi.png">
        <img src="images/release-notes/c4/c4-pleiades-ffi.png" class="img-responsive" alt="A flux scaling of the C4 module 15 FFI that matches Figure C4-FFI.">
    </a>
</div>

<br>


***Trans-Neptunian Object***

The Trans-Neptunian Object 2002 KY14 was observed in Campaign 4 by creating 1340 masks that cover the path of the TNO. The custom aperture numbers range from 200006425&ndash;200007764. These observations were taken as part of Guest Observer program GO4110 (PI:Schwamb).

<br>

***Pointing and Roll Performance***

The C4 pointing and roll behavior are well within the limits of that seen
in other K2 campaigns. The pipeline-calculated maximum distance between the
derived and nominal positions for any target (the "maximum attitude residual", or MAR)
for C4 is less than 2 pixels, well under the 4-pixel limit accommodated by the C4 aperture halos. Users should note that, while within limits,
the roll error does increase towards the end of the campaign and may result in increased photometric noise.

<div class="thumbnail" style="width: 49%;display: inline-block;">
<div class="caption">
<i>Figure C4-Roll-Error: the roll-error between the photometrically derived attitude (PAD) and the nominal pointing plotted against time for C4.</i>
<a href="images/release-notes/c4/c4_pad_pdq_attitude_roll.png">
<img src="images/release-notes/c4/c4_pad_pdq_attitude_roll.png" class="img-responsive" alt="Pipeline measured roll error for C4.">
</a>
</div>
</div>

<div class="thumbnail" style="width: 49%;display: inline-block;">
<div class="caption">
<i>Figure C4-MAR: the maximum distance between the photometrically derived attitude (PAD) and the nominal position plotted against time for C4.</i>
<a href="images/release-notes/c4/c4_pad_pdq_attitude_mar.png">
<img src="images/release-notes/c4/c4_pad_pdq_attitude_mar.png" class="img-responsive" alt="Maximum residual of the C4 attitude measured with PAD and PDQ.">
</a>
</div>
</div>

<br>


<h2>Data Quality and Processing Notes</h2>

***Non-Optimal Background Correction near the Pleiades***

Background removal for channels near the Pleiades has larger than normal residuals. These large residuals occur on mod.outs 10.3 and 15.1 through 15.4 due to the background on these channels being dominated by dust clouds near the Pleiades. The rich spatial structure of the Pleiades' dust clouds is poorly captured by the low order (≤ 4) polynomial model used to fit the background flux, with the best fit for these channels being given by a constant. This fit is done for every cadence, and the result is higher than normal background residuals, with residuals as large as 7 times the standard deviation of the background pixel values. (Normal residuals are typically less than the background standard deviation.)

We recommend caution when using light curves or the background model on these channels. Note that the FLUX column of the target pixel files contains calibrated pixels with the background subtracted. The amount of background that was subtracted per pixel can be found in the FLUX_BKG column and restored, if desired.

Local background estimates per star may produce higher-quality results. The change in the constant background level on these channels over time is in family with the median background change on other channels.

<br>


***Large Number of Saturated Stars***

Due to the Hyades and Pleiades clusters, there is a large number of bright stars that saturate the detector in Campaign 4. Users are cautioned to ensure that their target(s) are not affected by these bright, bleeding stars prior to analysis. For example, Figure C4-Chan15 highlights the number and extent of bleed trails on channel 52. Figure C4-Sat-Example shows an example of a typical target that is severely affected by the bleed from a bright star on the same column &mdash; examining a target's TPF image in this manner will reveal if it is affected directly by a bright stars' bleed.

<div class="thumbnail" style="width: 41%;display: inline-block;">
    <div class="caption">
        <i>Figure C4-Chan15: A scaled image of channel 52 (module.out = 15.4) showing the extent of charge bleeding due to saturated stars.</i>
    </div>
    <a href="images/release-notes/c4/c4r_ch52-orig.png">
        <img src="images/release-notes/c4/c4r_ch52-orig.png" class="img-responsive" alt="A scaled image of channel 52 (module.out = 15.4) showing the extent of charge bleeding due to saturated stars.">
    </a>
</div>

<div class="thumbnail" style="width: 58%;display: inline-block;">
    <div class="caption">
        <i>Figure C4-Sat-Example: A target pixel file image of a target severely affected by charge bleed from a bright star on the same column.</i>
    </div>
    <a href="images/release-notes/c4/ktwo211111489-c04_lpd-targ.fits.png">
        <img src="images/release-notes/c4/ktwo211111489-c04_lpd-targ.fits.png" class="img-responsive" alt="A target pixel file of a target clobbered by charge bleed from a bright star on the same column.">
    </a>
</div>

<br>


***Poor Smear Correction on Channel 25, Column 777***

The very bright (Kp=5.775), nearby (55.2 ly) solar-like star 39 Tauri was observed in Campaign 4. It it so bright that it saturates the smear calibration columns, and thus smear correction for column 777, and possibly neighboring columns, is not optimal. Caution is encouraged when analyzing other targets on this column as a result of the saturation and poor calibration, especially those at lower row numbers.

39 Tauri was only observed with a typical 4-halo aperture (instead of a dedicated disk as is more typical for bright stars). Thus, any analysis of 39 Tauri itself will be more challenging compared to analysis of other bright stars with dedicated disks.

<br>


***Several Stars Show Higher Than Expected Flux***

There is a group of target stars whose measured flux is more than twice that expected from their EPIC Kepler magnitudes. The figure below shows that these stars fall into spatial groups that are aligned with RA and Dec, rather than focal plane coordinates, strongly indicating that the cause of this anomaly is catalog error. The source of this error is presently unknown and is not correlated with Kepflag values. The optimal apertures used to generate light curves for these targets may be smaller than optimal, reducing their photometric precision.

<div class="thumbnail" style="width: 68%;">
    <div class="caption">
        <i>Figure C4-HighFlux-Stars: All C4 target stars plotted in celestial coordinates, colored by their Kepler magnitude inferred from their observed flux minus their Kepler magnitude from the EPIC catalog. There are two square-like regions and a line of blue markers, indicating stars whose inferred Kepler magnitude is about a magnitude smaller than their catalog magnitude, indicating that these stars are about a magnitude brighter than expected.</i>
    </div>
    <a href="images/release-notes/c4/C4radecKepMag-dr33.png">
        <img src="images/release-notes/c4/C4radecKepMag-dr33.png" class="img-responsive" alt="All C4 target stars plotted in celestial coordinates, colored by their Kepler magnitude inferred from their observed flux minus their Kepler magnitude from the EPIC catalog.">
    </a>
</div>

<br>


***Stars Show Lower Than Expected Flux***

The comparison of the measured flux to the flux based on their Kepler magnitudes in the EPIC catalog shows that ~3,752 stars (23.8% of all stellar targets) are too bright by about a magnitude. The EPIC catalog field Kepflag gives the provenance of the Kepler magnitude estimate by listing the catalog magnitudes used to estimate the Kepler magnitude. Stars with Kepflag = “JHK” or “J” have Kepler magnitudes that are generally overestimated. These stars appear at all magnitudes, but predominantly have EPIC Kepler magnitudes dimmer than 14. The optimal apertures used to generate light curves for these “JHK” or “J” targets may be larger than optimal, reducing their photometric precision.

<div class="thumbnail" style="width: 100%;">
    <div class="caption">
        <i>Figure-LowFlux-Stars: Histograms of the relative flux for C4 stellar targets. Left: the relative flux distribution of stellar targets with EPIC Kepflag values of “gri” or “BV”, showing that their measured flux is consistent with the expected flux. Right: The relative flux distribution of stellar targets with EPIC Kepflag values of “JHK” or “J”, showing that the observed flux is less than half the expected flux.</i>
    </div>
    <a href="images/release-notes/c4/lowfluxJband.png">
        <img src="images/release-notes/c4/lowfluxJband.png" class="img-responsive" alt="histograms of the relative flux for C4 stellar targets">
    </a>
</div>

<br>


***Stellar Targets with Negative Lightcurve Values***

Seventy-four stellar targets show negative flux values in their SAP_FLUX light curves, which is somewhat more than normally seen. Most of these are very dim, near background level targets at the edge of the focal plane where K2 roll has the largest impact, so it is not surprising that the roll causes negative flux values after background removal. The bright targets with negative flux values either have isolated negative flux outliers or are on the Pleiades channels, where there are large background residuals due to the constant background model on these channels, see above.

<br>


***Light Curve Quality***

As in other campaigns, the 6-hour spacecraft roll cycle dominates the systematic errors in C4 simple aperture photometry light curves.
The pipeline CDPP 12th magnitude noise benchmark for C4 (DR33) is comparable to that seen in other campaigns with similar star density.

The magnitude dependence of CDPP and its distribution over the focal
plane are shown below. Other CDPP benchmarks can be found in the
<a href="images/release-notes/c4/c4_bin1.00_sc1.00_CDPP_Summary_19071014.txt">
table giving 6.5-hr CDPP as a function of magnitude.</a>

<br>
<div class="thumbnail" style="width: 90%;">
<div class="caption">
<i>Figure C4-CDPP: 6.5-hr CDPP measurements for all targets as a function of Kepler magnitude. Dim targets have poorer overall photometric precision than bright targets, but can look better because the residual sawtooth falls below the noise floor. The saturated targets tend to have the lowest CDPP, but often show a residual sawtooth. </i>
</div>
<a href="images/release-notes/c4/cdpp_vs_mag_dr33.png">
<img src="images/release-notes/c4/cdpp_vs_mag_dr33.png" class="img-responsive" alt="CDPP measured for all targets as a function of Kepler magnitude.">
</a>
</div>

<div class="thumbnail" style="width: 90%;">
<div class="caption">
<i>Figure C4-CDPP FocalPlane: 6.5-hr CDPP measured as a function of position on the focal plane, for 12th and 14th magnitude dwarf stars. The photometric precision is generally better near the center of the focal plane where the variations in roll angle produce less pixel motion. All cadences coincident with a definite thruster firing are gapped.</i>
</div>
<a href="images/release-notes/c4/c4_dwarf_CDPP_by_mod_out_dr33.png">
<img src="images/release-notes/c4/c4_dwarf_CDPP_by_mod_out_dr33.png" class="img-responsive" alt="CDPP per channel for 12th and 14th magnitude dwarfs">
</a>
</div>

<br>

<hr>



# K2 Campaign 3

These release notes are for the C3 data currently available at MAST (Data Release 26) in the nominal K2 data locations, which have been processed with the final version of the K2 pipeline as part of the <a href="k2-uniform-global-reprocessing-underway.html">K2 global uniform reprocessing effort</a>. The original release notes corresponding to the previous version(s) of C3 data (Data Releases 5 and 10) can be found in the <a href="archived-k2-data-release-notes.html#k2-campaign-3">archived data release notes page</a>.

<h2>At a glance</h2>

<div class="col-lg-5">

    <b><i>Pointing</i></b>
    <ul>
        <li>RA: 336.66534641439 degrees</li>
        <li>Dec: -11.096663792177 degrees</li>
        <li>Roll: -158.494818065985 degrees</li>
    </ul>

    <b><i>Targets With Data Available at MAST</i></b>
    <ul>
        <li>16,833 EPIC IDs in long cadence (LC).</li>
        <li>216 EPIC IDs in short cadence (LC).</li>
        <li>Several custom targets (see below)</li>
    </ul>

    <b><i>Full Frame Images (FFI)</i></b>
    <ul>
        <li><a href="https://archive.stsci.edu/missions/k2/ffi/ktwo2014331202630-c03_ffi-cal.fits">ktwo2014331202630-c03_ffi-cal.fits</a></li>
        <li><a href="https://archive.stsci.edu/missions/k2/ffi/ktwo2015008010551-c03_ffi-cal.fits">ktwo2015008010551-c03_ffi-cal.fits</a></li>
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
    <li> <a href="k2-pipeline-release-notes.html#data-release-26">Data Release 26</a> </li>
    </ul>

</div>

<div class="col-lg-7">

    <div class="thumbnail">
        <div class="caption">
            <i>Figure: Figure C3-FOV: Schematic of Kepler's C3 field-of-view with high profile objects.</i>
        </div>
        <a href="images/k2/k2-c03-field.png">
            <img src="images/k2/k2-c03-field.png" class="img-responsive" alt="C3 field-of-view with selected targets">
        </a>
    </div>

    <div class="thumbnail">
        <div class="caption">
              <i>Figure C3-Mag: Distribution of the Kepler magnitudes of observed LC targets in C3. The bimodality is due to the large Guest Observer programs selected for C3.</i>
        </div>
        <a href="images/release-notes/c3/magnitudeDist.png">
            <img src="images/release-notes/c3/magnitudeDist.png" class="img-responsive" alt="Distribution of the Kepler magnitudes of observed LC targets in C3.">
        </a>
    </div>

</div>

<h2>Features and Events</h2>

***Neptune***

Neptune moved across the field of view during C3 and K2 observed it in both long and short cadence. Short cadence data were obtained approximately 20 days on each side of the stationary point of Neptune. The movie below shows Neptune and its moons, Triton and Nereid, as they move across the detector over approximately 50 days. Note that Neptune saturates the detector, which results in the observed spikes in the column direction as Neptune moves across the detector. The custom aperture numbers associated with Neptune are 200004468--200004923. These observations were taken as part of Guest Observer Programs GO3060 (PI:Rowe) and GO3057 (PI:Gaulme).

<div class="thumbnail">
<video width="100%" id="pelican-installation" class="video-js vjs-default-skin" controls loop preload="auto" data-setup="{}">
<source src="images/release-notes/c3/k2-neptune-c3.mp4" type='video/mp4' alt="Movie of Neptune in C3">
</video>
</div>


<br>

***Trans-Neptunian Object***

The Trans-Neptunian Object (225088) 2007 OR10 was observed with 2 masks and given custom aperture numbers 200004466 and 200004467. This target was observed as part of Guest Observer Program GO3053 (PI:Szabo).

<br>

***Premature End***

Campaign 3 had a nominal duration of 80 days, but an actual duration of 69.2 days. The campaign ended earlier than expected because the on-board storage filled up faster than anticipated due to poorer than expected data compression.

<br>

***Aperture Halos***

In order to ensure that the flux from each target is adequately captured in the presence of the K2 roll motion, for C3, 3-pixel halos were included around each target in the center half of the field of view, and 4-pixel halos around each target in the outer half of the field of view, as shown below. In comparison, many later campaigns were flown with only 2- and 3-pixel halos.

<div class="thumbnail" style="width: 90%;">
<div class="caption">
<i>Figure C3-Halos: The number of halo pixels that were placed around each target in campaign 3 to account for K2 roll motion. Targets farther from the center of the focal plane have more halos due to experiencing greater motion due to the spacecraft roll.</i>
</div>
<a href="images/release-notes/c3/c3_halo_assignment.png">
<img src="images/release-notes/c3/c3_halo_assignment.png" class="img-responsive" alt="Number of halo pixels around each target in C3">
</a>
</div>


<br>


<br>

<h2>Data Quality and Processing Notes</h2>

***Light Curve Quality***

As in other campaigns, the 6-hour spacecraft roll cycle dominates the systematic errors in C3 simple aperture photometry light curves.
The pipeline CDPP 12th magnitude noise benchmark for C3 (DR26) is comparable to that seen in other campaigns with similar star density.

The magnitude dependence of CDPP and its distribution over the focal
plane are shown below. Other CDPP benchmarks can be found in the
<a href="images/release-notes/c3/c3_bin1.00_sc1.00_CDPP_Summary_18081817.txt">
table giving 6.5-hr CDPP as a function of magnitude.</a>

<br>
<div class="thumbnail" style="width: 90%;">
<div class="caption">
<i>Figure C3-CDPP: 6.5-hr CDPP measurements for all targets as a function of Kepler magnitude. Dim targets have poorer overall photometric precision than bright targets, but can look better because the residual sawtooth falls below the noise floor. The saturated targets tend to have the lowest CDPP, but often show a residual sawtooth. </i>
</div>
<a href="images/release-notes/c3/cdpp_vs_mag_dr26.png">
<img src="images/release-notes/c3/cdpp_vs_mag_dr26.png" class="img-responsive" alt="CDPP measured for all targets as a function of Kepler magnitude.">
</a>
</div>

<div class="thumbnail" style="width: 90%;">
<div class="caption">
<i>Figure C3-CDPP FocalPlane: 6.5-hr CDPP measured as a function of position on the focal plane, for 12th and 14th magnitude dwarf stars. The photometric precision is generally better near the center of the focal plane where the variations in roll angle produce less pixel motion. All cadences coincident with a definite thruster firing are gapped.</i>
</div>
<a href="images/release-notes/c3/c3_dwarf_CDPP_by_mod_out_dr26.png">
<img src="images/release-notes/c3/c3_dwarf_CDPP_by_mod_out_dr26.png" class="img-responsive" alt="CDPP per channel for 12th and 14th magnitude dwarfs">
</a>
</div>

<br>

***Incorrect pixel-level calibration of some short-cadence TPFs***

Due to a processing error in <a href="k2-pipeline-release-notes.html#data-release-26">Data Release 26</a>, there are 57 C3 short-cadence targets that had incorrect calibration of their short-cadence pixel-level data. (Long cadence data is unaffected.) The list of affected C3 targets is below. Although it is estimated that only ~25% of them are affected at a non-negligible level, users are strongly encouraged to examine their target, if it is on the list below, to check the severity level and evaluate potential science impact. For a more detailed description of this issue, along with per-target diagnostics and a link to short-cadence TPFs from a previous processing that was not affected by this error, [please read this news post](incorrect-pixel-level-calibration-of-short-cadence-tpfs-for-some-c2r-c3r-and-c5r-targets.html).

200004841&emsp;&emsp;200004843&emsp;&emsp;200004844&emsp;&emsp;200004845&emsp;&emsp;200004846&emsp;&emsp;200004847&emsp;&emsp;200004848<br>
200004849&emsp;&emsp;200004851&emsp;&emsp;205917956&emsp;&emsp;205924248&emsp;&emsp;205962429&emsp;&emsp;205967173&emsp;&emsp;205974115<br>
205979004&emsp;&emsp;205982900&emsp;&emsp;205995584&emsp;&emsp;205997466&emsp;&emsp;206003187&emsp;&emsp;206009487&emsp;&emsp;206020725<br>
206053352&emsp;&emsp;206054604&emsp;&emsp;206064678&emsp;&emsp;206064711&emsp;&emsp;206070413&emsp;&emsp;206078331&emsp;&emsp;206085353<br>
206088888&emsp;&emsp;206094605&emsp;&emsp;206103150&emsp;&emsp;206107253&emsp;&emsp;206108325&emsp;&emsp;206135809&emsp;&emsp;206154641<br>
206167112&emsp;&emsp;206169988&emsp;&emsp;206180842&emsp;&emsp;206183149&emsp;&emsp;206184719&emsp;&emsp;206189170&emsp;&emsp;206189649<br>
206201061&emsp;&emsp;206225297&emsp;&emsp;206245055&emsp;&emsp;206262336&emsp;&emsp;206270336&emsp;&emsp;206289686&emsp;&emsp;206289767<br>
206292760&emsp;&emsp;206359447&emsp;&emsp;206368174&emsp;&emsp;206371648&emsp;&emsp;206445085&emsp;&emsp;206453540&emsp;&emsp;206496452<br>
206535752

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

<b><i>Targets With Data Available at MAST</i></b>
<ul>
<li>16,665 EPIC IDs in long cadence (LC).</li>
<li>54 EPIC IDs in short cadence (LC).</li>
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
            <i>Figure C2-Mag: Distribution of the Kepler magnitudes of observed LC targets in C2.  All targets are chosen by guest observers. The distribution is due to how the largest <a href="k2-approved-programs.html#campaign-2">GO Programs</a>
            were selected. </i>
        </div>
        <a href="images/release-notes/c2/c2_lc_magnitude_distribution.png">
            <img src="images/release-notes/c2/c2_lc_magnitude_distribution.png" class="img-responsive" alt="Distribution of the Kepler magnitudes of observed LC targets in C2.">
<!---        <a href="images/release-notes/c2/C2_lc_kp.png">
            <img src="images/release-notes/c2/C2_lc_kp.png" class="img-responsive" alt="Distribution of the Kepler magnitudes of observed targets in C2.">
--->
        </a>
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

***Light Curve Quality***

The dominant noise contributors in the C2 data are the saw-tooth roll signal inherent in
K2 data and an increased (compared to Kepler and later K2 campaigns) cross-boresight pointing motion
due to the lower bandwidth for the attitude determination and control system (ADCS)
used in K2 campaigns C0, C1, and C2. The low ADCS bandwidth was particularly
problematic for short cadence data, as it meant that the spacecraft pointing errors are on the
same time scale as the short-cadence exposure time, so that the pointing induced noise is correlated from
cadence to cadence. See notes under [C0](#k2-campaign-0) for details.

Analysis of the light curve quality reveals that long cadence CDPP values for dwarf stars are ~70%
higher than values from subsequent campaigns. This is likely due to the low ADCS bandwidth, Mars traversing the focal plane, and the
unflagged large pointing excursion towards the start of the campaign (see next section).
The magnitude dependence of CDPP and its distribution over the focal plane are shown below. Other CDPP benchmarks can be found in the
<a href="images/release-notes/c2/c2_bin1.00_sc1.00_CDPP_Summary_18050517.txt">
table giving 6.5-hr CDPP as a function of magnitude.</a>

<br>
<div class="thumbnail" style="width: 90%;">
<div class="caption">
<i>Figure C2-CDPP: 6.5-hr CDPP measurements for all targets as a function of Kepler magnitude. Dim targets have poorer overall photometric precision than bright targets, but can look better because the residual sawtooth falls below the noise floor. The saturated targets tend to have the lowest CDPP, but often show a residual sawtooth. </i>
</div>
<a href="images/release-notes/c2/cdpp_vs_mag_dr21.png">
<img src="images/release-notes/c2/cdpp_vs_mag_dr21.png" class="img-responsive" alt="CDPP measured for all targets as a function of Kepler magnitude.">
</a>
</div>

<br>


***Unflagged Large Pointing Excursion Towards Start of Campaign***

As part of the <a href="k2-uniform-global-reprocessing-underway.html">K2 global uniform reprocessing effort</a>, cadences are no longer automatically gapped based on the "Spacecraft is not in fine point" (QUALITY flag bit #16, decimal=32768) flag. Instead, the Kepler/K2 Science Office sets the "Spacecraft is in coarse point" flag (QUALITY flag bit #3, decimal=4) flag based on inspection of the actual pointing data for the campaign using high-frequency sub-cadence telemetry. For C2, the spacecraft was technically in 'coarse point' for LC cadences 95687&ndash;95696, which are early on in the campaign. However, the pointing was stable to ~2 pixels during this time period, which given the large size of the collected pixel-stamps for each target in C2 (3&ndash;4 pixels in a 'halo' around every target were collected), the decision was made to not set the "Spacecraft is in coarse point" flag (QUALITY flag bit #3, decimal=4) for these cadences.

While the targets did remain on downloaded pixels during this cadence range, a significant fraction of their flux came in and out of the pipeline-computed optimal photometric apertures. For the PA and PDC lightcurves, this results in some significant outliers during this cadence range, including some negative flux values. Consequently the CDPP (a measure of the detrended lightcurve scatter) is higher due both to the outliers themselves, and the PDC module likely wasting some of its 'detrending power' on trying to correct outliers instead of broader systematic features.

If users are utilizing the PA or PDC lightcurves, it is recommended that they discard the cadences in this range. However, if users are producing their own light curves, as long as their own photometric apertures are sufficiently large to capture each target's flux given the extra motion, or if their light-curve production/detrending technique utilizes all the pixels in the image, then these cadences should still be usable and result in good data.

<br>

***Incorrect pixel-level calibration of some short-cadence TPFs***

Due to a processing error in <a href="k2-pipeline-release-notes.html#data-release-21">Data Release 21</a>, there are 44 C2 short-cadence targets that had incorrect calibration of their short-cadence pixel-level data. (Long cadence data is unaffected.) The list of affected C2 targets is below. Although it is estimated that only ~25% of them are affected at a non-negligible level, users are strongly encouraged to examine their target, if it is on the list below, to check the severity level and evaluate potential science impact. For a more detailed description of this issue, along with per-target diagnostics and a link to correctly-calibrated target-pixel files for these targets, [please read this news post](incorrect-pixel-level-calibration-of-short-cadence-tpfs-for-some-c2r-c3r-and-c5r-targets.html).

202717132&emsp;&emsp;203092367&emsp;&emsp;203393495&emsp;&emsp;203514293&emsp;&emsp;203633963&emsp;&emsp;203734535&emsp;&emsp;203761347<br>
203770817&emsp;&emsp;203836090&emsp;&emsp;203889365&emsp;&emsp;203907143&emsp;&emsp;203927020&emsp;&emsp;203937317&emsp;&emsp;204141790<br>
204226766&emsp;&emsp;204241221&emsp;&emsp;204296786&emsp;&emsp;204313397&emsp;&emsp;204356572&emsp;&emsp;204371831&emsp;&emsp;204372172<br>
204399980&emsp;&emsp;204490599&emsp;&emsp;204494885&emsp;&emsp;204506777&emsp;&emsp;204506926&emsp;&emsp;204514548&emsp;&emsp;204550630<br>
204595607&emsp;&emsp;204624076&emsp;&emsp;204638251&emsp;&emsp;204662993&emsp;&emsp;204819556&emsp;&emsp;204926239&emsp;&emsp;204951731<br>
204959839&emsp;&emsp;204987685&emsp;&emsp;205010433&emsp;&emsp;205089975&emsp;&emsp;205204563&emsp;&emsp;205211890&emsp;&emsp;205311975<br>
205467732&emsp;&emsp;205703810

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

These release notes are for the C1 data currently available at MAST (Data Release 32) in the nominal K2 data locations, which have been processed with the final version of the K2 pipeline as part of the <a href="k2-uniform-global-reprocessing-underway.html">K2 global uniform reprocessing effort</a>. The original release notes corresponding to the previous version(s) of C1 data (Data Releases 3 and 14) can be found in the <a href="archived-k2-data-release-notes.html#k2-campaign-1">archived data release notes page</a>.

<h2>At a glance</h2>

<div class="row">
<div class="col-lg-5">

    <b><i>Pointing</i></b>
    <ul>
        <li>RA: 173.939610 degrees</li>
        <li>Dec: 1.4172989 degrees</li>
        <li>Roll: 157.641206 degrees</li>
    </ul>

    <b><i>Targets With Data Available at MAST</i></b>
    <ul>
    <li>21,647 EPIC IDs in long cadence (LC).</li>
    <li>56 EPIC IDs in short cadence (LC).</li>
    <li>1 custom target was selected in C1: TNO 2002 GV31, which was assigned EPIC ID 200001049</li>
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
    <li> <a href="k2-pipeline-release-notes.html#data-release-32">Data Release 32</a> </li>
    </ul>

    <br>

    <div class="thumbnail">
        <div class="caption">
            <i>Figure C1-Mag: Distribution of the Kepler magnitudes of observed LC targets in C1. All targets are chosen by Guest Observers. The shape is due to how the largest <a href="k2-approved-programs.html#campaign-1">Guest Observer programs</a> were selected.</i>
        </div>
        <a href="images/release-notes/c1/C1LcMagDistribution.png">
            <img src="images/release-notes/c1/C1LcMagDistribution.png" class="img-responsive" alt="Distribution of the Kepler magnitudes of observed LC targets in C1.">
        </a>
    </div>

</div>

<div class="col-lg-7">

<div class="thumbnail">
    <div class="caption">
    <i>Figure: Figure C1-FOV: Schematic of Kepler's C1 field-of-view with high profile objects.</i>
</div>
<a href="images/k2/k2-c01-field.png">
    <img src="images/k2/k2-c01-field.png" class="img-responsive" alt="C1 field-of-view with selected targets">
    </a>
</div>

<div class="thumbnail">
    <div class="caption">
    <i>Figure: Figure C1-FFI: A full frame image (FFI) taken during C1, with a flux scaling designed to highlight features of interest.</i>
</div>
<a href="images/release-notes/c1/C1R-FFI.png">
    <img src="images/release-notes/c1/C1R-FFI.png" class="img-responsive" alt="A C1 FFI">
    </a>
</div>

</div>

</div>


<h2>Features and Events</h2>

***Operational Considerations***

Campaign 1 (C1) was the first full length observing campaign for K2 where the targets were
selected by peer review. The project was uncertain of the pointing precision and compression
efficiency that could be achieved in early K2 operations and took steps to miminimize the risk
of losing science data. In order to allow for the potential of coarse point operations, all target apertures included six halo rings.
The oversized apertures and uncertain compression performance led the project to
include a mid-campaign break lasting 2.9 days (long cadences 93281&ndash;93420) in order to downlink data.

<br>

***Attitude Tweak***

The attitude of the spacecraft was tweaked by 3.3 pixels at cadence 91433 to better
position the targets in the centers of their apertures. All cadences in the first
2 days of C1 prior to this event (long cadences 91332&mdash;91433) have the first bit in the QUALITY column set
(integer value = 1) to indicate that they were taken prior to the tweak.

When creating light curves, the pipeline uses PA-COA to determine the optimal photometric
aperture that maximizes the signal-to-noise ratio for each target over the full
campaign. This static optimal aperture is determined from a robust average of
the achieved pointing, so relatively short segments of off-nominal pointing
tend to be excluded from the aperture calculation. In the case of C1, the optimal
apertures generally do not contain the target star in the pre-attitude tweak
cadences. Accordingly, the SAP-Flux and PDC-Flux values found in the light curve
files are gapped for the pre-tweak cadences (long cadences 91332&mdash;91433, where the QUALITY flag=1). In
addition, neither background flux (FLUX_BKG, FLUX_BKG_ERR) nor motion
polynomial values (POS_CORR1, POS_CORR2) were computed for the
pre-tweak cadences.

Because of the large C1 apertures (with six halos) the TPFs **do** fully contain the target in the pre-attitude tweak cadences.
However, due to the offset, incorrect background flux values are subtracted from the TPF pixel fluxes given
in the FLUX column of the TPF. Users wishing to recover photometry from these
cadences should add the per-cadence pixel background values (TPF column FLUX_BKG)
back into the pixel flux values and then compute their own background levels.
The position offset columns (POS_CORR1, POS_CORR2) should likewise be ignored
for these pre-tweak cadences.

Finally, in the pre-tweak cadences a small number of targets may have incorrect
smear calibrations due to bright saturating stars spilling charge into the
detector smear regions. Such effects are flagged and excluded from smear calibration
for the post-tweak cadences, but the pre-tweak positions of the bright stars
were not used to flag bad smear corrections. Only about 0.2% of the
focal plane columns were affected in this way, so the number of potentially
affected targets is very small.

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
2) assigned a new EPIC ID. EPIC IDs were created for 28 targets, ranging from
210282464 to 210282491. The remaining C1 targets have EPIC IDs ranging
from 20100000001 to 202059065.

<br>


<h2>Data Quality and Processing Notes</h2>

***Light Curve Quality***

The dominant noise contributors in the C1 data are the saw-tooth roll signal inherent in
K2 data and an increased (over Kepler and later K2 campaigns) cross-boresight pointing motion
due to the lower bandwidth for the attitude determination and control system (ADCS)
used in K2 campaigns C0, C1, and C2. The low ADCS bandwidth was particularly
problematic for short cadence data, as it meant that the spacecraft pointing errors are on the
same time scale as the SC exposure, so that the pointing induced noise is correlated from
cadence to cadence. See notes under [C0](#k2-campaign-0) for details.


The magnitude dependence of CDPP and its distribution over the focal
plane are shown below. Other CDPP benchmarks can be found in the
<a href="images/release-notes/c1/c1_bin1.00_sc1.00_CDPP_Summary_19051201.txt">
table giving 6.5-hr CDPP as a function of magnitude.</a>

<br>
<div class="thumbnail" style="width: 90%;">
<div class="caption">
<i>Figure C1-CDPP: 6.5-hr CDPP measurements for all targets as a function of Kepler magnitude. Dim targets have poorer overall photometric precision than bright targets, but can look better because the residual sawtooth falls below the noise floor. The saturated targets tend to have the lowest CDPP, but often show a residual sawtooth. </i>
</div>
<a href="images/release-notes/c1/cdpp_vs_mag_dr32.png">
<img src="images/release-notes/c1/cdpp_vs_mag_dr32.png" class="img-responsive" alt="CDPP measured for all targets as a function of Kepler magnitude.">
</a>
</div>

<div class="thumbnail" style="width: 90%;">
<div class="caption">
<i>Figure C1-CDPP FocalPlane: 6.5-hr CDPP measured as a function of position on the focal plane, for 12th and 14th magnitude dwarf stars. The photometric precision is generally better near the center of the focal plane where the variations in roll angle produce less pixel motion. All cadences coincident with a definite thruster firing are gapped.</i>
</div>
<a href="images/release-notes/c1/c1_dwarf_CDPP_by_mod_out_dr32.png">
<img src="images/release-notes/c1/c1_dwarf_CDPP_by_mod_out_dr32.png" class="img-responsive" alt="CDPP per channel for 12th and 14th magnitude dwarfs">
</a>
</div>

<br>

<hr>



# K2 Campaign 0

These release notes are for the C0 data currently available at MAST in the nominal K2 data locations, which have been processed with the final version of the K2 pipeline as part of the <a href="k2-uniform-global-reprocessing-underway.html">K2 global uniform reprocessing effort</a>. The original release notes corresponding to the previous version(s) of C0 data can be found in the <a href="archived-k2-data-release-notes.html#k2-campaign-0">archived data release notes page</a>.

Campaign 0 (C0) was implemented as a full-length engineering test to prove that K2 was a viable mission. It observed sources "at risk" from a community-provided target list.


<h2>At a glance</h2>

<div class="col-lg-5">

    <b><i>Pointing</i></b>
    <ul>
        <li>RA: 98.2985439 degrees</li>
        <li>Dec: 21.5904167 degrees</li>
        <li>Roll: 177.4754730 degrees</li>
    </ul>

    <b><i>Targets With Data Available at MAST</i></b>
    <ul>
        <li>7,902 EPIC IDs in long cadence (LC).</li>
        <li>13 EPIC IDs in short cadence (LC).</li>
        <li>Several custom targets (see below)</li>
    </ul>

    <b><i>Full Frame Images (FFI)</i></b>
    <ul>
        <li><a href="https://archive.stsci.edu/pub/k2/ffi/ktwo2014070234206-c00_ffi-cal.fits">ktwo2014070234206-c00_ffi-cal.fits</a></li>
        <li><a href="https://archive.stsci.edu/pub/k2/ffi/ktwo2014074233223-c00_ffi-cal.fits">ktwo2014074233223-c00_ffi-cal.fits</a><sup>†</sup></li>
        <li><a href="https://archive.stsci.edu/pub/k2/ffi/ktwo2014110010101-c00_ffi-cal.fits">ktwo2014110010101-c00_ffi-cal.fits</a><sup>†</sup></li>
    </ul>

<sup>†</sup>Taken while the telescope was in coarse point.<br><br>

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
    <li> <a href="k2-pipeline-release-notes.html#data-release-28">Data Release 28</a> </li>
    </ul>


</div>

<div class="col-lg-7">

    <div class="thumbnail">
        <div class="caption">
            <i>Figure C0-FOV: Schematic of Kepler's C0 field-of-view with high profile objects shown.</i>
        </div>
        <a href="images/k2/k2-c00-field.png">
            <img src="images/k2/k2-c00-field.png" class="img-responsive" alt="C0 field-of-view with high profile objects.">
        </a>
    </div>

    <div class="thumbnail">
        <div class="caption">
            <i>Figure C0-Mag: Distribution of the Kepler magnitudes of observed LC targets in C0.  All targets are chosen by guest observers. The distribution is due to how the largest <a href="k2-approved-programs.html#campaign-0">GO Programs</a>
            were selected. </i>
        </div>
        <a href="images/release-notes/c0/c0_lc_magnitude_distribution.png">
            <img src="images/release-notes/c0/c0_lc_magnitude_distribution.png" class="img-responsive" alt="Distribution of the Kepler magnitudes of observed LC targets in C0.">
        </a>
    </div>

</div>

<h2>Features and Events</h2>

***Large Pixel Masks***

When planning C0 observations, the pointing performance of K2 was not yet accurately known. The worst case scenario was that a star at the edge of the focal plane could move as much as 40" from its nominal position. Therefore each star was assigned a large pixel mask by first computing a Kepler-style optimal aperture and then adding 10 rings of pixels to account for a potential 40" pointing offset. (Later campaigns only added 2 &ndash; 4 rings of pixels.) Care will be needed when performing photometry on C0 data &mdash; simply including all collected pixels for a given target will not create a high signal-to-noise light curve. For tools to help choose your photometric aperture, see for example the [lightkurve Python package](https://docs.lightkurve.org), [PyKE software tool suite](http://pyke.keplerscience.org), or [other packages](https://archive.stsci.edu/missions-and-data/kepler/related-software-1).

<br>

***Pointing and Roll Performance***

C0 was the first full-length campaign observed by K2, and as such testing and refinement of the telescope control systems occurred during the campaign. The first ~18 days of observations had a mixture of fine and coarse pointing, at the end of which the telescope was put into safe mode for ~24 days to adjust the pointing control systems. The spacecraft then resumed observations, experiencing just over a day of coarse point, followed by ~37 days of fine point. Figure C0-Pointing shows the pointing history over the campaign by plotting the observed motion at the edge of the field of view in science pixels versus cadence.

<div class="thumbnail" style="width: 100%;display: inline-block;">
<div class="caption">
<i>Figure C0-Pointing: the observed amount of motion in pixels at the edge of field during C0.</i>
<a href="images/release-notes/c0/c0-entire-pointing.png">
<img src="images/release-notes/c0/c0-entire-pointing.png" class="img-responsive" alt="Pixels of motion at field edge during C0.">
</a>
</div>
</div>

Based on the pointing history, and known complications in processing data with large coarse pointing regions and data gaps, **while the entire C0 cadence range was processed by CAL (pixel calibration) and PA (simple aperture lightcurves), only long cadences 89407 &ndash; 91186 (and the corresponding short cadence range 2670670 &ndash; 2724069) were processed by PDC (systematic detrended lightcurves).** This corresponds to the ~37 days of fine point data at the end of the campaign.

During these ~37 days, examining Figure C0-MAR, the pipeline-calculated maximum distance between the derived and nominal positions for any target (the "maximum attitude residual", or MAR)
for C18 is less than 2.1 pixels, substantially under the 10-pixel limit accommodated by the aperture halos. (Note that long cadences 89407 &ndash; 89410 are flagged using QUALITY flag bit #3 to indicate significant pointing excursions, despite the spacecraft technically being in fine point, and users may wish to discard them.)


<div class="thumbnail" style="width: 48.75%;display: inline-block;">
<div class="caption">
<i>Figure C0-Roll-Error: the roll-error between the photometrically derived attitude (PAD) and the nominal pointing plotted against time for C0.</i>
<a href="images/release-notes/c0/c0_pad_pdq_attitude_roll.png">
<img src="images/release-notes/c0/c0_pad_pdq_attitude_roll.png" class="img-responsive" alt="Pipeline measured roll error for C0.">
</a>
</div>
</div>

<div class="thumbnail" style="width: 49.25%;display: inline-block;">
<div class="caption">
<i>Figure C0-MAR: the maximum distance between the photometrically derived attitude (PAD) and the nominal position plotted against time for C0.</i>
<a href="images/release-notes/c0/c0_pad_pdq_attitude_mar.png">
<img src="images/release-notes/c0/c0_pad_pdq_attitude_mar.png" class="img-responsive" alt="Maximum residual of the C0 attitude measured with PAD and PDQ.">
</a>
</div>
</div>

<br>


***No Data for Modules 3 and 7***

Prior to the start of C0, on January 21, 2014, the photometer was autonomously powered off by an under voltage fault in the Local Detector Electronics Power Supply. Since that time, module 7 (i.e., channels 17 to 20; see [this graphic](https://keplerscience.arc.nasa.gov/images/kepler_focal_plane_layout_channels_color.png)) has yielded no star data or charge injection signal. The subsequent behavior of this module is very similar to that of module 3 after it failed on January 19, 2010. Thus, there is no data for targets falling modules 3 or 7 for Campaign 0 or subsequent campaigns.

<br>


***Jupiter's Reflection***

Jupiter was in the K2 field of view during C0 from 2014-03-14 through 2014-05-12, but fell on the dead module 3. It creates a bright antipodal ghost on module 23, channel 79, and impacts all the targets observed in this region. See the FFI ktwo2014074233223-c00, extension 79, for an image of the reflection.

While Jupiter was on the focal plane, the background level was increased over its nominal value for nearly half the channels, with the largest impact seen in channels 53 &ndash; 84. In addition, as Jupiter moved on and off the focal plane, a specular reflection lasting approximately 6 hours was seen in these channels. The relative background levels as measured in the smear signal from channel 83 are shown below as Jupiter enters the focal plane (near cadence no. 87525) and leaves the focal plane (cadence no. 90375). The specular bump resulted in an increase in background level of 25 &ndash; 30% for the affected channels, while the quasi-static background increase for the time Jupiter was on the focal plane was 3 &ndash; 5%.

<div class="thumbnail" style="width: 49%;display: inline-block;">
    <div class="caption">
        <i>Figure: Part of an FFI showing the reflection of Jupiter as seen on channel 79.</i>
    </div>
    <a href="images/release-notes/c0/Jupiter-ghost3.png">
        <img src="images/release-notes/c0/Jupiter-ghost3.png" class="img-responsive" alt="FFI showing the reflection of Jupiter as seen on channel 79.">
    </a>
</div>

<div class="thumbnail" style="width: 49%;display: inline-block;">
    <div class="caption">
        <i>Figure: The background level on channel 83 as Jupiter enters (left) and leaves (right) the focal plane.</i>
    </div>
    <a href="images/release-notes/c0/ch83_jupiter_on_smear.png">
        <img src="images/release-notes/c0/ch83_jupiter_on_smear.png" class="img-responsive" alt="The background level on channel 83 as Jupiter enters (left) and leaves (right) the focal plane.">
    </a>
</div>


<br>

***Observations of M35 and NGC 2158***

The open clusters M35 (NGC 2168) and NGC 2158 were observed during this campaign by placing 154 separate 50x50 pixel masks over the densest portion of these two adjacent clusters. Each mask was given a custom aperture number to act as the unique identifier found in the file name. The target pixel files for these clusters have custom aperture numbers ranging from 200000811 to 200000964.

<div class="thumbnail" style="width: 50%; display: inline-block;">
    <div class="caption">
        <i>Figure: Individual masks when tiled together cover the field of view containing M35 and NGC 2158.</i>
    </div>
    <a href="images/release-notes/c0/M35_im1.png">
        <img src="images/release-notes/c0/M35_im1.png" class="img-responsive" alt="Individual masks when tiled together cover the field of view containing M35 and NGC 2158.">
    </a>
</div>

<br>


<h2>Data Quality and Processing Notes</h2>

<!--- Consider talking about CR correction before/after --->

***Dynablack Turned Off***

One of the new features in data processed as part of the <a href="k2-uniform-global-reprocessing-underway.html">K2 global uniform reprocessing effort</a> is the use of Dynablack, a more sophisticated algorithm to perform the pixel-level calibration, which also flags cadences that are likely affected by the presence of rolling bands. However, due to the large amount of coarse point data, combined with the ~24 day data gap due to the safe mode event, the Dynablack module did not have enough high-quality data to be able to run. Thus for this data release, the pixel-level calibrations were performed with the standard CAL module, and there are no rolling band flags in the delivered FITS files.

<br>


***PDC Only Run On Last ~37 Days***

Based on the pointing history and known complications in processing data with large coarse pointing regions and data gaps, **while the entire C0 cadence range was processed by CAL (pixel calibration) and PA (simple aperture lightcurves), only long cadences 89407 &ndash; 91186 (and the corresponding short cadence range 2670670 &ndash; 2724069) were processed by PDC (systematic detrended lightcurves).** This corresponds to the ~37 days of fine point data at the end of the campaign.

As a result, lightcurve files (\*llc.fits and \*slc.fits) will have valid SAP_FLUX values for most cadences throughout the entire time span of C0 when observations were taken. PDCSAP_FLUX values however will be 0 or NaN for cadences prior to 89407.

Similarly, the cotrending basis vector (CBV) file for C0 ([ktwo-c00-d28_lcbv.fits](https://archive.stsci.edu/missions/k2/cbv/ktwo-c00-d28_lcbv.fits)) will only have data for cadences 89407 &ndash; 91186.

<br>


***No ARP Files Available***

Since the necessary pixels were not collected in C0, note there are no artifact removal pixel (ARP) files available for C0 (see [S2.3.8 of the Kepler Archive Manual](https://archive.stsci.edu/kepler/manuals/archive_manual.pdf#page=51)).

<br>


***48 Targets Without Lightcurves***

The following 48 targets do not have associated lightcurve files, because the pipeline was unable to find a suitable photometric aperture for these targets. In general they are non-standard targets, such as clusters or very bright objects, or there is no significant flux at the target position. Users are encouraged to create their own lightcurves for these objects from the existing target pixel files using software such as [lightkurve Python package](https://docs.lightkurve.org), [PyKE software tool suite](http://pyke.keplerscience.org), or [other packages](https://archive.stsci.edu/missions-and-data/kepler/related-software-1).


202060164&emsp;&emsp;202060210&emsp;&emsp;202060421&emsp;&emsp;202060813&emsp;&emsp;202065115&emsp;&emsp;202065116<br>
202065117&emsp;&emsp;202065118&emsp;&emsp;202065119&emsp;&emsp;202065120&emsp;&emsp;202065121&emsp;&emsp;202065122<br>
202065123&emsp;&emsp;202065124&emsp;&emsp;202065125&emsp;&emsp;202065126&emsp;&emsp;202065127&emsp;&emsp;202065128<br>
202065129&emsp;&emsp;202065130&emsp;&emsp;202065131&emsp;&emsp;202065132&emsp;&emsp;202065133&emsp;&emsp;202065134<br>
202065135&emsp;&emsp;202065136&emsp;&emsp;202071440&emsp;&emsp;202071443&emsp;&emsp;202071445&emsp;&emsp;202071446<br>
202071448&emsp;&emsp;202071450&emsp;&emsp;202072947&emsp;&emsp;202072959&emsp;&emsp;202072962&emsp;&emsp;202072982<br>
202073036&emsp;&emsp;202073099&emsp;&emsp;202073125&emsp;&emsp;202073136&emsp;&emsp;202073152&emsp;&emsp;202073290<br>
202073323&emsp;&emsp;202073354&emsp;&emsp;202073360&emsp;&emsp;202073364&emsp;&emsp;202073377&emsp;&emsp;202073415<br>

<br>


***Degraded WCS Information***

Due the smaller number of targets, and large pixel-stamp size, in C0 compared to other fields, overall the World Coordinate System (WCS) solution for most channels is not as high-quality as other campaigns. Users should be especially cautious of the WCS information for the following channels (module.output) in C0, which may be inaccurate by up to several pixels / tens of arcseconds: 2 (2.2), 10 (4.2), 28 (9.4), 42 (13.2), 45 (14.1), 49 (15.1), 51 (15.3), 52 (15.4), and 62 (18.2).

The reduced WCS quality compared to other campaigns also applies to the full frame images (FFIs). Notably, the third FFI [https://archive.stsci.edu/missions/k2/ffi/ktwo2014110010101-c00_ffi-cal.fits](https://archive.stsci.edu/missions/k2/ffi/ktwo2014110010101-c00_ffi-cal.fits) has an inaccurate WCS that is off by several pixels / tens of arcseconds. Should users require a more accurate WCS, it is recommended to use the WCS info from the previous CO processing ([DR2](https://keplerscience.arc.nasa.gov/k2-pipeline-release-notes.html#data-release-2); [https://archive.stsci.edu/missions/k2/ffi/old_release_files/ktwo2014110010101-c00_ffi-cal.fits](https://archive.stsci.edu/missions/k2/ffi/old_release_files/ktwo2014110010101-c00_ffi-cal.fits)), which was produced using [astrometry.net](http://nova.astrometry.net).

<br>


***Potentially Poor Apertures in Channel 45 (14.1)***

A significant number of targets on channel 45 had sub-optimal apertures selected by the pipeline, and as a result the lightcurve quality will be poorer than other channels. Users with targets on this channel are encouraged to inspect the aperture selected by the pipeline (using the target pixel files) before using the lightcurves for science, and/or select a custom aperture and produce new lightcurves using tools such as the [lightkurve Python package](https://docs.lightkurve.org), [PyKE software tool suite](http://pyke.keplerscience.org), or [other packages](https://archive.stsci.edu/missions-and-data/kepler/related-software-1).

<br>


***Increased Photometric Jitter Caused by Lower ADCS Bandwidth***

For the K2 Mission, only one guide star was observed for each fine-guidance sensor. (Kepler had ten per sensor.) This change was demanded by the need for increased aperture sizes given the uncertainties in the star-tracker to boresight alignment, and the need to acquire an entirely new field-of-view every 80 to 90 days. To compensate for the increased sensor noise and assure that fine-point lock could be achieved, the attitude determination and control system (ADCS) bandwidth for K2 was set to 0.02 Hz for C0, C1, and C2. (Kepler used 0.1 Hz.) This low bandwidth meant that the cross-boresight attitude (i.e., RA and Dec) had a time constant of 50 seconds, which is comparable to the short-cadence duration of 58.89 seconds. As a result, pointing-induced noise is correlated from cadence to cadence for short-cadence observations, resulting in significantly increased photometric jitter for short-cadence lightcurves. It is likely that long-cadence lightcurves also have a slightly increased photometric jitter due to the low ADCS bandwith. Starting with C3, the ADCS bandwidth was increased to 0.05 Hz (20 seconds) to mitigate this effect.

<br>


***Light Curve Quality***

The 6-hour spacecraft roll cycle dominates the systematic errors in C0 simple aperture photometry light curves. In general the PDCSAP_FLUX photometric quality (produced only for the last ~37 days of the campaign) is comparable to later campaigns.

The magnitude dependence of CDPP and its distribution over the focal
plane are shown below. Other CDPP benchmarks can be found in the
<a href="images/release-notes/c0/c0_bin1.00_sc1.00_CDPP_Summary_19052401.txt">
table giving 6.5-hr CDPP as a function of magnitude.</a>

<br>
<div class="thumbnail" style="width: 90%;">
<div class="caption">
<i>Figure C0-CDPP: 6.5-hr CDPP measurements for all targets as a function of Kepler magnitude. Dim targets have poorer overall photometric precision than bright targets, but can look better because the residual sawtooth falls below the noise floor. The saturated targets tend to have the lowest CDPP, but often show a residual sawtooth. </i>
</div>
<a href="images/release-notes/c0/cdpp_vs_mag_dr28.png">
<img src="images/release-notes/c0/cdpp_vs_mag_dr28.png" class="img-responsive" alt="CDPP measured for all targets as a function of Kepler magnitude.">
</a>
</div>

<div class="thumbnail" style="width: 90%;">
<div class="caption">
<i>Figure C0-CDPP FocalPlane: 6.5-hr CDPP measured as a function of position on the focal plane, for 12th and 14th magnitude dwarf stars. The photometric precision is generally better near the center of the focal plane where the variations in roll angle produce less pixel motion. All cadences coincident with a definite thruster firing are gapped.</i>
</div>
<a href="images/release-notes/c0/c0_dwarf_CDPP_by_mod_out_dr28.png">
<img src="images/release-notes/c0/c0_dwarf_CDPP_by_mod_out_dr28.png" class="img-responsive" alt="CDPP per channel for 12th and 14th magnitude dwarfs">
</a>
</div>

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

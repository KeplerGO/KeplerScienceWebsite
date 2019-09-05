Title: Incorrect pixel-level calibration of short-cadence TPFs for some C2R, C3R, and C5R targets
Date: 2019-07-16 17:00
Author: Jeff Coughlin and Geert Barentsen

There is an issue that affects the calibrated data in some of the the short-cadence target-pixel files (and resulting short-cadence lightcurves) for the most recent C2, C3, and C5 deliveries (Data Releases 21, 26, and 31).

<u> ** What is it? ** </u>

Previously [we announced](problem-with-kepler-and-k2-short-cadence-pixel-calibration.html) that the short-cadence data for some targets in Kepler and early (C0&ndash;C5) K2 campaigns were incorrectly calibrated. Specifically, due to an ambiguous technical specification describing the Pixel Mapping Reference File (PMRF), the collateral smear data correction, used to correct for the effects of Kepler’s shutterless readout, was sometimes applied to the wrong target when calibrating the short-cadence pixel-level data. This can result in an additive effect on individual pixels, as well as a time-varying signal, visible as vertical stripes in the short-cadence images, as shown in the figures at the bottom of the page. (See [§2.6.3 of the Kepler Instrument Handbook](https://archive.stsci.edu/files/live/sites/mast/files/home/missions-and-data/kepler/_documents/KSCI-19033-002-instrument-hb.pdf#page=25) and [§5.3.7 of the Kepler Data Processing Handbook](https://archive.stsci.edu/files/live/sites/mast/files/home/missions-and-data/kepler/_documents/KSCI-19081-002-KDPH.pdf#page=120) for detailed descriptions of smear correction.) Note that the long-cadence data for these or other targets was *not* affected.

The incorrect calibration was documented via [KSCI-19080-002.pdf](data/documentation/KSCI-19080-002.pdf) and [this 2016 news post](problem-with-kepler-and-k2-short-cadence-pixel-calibration.html), which listed the short-cadence targets that could have possibly been affected by the error at any level, and an estimate that ~25% were affected at a non-negligible level. New versions of the PMRF files were generated that conform to a unified technical specification, and correctly processed short-cadence target pixel files were later delivered for C1 and C3&ndash;C5.

As part of the K2 [global uniform reprocessing effort](k2-uniform-global-reprocessing-underway.html) the mission set up a second computing cluster to be able to process two campaigns simultaneously. Unfortunately, a misconfiguration in the setup of this second cluster resulted in the original PMRF files being used for the recently reprocessed C2, C3, and C5 data. This resulted again in the incorrect calibration of the short-cadence target pixel files (TPFs) of select targets in C2, C3, and C5. No other campaigns were affected. Of the 474 short-cadence target files among these three campaigns, from the investigation documented in [KSCI-19080-002.pdf](data/documentation/KSCI-19080-002.pdf), we know that 175 are possibly affected at any level, and ~25% of those 175 targets are affected at a non-negligible level. [Click here to get the list of the 175 affected targets.](/data/documentation/k2_reproc_c2_c3_c5_bad_short_cadence_target_list.csv)

<br>

<u> ** What should users do if their target is impacted? ** </u>

We recommend that users whose C3 or C5 targets are impacted (at any level) use the previous processing (Data Release 10) of C3 and C5, available at MAST as individual FITS files [in this directory for C3](https://archive.stsci.edu/missions/k2/target_pixel_files/old_release_bundles/c3/c3_old_release_files/) and [in this directory for C5](https://archive.stsci.edu/missions/k2/target_pixel_files/old_release_bundles/c5/c5_old_release_files/). Note that these directories follow the usual MAST K2 directory structure of /XXXX00000/YY000/, where the EPIC ID is XXXXYYZZZ (e.g., data for EPIC 211934173 can be found under /211900000/34000/).

We recommend that users whose C2 targets are impacted use a special release of C2 short-cadence TPFs made available in September 2019 under [Data Release 34](k2-pipeline-release-notes.html#data-release-34).  These short-cadence TPFs are from a previously unreleased processing of C2 that had correctly calibrated short-cadence data, but used a version of the pipeline similar to C14, i.e., just before implementing the settings used for the [global uniform reprocessing effort](k2-uniform-global-reprocessing-underway.html). The only significant effect for short-cadence target-pixel files in this case is the lack of Dynablack, i.e., the less sophisticated pixel-level calibration method was used and the FITS files will not contain rolling-band flags.

<br>

<u> ** Which targets are most impacted and what do they look like? ** </u>

We further investigated the impact to individual targets by comparing the short- and long-cadence TPFs and lightcurves. In general, when thirty short-cadence exposures are summed to match the corresponding long-cadence exposure, it should result in nearly identical fluxes &mdash; when it does not, that is a good indication that there is likely a discrepancy in the short- vs long-cadence pixel-level calibration. Some differences will naturally occur due to slight variations in how the short- and long-cadence pixels are calibrated, but for most targets, large differences likely indicate the PMRF issue. This is especially true when an anomalously bright or dark column is seen in the short-cadence TPF (e.g., see the example of 211934173 below). We computed the standard deviation (in ppm) of the difference between the short-cadence lightcurve (summed every thirty short cadences) and the long-cadence lightcurve for each target in C2, C3, and C5. [Click here for the list of values for each possibly affected target](/data/documentation/k2_reproc_c2_c3_c5_short_long_lightcurve_diff_std.csv). (Note that for 4 targets the metric was unable to be computed.)

In addition, we are providing plots for each target to aid in visually diagnosing significantly affected targets. The plots show the short- and long-cadence lightcuves and their differences, which visually demonstrates the size of the signal due to the PMRF issue compared to the lightcurve. In addition, we summed up every 30 short-cadence pixel-level images and computed the difference to the corresponding long-cadence image. The plots also show the median of these differenced images, which will reveal bright or dark vertical stripes when the target is affected. The amplitude of this difference image, compared to the overall flux of the object, is also helpful in diagnosing the severity of the impact on each target on a desired scientific investigation. [Click here for diagnostic plots of all C2, C3, and C5 targets](/images/news/pmrf/).

Users are encouraged to check the long- vs short-cadence difference metric, as well as the individual plots, for all possibly affected targets to gauge the possible scientific impact. Note that 9 of the 161 one-pixel wide strips used to observe Neptune in C3 are affected.

<br>

**If users have any questions about the data or the provided plots/analysis, please contact [the Kepler/K2 helpdesk](https://keplerscience.arc.nasa.gov/helpdesk.html) at <keplergo@mail.arc.nasa.gov>.**

<br>

<div class="thumbnail" style="width: 49%;display: inline-block;">
<div class="caption">
<i>Long-cadence image of EPIC 211934173 in most recent C5 processing (Data Release 31).</i>
<a href="images/news/epic211934173-lc.png">
<img src="images/news/epic211934173-lc.png" class="img-responsive" alt="EPIC 211934173 long-cadence image">
</a>
</div>
</div>

<div class="thumbnail" style="width: 49%;display: inline-block;">
<div class="caption">
<i>Short-cadence image of EPIC 211934173 in most recent C5 processing (Data Release 31).</i>
<a href="images/news/epic211934173-sc.png">
<img src="images/news/epic211934173-sc.png" class="img-responsive" alt="EPIC 211934173 short-cadence image">
</a>
</div>
</div>

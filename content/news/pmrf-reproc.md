Title: Incorrect pixel-level calibration of short-cadence TPFs for some C2R, C3R, and C5R targets
Date: 2019-07-09 10:00
Author: Jeff Coughlin and Geert Barentsen

There is an issue that affects the calibrated data in some of the the short-cadence target-pixel files (and resulting short-cadence lightcurves) for the most recent C2, C3, and C5 deliveries.


### What is it?

Previously [we announced](problem-with-kepler-and-k2-short-cadence-pixel-calibration.html) that some targets in Kepler and early (C0--C5) K2 campaigns had their short-cadence data incorrectly calibrated. Specifically, due to an ambiguous technical specification describing the Pixel Mapping Reference File (PMRF), the collateral smear data correction, used to correct for the effects of Kepler’s shutterless readout, was sometimes applied to the wrong target when calibrating the short-cadence pixel-level data. This can result in an additive effect on individual pixels, as well as a time-varying signal. (See [§2.6.3 of the Kepler Instrument Handbook](https://archive.stsci.edu/files/live/sites/mast/files/home/missions-and-data/kepler/_documents/KSCI-19033-002-instrument-hb.pdf#page=25) and [§5.3.7 of the Kepler Data Processing Handbook](https://archive.stsci.edu/files/live/sites/mast/files/home/missions-and-data/kepler/_documents/KSCI-19081-002-KDPH.pdf#page=120) for detailed descriptions of smear correction.) Note that the long-cadence data for these or other targets was *not* affected.

The incorrect calibration was documented (see [KSCI-19080-002.pdf](data/documentation/KSCI-19080-002.pdf)), including a list of the short-cadence targets that could have possibly been affected by the error at any level. New versions of the PMRF files were generated that conformed to a unified technical specification, and correctly processed short-cadence target pixel files were later delivered for C1 and C3--C5.  CLAIRFY KSCI + SEPARATE LIST (point to below).

As part of the K2 [global uniform reprocessing effort](k2-uniform-global-reprocessing-underway.html) the mission set up a second computing cluster to be able to process two campaigns simultaneously. Unfortunately, a misconfiguration in the setup of this second cluster resulted in the original PMRF files being used for the recently reprocessed C2, C3, and C5 data. This resulted again in the incorrect calibration of the short-cadence target pixel files (TPFs) of select targets in C2, C3, and C5. No other campaigns were affected. Of the 474 short-cadence target files among these three campaigns, from the investigation documented in [KSCI-19080-002.pdf](data/documentation/KSCI-19080-002.pdf) we know that 175 are possibly affected at any level, and ~25% of those 175 targets are affected at a non-negligible level.


### Which targets are most impacted?

We further investigated the impact to individual targets by comparing the short- and long-cadence TPFs and lightcurves. In general, when thirty short-cadence exposures are summed to match the corresponding long-cadence exposure, it should result in nearly identical fluxes &mdash; when it does not, that is a good indication that there is likely a discrepancy in the short- vs long-cadence pixel-level calibration. Some differences will occur due to slight variations in how the short- and long-cadence pixels are calibrated, but for most targets, large differences likely indicate the PMRF issue, especially when an anomalously bright or dark column is seen in the short-cadence TPF.

We computed the standard deviation of the difference between the short-cadence lightcurve (summed every thirty short cadences) and the long-cadence lightcurve for each target in C2, C3, and C5, and list the value for each of the possibly affected targets below. Users are encouraged to check if their target shows a large deviation and thus might be affected at a significant level.

ENCOURAGE USERS TO CHEKC TARGET REGARDLESS OF METRIC, and USE OLD PROC.

In addition, we are providing plots for each target to aid in visually diagnosing significantly affected targets. The plots show the short- and long-cadence lightcuves and their differences, which visually shows the size of the signal due to the PMRF issue compared to the lightcurve. In addition, we summed up every 30 short-cadence pixel-level images and computed the difference to the corresponding long-cadence image. The plots also show the median of these differenced images, which will show bright or dark vertical stripes when the target is affected. The amplitude of this image is also helpful in diagnosing the severity of the impact on each target.

NOTE NEPTUNE C3



List of possibly affected C2, C3, and C5 targets: XXXXX.csv
Short- vs long-cadence analysis for all C2, C3, and C5 targets: YYYYYY.txt
Plots of each target:  /dir/dir/


### What should users do if thier target is significantly impacted?

Users whose C3 or C5 targets are significantly impacted by the incorrect calibration are recommended to use the previous processing (Data Release 10) of C3 and C5, available at MAST as individual FITS files[in this directory for C3](https://archive.stsci.edu/missions/k2/target_pixel_files/old_release_bundles/c3/c3_old_release_files/) and [in this directory](https://archive.stsci.edu/missions/k2/target_pixel_files/old_release_bundles/c5/c5_old_release_files/) for C5. C2

NOTE PREV C2 PROC ALSO AFFECTED, SO NO NON-AFFECTED FILES AVAILBLBE FOR C2.

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

<!---The mission is currently exploring possible options to produce correct short-cadence TPFs for affected C2 targets. --->

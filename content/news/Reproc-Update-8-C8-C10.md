Title: K2 Campaigns 8 and 10 reprocessed
Date: 2020-01-29 18:00
Author: Jeff Coughlin

Almost two years ago [we announced](k2-uniform-global-reprocessing-underway.html) that we were undertaking an effort to reprocess campaigns 0&ndash;14 using the same version of the Kepler/K2 pipeline used for C15 and subsequent campaigns. This version introduced several new features and improvements, such as more sophisticated pixel calibration, better identification of spacecraft pointing, improved cosmic ray correction, and production of short-cadence lightcurves, along with several other minor improvements. Please see the [associated news post](k2-uniform-global-reprocessing-underway.html) for details on each feature.

Reprocessed data and release notes from campaigns 8 and 10 are now available; 0&ndash;7, 11 and 13 were made available previously (see processing status figures below). The newest data are available via the usual [K2 data download interfaces at the MAST archive](https://archive.stsci.edu/k2/); the older data has been kept available via the [MAST browser interface](https://archive.stsci.edu/missions/k2/) (e.g., [here](https://archive.stsci.edu/missions/k2/target_pixel_files/old_release_bundles/) for tarballs of the old target pixel files (TPFs) and [here](https://archive.stsci.edu/missions/k2/lightcurves/old_release_tarfiles/) for tarballs of the old lightcurve files, if previously produced). The data release notes have been updated for each reprocessed campaign, available at the nominal [K2 Data Release Notes page](k2-data-release-notes.html); links to the old version of the release notes are also provided for posterity.

**As always, users are highly encouraged to read the updated [C8 Data Release Notes](k2-data-release-notes.html#k2-campaign-8) and [C10 Data Release Notes](k2-data-release-notes.html#k2-campaign-10).**  

Some notable changes with the C8 and C10 reprocessings include:

* Overall improved pixel-level calibration for both campaigns, especially for channels affected by FGS crosstalk.
* Improved spacecraft pointing outlier detection for both campaigns.
* Production of short-cadence lightcurves (63 C8 targets and 138 C10 targets), which previously did not exist.
* Use of the momentum dump flag (QUALITY bit #6, decimal value = 32) to discard cadences with poor data as a result of significant spacecraft motion.
* A worsening of smear calibration for channel 42 in C8 (the channel containing the Uranus superstamp).


The reprocessing priority of the remaining campaigns is C12, C14, C9.

<br>

Questions/Comments?  Please e-mail [Jeff Coughlin](mailto:jeffrey.l.coughlin@nasa.gov) or [the Kepler/K2 helpdesk](https://keplerscience.arc.nasa.gov/helpdesk.html) at <keplergo@mail.arc.nasa.gov>.

<br>

<div class="thumbnail" style="width: 90%; display: inline-block;">
<div class="caption">
<i>The status of major processing features for each campaign as of January 29, 2020. Check marks indicate that the feature is present in the currently available data for that campaign. Blue check marks are features/improvements added a result of the global uniform reprocessing effort.</i>
</div>
<img style="text-align: center" src="images/news/reproc-status-8-major.png" width="100%" align="center"  class="img-responsive">
</div>

<div class="thumbnail" style="width: 90%; display: inline-block;">
<div class="caption">
<i>The status of minor processing features for each campaign  as of January 29, 2020. Check marks indicate that the feature is present in the currently available data for that campaign. Blue check marks are features/improvements added a result of the global uniform reprocessing effort.</i>
</div>
<img style="text-align: center" src="images/news/reproc-status-8-minor.png" width="100%" align="center"  class="img-responsive">
</div>

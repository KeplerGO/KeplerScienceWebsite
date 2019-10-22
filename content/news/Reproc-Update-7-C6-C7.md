Title: K2 Campaigns 6 and 7 reprocessed
Date: 2019-10-22 11:00
Author: Jeff Coughlin

A year ago [we announced](k2-uniform-global-reprocessing-underway.html) that we were undertaking an effort to reprocess campaigns 0&ndash;14 using the same version of the Kepler/K2 pipeline used for C15 and subsequent campaigns. This version introduced several new features and improvements, such as more sophisticated pixel calibration, better identification of spacecraft pointing, improved cosmic ray correction, and production of short-cadence lightcurves, along with several other minor improvements. Please see the [associated news post](k2-uniform-global-reprocessing-underway.html) for details on each feature.

Reprocessed data and release notes from campaigns 6 and 7 are now available; 0&ndash;5, 11 and 13 were made available previously (see processing status figures below). The newest data are available via the usual [K2 data download interfaces at the MAST archive](https://archive.stsci.edu/k2/); the older data has been kept available via the [MAST browser interface](https://archive.stsci.edu/missions/k2/) (e.g., [here](https://archive.stsci.edu/missions/k2/target_pixel_files/old_release_bundles/) for tarballs of the old target pixel files (TPFs) and [here](https://archive.stsci.edu/missions/k2/lightcurves/old_release_tarfiles/) for tarballs of the old lightcurve files, if previously produced). The data release notes have been updated for each reprocessed campaign, available at the nominal [K2 Data Release Notes page](k2-data-release-notes.html); links to the old version of the release notes are also provided for posterity.

**As always, users are highly encouraged to read the updated [C6 Data Release Notes](k2-data-release-notes.html#k2-campaign-6) and [C7 Data Release Notes](k2-data-release-notes.html#k2-campaign-7).**  

Some notable improvements with the C6 and C7 reprocessings include:

* Improved pixel-level calibration for both campaigns, especially for channels affected by FGS crosstalk.
* Improved spacecraft pointing outlier detection for both campaigns.
* Significantly improved PDC (PDCSAP_FLUX) detrending for C7 as a result of better spacecraft pointing outlier detection.
* Production of short-cadence lightcurves (84 C6 targets and 72 C7 targets), which previously did not exist.
    - See the [C6 Data Release Notes](k2-data-release-notes.html#k2-campaign-6) for an issue with missing short-cadence PDC (PDCSAP_FLUX) data.
* Improved smear correction due to higher fidelity detection of cosmic rays, especially in C7.


The reprocessing priority of the remaining campaigns is C8, C10, C12, C14, C9.

<br>

Questions/Comments?  Please e-mail [Jeff Coughlin](mailto:jeffrey.l.coughlin@nasa.gov) or [the Kepler/K2 helpdesk](https://keplerscience.arc.nasa.gov/helpdesk.html) at <keplergo@mail.arc.nasa.gov>.

<br>

<div class="thumbnail" style="width: 90%; display: inline-block;">
<div class="caption">
<i>The status of major processing features for each campaign as of October 22, 2019. Check marks indicate that the feature is present in the currently available data for that campaign. Blue check marks are features/improvements added a result of the global uniform reprocessing effort.</i>
</div>
<img style="text-align: center" src="images/news/reproc-status-7-major.png" width="100%" align="center"  class="img-responsive">
</div>

<div class="thumbnail" style="width: 90%; display: inline-block;">
<div class="caption">
<i>The status of minor processing features for each campaign  as of October 22, 2019. Check marks indicate that the feature is present in the currently available data for that campaign. Blue check marks are features/improvements added a result of the global uniform reprocessing effort.</i>
</div>
<img style="text-align: center" src="images/news/reproc-status-7-minor.png" width="100%" align="center"  class="img-responsive">
</div>

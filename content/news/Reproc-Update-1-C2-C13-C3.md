Title: K2 Campaigns 2, 3, and 13 Reprocessed
Date: 2018-09-28 10:00
Author: Jeff Coughlin

A few months ago we announced that we were undertaking an effort to reprocess campaigns 0&ndash;14 using the same version of the pipeline used for campaign 15 and subsequent campaigns. This version introduced several new features, such as more sophisticated pixel calibration, better identification of spacecraft pointing, improved cosmic ray correction, and production of short-cadence lightcurves, along with several other minor improvements. Please see the [associated news post](k2-uniform-global-reprocessing-underway.html) for details on each feature.

Reprocessed data and release notes from campaigns 2, 3, and 13 are now available. The newest data are available via the usual [K2 data download interfaces at the MAST archive](https://archive.stsci.edu/k2/); the older data has been kept available via the [MAST browser interface](https://archive.stsci.edu/missions/k2/) (e.g., [here](https://archive.stsci.edu/missions/k2/target_pixel_files/old_release_bundles/) for tarballs of the old TPF files and [here](https://archive.stsci.edu/missions/k2/lightcurves/old_release_tarfiles/) for tarballs of the old lightcurves files, if previously produced). The data release notes have been updated for each reprocessed campaign, available at the nominal [K2 Data Release Notes page](k2-data-release-notes.html); links to the old version of the release notes are also provided for posterity.

In the two figures below, we show the current status of major and minor features/improvements as a result of the reprocessing effort. While all these apply, further below we highlight a few examples of these improvements and new features from C2, C3, and C13 that are likely to be of interest to users:

<div class="thumbnail" style="width: 90%; display: inline-block;">
<div class="caption">
<i>The status of major pipeline features for each campaign as of September 28, 2018. Blue check marks are features added a result of the global uniform reprocessing effort.</i>
</div>
<img style="text-align: center" src="images/news/reproc-status-1-major.png" width="100%" align="center"  class="img-responsive">
</div>

<div class="thumbnail" style="width: 90%; display: inline-block;">
<div class="caption">
<i>The status of minor pipeline features for each campaign  as of September 28, 2018. Blue check marks are features added a result of the global uniform reprocessing effort.</i>
</div>
<img style="text-align: center" src="images/news/reproc-status-1-minor.png" width="100%" align="center"  class="img-responsive">
</div>

<br>


- In the original C2 processing, lightcurves were not produced, and TPFs were "Type-1", which had poor WCS information and other limitations compared to the "Type-2" TPFs that were produced in later campaigns. (For details on the difference between Type-1 and Type-2 TPFs, see [section 2.4 15 of the K2 Handbook](https://archive.stsci.edu/k2/manuals/k2_handbook.pdf#page=15)). As a result of reprocessing, Type-2 TPFs, lightcurves (both long- and short-cadence), and cotrending basis vectors (CBVs) are now available for C2.

- One of the major improvements from the global reprocessing is the use of an algorithm called "Dynablack", which is essentially a more sophisticated way to perform the CCD pixel-level calibration that accounts for time-varying, instrument-induced artifacts in the pixel data. One benefit of Dynablack is that is is able to correct crosstalk from the fine guidance sensors, resulting in much better background correction for certain channels. As shown below, for channel 41 in the original C2 processing, regular calibration resulted in varying background level as a function of position on the CCD. In the reprocessing, the use of Dynablack resulted in a significantly better correction and uniform background levels.

<div class="thumbnail" style="width: 80%; display: inline-block;">
<div class="caption">
<i>The residuals in the background correction fit as a function of row position on the CCD. <b>Left:</b> The original C2 processing. <b>Right:</b>The same figure from the C2 reprocessing. (Note the different y-axis scale between the two figures.)</i>
</div>
<img style="text-align: center" src="images/news/c2-dynablack-correction.png" width="100%" align="center"  class="img-responsive">
</div>

<br>

- While no work was able to be done to adapt the detrending method used for Kepler short-cadence lightcurves to those from K2, and thus on a whole are expected to be of varying quality, we are producing short-cadence lightcurves with the expectation that some objects will be of high quality and/or spurn more detailed investigation. Below we show the short-cadence PDC lightcurve for EPIC 206003187, an RR Lyrae-type variable observed in C3. While there are still residual systematics near thruster-firing events, simply removing those points near thruster firing events results in a well-detrended phased light curve with a clearly visible [Blazhko effect](https://en.wikipedia.org/wiki/Blazhko_effect).

<div class="thumbnail" style="width: 56%; display: inline-block;">
<div class="caption">
<i>A 10-day segment of the RR Lyrae-type variable EPIC 206003187, observed in C3, with data near thruster firings shown in red. <span style="float:right;"><small>Credit: Dr. Ken Mighell</small></span> </i>
</div>
<img src="images/news/C3R-RRLyr-EPIC0206003187-Unphased-Uncleaned.png" width="100%" align="left"  class="img-responsive">
</div>
<div class="thumbnail" style="width: 42%;display: inline-block;">
<div class="caption">
<i>The phased, short-cadence PDC lightcurve of EPIC 206003187 after removing cadences near thruster firings. <span style="float:right;"><small>Credit: Dr. Ken Mighell</small></span> </i>
</div>
<img src="images/news/C3R-RRLyr-EPIC0206003187-Phased-Cleaned.png" width="100%" align="left"  class="img-responsive">
</div>

<br>

- In the original processing of C13, the presence of the first magnitude star Aldebaran on channel 73 led to a time-varying error in the smear correction for channel 74, which shares the same physical CCD. As a result every target on channel 74 had time-varying background levels, and the resulting lightcurves showed a "chattering" effect of significant point-to-point changes in flux (see [the old C13 data release notes](http://localhost:8000/archived-k2-data-release-notes.html#k2-campaign-13-archived) for details). Below we show an example target from channel 74, EPIC 246810163, a hot star with apparent astrophysical variability. As can be seen on the left, the "chattering" effect is visible in both the background flux and resulting lightcurve for this target. When reprocessing, an update to the smear correction routine was able to significantly better account for the flux bleed from Aldebaran, and thus result in a nominal, smoothly time-varying background flux and thus significantly better lightcurve.

<div class="thumbnail" style="width: 80%;display: inline-block;">
<div class="caption">
<i><b>Left column:</b> Data for target EPIC 246810163 from the original C13 processing. <b>Right column:</b> Data for target EPIC 246810163 from the C13 reprocessing. <b>Top row</b>: The background flux level over the entire timespan of C13. <b>Bottom row</b>: The long-cadence PDC lightcurve of EPIC 246810163 over a time-span of ~10 days. <span style="float:right;"><small>Credit: Dr. Ken Mighell</small></span> </i>
</div>
<img align="center" src="images/news/c13-chattering-fixed.png" width="100%" align="middle"  class="img-responsive">
</div>

<br>

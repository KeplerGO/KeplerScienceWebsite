Title: K2 Uniform Global Reprocessing Underway
Date: 2018-04-11 12:00
Author: Jeff Coughlin


The K2 mission has begun a global reprocessing of the C0–C14 K2 data with an updated, uniform version of the Kepler/K2 pipeline — C15 and later campaigns will be processed with the same pipeline version. This effort should enhance the scientific return of the K2 mission by providing users with a high quality, uniformly processed and documented K2 dataset. This work will be performed on a best-effort basis as long as mission resources are available to do so. The campaigns have been prioritized by enhanced scientific return as a result of reprocessing. Note that processing of new campaigns (e.g., C16, C17, etc.) will always be prioritized over reprocessing of older campaigns.

**Priority of Older Campaigns**: C2, C13, C0, C11, C1, C3, C4, C5, C6, C7, C8, C9, C10, C12, C14.

All data will be delivered to the [K2 data archive at MAST](http://archive.stsci.edu/k2) as it is reprocessed, where the reprocessed data for a given campaign will replace the older processing when searching for data via [MAST's K2 Data Search and Retrieval page](https://archive.stsci.edu/k2/data_search/search.php) and any other interfaces. The older data will remain available to users via a subdirectory in the [MAST browser interface](https://archive.stsci.edu/missions/k2/).


## Changes

### Significant Changes

The changes listed below affect all of the data at a significant level.

#### Dynablack

A new feature of the Kepler pipeline that was implemented for K2 processing, starting with C15, is the use of Dynamic Black Correction, or "Dynablack", which is essentially a more sophisticated algorithm to perform the CCD pixel-level calibration that accounts for time varying, instrument-induced artifacts when calibrating the data.

Dynablack uses the full-frame images and collateral pixels to provide two main benefits compared to traditional pixel calibration:

* Correct thermally dependent fine guidance sensor crosstalk pixels.

* Identify rolling-band artifacts (see [§6.7 of the Instrument Handbook](https://archive.stsci.edu/kepler/manuals/KSCI-19033-002.pdf#page=75)) with flags in the target pixel files.

For the latter case, users can utilize the new RB_LEVEL flags in the FITS files. See [§A.1.1 of the Kepler Data Release 25 Notes](https://archive.stsci.edu/kepler/release_notes/release_notes25/KSCI-19065-002DRN25.pdf#page=11) and [§2.3.2 of the Kepler Archive Manual](https://archive.stsci.edu/kepler/manuals/archive_manual.pdf#page=24) for information on how to interpret and utilize the RB_LEVEL flags.


#### Pointing Flags

As mentioned in the C14 release notes, a change in the on-board fine point fault logging threshold
results in additional cadences being flagged as "Spacecraft is not in fine point"
(QUALITY flag bit #16, decimal=32768). Starting with C15, the pipeline is now ignoring the
spacecraft not-in-fine-point flag and using the "Spacecraft is in coarse point" flag (QUALITY
flag bit #3, decimal=4). This flag is set by the project based on the measured pointing error exceeding
1.5 pixels for 4 or more continuous cadences, or exceeding 2.5 pixels for a single cadence. The pipeline will treat
these "coarse-point" cadences as "not-in-fine-point" cadences were treated in previous campaigns
up to and including C14, i.e., there will be calibrated pixels, but light curve data will be gapped
for the flagged cadences. The project recommends that starting with C15, users look to
QUALITY flag bit #3 as an indicator of poor spacecraft pointing.

#### Cosmic-Ray Threshold


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




#### Short-Cadence

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
<i>Figure C15-SC-Example-2: The AM CVn type Binary HP Lip / EPIC 250105131</i><br>
<a href="images/release-notes/c15/epic_250105131_zoom1.png">
<img src="images/release-notes/c15/epic_250105131_zoom1.png" class="img-responsive" alt="The AM CVn type Binary HP Lip / EPIC 250105131.">
</a>
</div>
</div>



</div>
 <i>
 The status of major changes planned for the final uniform processing.
 <br>
 <font color="red">Red indicates the final processing setting is *not* yet implemented in currently available data.</font>
 &ensp;
 <font color="blue">Blue indicates the final processing setting has been implemented in currently available data.</font></span>
 </i>
 <a href="images/news/K2-Proc-Status-Major.png"><img class="img-responsive" style="padding:0.5em;" src="images/news/K2-Proc-Status-Major.png" id="k2-proc-status-major" alt="Status of K2 Processing Major Issues">
</a>
</div>


### Minor Changes

The changes listed below affect only portions of the K2 data and/or at a minor level.

#### C13 Aldeberan


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


#### Scrambled uncertatinties

#### Momentum dump flag

#### LDE parity error

#### Exported Targets

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

</div>
 <i>
 The status of major changes planned for the final uniform processing.
 <br>
 <font color="red">Red indicates the final processing setting is *not* yet implemented in currently available data.</font>
 &ensp;
 <font color="blue">Blue indicates the final processing setting has been implemented in currently available data.</font></span>
 </i>
 <a href="images/news/K2-Proc-Status-Minor.png"><img class="img-responsive" style="padding:0.5em;" src="images/news/K2-Proc-Status-Minor.png" id="k2-proc-status-major" alt="Status of K2 Processing Major Issues">
</a>
</div>

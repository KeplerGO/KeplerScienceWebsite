Title: K2 Archived Data Release Notes
Save_as: archived-k2-data-release-notes.html

[TOC]

This page contains *OUT-OF-DATE*, archived data release notes for past pipeline processings. Campaigns seen here have been processed with the final version of the K2 pipeline (<a href="k2-uniform-global-reprocessing-underway.html">see news post here</a>) and new, up-to-date release notes corresponding to the newest data are available <a href="k2-data-release-notes.html#k2-campaign-2">at the nominal data release note webpage</a>.

The notes below are kept here in case users find a need to use the old, out-of-date processed data, which is still accessible at MAST in these locations for each file type:
<ul>
<li>Target Pixel Files: <a href="http://archive.stsci.edu/missions/k2/target_pixel_files/old_release_bundles/">http://archive.stsci.edu/missions/k2/target_pixel_files/old_release_bundles/</a>
<li>Lightcurves: <a href="http://archive.stsci.edu/missions/k2/lightcurves/old_release_tarfiles/">http://archive.stsci.edu/missions/k2/lightcurves/old_release_tarfiles/</a>
<li>CBV files: <a href="http://archive.stsci.edu/missions/k2/cbv/old_release_files/">http://archive.stsci.edu/missions/k2/cbv/old_release_files/</a>
<li>FFIs: <a href="http://archive.stsci.edu/missions/k2/ffi/old_release_files/">http://archive.stsci.edu/missions/k2/ffi/old_release_files/</a>
</ul>

<br>


# K2 Campaign 13 (**Archived**)

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


# K2 Campaign 3  (**Archived**)

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


# K2 Campaign 2 (**Archived**)

<h2>At a glance</h2>

<div class="row">
<div class="col-lg-5">

    <b><i>Pointing</i></b>
    <ul>
        <li>RA: 246.1264 degrees</li>
        <li>Dec: -22.4473 degrees</li>
        <li>Roll: 171.2284 degrees</li>
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

</div>

<div class="col-lg-7">

    <div class="thumbnail">
        <div class="caption">
            <i>Figure: Schematic of Kepler's C2 field-of-view with selected targets shown with purple dots.</i>
        </div>
        <a href="images/campaign_selected/C2_selected.png">
            <img src="images/campaign_selected/C2_selected.png" class="img-responsive" alt="C2 field-of-view with selected targets">
        </a>
    </div>

    <div class="thumbnail">
        <div class="caption">
            <i>Figure: Distribution of the Kepler magnitudes of observed targets in C2.</i>
        </div>
        <a href="images/release-notes/c2/C2_lc_kp.png">
            <img src="images/release-notes/c2/C2_lc_kp.png" class="img-responsive" alt="Distribution of the Kepler magnitudes of observed targets in C2.">
        </a>
    </div>

</div>

</div>

<div class="thumbnail">
    <div class="caption">
        <i>Figure: Full Frame Image Highlights</i>
    </div>
    <a href="images/release-notes/c2/K2-new-litho_2015.png">
        <img src="images/release-notes/c2/K2-new-litho_2015.png" class="img-responsive" alt="Campaign 2 Full Frame Image Highlights.">
    </a>
</div>


<h2>Features and events</h2>

<br>
***Solar Activity***

During C2 Kepler experienced two energetic particle events of note, likely caused by solar activity. Both events affected all channels as can be seen in the dark current metric plot for the first 26 days of C2 (see below). The first was a broad peak lasting approximately from cadence 95924 -- 96335 (01-Sep-2014 11:51:30 Z [MJD: 56901.4941] to 09-Sep-2014 21:24:55 Z [MJD: 56909.8923]). The second was a stronger more-peaked event lasting approximately from cadence 96357 -- 96551 (10-Sep-2014 17:01:54 Z [56910.7096] to 14-Sep-2014 07:20:35 Z [56914.30596]). At the peak of the 10-Sep-2014 event the average dark current increased by a factor of ~7 over the quiescent level. The GOES x-ray flux plot for this time shows an increased x-ray flux at Earth, though we don't have an independent measure of the exact timing and magnitude at the location of Kepler. The impact to the data will be in the form of increased background level, and increased photometric noise. The impact will be largest for faint targets.

<div class="thumbnail" style="width: 68%;">
    <div class="caption">
        <i>Figure: Dark Current Metric plotted against time.</i>
    </div>
    <a href="images/release-notes/c2/c2_dark_current_metric.png">
        <img src="images/release-notes/c2/c2_dark_current_metric.png" class="img-responsive" alt="Dark Current Metric plotted against time.">
    </a>
</div>


<br>
***Mars***

Mars passed across the field of view between October 1 and October 23. See the figure below for a prediction of where Mars is on the focal plane during Campaign 2. Mars is a bright object which will saturate the CCD. Both its image and its reflection will likely contaminate nearby stars.

<div class="thumbnail" style="width: 68%;">
    <div class="caption">
        <i>Figure: Schematic of Kepler's C2 field of view (outlined in blue) with the positions of Mars shown as small red squares.</i>
    </div>
    <a href="images/release-notes/c2/f2-fov.png">
        <img src="images/release-notes/c2/f2-fov.png" class="img-responsive" alt="Schematic of Kepler's C2 field of view.">
    </a>
</div>


<br>
***LDE Flags***

During the latter half of C2 we experienced a large number of parity errors coming from the photometer's local detector electronics (LDE). These LDE parity errors can occur when a very bright star saturates and spills charge into the CCD serial readout register, causing an overflow at the input to the analog-to-digital converter. While these errors were rare in Kepler, the very bright stars, or solar system planets, on the focal plane in K2 can cause frequent parity errors. For example, stars on channels 67 and 75 were the source of many of the parity errors during C2. These errors do not affect the quality of data from pixels on the active focal plane.

The LDE parity error triggers a flag (bit 15, decimal=16384) in the QUALITY column of the target pixel files. This flag is set for the majority of cadences in the second half of the campaign.

<br>
***Attitude Tweak***

The pointing of the spacecraft was adjusted by approximately 10" on 2014-Aug-25, during cadence 95546, in order to ensure that the observed targets were centered in their masks. This event is flagged in the QUALITY column of the target pixel files with bit 1 (decimal=1). The data collected before the tweak may fall close to the edge of the collected mask and some of the object's flux may have been lost. Use these cadences with caution.
Note, in Data Release 4, because of an operator error, the tweak is marked on the previous cadence, 95545.

<br>
***Two Globular Clusters***

The clusters M4 and M80 were observed in C2 by collecting all the pixels in 50x50 pixel masks. For M4, 16 of these custom apertures were collected and for M80, 4 were collected. The data files for M4 range from 200004370 -- 200004385. The data files for M80 range from 200004386 -- 200004389. The target pixel files may be found by using the Object Type field on the <a href="http://archive.stsci.edu/k2/data_search/search.php">MAST K2 data search</a> page.

<br>
***Two Solar System Objects***

Comet C/2013 A1 (Siding Spring) was observed by obtaining 2583, 25x1 pixel, masks across module.outputs 2.3, 4.2, 4.3 and 4.4. These apertures were given custom aperture numbers ranging from 200001787 -- 200004369. This target was observed as part of the Guest Observer Programs GO2030 (PI:Kelley) and GO2046 (PI:Lisse).

The Trans-Neptunian Object (268361) 2007 JJ43 was observed with 661, 11x1 or 13x1 pixel, masks and given custom aperture numbers ranging from 200001126 -- 200001786. This target was observed as part of Guest Observer Program GO2066 (PI:Schwamb).

These data sets can be found at the <a href="http://archive.stsci.edu/k2/data_search/search.php">MAST</a> by entering the Investigation ID on the search form. The Investigation ID matches the GO Program number that requested the observations.

<div class="thumbnail" style="width: 68%;">
    <div class="caption">
        <i>Figure: The path (shown in blue) of C/2013 A1 (Siding Spring) runs along modules 2 and 4 during C2.</i>
    </div>
    <a href="images/release-notes/c2/comet-path.png">
        <img src="images/release-notes/c2/comet-path.png" class="img-responsive" alt="Path of comet Siding Spring.">
    </a>
</div>

<div class="thumbnail" style="width: 68%;">
    <div class="caption">
        <i>Figure: The masks selected for mod.out 17.3 are shown in green. Those selected to capture the TNO 2007 JJ43 are shown as a green arc in the lower right-hand corner of this figure.</i>
    </div>
    <a href="images/release-notes/c2/jj43_path.png">
        <img src="images/release-notes/c2/jj43_path.png" class="img-responsive" alt="Masks selected to capture TNO 2007 JJ43.">
    </a>
</div>

<br>
***EPIC Catalog Assignment***

For C2, a number of targets were proposed without <a href="https://archive.stsci.edu/k2/epic.pdf">EPIC</a> ID numbers. If a target was observed, it was either 1) given an EPIC ID number from the regular catalog if that target matched a target in the catalog, or 2) assigned a new EPIC ID. We created EPIC ID numbers for 69 targets, ranging from 210282492 -- 210282560.

<h2>Release History</h2>

The following is the data release history for this campaign. Follow the link for information about some of the features of the software used to reduce and export these data. There will be a new entry each time the data is released by the mission.

* <a href="k2-pipeline-release-notes.html#data-release-4">Data Release 4</a>

<hr>

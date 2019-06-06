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


# K2 Campaign 11 (**Archived**)

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
<i>Figure C11-Mag: Distribution of the Kepler magnitudes of observed LC targets. All targets are chosen by guest observers. The distribution is due to the <a href="k2-approved-programs.html#campaign-11">GO  programs</a> that were selected.</i>
</div>
<a href="images/release-notes/c10/c10LcMagDistribution.png">
<img src="images/release-notes/c10/c10LcMagDistribution.png" class="img-responsive" alt="Distribution of the Kepler magnitudes of observed C11 LC targets.">
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


# K2 Campaign 5 (**Archived**)

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
            <i>Figure: Distribution of the Kepler magnitudes of observed LC targets in C5. All targets are chosen by Guest Observers. The bimodality is due to how the largest <a href="k2-approved-programs.html#campaign-5">Guest Observer programs</a> were selected.</i>
        </div>
        <a href="images/release-notes/c5/C5LcMagDistribution.png">
            <img src="images/release-notes/c5/C5LcMagDistribution.png" class="img-responsive" alt="Distribution of the Kepler magnitudes of observed LC targets in C5.">
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

Neptune moved across the field of view during C3 and K2 observed it in both long and short cadence. Short cadence data were obtained approximately 20 days either side of the stationary point of Neptune. See this time lapse <a href="https://www.youtube.com/watch?v=Tw-q3uM_5_0">movie</a> created by Jason Rowe that clearly shows Neptune and its moons, Triton and Nereid. The custom aperture numbers associated with Neptune are 200004468--200004923. These observations were taken as part of Guest Observer Programs GO3060 (PI:Rowe) and GO3057 (PI:Gaulme).

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




# K2 Campaign 1 (**Archived**)

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
from 20100000001 to 202059065.

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



# K2 Campaign 0 (**Archived**)

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

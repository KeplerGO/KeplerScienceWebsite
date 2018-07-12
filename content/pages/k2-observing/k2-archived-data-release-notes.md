Title: K2 Archived Data Release Notes
Save_as: ./archived-k2-data-release-notes.html

[TOC]

This page contains *OUT-OF-DATE*, archived data release notes for past pipeline processings. Campaigns seen here have been processed with the final version of the K2 pipeline (<a href="k2-uniform-global-reprocessing-underway.html">see news post here</a>) and new, up-to-date release notes corresponding to the newest data are available <a href="k2-data-release-notes.html#k2-campaign-2">at the nominal data release note webpage</a>.

The notes below are kept here in case users find a need to use the old, out-of-date processed data, which is still accessible at MAST here: LOCATION TBD


# K2 Campaign 2

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

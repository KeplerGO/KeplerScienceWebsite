Title: K2 Pipeline Release Notes
Save_as: k2-pipeline-release-notes.html

[TOC]

Below are notes on the features of the software used to process the K2 data. Any changes to the pipeline that directly impact the data quality or format are listed for each data release. Any change impacts all subsequent data releases unless stated otherwise.

For more information about the Kepler pipeline see the Kepler manuals: <a href="http://archive.stsci.edu/kepler/manuals/KSCI-19081-001_Data_Processing_Handbook.pdf">Data Processing Handbook</a> and <a href="http://archive.stsci.edu/kepler/manuals/archive_manual.pdf">Archive Manual.</a>

Information about each specific campaign can be found in the links associated with each data release.

### Data Release 21

* March 2018
* SOC 9.3
* Campaigns: [C15](k2-data-release-notes.html#k2-campaign-15)

This is the first delivery of C15. There have been some pipeline changes put in place for this
delivery that are designed to support the uniform reprocessing of all K2 campaigns, which will be explained shortly
via a news item. The
changes include activating the dynamic black correction algorithm used during Kepler data processing,
producing short cadence light curves, correcting bugs in the processing.
For additional information about the content of this delivery see the previous Release Notes
below.

Pipeline changes put in place for Data Release 21:

1. Dynablack

2. Short Cadence light curves

3. FFI interpolation bug fix

4. Use of coarse point flag for data gapping

<hr>

### Data Release 20

* December 2017
* SOC 9.3
* Campaigns: [C14](k2-data-release-notes.html#k2-campaign-14)

This is the first delivery of C14. No features of the pipeline or data files have changed.
For further information about the content of this delivery see the previous Release Notes
below.

<hr>

### Data Release 19

* August 2017
* SOC 9.3
* Campaigns: [C13](k2-data-release-notes.html#k2-campaign-13)

This is the first delivery of C13. No features of the pipeline or data files have changed.
For further information about the content of this delivery see the previous Release Notes
below.

<hr>

### Data Release 18

* August 2017
* SOC 9.3
* Campaigns: [C12](k2-data-release-notes.html#k2-campaign-12)

This is the first delivery of C12. No features of the pipeline or data files have changed.
For further information about the content of this delivery see the previous Release Notes
below.

<hr>

### Data Release 17
* June 2017
* SOC 9.3
* Campaigns: [C11](k2-data-release-notes.html#k2-campaign-11)

This is the first delivery of C11. The release consists of Type-1 target pixel
files and Type-2 light curve files for both C11a (23 days) and C11b (48 days).
There were two changes of note in the processing pipeline for C11:

1. The collateral
cosmic ray detection threshold used in pixel-level calibration was increased
from 4.0 to 7.0 sigma in order to minimize false detections triggered by K2's roll motion.
Based on analysis of reprocessed data from C0, the project realized that
false cosmic ray detections resulted in poor smear correction for individual columns,
creating positive-going stripes in the image (see
[C8: Intermittent Streaks](k2-data-release-notes.html#k2-campaign-8)
section for an example). The increased threshold has greatly reduced this
processing artifact.

2. Pipeline testing uncovered an error in the assignment of the collateral smear
uncertainty to the appropriate CCD column. The error has been corrected with this
pipeline release. This error meant that the incorrect smear
uncertainty was added in quadrature with the other noise terms, resulting in erroneous
target pixel and light curve flux uncertainties. Because the pixel uncertainties are used
in determining the photometric aperture, the aperture selection for some targets was
affected by this bug. For bright targets the effect is generally small. The project is
working on an accounting of the impact of this bug on existing K2 data.

No other features of the data processing have changed.  See below for previous
updates to the K2 pipeline.

### Data Release 16
* pending
* SOC 9.3
* Campaigns: C0

The updated release of C0 is pending.

### Data Release 15
* December 2016
* SOC 9.3
* Campaigns: [C10](k2-data-release-notes.html#k2-campaign-10)

This is the first delivery of C10. The release consists of Type-1 target pixel
files for the first six days of the campaign (C10a) and Type-2 TPFs and light curve
files for the remainder of the campaign (C10b). No light curve files were
generated for C10a.
See the [C9 data release notes](k2-data-release-notes.html#k2-campaign-9)
for a description of the content of Type-1 versus Type-2 (nominal) TPFs.  No other features of the data processing have changed.  See below for previous updates to the K2 pipeline.

### Data Release 14
* December 2016
* SOC 9.3
* Campaigns: [C1](k2-data-release-notes.html#k2-campaign-1)

This is a re-delivery of C1, including the first delivery of C1 long cadence light curve files.
No other features of the the data processing have changed. See below for previous updates to the K2 pipeline.

### Data Release 13
* pending
* SOC 9.3
* Campaigns: C2

The updated release of C2 is pending.

### Data Release 12
* September 2016
* SOC 9.3
* Campaigns: [C9](k2-data-release-notes.html#k2-campaign-9)

This is the first delivery of C9. The release consists of Type-1 target pixel files and supporting calibration files. No light curve files were generated for C9. See the [C9 data release notes](k2-data-release-notes.html#k2-campaign-9) for a description of the the content of Type-1 versus Type-2 (nominal) TPFs.  No other features of the data processing have changed.  See below for previous updates to the K2 pipeline.

### Data Release 11
* July 2016
* SOC 9.3
* Campaigns: [C8](k2-data-release-notes.html#k2-campaign-8)

This is the first delivery of C8. No features of the files or the data processing have changed.  See below for previous updates to the K2 pipeline.

### Data Release 10
* July 2016
* SOC 9.3
* Campaigns: [C3, C4, C5](k2-data-release-notes.html#k2-campaign-3)

Data Release 10 includes the reprocessing of the short cadence data for Campaigns 3, 4, and 5. This reprocessing corrects the short cadence collateral bug described in the <a href="http://archive.stsci.edu/kepler/KSCI-19080-002.pdf">Global Erratum for Kepler Q0-Q17 & K2 C0-C5 Short-Cadence Data, KSCI-19080</a>. This release replaces short cadence data previously delivered to the archive in Data Releases 5, 6, and 7. Specific targets known to have their calibration improved by Data Release 10 are identifed in the <a href="http://archive.stsci.edu/missions/k2/catalogs/K2_scrambled_short_cadence_collateral_target_list.csv">list of affected targets at the MAST</a>. No other features of the files or the data processing have changed. The long cadence data are unchanged.

### Data Release 9
* April 2016
* SOC 9.3
* Campaigns: [C7](k2-data-release-notes.html#k2-campaign-9)

This is the first delivery of C7. No features of the files or the data processing have changed.  See below for previous updates to the K2 pipeline.


### Data Release 8
* February 2016
* SOC 9.3
* Campaigns: [C6](k2-data-release-notes.html#k2-campaign-8)

This is the first delivery of C6. All changes to the pipeline for this data release are reported below.

***CAL inputs***

One change was made to the smear pixel mapping information used by CAL. This fixed the long-standing problem reported [in the Erratum below](#sc-smear-erratum) where the smear values were being applied to the wrong columns in short cadence data.  

For further information about the processing and content of this delivery, see the previous release notes.


<hr>
### SC Smear Erratum

<div class="well">

<h2> Incorrect SC Smear </h2>
<p> Reported in February 2016, the Erratum applies to short cadence data in K2 data releases 1-7.</p>

<p>An accounting error has scrambled much of the short cadence collateral smear data used to correct for the effects of Kepler’s shutterless readout.  This error has been present since launch and affects approximately half of all short cadence targets observed by Kepler and K2 to date.  The resulting calibration errors are present in both the short cadence target pixels and the short cadence light curves for Kepler Data Releases 1-24 and K2 Data Releases 1-7. This error does not affect long cadence data. </p>

<p>Since it will take some time to correct this error and reprocess all Kepler and K2 data, a <a href="http://archive.stsci.edu/missions/k2/catalogs/K2_scrambled_short_cadence_collateral_target_list.csv">list of affected targets is provided</a>.  Even though the affected targets are readily identified, the science impact for any particular target may be difficult to assess.  Since the smear signal is often small compared to the target signal, the effect is negligible for many targets. However, the smear signal is scene-dependent, so time-varying signals can be introduced into any target by the other stars falling on the same CCD column.  </p>

<p>Some tips on how to assess the severity of the calibration error and more details on how this problem occurred are provided in the <a href="http://archive.stsci.edu/kepler/KSCI-19080-002.pdf">Erratum Document KSCI-19080</a>. </p>

</div>

<hr>
### Data Release 7

* November 2015
* SOC 9.3
* Campaigns: [C5](k2-data-release-notes.html#k2-campaign-5)

This is the first delivery of C5.

One procedural change was made to how the data were processed, resulting in improvements to how the optimal apertures are selected. In C4 it was discovered that the optimal apertures selected by the pipeline were too small. Starting with Data Release 7 the apertures are no longer selected by including information about the motion polynomials and this change in process has proven to select larger and better optimal apertures.  </p>       

For further information about the content of this delivery see the previous Release Notes.

<hr>

### Data Release 6

* September 2015
* SOC 9.3
* Campaigns: [C4](k2-data-release-notes.html#k2-campaign-4)

This is the first delivery of C4. No features of the files have changed. For further information about the content of this delivery see the previous Release Notes.

<hr>

### Data Release 5

* July 2015
* SOC 9.3
* Campaigns: [C3](k2-data-release-notes.html#k2-campaign-3)

This is the first delivery of C3. In addition to the FFIs and the target pixel files, the project is delivering long cadence light curves, background pixels and collateral data.</p>

***PA***

The method used to generate optimal apertures was improved for the SOC 9.3 pipeline. It now includes a data driven approach that uses the actual mask scene data to calculate the pixel noise in the SNR calculation. It also optimizes apertures based on CDPP. We are finding a significant improvement in CDPP for many targets.  As with Kepler, the pixels used to create the light curve seen in the SAP_FLUX data column are shown in the APERTURE extension of the exported light curve and target pixel files.  

PA fits motion polynomials (2D polynomial models mapping celestial coordinates to pixel coordinates) to PRF-fitted centroids of bright, well-isolated targets on each channel. We have found the PRF-centroids to be reliable for both Kepler and K2, so the residual errors in the models provide a measure of quality. The median model residual over all targets and cadences across the entire FOV was 0.047 pixels for Kepler Q14 (processed with SOC 9.3) and 0.070 pixels for C3. The relative motion of the star, evaluated for each star and cadence, is available in the POS_CORR columns of the light curve and target pixel files.

***PDC***

The method used to remove systematic trends in the K2 light curves is very similar to that used for Kepler data. However, we note some distinct differences:

<ul class="text">
    <li><p> Generally, 12 basis vectors are used instead of 8. The roll motion results in a very strong “sawtooth” trend in the simple aperture photometry light curves. It has been found that 12 basis vectors effectively remove this strong trend and yet the number of basis vectors is sufficiently small to avoid overfitting.</p></li>
    <li><p> Three corrected light curves are generated: a) a Bayesian MAP fit, b) a Robust Least Squares fit and c) no correction. PDC then selects the fit that results in the best photometric precision. The least squares fit is chosen a majority of the time. However, for more variable targets the MAP prior is used. For exceedingly variable targets and other corner cases, no correction is chosen. For targets with stronger roll sawtooth, the least squares fit is generally better. </p></li>
    <li><p>Photometric precision is measured using a 6 hour CDPP measurement. The roll tweak correction occurs up to every 6 hours (every 12th long cadence). The sawtooth therefore has a periodicity of 6 hours and so a 6 hour transit test signal is ideal for measuring residual sawtooth in the corrected light curves.</p> </li>
</ul>

*** Exporter (AR)***

<ul class="text">
        <li><p>Thruster Firing flags have been added to the QUALITY column.</p>
            <ul class="text"><li><p>Possible Thruster Firing (bit 20) indicates that one sor more thrusters may have fired during the indicated cadence. Because the thruster firings are only reported every 16 seconds, if one occurs near a cadence boundary, which cadence contains the thruster firing is unknown. As a result, this flag is most commonly set in short cadence.</p></li>
                <li><p>Definite Thruster Firing (bit 21) indicates that at least one of the thrusters is known to have fired during that cadence.</p></li>
            </ul>

    <li><p>WCS coordinates, calculated with the Kepler motion polynomials, are available in the FFI headers. </p></li>

    <li><p>The modeled background level has been subtracted from the calibrated pixels available in the target pixel files. The per pixel background that was removed is available in the FLUX_BKG column of the target pixel files. To create non-background subtracted pixels, simply add the FLUX_BKG column to the FLUX column.</p></li>
        <li><p>Motion Polynomials have been calculated per cadence. The mesured motion relative to the location near the middle of the campaign is recorded in the two POS_CORR columns.</p></li>
        <li><p>All Kelper data products are now available, except for SC light curve files. This includes the Target Pixel, Light Curve, FFI, Collateral, Background, Artifact Removal Pixel and Cotrending Basis Vector files.</p></li>
</ul>

<hr>

### Data Release 4
* March 2015
* SOC 9.2
* Campaigns: [C2](k2-data-release-notes.html#k2-campaign-2)

This is the first delivery of C2.  

The algorithm used by the CAL module to propagate the errors on the flux was turned off to expedite processing. Consequently, the reported error for each pixel at each cadence is the minimal error (shot noise plus read noise) as it does not include the associated offset term resulting from the full propagation of errors. See Section 5.1.3 of the [Data Characteristics Handbook (DCH, Christiansen et al. , 2013)](http://archive.stsci.edu/kepler/manuals/Data_Characteristics.pdf) for more details.  

No features of the files have changed. For further information about the content of this delivery see the previous Release Notes.

<hr>

### Data Release 3

* December 2014
* SOC 9.2
* Campaigns: [C1](k2-data-release-notes.html#k2-campaign-1)

This is the first delivery of C1.  </p>

No features of the files have changed. For further information about the content of this delivery see the previous Release Notes.</p>

<hr>

### Data Release 2

* October 2014
* SOC 9.2
* Campaigns: [C0](k2-data-release-notes.html#k2-campaign-0)

This delivery was made to fix two problems found in the target pixel files delivered for Data Release 1.

<ul class="text">
    <li><p>The world coordinate system specified in header of the Target Pixel File is now accurate for the middle cadence of the data to within a pixel.
    </p></li>
    <li><p>All of the pixels collected for a target are now being calibrated and delivered in the FLUX column of the target pixel files.  Previously the FLUX column had a few pixels filled with zeros (or values from an earlier processing of the data) that should have contained calibrated pixels.  
    </p></li>
</ul>

No other features of the files have changed. For further information about the content of this delivery see the previous Release Notes.

<hr>

### Data Release 1

* September 2014
* SOC 9.2
* Campaigns: [C0](k2-data-release-notes.html#k2-campaign-0)

***Overview***

To date, only calibrated target pixel files and FFIs are being archived. This involves the first pipeline module, CAL, and a portion of the exporter.

*** Exporter (AR) ***

<ul class="text">

    <li><p>No sky WCS coordinates were calculated for the FFIs. All keywords related to this WCS were removed from these files. </p></li>

    <li><p>No cosmic rays have been detected or removed from the calibrated pixels in the column FLUX.</p></li>

    <li><p>The following columns are not populated in the target pixel files: COSMIC_RAYS, FLUX_BKG, FLUX_BKG_ERR, POS_CORR1, and POS_CORR2. The information that is normally contained in these fields is currently not being calculated by the pipeline. </p></li>

    <li><p>The keywords CAMPAIGN, DATA_REL and MISSION are present in the primary headers of the exported files to help users identify the data set. CAMPAIGN contains the campaign number, DATA_REL contains the data release number, and MISSION indicates that it is data collected as part of 'K2'.</p></li>

    <li><p>With the limited pipeline and the different mission, not all quality flags are being populated. Inactive quality flags will remain zero for all cadences.  The following quality flags are valid in the exported files and can be used for information about the data:    </p></li>
    <ul>
        <li>Attitude Tweak (bit 1)</li>
        <li>Safe Mode (bit 2)</li>
        <li>Earth Point (bit 4)</li>
        <li>Resaturation Events (bit 6)</li>
        <li>Cosmic Ray Detected in Collateral (bit 14)</li>
        <li>Detector Anomaly (bit 15)</li>
        <li>Spacecraft is not in Fine Point (bit 16)</li>
        <li>No Data Reported (bit 17)</li>
    </ul>

</ul>


<hr>
<br>
Page last updated on:
<script>
document.write(document.lastModified);
</script>

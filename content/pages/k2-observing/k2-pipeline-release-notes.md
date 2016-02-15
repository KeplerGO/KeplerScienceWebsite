Title: K2 Pipeline Release Notes
Save_as: k2-pipeline-release-notes.html

[TOC]

Below are notes on the features of the software used to process the K2 data. Any changes to the pipeline that directly impact the data quality or format are listed for each data release. Any change impacts all subsequent data releases unless stated otherwise.

For more information about the Kepler pipeline see the Kepler manuals: <a href="http://archive.stsci.edu/kepler/manuals/KSCI-19081-001_Data_Processing_Handbook.pdf">Data Processing Handbook</a> and <a href="http://archive.stsci.edu/kepler/manuals/archive_manual.pdf">Archive Manual.</a>

Information about each specific campaign can be found in the links associated with each data release. 

### Data Release 8 
* February 2016
* SOC 9.3
* Campaigns: [C6](k2-data-release-notes.html#k2-campaign-6)

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

<p>Since it will take some time to correct this error and reprocess all Kepler and K2 data, a <a href="http://archive.stsci.edu/missions/k2/catalogs/k2_bad_short_cadence_target_list.csv">list of affected targets is provided</a>.  Even though the affected targets are readily identified, the science impact for any particular target may be difficult to assess.  Since the smear signal is often small compared to the target signal, the effect is negligible for many targets. However, the smear signal is scene-dependent, so time-varying signals can be introduced into any target by the other stars falling on the same CCD column.  </p>

<p>Some tips on how to assess the severity of the calibration error and more details on how this problem occurred are provided at the <a href="http://archive.stsci.edu/kepler/KSCI-19080-001.pdf">MAST archive.</a> </p>

</div>

<hr>
### Data Release 7 

* November 2015 
* SOC 9.3
* Campaigns: <a href="k2-data-release-notes.html#k2-campaign-5">C5</a>

This is the first delivery of C5.

One procedural change was made to how the data were processed, resulting in improvements to how the optimal apertures are selected. In C4 it was discovered that the optimal apertures selected by the pipeline were too small. Starting with Data Release 7 the apertures are no longer selected by including information about the motion polynomials and this change in process has proven to select larger and better optimal apertures.  </p>       

For further information about the content of this delivery see the previous Release Notes.

<hr>

### Data Release 6 

* September 2015
* SOC 9.3
* Campaigns: <a href="k2-data-release-notes.html#k2-campaign-4">C4</a></p>

This is the first delivery of C4. No features of the files have changed. For further information about the content of this delivery see the previous Release Notes.
    
<hr>
    
### Data Release 5

* July 2015
* SOC 9.3 
* Campaigns: <a href="C3drn.shtml">C3</a></p>

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
* Campaigns: <a href="k2-data-release-notes.html#k2-campaign-1">C2</a>

This is the first delivery of C2.  

The algorithm used by the CAL module to propagate the errors on the flux was turned off to expedite processing. Consequently, the reported error for each pixel at each cadence is the minimal error (shot noise plus read noise) as it does not include the associated offset term resulting from the full propagation of errors. See Section 5.1.3 of the [Data Characteristics Handbook (DCH, Christiansen et al. , 2013)](http://archive.stsci.edu/kepler/manuals/Data_Characteristics.pdf) for more details.  
    
No features of the files have changed. For further information about the content of this delivery see the previous Release Notes.

<hr>

### Data Release 3 

* December 2014
* SOC 9.2 
* Campaigns: <a href="k2-data-release-notes.html#k2-campaign-1">C1</a>

This is the first delivery of C1.  </p>

No features of the files have changed. For further information about the content of this delivery see the previous Release Notes.</p>

<hr>

### Data Release 2 

* October 2014
* SOC 9.2 
* Campaigns: <a href="k2-data-release-notes.html#k2-campaign-0">C0</a>

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
* Campaigns: <a href="k2-data-release-notes.html#k2-campaign-0">C0</a>

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

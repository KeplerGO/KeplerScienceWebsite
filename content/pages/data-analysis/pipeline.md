Title: Kepler and K2 Data Processing Pipeline
Save_as: pipeline.html

[TOC]

Users are strongly encouraged to review the following papers, a subset
of the Kepler documentation, prior to working with the data. These
papers describe the science operations, processing and characteristics
of the light curves. As our understanding of the instrument
progresses, additional discussion of systematic error mitigation, data
quality issues, and calibration will be provided. In addition to these
peer-reviewed papers, the user is also directed to the Kepler
Instrument Handbook, the Data Release Notes, the Data Charactistics
Handbook, which can all be found on the [data releases page]().

* Kepler Mission Design, Realized Photometric Performance, and Early
Science (Koch, David G., et al, 2010, ApJ, 713, L79)
* Kepler Science Operations (Haas, Michael R., etal, 2010, ApJ, 713, L115)
* Instrument Performance in Kepler's First Months (Caldwell, Douglas A., etal, 2010, ApJ, 713, L92)
* Overview of the Kepler Science Processing Pipeline (Jenkins, Jon M., etal, 2010, ApJ, 713, L87)
* The Kepler Pixel Response Function (Bryson, Stephen T., etal, 2010, ApJ, 713, L97)
* Initial Characteristics of Kepler Short Cadence Data (Gilliland, Ronald L., etal, 2010, ApJ, 713, 160)
* Initial Characteristics of Kepler Long Cadence Data for Detecting
Planet Transits (Jenkins, J. etal, 2010 ApJ 713, 120)
* Preliminary Astrometric Results from Kepler (Monet, David G., etal,
2010, ApJ, submitted)

### Pipeline Overview

Data collected by the photometer are recorded on orbit, downlinked,
archived, and end up at the Space Science Division of NASA's Ames
Research Center. All science data is processed and calibrated through
the Kepler Science Pipeline. The pipeline converts raw data numbers,
pixel locations, and ancillary engineering data into calibrated counts
and astrometric coordinates. After summing the counts within defined
apertures, estimating and subtracting background light, and adjusting
for cosmic rays, calibrated light curves are created for each selected
source. Further processing corrects these light curves for a variety
of instrumental artifacts and conditions the data for the next step, a
numerical search for candidate planetary transit events. These
candidate transits are then validated in the final processing stage.

Processed data is written to FITS-formatted files and exported to the
[MAST](http://archive.stsci.edu/) archive at the Space Telescope
Science Institute. The archived data includes the raw and calibrated
pixel values for all sources, background pixels, calibrated and
corrected light curves, and related ancillary engineering
data. Results of the transit search segment of the pipeline are not
archived; these data inform the science team of planet candidates for
followup investigation. The specific data products and content
archived at MAST will change during the course of the mission. Users
should examine the Archive Manual, the Data Release Notes, and the
Data Products page to track these changes.

**Pipeline components**

Each processing step is executed via a software module, developed and
implemented by the Science Operations Center (the "SOC") at NASA
Ames. Each module is composed of a number of procedures coded in
Matlab. A global schematic of the pipeline flow is presented
below. The principal elements of the pipeline are entitled (followed
by their common use abbreviations):

* Calibration   (CAL)
* Photometric Analysis   (PA)
* Pre-search Data Conditioning   (PDC)
* Transiting Planet Search   (TPS)
* Data Validation   (DV)

Users should note that in the current pipeline (SOC 6) the term raw
flux light curves are actually derived from calibrated pixels, a
somewhat confusing nomenclature. "Raw" light curves was adopted to
differentiate between light curves summed directly from the assigned
apertures - the output of PA, and light curves corrected for
instrumental artifacts and other known systematics errors - the output
from PDC.

A schematic of the Kepler Processing Pipeline is shown below. The
primary software modules are indicated on the left.

<img class="img-responsive" style="min-width:97%;" src="images/pipeline1_drn5.jpg">

#### Calibration (CAL)

This component of the pipeline converts counts to calibrated pixels.

The initial step in the Kepler science data pipeline is performed by
the software module termed CAL . CAL converts raw data numbers into
calibrated pixels, which are then passed to the Photometric Analysis
module for compilation into a light curve. The Science Operations
Center at Ames receives pixel data (Haas etal 2010) from the Data
Management Center at STScI. Data from each Kepler CCD is formatted as
FITS files, including collateral pixel data, collected for
calibration. CAL operates on both the 30 min (long cadence) and 1 min
(short cadence) observations, as well as on the full frame
images. Users of CCD data will be familiar with most functions of the
calibration module, however we note a few aspects peculiar to the
operational modes of Kepler. In general, most users of Kepler
photometry will not work directly with raw counts, so the information
provided here is to inform users on the the process by which
calibrated pixels are generated.

**Documentation**

The purpose of this webpage is to provide a brief guide to CAL
functions. GOs and archival users are urged to examine the primary
documentation, and look on this page for discussion of specific
issues. Primary documentation includes:

* Kepler Instrument Handbook, Version 1, 15-July-2009.
* Release Notes, which provide detailed information for each data release, either initial or reprocessed data per quarter.
* Jenkins etal, 2010, "Overview of the Kepler Science Processing Pipeline".
* Caldwell etal, 2010, "Instrument Performance in Kepler's First Months".
* "Pixel-Level Calibration in the Kepler Science Operations Center
  Pipeline", by E. Quintana etal, SPIE Conference on Astronomical
  Instrumentation, June 2010 (paper available July 2010).

**CAL functions**

CAL performs a number of functions familiar to CCD photometrists to
transform raw data counts into calibrated pixels, operating on a
single CCD channel at a time. Detailed models of each CCD were
developed during pre-flight testing, and are combined with full-frame
images obtained during the commissioning perior both before and after
ejection of the aperture cover. Each CCD channel consists of 1070 rows
by 1132 columns, of which only a subset (1024 x 1100) is used for
photometry.

Below is a block diagram of a Kepler CCD, showing the science and collateral pixel locations.

<img class="img-responsive" style="min-width:97%;" src="images/CCD_blockdiagram1.jpg">

The focal plane CCD models are applied within CAL to execute the following tasks:

* **Bias level**<br/>
The CCD bias level is determined using collateral pixels obained with
each CCD read. Users should note that the term "black level" is used
in much of the Kepler documentation, as a synonym for the more
commonly used "bias level". The bias level contains both a 2D map, and
an additional 1D "dynamic" bias correction. Once the 2D black level is
removed, a fit to the residual bias is used to estimate a 1D black
correction. Note the difference between Kepler's bias subtraction
method, and the approach commonly used for shuttered, non-continuous
CCD operation, in which the user takes separate bias frames, before,
during and after data collection.<br/>

* **Dark current**<br/>
Dark current is estimated from the masked and virual smear
pixels. Since the focal plane is maintained at −85 C, the effective
dark current is essentially zero. (Caldwell etal 2010). <br/>

* **Smear**<br/>
Kepler observes continuously, with no shutter; therefore stars
illuminate the CCDs during readout. This "staring" mode produces
trails along columns that contain stars, as charge is smeared out
during the read. Each pixel in a given column of the image receives
the same smear signal. These values are typically small, since each
pixel only “sees” a star for the readout time, 520 milli-seconds,
divided by the number of rows 1070. The smear level corrction in each
image is determined using the masked and virtual smear pixels set
aside for this purpose, as seen in the figure above. <br/>

* **Gain**<br/>
The gain function associates observed photoelectrons (e-) to the
analog/digital units generated by the A/D converter. Gain is the
average slope of the transfer function, and has a median value of 112
e-/ADU across the focal plane (Caldwell 2010). A measure of the
deviation from the linear transfer function is estimated at each ADU
signal level; this nonlinearity model provides appropriate
corrections. <br/>

* **Undershoot**<br/>
An issue noted during pre-flight testing can be described as a large,
signal-dependent trailing undershoot in the image, traced to an
amplifier in the local detector electronics. An undershoot model is
applied to correct affected pixels. <br/>

* **Flat field**<br/>
A flat field correction is the last step in CAL, applied to
photometric pixels to correct for spatial variations in pixel
sensitivity to a uniform light source. CAL uses a local flat field,
also termed the pixel response non-uniformity (PRNU) map. The PRNU
image maps each pixel’s relative brightness variation from the local
mean, expressed in percent (Van Cleve & Caldwell 2009). The median
standard deviation of the pixel values in the PRNU image across the
focal plane is 0.96 %. The flat field was developed during ground
testing prior to launch; there are no separate flatfield exposures
obtained on orbit.
 
CAL produces the basic photometric product of Kepler: a series of
calibrated target pixel images within a pre-set aperture. The
photometric time series is constructed from these images, in the next
step, Photometric Analysis, or PA.

#### Photometric Analysis (PA)

This component sums pixels within a defined aperture, to create light
curves.

The PA module constructs a photometric time series, i.e., a light
curve from the pixels defined to contain the optimal aperture, and
associated background pixels. The data are in the form of integrated
(total) photoelectrons collected during either a 1-minute or 30-minute
observation. For each observation, a timestamp is associated, defined
as the modified Julian date at the midpoint of the observation. Each
data point in the time series is the direct sum of the photoelectron
counts within a pre-defined target aperture. Bright star apertures may
contain scores of pixels, while the faintest sources may have a
single-pixel aperture. Source apertures are constructed to maximize
the signal-to-noise ratio of the light curves and take into account
the varying pixel response function across the focal plane. Details
about the source apertures are provided here, and by Bryson etal.

The primary functions of PA are: (a) Derive the integrated flux for up
to 165,000 sources observed on 30 minute timescales (long cadence
data) and up to 512 sources observed on one minute timescales (short
cadence data), from the calibrated pixels in each target’s
aperture. (b) Determine the photocenters of each source in detector
and astronomical coordinates. (c) Compute barycentric corrected
timestamps for each target. This software component consists of a few
dozen procedures, coded in Matlab.

The tasks performed by PA are:

* **Barycentric time correction**<br/>
Photometry is collected on a mobile platform, not connected to Earth,
moving in a Earth-trailing heliocentric orbit. Timestamps associated
with each observation must be adjusted to a common system for
comparison to related and ancillary observations taken on Earth or
other spacecraft. Additionally, precision timing is essential for
interpretation of transit photometry, therefore the Project continues
to work to improve the accuracy of derived timestamps. These values
are computed using the onboard clock and a detailed ephemeris of the
spacecraft trajectory. A further correction is applied such that the
mid-cadence timestamp references the time of signal capture at the
solar system barycenter. The barycentric corrections produced in PA
also compensates for the small timing offsets produced by readout of
the array. <br/>

* **"Argabrightening" event detection** <br/>
During the initial quarters of science operation, an occasional
diffuse illumination of portions of the focal plane lasting a few
minutes was detected. The origin of these brightenings is not
currently known. The software searches for these events, and flags the
affected pixels. Event detection occurs first in the PA module flow,
to ensure that this brightening is not confused with much more
localized excess photoelectrons produced by cosmic rays. Pixels
affected by argabrightening are "gapped" in the light curve, i.e., set
to -Inf. Listings of the specfic affected cadences are presented in
the relevant data release notes for each quarter; users should examine
the release note associated with your data and note possibly corrupted
observations. <br/>

* **Cosmic ray cleaning** <br/>
Kepler is affected by the solar and Galactic high energy particle
flux, with an expected rate of ~3 per day per pixel (Jenkins etal
2010). CRs impact at all angles of incidence; each event contributes
charge to ~4 adjacent pixels. In PA, CRs are identified and subtracted
in both background and source pixels, using a robust outlier
identification algorithm. Since CRs are more easily detected in
photometrically quiet sources, miitigation is more effective for those
sources. The user is cautioned that CRs may not be adequately removed
from bright pixels, but the overall effect on light curve precision
will be minimal. The same method and parameters are used for both long
and short cadence observations. PA also logs detected CRs, and derived
CR metrics for impact rate and mean depositd energy. CR maps for
pixels of interest will eventually be available through MAST.<br/>

* **Background removal**<br/>
A background signal is subtracted from each pixel (before summing) in
the optimal aperture. Since each source aperture does NOT include
extra pixels to evaluate the local background, Kepler collects a
distinct set of background pixels on each channel for this purpose. A
grid of background apertures are defined on each channel, roughly
symmetric across the focal plane. Each aperture generally contains
four pixels, ~8x8'' square. About 4400 usuable pixels within 1125
apertures lie in each channel, selected to avoid nearby stars and
potentially saturated columns. The integrated diffuse background at
each target pixel location is derived by fitting a 2-D polynomial to
the calibrated background pixels for each cadence, then interpolating
the fit for the specific pixels in the target aperture.<br/>
<br/>No background pixels are collected at 1-minute intervals. For this
data, the long cadence background polynomials are temporally
interpolated to the midpoints of the short cadence intervals. Short
cadence data users should be aware that changes in the background
which occur on timescales less than 30 minutes are not captured by the
current operations mode.<br/>
<br/>Additional information about backgrounds can be found here and in the
data release notes. <br/>

* **Aperture photometry**<br/>
Each source is defined by a target aperture mask and the optimal
photometric aperture. The optimal aperture contains a subset of the
total pixels in the mask. Ideally the number of extra pixels recorded
should be small, to maximize the number of observed sources, however a
contrasting constraint is the desire to capture all pixels which might
be useful. Users may wish to perform custom photometry, by altering
the mix of included pixels, but have no recourse if the needed pixels
were not obtained in the first place.<br/>
<br/>The flux is the unweighted sum of pixels in the optimal aperture after
background removal, termed Simple Aperture Photometry, (SAP). This
aperture is defined as the pixel set with the largest derived
signal-to-noise ratio, taking into account the Poisson noise for the
source and background, read noise, and quantization noise. Note that
the optimal aperture does not necessarily capture the total flux from
a source, but is designed to minimize noise for maximum transit
detection sensitivity. Users with other science applications should
keep this issue in mind. Users should also note that not all of the
flux in the optimal aperture is due to the primary target. The PSF
wings from surrounding sources will affect photometry in the optimal
aperture. The crowding metric is defined as the fraction of flux in
the optimal aperture produced by the target. This metric is computed
for each target list each quarter. The excess flux due to crowding
within the optimal aperture is removed when the light curves are
corrected in the next processing step, PDC.<br/>
<br/>Since the spacecraft rolls 90 degrees each quarter, any given
source will lie on a different CCD after each roll. Apertures are
re-defined for each quarter, to account for the different pixel
response functions of the CCDs on which the source may fall.<br/>
<br/>In the currently exported FITS light curve files, the output of
PA is labeled "raw" flux to distinguish it from light curves which
have been corrected for systematic effects in the subsequent PDC
software module. At present, there is no flagging of individual bad
pixels in the aperture photometry, nor does PA exclude known bad
pixels by "gapping" observations. Compromised data is marked on a per
channel and cadence basis, e.g., the Argabrightening events described
above. Individual bad pixels will affect one or more cadence
observations of individual targets; users are cautioned to inspect the
target pixels if they suspect corrupted data is producing an odd light
curve.<br/>
<br/>Below is an example of an aperture mask. The grey pixels define the total assigned aperture; the white pixels
define the optimal photometric aperture.

<img class="img-responsive" style="min-width:97%;" src="images/target_pixel_image.jpg">

* **Source centroids**<br/>
Target motions occur for a number of known and unplanned reasons. The
photocenter of each source is referred to as the source centroid. Both
to quantify source motion amplitudes, and to identify and potentially
correct systematic motions, flux-weighted centroids are calculated for
all defined sources for each cadence. These data are also important
for transit analysis and false postive rejection. <br/>
<br/> The dominant source of long-term source motion, differential
velocity abberation (DVA), is produced by the spacecraft motion during
each quarter. Each source traces a small elliptical arc across the
detectors over the period of Kepler's orbit. Unplanned source motions
may occur due to random pointing jitter, pointing drift, and focus
changes induced by thermal transients. During the course of each
quarterly observing cycle, a set of (~325) reference pixels data are
downlinked twice per week, to monitor the health of the spacecraft. If
a serious amount of drift is seen in the centroids of these pixels, a
commanded attitude adjustments may be initiated, producing a
quasi-discontinuous change in the centroid locations. <br/>
<br/> The derived centroids are tabulated in the light curve file
exported to MAST, and provide a centroid motion time series for each
source. These data can be used by GOs to ascertain the effect of
positional stability on their light curves. <br/>
<br/>An example of a motion centroid time series is shown
below. Motion of the nominal "center" of channel 1 (also termed
mod.out 2.1) is displayed for Q0. The large systematic drift is due to
differential velocity abberation. Since this channel is located at the
edge of the FOV, it also exhibits greater sensitivity to focus jitter
and drift. The total amplitude of the centroid motion is on order 0.1
pixels, equivalent to 0.4 arcseconds.

<img class="img-responsive" style="min-width:97%;" src="images/centroid_motion_drn5f4.jpg">

* **Astrometric solution**<br/>
PA performs a standard function of astronomical data pipelines:
assignment of celestial coordinates to detector pixels. On order 200
optimal sources are selected on each channel: bright, unsaturated,
minimally-crowded, main sequences stars. A 2-D polynomial fit is
constructed from the source row and column centroids for each channel
and cadence. Right ascension and declination for each pixel are
interpolated by mapping the polynomial fit to detector locations (row,
column) for a given output channel. The astrometric solution is
derived for each cadence independently.
 
 * **Computation of metrics**<br/>
 The PA module computes a variety of measures describing photometer
 performance, both as a health assessment and to support systematic
 error mitigation in following processing steps. <br/>
<br/>The output of this module is a photometric time series: flux per
 unit time interval continuously observed for about 90 days, excluding
 about 1 day each month for the data downlink, and any safe modes or
 other anomaly. These light curves are then passed to the Pre-Search
 Data Conditioning (PDC), for correction of systematic errors.

#### Pre-search Data Conditioning (PDC)

This component applies instrumental and systematic corrections to the
light curves prior to the transit planet search.

The PDC software module examines the calibrated light curve produced
by PA, and applies a series of corrections, based on both known
instrumental and spacecraft anamolies, and unanticipated artifacts
found in the data. "Pre-search" refers to data conditioning prior to
executing a transit search, which is undertaken by the next module in
the pipeline, TPS.

The primary tasks of PDC are: (A) Correct systematic errors, (B)
Remove excess flux in source apertures due to contamination from
nearby stars, (C) Identify outlying data points. PDC was designed to
remove systematic errors that are correlated with known spacecraft
anomalies, ancillary engineering data,or pipeline generated data, such
as the centroid motion time series. Its fundamental purpose is to
condition long cadence light curves for the following transiting
planet search, executed in the TPS module. The goals of conditioning
light curves for optimal transit analysis, and robust detection of
other time-variable astrophysical phenomena which may be present, are
not in principle or in practice mutually realizable. Significant
programming efforts have been made to preserve natural variability of
sources in the PDC software. The Kepler project continues an active
program of testing and modifying the software to both validate and
improve the realiability of transits and intrinsic variabilty
detection. For a large range of variable sources, the output of PDC
appears well aligned with the output of PA, the quality of the light
curves are improved after correction for systematic errors, and the
instrinsic variabilty preserved. Users should exercise caution if
their phenomena of interest are much shorter (<1 h) or much longer (>5
d) than transit timescales, or display complex light curves with
timescales similar to those expected for Earth-like transits (1-10
hrs), e.g., eclipsing binaries.

Users should always compare the light curves produce by PA and PDC,
and be cognizant of the differences. Please examine the relevant
release notes, as well as additional commentary on these pages.

**Documentation**

The purpose of this webpage is to provide a guide to PDC
functionality, and describe our understanding of the accuracy of its
output. GOs and archival users are urged to review the primary
documentation, and look here for updates and discussion of specific
issues. Primary documentation includes:

* Kepler Instrument Handbook, Version 1, 15-July-2010.
* Data Release Notes, detailed information for each data release, either initial or reprocessed data per quarter.
* Jenkins etal, 2010, "Overview of the Kepler Science Processing Pipeline".
* Jenkins etal, 2010, "Initial Characteristics of Kepler Long Cadence Data for Detecting Transiting Planets".
* "Presearch Data Conditioning in the Kepler Science Operations Center
Pipeline", by J. Twicken etal, SPIE Conference on Astronomical
Instrumentation, June 2010 (paper available July 2010).

**PDC functions**

PDC is executed in single channel "chunks", in which all sources
located on a single channel (aka "mod.out") are processed through the
software. For 1-min observations (short cadence), the duration is one
month; for 30-min observations, an entire quarter is processed. In
order PDC executes the following tasks.

* **Data anomaly flagging**<br/>
At initiation, observations affected by known anomlies are flagged, to
exclude their use in systematic error corrections. Discrete
discontinuities are introduced into the light curves by known
spacecraft activities such as the monthly Earth point downlinks, and
commanded attitude adjustments, and by unanticipated events, e.g., the
occasional safe mode. In addition to missing data, photometry may be
present for some cadences but in a degraded form due to planned
activities such as the reaction wheel desaturations (affects 1 cadence
every 3 days), and unanticipated events, e.g.., argabrightenings
identified by PA, and loss of fine point. Effected cadences and their
corresponding data anomalies are tabulated in the data release notes
specific to the dataset under study. Users must identify corrupted
cadences using the data release notes, as these data anomaly flags are
not currently tabulated in the light curve files released by MAST. The
Project is currently working to expand and update the content of the
light curve tables, to include these data flags. We expect these
upgrades to be included in Release 7.0 of the pipeline software.

* **Resample ancillary spacecraft data**<br/>
Engineering data is obtained on a variety of timescales. Before
correlating these data to the photometry, the ancillary data is
rebinned to match the sampling rate (1 & 30 mins) of the cadence data.

* **Identification and correction of discontinuities**<br/>
In addition to known data gaps described above, source-specific flux
discontinuities have been observed since Q0. Many, but not all, random
flux discontinuities are likely caused by impacts of solar and
galactic cosmic rays on the CCDs. Impulsive energy deposition from
cosmic rays alters the photo-sensitivity of individual pixels, which
may recover on a variety of timescales. In this step, PDC identifies
discontinuities in the light curves, and estimates the flux
offset. Discontinuities are corrected on a single or multiple cadence
basis, using the estimated offsets. An example is presented below.

<img class="img-responsive" style="min-width:97%;" src="images/PDC_example2_variable_drn5.jpg">

Example of PDC systematic error correction for a smoothly varying
star. This source was observed during Q1 and has Kp = 14.5. A flux
discontinuity specific to this star is observed at a cadence index of
~1450. PDC corrects this anomaly by "stiching" the curves
together. PDC output is coded red in the figure; this light curve is
tabulated as the "corrected" light curve in the files available from
MAST. (Adapted from DRN5).

* **Identify variable stars**<br/>
PDC attempts to separate "quiet" stars from variable sources, using a
tunable variability filter. Values of 0.5 and 0.25 % center-to-peak
variation has been used in different data releases; check the relevant
release notes for your data. This switch determines the following
detrending options; variable stars are treated differently than
quiescent stars.

* **Identify astrophysical events**<br/>
Astrophysical events must be identifed, as best as possible, to
prevent those events from affecting the correlation of the
synchronized engineering data to the light curves. These signatures,
e.g., giant planet transits, stellar eclipses, flares and microlensing
events, are located in the calibrated light curves, and replaced
temporarily with values interpolated across relevant candences.

* **Systematic error correction for quiet stars**<br/>
For sources below the variability threshold, the light curve is
compared to the resampled ancillary engineering data and centroid
motion time series, to identify and remove correlated trends. This
process is termed contrending in the Kepler documentation. A singular
value decomposition approach is utilized, to identify systematic
trends at many frequencies in the data which appear to be induced by
some spacecraft or detector process. An example would be an observed
flux variation correlated with periodic focus changes induced by
flexure in the optics. The goal of contrending is to remove flux
signatures that are correlated with the ancillary data on the
specified time scales. During the first year of operation, the project
has found that the systematic errors are caused primarily by target
motion at the pixel or sub-pixel level, which modifies the collected
signal. Contrending against the centroid motion time series improves
the quality and noise content of the data. Another noise source is
thermal transients observed following safe modes and the monthly
downlinks. The changing thermal environment of the spacecraft
following these events induces focus changes, which alters the source
PSFs. These transients last a few days (1 day = 48 30-min
observations), affecting a few hundred long cadence
datapoints. Systematic error correction is vital for the capability to
identify transiting planet search, especially the small signal (on
order 100 PPM) expected from Earth-sized planets. Without these
corrections, large numbers (thousands) of possible transit detections
would be triggered, severely impacting the science. Users are
cautioned to be aware that low amplitude periodic astrophysical
signals which are correlated with the ancillary data will likely be
compromised. Comments on the performance of PDC are provided below.

<img class="img-responsive" style="min-width:97%;" src="images/PDC_example1_drn5.jpg">

Example of PDC systematic error correction of a quiet star. This
source was observed during Q3 and has Kp = 14.6. The gap between
cadence indices 3000 and 3100 was produced by a safe mode event
followed by the monthly data download and subsequent thermal
transient. Here PDC corrected the light curve slope based on
contrending with the centroid motion solution, corrected the
discontinuity due to the downlink, and corrected for focus changes
induced by the thermal transient produced by the downlink. (Adapted
from DRN5).

* **Systematic error correction for variable stars**<br/>
Systematic error correction is a challenge when intrinsic variability
is present, as noted above. For sources exceeding the variability
threshold, PDC attempts to model periodic behavior, in order to fit
and remove this component and correlate against the underlying light
curve. Note that robust detection of variability can be comprised in
the presence of large discontinuities in the data; in these cases PDC
may produce spurious results. On the other hand smoothly varying stars
are generally well-fit by PDC, preserving the astrophysical signal,
and reducing the noise level. For stars tagged as variable, the
following steps are taken:<br/>
<br/>
(a)   Correct for thermal transients and differential velocity abberation <br/>
(b)   Fit the periodic content. If successful, remove the fitted harmonic content from the light curves. <br/>
(c)   Apply the contrending procedure to the residual light curve <br/>
(d)   Apply metrics to assess the results <br/>
(e)   Choose the non-variable or variable cotrending result for each target initially identified as variable. <br/>

<img class="img-responsive" style="min-width:97%;" src="images/PDC_example3_quietstar_drn5.jpg">

<br/>Example of PDC systematic error correction for a variable star
without a strong periodic component. The star is variable on short
time scales; over Q3 two discontinuities are observed, along with a
linear term produced by differential velocity aberration. (Adapted
from DRN5).<br/>
<br/>For some sources, the cotrending has been found to produce
unacceptable results. In these situations, the calibrated light curve
(PA output) is substituted for the cotrended light curve. For these
targets, systematic effects which are a component of the contrending
algorithm are not addressed in PDC.

* **Correct excess flux**<br/>
Some of the signal within the optimal aperture arises from the PSF
wings of nearby sources, contaminating the signal from the target. PDC
subtracts an estimate of this excess flux, based on a source-specific
crowding metric, defined as the fraction of starlight arising from the
target star. This metric has a range of [0-1], where 1 implies all
light comes from the target, and 0 = all background. Simple aperture
photometry produced by PA is not corrected for source crowding. The
crowding metric is derived from the distribution of surrounding stars
as tabulated in the KIC, and the measured structure of the
pixel-response functions of the source and nearby stars. Since each
source is observed on a dfferent location of the focal plane each
quarte, a consequence of the quarterly roll; the PRFs, optimal
apertures, and crowding metric are defined each quarter. <br/>
<br/> Users will see an offset in flux level when plotting PA output
versus PDC output. The offset is a measure of the source contamination
correction.

* **Identification of outlying data points**<br/>
To aid in the transit search, PDC searches for data points lying
outside (+/-) an adjustable range. A median filter is applied after
masking of potential astrophysical events, such as giant planet
transits, stellar flares, and microlensing. After removing the median,
the residual light curve is examined for points lying further than a
pre-set value. In the subsequent transit search phase, flagged points
are filled ("gapped") via interpolation. However, GO and archival
users will see light curves in which outliers are NOT removed; the
data is unaltered for user interpretation.

**Performance and cautions**

The Kepler data pipeline is optimized for transit searches, especially
for sensitivity to weak signals from Earth-sized planets. Note that
the motivation for fitting and removing periodic signals is to reduce
systematic noise even in highly variable stars, so that transits can
be robustly detected against the background of source
variability. Kepler expected to and is finding many eclipsing
binaries, in which the ampltiude of the stellar periodic signal
greatly exceeds any planet transit. Such systems are top priority
candidates for transit detection, since the orbital orientation of the
stellar pair is known, and close to 90 degrees. Significant effort is
being expended to preserve source variability and maximize transit
detections. Some precautions for working with the conditioned data:

Kepler is more sensistive then any previous photometer producing
near-continuous time series. The mission is also exploring a
variability domain not previously accessible. Therefore, we are
encountering subtleties in the data and the data processing not seen
before. Kepler is an ongoing experiment, in which the accuracy of the
data will improve with time, as understanding of the detectors,
processing algorithms, and natural variability increase.

Users are reminded to compare the calibrated light curve (PA) to the
corrected light curves (PDC), to ascertain the reliability of any
astrophysical signature in your data.

PDC gives satisfactory results on most stars which are either
intrinsically quiet, or have well-defined harmonic light curves. It
also performs well in cases where the star is variable, but without a
dominant harmonic term (see figure below). Following are examples of
specifc situations found in PDC output of which the user should be
aware:

(a)   Fails to identify and correct a source-specific discontinuity. <br/>
(b)   Poor detrending may introduce noise into complex lightcurves. <br/>
(c)   May identify a stellar eclipse as a flux discontinuity. <br/>
(d)   Fail to accurately track slowly rising or declining flux levels over a quarter. If this linear term is correlated with centroid motion times series, the linear term may be removed from the data. <br/>
(e)   Positive outlyers which are real events, but not flagged as such. PDC may tag these events as discontinuities, and attempt to correct. 

<img class="img-responsive" style="min-width:97%;" src="images/PDC_example_Jenkinsb_fig3.jpg">

Output of PA (top curve) and PDC (bottom curve) for a variable star
observed during Q1. This source displays periodic behavior with ~1%
peak-to-peak amplitude on a timescale of ~5 days. The figures show
that the overall source variability is preserved by PDC. Systematic
noise introduced by an onboard heater can be seen as the short period
wiggles in the upper light curves. This noise is removed by PDC as the
noise signal is correlated with ancillary engineering data (Jenkins
etal 2010).

Kepler is sensitive to an enormous volume of variability phase
space. At present, analysis of the appropriate level and specifics of
systematic error correction, for the full range of phase space sample
by Kepler is incomplete. Overall, the corrected light curves are
excellent probes of the underlying variations on a wide range of
sources. In broad terms users should we cognizant of three types of
phenomena for which the validity of the corrected light curves warrant
caution:

(1) Low amplitude (10s-100s PPM) variability with periods > 10 days. <br/>
(2) Strongly episodic variable stars, such as cataclysmic binaries. PDC may flag eruptive phenomena as discontinuties, or attempt a fit which may unintentially modify the data. <br/>
(3) Complex light curves, exhibiting multiple varying components, for
example and eclipsing binary with one or both components also
variable.

Each of these situations describe astrophysically important sources
for Kepler's varied science programs, and considerable effort is
ongoing to address the fidelity of the systematic error corrections to
(a) preserve instrinsic signals, and, (b) not introduce false
signals. These efforts include testing alternative correction
algorithms, and a series of numerical experiments in which test
signals are inserted into observed light curves and passed through
PDC. Results will be posted here in the near future.

### Calibration of Kepler data

The interpretation of Kepler light curves requires a careful
understanding of the properties of the photometer, observing sequence,
standard pipeline processing of the data, formats of data products,
noise and systematic effects within the data. In this segment of the
GO webpage we provide details on calibration and data quality issues
of immediate concern to GOs. Within the Pipeline webpage we provide an
overview of the Kepler science data pipeline. Under the Data Analysis
webpage, users will find information concerning science operations,
data products, visualization and analysis software.

Observers who are attempting to analyze variability phenomena having
amplitudes less than ~5 mmag peak-to-peak should pay particular
attention to the information about pipeline conditioning of the
data. For stars with long-period, low amplitude signals, the light
curves provided from the pipeline software should be used with caution
because the techniques used to mitigate systematic effects and
eliminate instrumental artifacts caused by e.g., spacecraft roll,
differential velocity aberration, and pointing drift and jitter may
also reduce or remove legitimate astrophysical signals having
timescales exceeding several days.

Users are strongly encouraged to review the following papers, a subset
of the Kepler documentation, prior to working with the data. These
papers describe the science operations, processing and characteristics
of the light curves. Examples of "first light" science results, on
topics other than exoplanet detection, are also listed. As our
understanding of the instrument progresses, additional discussion of
systematic error mitigation, data quality issues, and calibration will
be provided. In addition to these peer-reviewed papers, the user is
also directed to the first edition of the Kepler Instrument Handbook,
produced by the Project, and the Data Release Notes, one set of notes
for each data release, available at MAST.

#### Orbit

Kepler is in an Earth-trailing heliocentric orbit, which insured a
thermally stable environment and provided the ability to remain on a
single pointing for the duration of the prime Kepler mission. Pointed
observations away from the single stare position of the mission could not be accommodated by Kepler; all targets were limited to the objects available in the fixed FOV. Quarterly rolls were performed – one roll every 93 days – to reorient the solar arrays. With each roll, the stars in the FOV land on different regions of the detector relative to their pre-roll position, introducing quarterly discontinuities in the light curves.

#### Field of view

The Kepler photometer consists of 21 CCD modules (each with two 2200x1024
pixel CCDs).  Each module covers 5 square degrees.  The full 116
square degree field of view on the sky is illustrated below.  Tables that contain the corners of each Kepler CCD
module are available for download (ascii and Microsoft Excel).
Corners are provided in J2000 celestial coordinates for all four seasonal roll rotations.

<img class="img-responsive" style="min-width:97%;" src="images/Keplerfieldofviewstarchart.gif">

#### Instrument response

This section describes the wavelength-dependent response function of
the Kepler photometer.

Investigators can find current ascii tables behind the following links
containing the Kepler instrument response curve in hi-res and low-res
tabulations.

The Kepler photometer utilizes one broad bandpass, ranging from 4,200
to 9,000 Å.

<img class="img-responsive" style="min-width:97%;" src="images/kepler_CCDarray.jpg">
<img class="img-responsive" style="min-width:97%;" src="images/kepler_focalplane1.jpg">

The Kepler focal plane detectors and the optical elements within the
Kepler telscope. From the Kepler Instrument Handbook (KIH).

The primary instrument aboard Kepler is the focal plane array
consisting of 21 science and 4 Fine Guidance Sensor CCD modules. Field
flattener lenses on each module map the spherical telescope image
surface onto the flat CCD chips, and define the overall wavelength
bandpass. Each science module is an array of 2200 by 2048
pixels. These 21 modules each have 4 output channels, for a total of
84 channels and 94.6 million active pixels that view the sky, with
additional masked real pixels and virtual pixels for collection of
collateral data.

The shape of the bandpass, described below, was chosen to contain most
of the optical spectrum. This choice maximizes the sensitivity of the
telescope + detector combination for detecting planets transiting
solar-type stars. Kepler contains no "true" filter, in the sense that
HST imaging instruments include filter wheel assemblies with multiple,
specifically-defined bandpasses. Here, the intent is to utilize the
entire optical range, except for the short wavelengths, which were
truncated to avoid chromspheric emission lines in solar-type
stars. The photometer provides no color information, but does provide
excellent depth. Kepler's wide-band images are similar to the clear
filter frames taken with HST/STIS.

<img class="img-responsive" style="min-width:97%;" src="images/kepler_response1.jpg">

To achieve maximum sensitivity, the Kepler bandpass is wider than the
typical broad-band filters commonly used in optical astronomy
(e.g. Johnson UBVRI, Sloan ugriz). The absolute Kepler sensitivity
curve is displayed in the clickable figure (Fig 2) to the right. The
displayed response curve was derived during pre-flight testing, and
represents the laboratory calibration of the Kepler photometer. Links
to the tabulated values for the wavelength response are provided at
the top of the page in both high- and low- spectral resolution forms.

<img class="img-responsive" style="min-width:97%;" src="images/kepler_response2.jpg">

Optical element components of the Kepler Instrument Response compared
to approximate M5 and G2 stellar spectra.

The total photometer spectral response is a combination of the
transmission functions of all optical elements, including the Schmidt
corrector, the primary mirror assembly, the field flatterner lenses on
each CCD module, and the wavelength dependent quantum efficiency of
the detectors (Fig 3). The front surfaces of the field flatteners are
anti-reflection coated; a bandpass filter coating was applied to the
back surfaces. This bandpass was chosen to minimize the effects of
stellar variability in the near-ultraviolet (λ ≤ 420 nm), especially
the Ca II H & K emission lines, which would impact exooplanet transit
detection. At long wavelengths the coating was designed to minimize
fringing.

<img class="img-responsive" style="min-width:97%;" src="images/kepler_bandpass_jason1.jpg">

Comparison of the Kepler, MOST, CoRoT and Johnson response
curves. Kindly provided by Jason Rowe (NASA Ames) and extracted from
2009IAUS..253..121R.

Fig 4 compares the Kepler response function with those of two similar
missions: the MOST spacecraft, and the CoRoT mission. The response
functions for all three experiments are displayed from 4000 to 9000
Å. The MOST bandpass bandpass is marked by the dashed line, the Kepler
bandpass is shown in black and the CoRoT bandpass is shown by the
dot-dashed line. The transmission functions for the Johnson B,V,R,I
filters are shown from left to right in blue, green, red and magenta
respectively and have been scaled to peak at 100% transmission. The
spectrum for an A2V star is shown in cyan, which peaks in the UV and
the spectrum for a M2V star is shown in orange which peaks in the
infrared. The two spectra have been scaled to have equal flux in the
Johnson V filter.

#### Pixel response function

This section describes the properties of the detector pixels across
the focal plane.

Image scale:   3.98 arcseconds per pixel 
Pixel size:   27 × 27 microns

**Definition**

Kepler was designed as a high precision photometer, not as an imaging
experiment. The design requirements emphasize photometric stability
and minimizing noise sources, in order to detect the small dips in
observed flux produced by planet transits. Users should recognize that
the optimum focal plane geometry for flux collection will not in
principle provide the most compact point spread function, as is
usually desired for imaging experiments. In particular, Kepler's pixel
size precludes the type of high-resolution imagery obtained in the
optical with Hubble, but is similar to other space-based
multiwavelength imagers, e.g., GALEX. Kepler "images" will appear
pixelated; modeling the PSF, if desired by the user, will require
substantial effort.

The Kepler point spread function varies considerably across the focal
plane, due primarily to the Schmidt optics, which provide a large FOV
approximately 16° in diameter. The Project quantifies the total
response of the instrument to incident light in terms of its pixel
response function, which represents the observed appearance of point
sources. The PRF is a combination of the optical design, focus
setting, CCD detector mechanical and electronic properties, and the
temporal sequence of spacecraft pointing stability during an
observation. Not only does the PRF depend on location within the the
focal plane, as defined by a source's CCD channel, row and column
location, but also depends on the intrapixel location of the source
centroid (peak incident light). Note that this definition is somewhat
different from the more common usage. A detailed summary of the
characteristics and modeling of the PRF is provided by Bryson, etal;
(2010), the reader is strongly encouraged to review this paper,
especially if the shape of the PSF is important to your science.

**Distribution on the focal plane**

Concentrating light in the brightest pixel will degrade the resulting
photometry by increasing sensitivity to image motion, and constrain
the ability to determine image centroids. Conversely, a too-broad PRF
will include additional background flux and noise, reducing the
signal-to-noise ratio of the source. Therefore, the optimal pixel
response function for Kepler science operations was carefully designed
to maximize photometric stability. The Project uses these metrics to
quantify the PRF: the brightest pixel flux fraction (BPFF) and the 95%
encircled energy diameter (EE95), evaluated for the spectrum of a G2V
star. Level 1 requirements are: BPFF should be < 60%; the EE95 is
required to be < 7.0 pixels.

During the commissioning period, the focus was adjusted, and the
resulting PRFs measured, using a large set of test stars. Images from
this analysis, selected to have the stellar centroid closest to a
pixel center are shown below in the Y+ Z+ focal plane array coordinate
system. These images and the 95% encircled energy diameters are meant
to give the observer a qualitative idea of how the PRF varies across
the focal plane.

<img class="img-responsive" style="min-width:97%;" src="images/KIH_fig15.jpg">

Examples of scaled pixel-centered pixel response functions based on
commissioning data. The color bar indicates the square-root scaled
value. PRFs are calculated near the center of the an output channel at
row 535.0, column 550.0. Left: mod.out 9.2 (channel 26), smallest
EE95. Middle: mod.out 13.2 (channel 42), median EE95. Right:
mod.out 10.4 (channel 32), largest EE95.

<img class="img-responsive" style="min-width:97%;" src="images/KIH_fig16.jpg">

Pixel-centered images across the focal plane after focus adjustment
during commissioning. Each source is normalized to the brightest pixel
in the target aperture, rotated and translated to the common focal
plane coordinate system, and linearly scaled to the color bar. Black
lines along the color bar represent 10% intervals. (Some channels did
not have satisfactory targets). The encircled energy targets are
magnified by 50x compared to the spacing between them in this
image. (Adapted from the Kepler Instrument Handbook)

<img class="img-responsive" style="min-width:97%;" src="images/bryson_prfs1.jpg">

Expanded representation of the PRF at two locations in the focal
plane. On the left: a PRF from near the edge; on the right: a PRF near
the center. The pixelated image is shown below and a contoured version
above. (Adapted from Bryson, etal).

**Vignetting**

As seen in the figures above, vignetting affects the PRF at increasing
distance from the center of the FOV, a consequence of the Schmidt
optical design and large FOV. Somewhat less than half of the active
FOV is unvignetted, and another ~30% is affected, but considered
usable. Vignetting is negligible within 4.6° of the center, and
increases to ~11% at the edge of the FOV at 6.94 degrees off-axis. The
area of sky which is vignetted < 11% is 151.2 square degrees, and the
sky area imaged onto active pixels with < 11% vignetting is 101 square
degrees since there are gaps between modules, a gap between the two
CCDs on each module, and inactive areas on each CCD. Further details
are found in the Kepler Instrument Handbook, and the paper referenced
at the top.

**Guest Observer considerations**

Astronomers frequently use knowledge of the PSF to derive photometry
of their sources. Essentially there are three general methods for
source photometry: 1) annular aperture photometry (with or without
aperture corrections), 2) fitting the PSF to a mathematical form,
e.g., Gaussian-fitting, and, 3) empirical PSF-fitting. The latter is
often used in crowded fields or where the PSF lacks symmetry (as with
many of the Kepler sources). Some considerations for Guest Observers:

* Light curves are produced using optimal aperture photometry in the
  PA module: straightforward addition of the flux within the optimal
  source aperture. No PRF-fitting is involved in this photometry, but
  each source's optimal aperture is defined by the interpolated PRF at
  the source location, coupled with the source brightness and a model
  of the background.</br>

* The Project measured the PRF across the FOV during commissioning
  using ~19,000 relatively isolated stars with 12 < Kp
  < 13. Additional PRFs are measured each quarter to determine the
  motion time series produced by spacecraft drift and jitter. </br>

* PRF-fit photometry is under consideration, but not likely to be
  implemented in the near-term due to the computational resources
  involved, and the team's effort to improve other aspects of the
  photometric pipeline. </br>

* In planning observations, GOs should keep the shape of the PRF
  across the focal plane in mind. If possible, choose sources near the
  center of the FOV, for the most symmetric PRFs.

#### Backgrounds

This section describes the instrumental and natural background level
and background corrections.

To derive calibrated photometry, robust background subtraction is a
necessary and familiar step. Source photometry is affected by a number
of backgrounds contributors, both celestial and instrumental
backgrounds. During nominal science data collection, pixels designated
as background are measured in addition to target pixels. These data
are used to correct the photometry within the Photometric Analysis
pipeline module.

In addtion to correction of source photometry, measures of the spatial
and temporal background flux are by themselves an important science
topic, with a long and rich pedigree (e.g., the CMBR). Backgrounds at
many wavelengths are the sum of a number of processes; peeling back
each layer has provided valuable insight onto cosmic evolution
[ultraviolet: Bowyer, AnnRev 29, 59 (1991); Henry, AnnRev 29, 89 (1991); infrared: Hauser & Dwek, AnnRev 39, 249 (2001); soft x-rays: McCammon & Sanders, AnnRev 657, (1990)]. Kepler
provides a continuous measure of the celestial background in a wide
optical/near-IR band over a 100 square degree FOV for 3.5 years
nominal mission length.

Due to Kepler's unusual operational strategy, the method applied for
background removal differs from the most common approach used in
astronomical applications. Backgrounds are usually estimated from a
annulus of pixels immediately adjacent to the source, scaled to a
common area. Kepler does not use this approach, rather a separate set
of background apertures are collected across the focal plane, and a
background measure derived from these pixels. GOs should note that the
pipeline does not use pixels within the source aperture to measure the
local background.

**Components**

Celestial backgrounds arise from a number of sources, both from
spatially smooth, diffuse light which affects all pixels in the
aperture, and from transient events, which affect a few pixels.

* Zodical light, produced by sunlight scatered from dust in the
ecliptic plane.</br>

* Diffuse scattered starlight, produced by dust in the Galaxy. Due to
  Kepler's large FOV, the Galactic component shows a spatial gradient,
  increasing at lower galactic latitudes. </br>

* Unresolved starlight. Given the 4x4 arcsecond dimensions of the
  pixels, some light in the aperture arises from faint field stars. As
  with the diffuse Galactic emission, the contribution from unresolved
  starlight increases with decreasing Galactic latitude. </br>

* Cosmic ray impacts which corrupt individual pixels. The pipeline
  software flags and removes cosmic ray events from the pixel counts,
  within the Photometric Analysis module. Each cosmic ray event is
  replaced with a temporally local average of the pixel's time series
  without the cosmic ray pixel events. </br>

* Surrounding sources. A type of background which will affect source
  photometry are the residual wings of the PSFs produced by nearby
  stars, which may overlap the PSF of the target. Observers may
  visualize this effect by considering an image taken with poor seeing
  (equivalently poor focus). Faint PSF wings of surrounding sources
  will fall across the target, requring either PSF-fitting photometry
  or some form of aperture correction. A particular challenge for
  Kepler observers is that the user does not receive an entire image
  of the surrounding field, just the target pixel image. Stars outside
  of the this aperture may affect the target photometry, even though
  those stars were not actually measured. Also remember that nearby
  sources may be variable, producing a time-dependent
  background. </br>
</br> A correction for contaminating flux in the source aperture
  produced by surrouding sourcs is applied within the PDC pipeline
  module - a single valued subtraction, termed the crowding metric. In
  ideal situations the PSFs of neighboring stellar sources would not
  change over time, expect for possible intrinsic source
  variabilty. Observers should be aware that spacecraft operations may
  induce changes in the source PSFs, through focus changes, and
  spacecraft motions (jitter and drift). Motion of the source center
  during an observing season, even at the millipixel level, will
  induce variations in the contaminating flux, introducing small
  levels of noise into thelight curve. In preparing proposals, GO
  should choose sources as isolated as possible, and be aware of the
  constraints for achieving excellent time series photometry under
  strong crowding situations. </br>

Instrumental backgrounds include the detector bias level (also termed
black level), which is removed in the CAL pipeline module, some
anticipated issues, such as scattered light, unexpected electronic
issues discovered during pre-flight characterization of the detectors,
and some features seen during early flight operations,
e.g.,v"argabrightening", an anomalous full-field illumination, whose
origin is under investigation by the instrument team (Jenkins etal
2010). Spatially varying backgrounds produced by the detector
electronis are full described in the Kepler Instrument Handbook
(KIH). The Kepler project is investing considerable effort to
identify, assess, and develop corrections for instrumental signatures
discovered during the early phase of data collection. Additional
details on the spatially-varying image artifacts, and their
corrections can be found on the GO Data Artifacts page.

**Measurement and removal**

Kepler constructs a background flux map using a set of target pixels
specifically assigned for this purpose. Background "targets" are small
(nominally 2 x 2 pixels) postage stamp images which measure the
background signal in the long cadence observations. Since backgrounds
must be estimated and removed from all observed sources in the FOV, a
method was adopted to interpolate background values from all targets
pixels in a channel using the background apertures in that channel. A
maximum of 1125 background apertures and 4,500 pixels (~4 pixels per
target) are allocated for each of the 84 output channels. These
background targets are selected to optimize a 2D polynomial
representation of the background flux distribution, derived separately
for each channel.

For robust fitting, background apertures should be uniformly
distributed on each CCD array. To mitigate edge effects, more
background apertures are positioned at the frame edges. During target
management prior to each quarter, background pixels are selected,
avoiding stars and locations affected by charge bleeds.

<img class="img-responsive" style="min-width:97%;" src="images/bryson_background1.jpg">

Distribution of background apertures in a typical Kepler CCD
frame. Spacing of background pixels is increased along the frame edge
to improve the fit to the background.

Background pixels are calibrated in the same manner as source pixels
in the CAL pipeline module. Background channel maps are generated in
PA; interpolated background values are then subtracted from the pixel
values prior to aperture photometry.

A measure of the celestial background in the Kepler FOV is provided by
VanCleve in Data Release Notes 5. The figure below shows the
background flux time series for the Q0+Q1 observing season, derived
from the reprocessed data released on 15-June-2010. Time series are
shown for the full focal plane, and for channels closest to and
furthest from the Galactic plane. From this plot, a few items are
evident:

* The temporal and FOV-averaged value background value is ~2.7 × 10−5
  electrons per cadence. This value corresponds to the expected signal
  from a star with Kp ~ 18.3.</br>

* The difference in background counts produced by viewing
perpendicular to the Galactic plane is about a factor of 1.8.

<img class="img-responsive" style="min-width:97%;" src="images/kepler_background_Q0+1.jpg">

Background time series for observing quarters Q0 + Q1. The curves show
average over all mod.outs (CCD channels), the modules furthest from
(mod.out 2.4 = channel 4) and nearest to (mod.out 24.4 = channel 84)
the Galactic plane. The vertical offset is produced by the
spatially-dependent Galactic emission; the horizontal trend is caused
by variation in the zodical light. The narrow spikes visible in all 3
curves are Argabrightening events. Observations affected by these
diffuse brightenings are tabulated in the release notes.

**Guest Observer considarations**

What should GOs be concerned about regarding backgrounds ?? Background
subtraction is normally a user-driver reduction step, not a pipeline
function. The current assessment is that the pipeline background
corrections do not produce significant noise or errors in the
extracted light curves. A few steps which GOs can take to examine
their specific situations:

(1) Inspect the FOV around sources using a full-frame image. Look for
nearby bright sources which may affect your target, especially the
potential for unknown variable stars. Isolated sources should present
no issues, whereas the treatment of the background by the pipeline for
crowded sources may not be optimal. Also look for saturated stars in
the same (+/-1) column to check for unfortunately placed charge
bleeds.</br>

(2) Compare the Kepler view of your sources with a DSS image. The
later have a resolution of about 1.5 arcseconds, and may show faint
sources in the source apertures.</br>

(3) When the target pixels images become available for GO use, users
may wish to contruct their own background estimates using the
ancillary background aperture photometry. Background values are not
presently supplied with the light curves, and can only be roughly
estimated on a per pixel basis using a full-frame image from the same
observing season.

#### Signal-to-noise properties

This section details the systematics of the detected flux and
associated noise.

Identification of astrophysically interesting signals in the Kepler
time series requires an assessment of the noise characteristics of the
photometer. Users of Kepler data will need information about both the
usual signal-to-noise issues, e.g., photon and read noise, background
flux, and the temporal stability due to systematic and episodic noise
sources. Detection of weak transits against a bright stellar
background is the primary objective of the Kepler mission, therefore
the photometric stability of the instrument was of paramount
importance during the design phase. The Project is investing
considerable effort to identify and account for systematic noise
sources in the Kepler time series. These efforts are described in the
Instrument Handbook, the Kepler Data Analysis Handbook (Fall 2010),
and a series of data release notes, distributed when large datasets
are released to the archive. Individual data release notes are found
in the Data Release folder at MAST. Users of Kepler data are strongly
encouraged to read these detailed descriptions.

The following plot provides an ensemble comparison of Kepler
three-wheel fine-point precision (red), K2 two-wheel coarse-point
precision (green) and K2 two-wheel fine-point precision (blue). The
red lines are carefully-selected quiet G dwarfs, falling upon
arbitrary modules of the Kepler detector.

<img class="img-responsive" style="min-width:97%;" src="images/Feb2014Precision.png">

**Observing limits**

The limiting factor for observations of faint sources is set by source
confusion, rather than the photometric accuracy computed for isolated
sources. Users wanting to observe objects with Kepler magnitudes less
than 17.0, should carefully examine the field around their source, and
estimate the contamination from the PSFs of surrounding objects. Note
that an estimate of the crowding metric is provided for most sources
brighter than Kp = 17.0 in the Kepler Target Catalog, look under the
field labeled "Contamination" in the output of a target
search. Contamination is defined as (1 - crowding_value), where the
crowding value was derived when the Kepler Target Catalog was
created. A value of 0 implies no contamination, 1 implies essentially
all background, i.e., complete contamination of the source by
surrounding objects. For fainter sources, observers can estimate the
contamination using imagery from the Digital Sky Survey, supplemented
with the Kepler Full Frame Images (FFIs) as the latter become
available.

For bright sources the observed signal in the central pixel(s) will
increase linearly until the well depth is reached. Beyond that level,
charge will bleed into adjacent pixels in the column containing that
source. However, even when the central pixel is saturated, the target
aperture can extend along the bleed column, preserving most or all of
the signal from the source. Guest observers may propose for bright
stars, with the caveats that these sources are expensive in pixel
terms. A custom aperture may be required, and the project cannot
guarentee that a custom aperture can be created for the proposed
observations.

#### Flux calibration

This section describes the conversion of detected photoelectrons to
incident flux.

**Photometric zeropoint**

Kepler's primary mission of precision transit photometry requires
differential photometric ability only. Absolute photometric
calibration is not essential to the success of the exoplanet
mission. A community-led program is underway to flux calibrate the
Kepler instrument in-flight for the GO program. Although caveats are
created by the broad 4,300 − 9,000 Å spectral response of the Kepler
instrument, zeropoint calibrations for standard photometric systems
will appear as updates on this page over time.

**Kepler magnitudes**

Each Kepler target has a pre-set observing aperture uploaded to the
spacecraft. These apertures are defined in terms of the number of
pixels and shape of the array. The brigter a source, the larger the
aperture needed to collect the photons for an optimal detection of
that source. Aperture size is primarily defined by the source's Kepler
magnitude (Kp), a measure of the source intensity as observed through
the wide Kepler bandpass.

* The Kepler Science Team conducted an extensive observing program
  prior to launch in order to classify stars in the FOV. The
  fundamental goal was to develope a list of FGKM dwarf stars as the
  primary source list for exoplanet detection. Objects were observed
  in the SDSS griz bands. This photometry, along with 2MASS data form
  the basis of the Kepler Input Catalog.</br>

* No observations were obtained from the ground using a pseudo-Kepler
  band filter. The Project constructed a set of stellar spectral
  synthesis models covering a range of effective temperature, gravity
  and mean abundance, and derived g,r,i,Kp magnitudes by convolving
  the filter response functions with the models. Using correlations
  between these values, Kepler magnitudes are estimated from the
  observed SDSS magnitudes using empirical formulae.</br>

* Most proposers will adopt the Kp values directly from the
  KIC. Exceptions are strongly variable stars, in which a magnitude
  range should be provided as described on the Target Checks page, and
  sources lacking a Kepler magnitude. For the latter, an approximate
  esimate of Kp can be derived using the following exxpression, which
  is based on the empirical relations used by the Kepler Stellar
  Classifiction Program.</br>

If only B,V magnitudes are available, the user can convert B,V into
SDSS g,r using the transformation derived by Smith etal (ApJ 123,
2121, 2002, Table 7). The expression below uses this transformation
equation. If SDSS g,r values are available, just use the conditional
statements in line 3 and 4 below.

(1) g   =   0.54 B   +   0.46 V   −   0.07 </br>
(2) r   =   −0.44 B   +   1.44 V   +   0.12 </br>
(3) if   ( g − r )   ≤   0.8    then    Kp   =   0.2 g   +   0.8 r </br>
(4) if   ( g − r )   >   0.8     then    Kp   =   0.1 g   +   0.9 r </br>

This expression is accurate to about ±0.2 mag for stars hotter than
3500 K. For M stars, users are cautioned that systematic errors may
exceed 0.6 mag, in the sense that Kp returns magnitudes that are too
faint.

Derivation of Kepler magnitudes will be detailed further in a paper
describing the Stellar Classification Program, and the generation of
the Kepler Input Catalog. In the interim, interested users may examine
the KIC algorithms document.

Given a calibration of (B−V) color with spectral type (effective
temperature), a Kepler magnitude can be estimated. Values for (Kp−V)
are presented below for main-sequence stars, based on the above
relation. This color can be applied to stars whose apparent Johnson V
magnitude is known to obtain Kp. Again, note that for stars cooler
than M0, the estimated Kp may be too faint.

#### Astrometry

This section details the image centroids and associated celestial coordinates.

Precise coordinates for Kepler targets are essential, both in the
target assignment phase and during subsequent photometric
analysis. Source coordinates are provided by the Kepler Input Catalog
(KIC), searchable via the MAST interface. Astrometric calibration of
the source centroids occurs in the Photometric Analysis (PA) pipeline
module. Precise centroids of sources within the target aperture
permits correction of the photometry for spacecraft motions during the
observing season.

The focal plane array contains significant gaps between the detectors,
designed to exclude very bright stars from falling photo-active
pixels. Too-bright stars will induce excessive bleeding along the
read-out columns, and exhibit significant PSF wings, corrupting
photometry of surrounding stars. These gaps will cause some sources,
which appear to lie on the FOV, to actually be not observable. The
Kepler FOV is shown to the right, where some of the excluded bright
stars are indicated. Observers should carefully check to see if their
proposed sources land on active silicon.

**Source astrometry**

Guest observers obtain coordinates for their sources from the Kepler
Input Catalog (KIC). The source of the astrometry depends on which
catalog (or catalogs) contain data for that source. The order for the
choice of astrometric values is described in the release notes for the
Kepler Input Catalog. Those catalogs are listed here, with an estimate
of their positional accuracy.

  1. Kepler Stellar Classification Program; 50 milliarcseconds, data obtained closer to the Kepler epoch, minimizing proper motion offsets 
  2. Hipparcos; 10 milliarcseconds 
  3. Tycho-2; for V brighter than 8.0; 20 milliarcseconds 
  4. UCAC2; 40 milliarcseconds 
  5. 2MASS; 70 milliarcseconds 
  6. USNO-B1.0; 200 milliarcseconds

The values listed in the KIC arise from the first catalog in the above
list that contains a measure for that source. The source catalogs
should be consulted for a detailed discussion of astrometric
accuracy. The Kepler Project required positions to be accurate to 200
milliarcseconds, and proper motions to 20 millarseconds per year.

**Observed astrometry**

Observers will generally want to know where their sources lie within
the assigned target aperture. Image centroids are calculated as part
of the calibration pipeline, within the Photometric Analysis (PA)
module. PA computes flux-weighted mean centroids for all stars, which
are tabulated in the light curve files, expressed as row and column
pixels values. These data provide an image centroid time series, and
enable observers to assess target placement during the observing
sequence. On each channel, a set of bright (but not saturated),
relatively isolated stars are chosen to provide a reference grid for
astrometry. Photometry for this set of reference stars is processed
within the Photometer Performance Assessment (PPA) pipeline module to
provide metrics of the photometric and astrometric stability of the
instrument. Image centroids for these stars are used to create a
"plate" solution specific for each CCD channel. This solution is then
interpolated to convert detector coordinates (row, column) to
celestial coordinates (RA, Dec).

In the currently released data (Q0-Q3), both public and proprietary
Guest Observer data, the derived celestial coordinates are not
provided in the light curve tables. Analysis of centroid motion is not
encumbered by the lack of this calibration; both significant and more
subtle motions can be discerned in the centroid time series (detailed
in the paper mentioned below). In particular, the flux-weighted
centroid will respond to photometric variability when two or more
stars are present within the aperture. The centroid will appear to
move in a systematic manner as one star varys in brightness; the
resulting motion time series can be used to help identify false
positive transit signatures. We anticipate that astrometric
coordinates will be included within Pipeline Version 7.0,
approximately coincident with the first Cycle 2 data release.

FFIs:   The full frame images were designated as engineering data by
the Project, and no astrometric calibration was initally
intended. MAST developed an astrometric solution for the 8 Golden
full-frame images, using the public astrometry.net tool, developed by
Blanton, Hogg, Lang, Mierle & Rowies. These 8 FFIs were taken under
ideal pointing and thermal stability at the start of the mission, and
are avaiable here. Subsequent FFIs do not yet contain
astrometry. Plans for the possible astrometric calibration of all FFIs
is under review.

**Astrometric science with Kepler**

The high signal-to-noise ratios achieved with Kepler permit a high
level of astrometric accuracy, despite the large pixel scale and large
field of view. In principle the Kepler data can be used to determine
parallaxes and proper motion for tens of thousands of stars, and
explore more subtle motions, hinting at planetary companions. The
Kepler Project is working towards understanding the astrometric
precision of the data, and its potential applications. Based on
analysis of the Q0+Q1 data, Monet provides an estimate of Kepler's
astrometric precision of ~4 milliarcseconds over a single 30 minute
observation (1 long cadence). Additional details are provided in an
initial report on astrometric results from Kepler.

The abtract from this paper (Monet etal 2010):

Although not designed as an astrometric instrument, Kepler is expected
to produce astrometric results of a quality appropriate to support
many of the astrophysical investigations enabled by its photometric
results. On the basis of data collected during the first few months of
operation, the astrometric precision for a single 30 minute measure
appears to be better than 4 milliarcseconds (0.001 pixel). Solutions
for stellar parallax and proper motions await more observations, but
the analysis of the astrometric residuals from a local solution in the
vicinity of a star have already proved to be an important tool in the
process of confirming the hypothesis of a planetary transit.

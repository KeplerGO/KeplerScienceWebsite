Title: Kepler and K2 Data Processing Pipeline
Save_as: pipeline.html

[TOC]

Users are strongly encouraged to review the following papers prior to
working with Kepler data. These
papers describe the science operations, processing and characteristics
of the light curves.  While operations for K2 are slightly different,
these papers still provide a useful overview of the Kepler (and now
K2) pipeline.  In addition to these papers, the user is also directed to the Kepler
Instrument Handbook, the Data Release Notes, the Data Charactistics
Handbook, links to which can all be found on the [data releases page](data-releases.html).

* [Kepler Mission Design, Realized Photometric Performance, and Early
Science](http://adsabs.harvard.edu/abs/2010ApJ...713L..79K) (Koch, D. G., et al., 2010 ApJ, 713, L79)
* [Kepler Science Operations](http://adsabs.harvard.edu/abs/2010ApJ...713L.115H)
  (Haas, M. R., et al., 2010 ApJ, 713, L115)
* [Instrument Performance in Kepler's First Months](http://adsabs.harvard.edu/abs/2010ApJ...713L..92C)
  (Caldwell, D. A., et al., 2010 ApJ, 713, L92)
* [Overview of the Kepler Science Processing Pipeline](http://adsabs.harvard.edu/abs/2010ApJ...713L..87J)
  (Jenkins, J. M., et al., 2010 ApJ, 713, L87)
* [The Kepler Pixel Response Function](http://adsabs.harvard.edu/abs/2010ApJ...713L..97B)
  (Bryson, S. T., et al., 2010 ApJ, 713, L97)
* [Initial Characteristics of Kepler Short Cadence Data](http://adsabs.harvard.edu/abs/2010ApJ...713L.160G)
  (Gilliland, R. L., et al., 2010 ApJ, 713, 160)
* [Initial Characteristics of Kepler Long Cadence Data for Detecting Planet Transits](http://adsabs.harvard.edu/abs/2010ApJ...713L.120J)
  (Jenkins, J. M., et al., 2010 ApJ, 713, 120)
* [Preliminary Astrometric Results from Kepler](http://adsabs.harvard.edu/abs/2010arXiv1001.0305M)
  (Monet, D. G., et al., 2010 ApJL, submitted)
* [Pixel-Level Calibration in the Kepler Science Operations Center
Pipeline](http://adsabs.harvard.edu/abs/2010SPIE.7740E..1XQ)
(Quintana, E. V., et al., 2010 Proc. SPIE, 7740, 77401X)
* [Presearch Data Conditioning in the Kepler Science Operations Center Pipeline](http://adsabs.harvard.edu/abs/2010SPIE.7740E..1UT)
  (Twicken, J. D., et al., 2010 Proc. SPIE, 7740, 77401U)


### Pipeline Overview

Data collected by the Kepler photometer are recorded on orbit, downlinked,
archived, and end up at the Space Science Division of NASA's Ames
Research Center. All science data is processed and calibrated through
the Kepler Science Pipeline. The pipeline converts raw data numbers,
pixel locations, and ancillary engineering data into calibrated counts
and astrometric coordinates. After summing the counts within defined
apertures, estimating and subtracting background light, and adjusting
for cosmic rays, calibrated light curves are created for each selected
source. Further processing corrects these light curves for a variety
of instrumental artifacts and conditions the data for the next step (a
numerical search for candidate planetary transit events in the case of
Kepler data). Kepler candidate transits are then validated in the final processing stage.

Processed data is written to FITS-formatted files and exported to the
[MAST](http://archive.stsci.edu/) archive at the Space Telescope
Science Institute. The archived data includes the raw and calibrated
pixel values for all sources, background pixels, calibrated and
corrected light curves, and related ancillary engineering
data. The specific data products and content
archived at MAST are detailed [here](data-releases.html).

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

For Kepler data only, the pipeline also included the following
elements:

* Transiting Planet Search   (TPS)
* Data Validation   (DV)

A schematic of the Kepler Processing Pipeline is shown below. The
primary software modules are indicated on the left.

<img class="img-responsive" style="min-width:97%;" src="images/pipeline1_drn5.jpg">

#### Calibration (CAL)

The initial step in the Kepler science data pipeline is performed by
the software module termed CAL. CAL converts raw data numbers into
calibrated pixels, which are then passed to the Photometric Analysis (PA)
module for compilation into a light curve. The Science Operations
Center at Ames receives pixel data from the Data
Management Center at STScI.  Data from each Kepler CCD is formatted as
FITS files, including collateral pixel data, collected for
calibration. CAL operates on both the 30 min (long cadence) and 1 min
(short cadence) observations, as well as on the full frame
images. Users of CCD data will be familiar with most functions of the
calibration module, however we note a few aspects peculiar to the
operational modes of Kepler. In general, most users of Kepler or K2
data will not work directly with raw counts, so the information
provided here is to inform users on the the process by which
calibrated pixels are generated.

**CAL functions**

CAL performs a number of functions familiar to CCD photometrists to
transform raw data counts into calibrated pixels, operating on a
single CCD channel at a time. Detailed models of each CCD were
developed during pre-flight testing, and are combined with full-frame
images obtained during the commissioning period both before and after
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
dark current is essentially zero
[(Caldwell et al. 2010)](http://adsabs.harvard.edu/abs/2010ApJ...713L..92C). <br/>

* **Smear**<br/>
Kepler observes continuously, with no shutter; therefore stars
illuminate the CCDs during readout. This "staring" mode produces
trails along columns that contain stars, as charge is smeared out
during the read. Each pixel in a given column of the image receives
the same smear signal. These values are typically small, since each
pixel only “sees” a star for the readout time, 520 milli-seconds,
divided by the number of rows 1070. The smear level correction in each
image is determined using the masked and virtual smear pixels set
aside for this purpose, as seen in the figure above. <br/>

* **Gain**<br/>
The gain function associates observed photoelectrons (e-) to the
analog/digital units generated by the A/D converter. Gain is the
average slope of the transfer function, and has a median value of 112
e-/ADU across the focal plane [(Caldwell et al. 2010)](http://adsabs.harvard.edu/abs/2010ApJ...713L..92C). A measure of the
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
mean, expressed in percent. The median
standard deviation of the pixel values in the PRNU image across the
focal plane is 0.96%. The flat field was developed during ground
testing prior to launch; there are no separate flat field exposures
obtained on orbit.
 
CAL produces the basic photometric product of Kepler: a series of
calibrated target pixel images within a pre-set aperture. The
photometric time series is constructed from these images in the next
step, Photometric Analysis (PA).

#### Photometric Analysis (PA)

The PA module constructs a photometric time series, i.e. a light
curve, from the pixels defined to contain the optimal aperture and
associated background pixels. The data are in the form of integrated
(total) photoelectrons collected during either a 1-minute or 30-minute
observation. For each observation, a timestamp is associated, defined
as the modified Julian date at the midpoint of the observation. Each
data point in the time series is the direct sum of the photoelectron
counts within a pre-defined target aperture. Source apertures are constructed to maximize
the signal-to-noise ratio of the light curves and take into account
the varying pixel response function across the focal plane. Details
about the source apertures are provided
[here](pipeline.html#pixel-response-function) and in [Bryson et al. 2010](http://adsabs.harvard.edu/abs/2010ApJ...713L..97B).

**PA functions**

The tasks performed by PA are:

* **Barycentric time correction**<br/>
Timestamps are computed using the onboard clock and a detailed ephemeris of the
spacecraft trajectory. A further correction is applied such that the
mid-cadence timestamp references the time of signal capture at the
solar system barycenter. The barycentric corrections produced in PA
also compensates for the small timing offsets produced by readout of
the array. <br/>

* **"Argabrightening" event detection** <br/>
An occasional diffuse illumination of portions of the focal plane lasting a few
minutes was detected. The origin of these brightenings is not
currently known. The software searches for these events, and flags the
affected pixels. Event detection occurs first in the PA module flow,
to ensure that this brightening is not confused with much more
localized excess photoelectrons produced by cosmic rays. Pixels
affected by Argabrightening are "gapped" in the light curve, i.e., set
to -Inf. Listings of the specfic affected cadences are presented in
the relevant data release notes for Kepler and K2. <br/>

* **Cosmic ray cleaning** <br/>
Kepler is affected by the solar and Galactic high energy particle
flux, with an expected rate of ~3 per day per pixel [(Jenkins et al.
2010)](http://adsabs.harvard.edu/abs/2010ApJ...713L.120J). Cosmic rays
(CRs) impact at all angles of incidence; each event contributes
charge to ~4 adjacent pixels. In PA, CRs are identified and subtracted
in both background and source pixels, using a robust outlier
identification algorithm. Since CRs are more easily detected in
photometrically quiet sources, mitigation is more effective for those
sources. The user is cautioned that CRs may not be adequately removed
from bright pixels, but the overall effect on light curve precision
will be minimal. The same method and parameters are used for both long
and short cadence observations. PA also logs detected CRs and derived
CR metrics for impact rate and mean deposited energy. <br/>

* **Background removal**<br/>
A background signal is subtracted from each pixel (before summing) in
the optimal aperture. Since each source aperture does not include
extra pixels to evaluate the local background, Kepler collects a
distinct set of background pixels on each channel for this purpose. A
grid of background apertures are defined on each channel, roughly
symmetric across the focal plane. Each aperture generally contains
four pixels, an 8x8 arcsec square, which are selected to avoid nearby stars and
potentially saturated columns. The integrated diffuse background at
each target pixel location is derived by fitting a 2-D polynomial to
the calibrated background pixels for each cadence, then interpolating
the fit for the specific pixels in the target aperture. *No background pixels are collected at 1-minute intervals. For this
data, the long cadence background polynomials are temporally
interpolated to the midpoints of the short cadence intervals. Short
cadence data users should be aware that changes in the background
which occur on timescales less than 30 minutes are not captured by the
current operations mode.* Additional information about backgrounds can be found [here](pipeline.html#backgrounds). <br/>

* **Aperture photometry**<br/>
Each source is defined by a target aperture mask and the optimal
photometric aperture. The optimal aperture contains a subset of the
total pixels in the mask. The flux is the unweighted sum of pixels in the optimal aperture after
background removal, termed Simple Aperture Photometry (SAP). This
aperture is defined as the pixel set with the largest derived
signal-to-noise ratio, taking into account the Poisson noise for the
source and background, read noise, and quantization noise. Note that
the optimal aperture does not necessarily capture the total flux from
a source, but for Kepler was specifically designed to minimize noise for maximum transit
detection sensitivity. Also, the PSF wings from surrounding sources will affect photometry in the optimal
aperture. The crowding metric is defined as the fraction of flux in
the optimal aperture produced by the target. This metric was computed
for each target list each quarter for Kepler. The excess flux due to crowding
within the optimal aperture is removed when the light curves are
corrected in the next processing step (PDC). Furthermore, since the spacecraft rolled 90 degrees each quarter during the
Kepler mission, any given Kepler target will lie on a different CCD after each roll. Apertures were
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
curve. In general, users may wish to perform custom photometry by altering
the mix of included pixels.

* **Source centroids**<br/>
The photocenter of each source is referred to as the source centroid. Flux-weighted centroids are calculated for
all defined sources for each cadence. The derived centroids are tabulated in the light curve file
exported to MAST and provide a centroid motion time series for each
source. <br/>
<br/> The dominant source of long-term source motion for Kepler targets, differential
velocity abberation (DVA), is produced by the spacecraft motion during
each quarter. Each source traces a small elliptical arc across the
detectors over the period of Kepler's orbit. Source motions also may occur due to random pointing jitter, pointing drift, and focus
changes induced by thermal transients. For K2, low-frequency motion due to solar pressure and subsequent thruster firings causes targets to drift across detector pixels. <br/>
<br/>An example of a motion centroid time series for Kepler is shown
below. Motion of the nominal "center" of channel 1 (mod.out 2.1) is displayed for Q0. The large systematic drift is due to
differential velocity abberation. Since this channel is located at the
edge of the FOV, it also exhibits greater sensitivity to focus jitter
and drift. The total amplitude of the centroid motion is on order 0.1
pixels, equivalent to 0.4 arcseconds.

<img class="img-responsive" style="min-width:97%;" src="images/centroid_motion_drn5f4.jpg">

* **Astrometric solution**<br/>
PA performs a standard function of astronomical data pipelines:
assignment of celestial coordinates to detector pixels. On order 200
optimal sources are selected on each channel: bright, unsaturated,
minimally-crowded, main sequence stars. A 2-D polynomial fit is
constructed from the source row and column centroids for each channel
and cadence. Right ascension and declination for each pixel are
interpolated by mapping the polynomial fit to detector locations for a given output channel. The astrometric solution is
derived for each cadence independently.
 
 * **Computation of metrics**<br/>
 The PA module computes a variety of measures describing photometer
 performance, both as a health assessment and to support systematic
 error mitigation in following processing steps. <br/>

The output of this module is a photometric time series. These light curves are then passed to the Pre-Search
 Data Conditioning (PDC) for correction of systematic errors.

#### Pre-search Data Conditioning (PDC)

The PDC software module examines the calibrated light curves produced
by PA and applies a series of corrections, based on known
instrumental and spacecraft anomalies as well as unanticipated artifacts
found in the data. "Pre-search" refers to data conditioning prior to
executing a transit search, which was undertaken by the next module in
the pipeline (TPS) for the Kepler mission only.

For a large range of variable sources, the output of PDC
appears well aligned with the output of PA, the quality of the light
curves are improved after correction for systematic errors, and the
instrinsic variabilty preserved. Users should exercise caution if
their phenomena of interest are much shorter (<1 h) or much longer (>5
d) than transit timescales, or display complex light curves with
timescales similar to those expected for Earth-like transits (1-10
hrs), e.g., eclipsing binaries.

**PDC functions**

PDC is executed in single channel "chunks", in which all sources
located on a single channel ("mod.out") are processed through the
software. PDC executes the following tasks in the order listed:

* **Data anomaly flagging**<br/>
Observations affected by known anomalies are flagged to
exclude their use in systematic error corrections. Discrete
discontinuities are introduced into the light curves by known
spacecraft activities such as the monthly Earth point downlinks for Kepler, and
commanded attitude adjustments, and by unanticipated events, e.g., the
occasional safe mode. In addition to missing data, photometry may be
present for some cadences but in a degraded form due to planned
activities such as the reaction wheel desaturations (affects 1 cadence
every 3 days for Kepler), and unanticipated events, e.g., Argabrightenings
identified by PA, and loss of fine point.

* **Resample ancillary spacecraft data**<br/>
Engineering data is obtained on a variety of timescales. Before
correlating these data to the photometry, the ancillary data is
rebinned to match the sampling rate of the long and short cadence data.

* **Identification and correction of discontinuities**<br/>
In addition to known data gaps described above, source-specific flux
discontinuities have been observed. Many, but not all, random
flux discontinuities are likely caused by impacts of solar and
galactic cosmic rays on the CCDs. Impulsive energy deposition from
cosmic rays alters the photo-sensitivity of individual pixels, which
may recover on a variety of timescales. In this step, PDC identifies
discontinuities in the light curves, and estimates the flux
offset. Discontinuities are corrected on a single or multiple cadence
basis, using the estimated offsets.

* **Identify variable stars**<br/>
PDC attempts to separate "quiet" stars from variable sources, using a
tunable variability filter. Values of 0.5% and 0.25% center-to-peak
variation has been used in different data releases. This switch
determines the detrending options; variable stars are treated differently than
quiescent stars.

* **Identify astrophysical events**<br/>
Astrophysical events must be identifed, as best as possible, to
prevent those events from affecting the correlation of the
synchronized engineering data to the light curves. These signatures,
e.g., giant planet transits, stellar eclipses, flares and microlensing
events, are located in the calibrated light curves, and replaced
temporarily with values interpolated across relevant cadences.

* **Systematic error correction for quiet stars**<br/>
For sources below the variability threshold, the light curve is
compared to the resampled ancillary engineering data and centroid
motion time series to identify and remove correlated trends. This
process is termed cotrending in the Kepler documentation. A singular
value decomposition approach is utilized, to identify systematic
trends at many frequencies in the data which appear to be induced by
some spacecraft or detector process. An example would be an observed
flux variation correlated with periodic focus changes induced by
flexure in the optics. The goal of cotrending is to remove flux
signatures that are correlated with the ancillary data on the
specified time scales. During the first year of operation of the
Kepler mission, the project
 found that the systematic errors are caused primarily by target
motion at the pixel or sub-pixel level, which modifies the collected
signal. Cotrending against the centroid motion time series improves
the quality and noise content of the data. Another noise source is
thermal transients observed following safe modes and the monthly
downlinks. The changing thermal environment of the spacecraft
following these events induces focus changes, which alters the source
PSFs. These transients last a few days (1 day = 48 30-min
observations), affecting a few hundred long cadence
datapoints. Users should note that low amplitude periodic astrophysical
signals which are correlated with the ancillary data will likely be
compromised in the Kepler data.

* **Systematic error correction for variable stars**<br/>
For sources exceeding the variability
threshold, PDC attempts to model periodic behavior, in order to fit
and remove this component and correlate against the underlying light
curve. Smoothly varying stars
are generally well-fit by PDC, preserving the astrophysical signal,
and reducing the noise level. For stars tagged as variable, the
following steps are taken:<br/>
<br/>
(a)   Correct for thermal transients and differential velocity aberration. <br/>
(b)   Fit the periodic content. If successful, remove the fitted harmonic content from the light curves. <br/>
(c)   Apply the cotrending procedure to the residual light curve. <br/>
(d)   Apply metrics to assess the results. <br/>
(e)   Choose the non-variable or variable cotrending result for each target initially identified as variable. <br/>
<br/>For some sources, the cotrending has been found to produce
unacceptable results. In these situations, the calibrated light curve
(PA output) is substituted for the cotrended light curve (PDC output). For these
targets, systematic effects which are a component of the cotrending
algorithm are not addressed in PDC.<br/>
<br/>An example of PDC systematic error correction for a variable star
observed by Kepler
without a strong periodic component is shown below. The star is variable on short
time scales; over Q3 two discontinuities are observed, along with a
linear term produced by differential velocity aberration. (Adapted
from DRN5.)<br/>

<img class="img-responsive" style="min-width:97%;" src="images/PDC_example3_quietstar_drn5.jpg">

* **Correct excess flux**<br/>
Some of the signal within the optimal aperture arises from the PSF
wings of nearby sources, contaminating the signal from the target. PDC
subtracts an estimate of this excess flux, based on a source-specific
crowding metric, defined as the fraction of starlight arising from the
target star. This metric has a range of [0-1], where 1 implies all
light comes from the target, and 0 = all background. Simple aperture
photometry produced by PA is not corrected for source crowding. The
crowding metric is derived for Kepler targets from the distribution of surrounding stars
as tabulated in the KIC, and the measured structure of the
pixel-response functions of the source and nearby stars. Since each
source is observed on a different location of the focal plane each
quarter due to the quarterly roll, the PRFs, optimal
apertures, and crowding metric are defined for each quarter. Users will see an offset in flux level when plotting PA output
versus PDC output. The offset is a measure of the source contamination
correction.

* **Identification of outlying data points**<br/>
PDC searches for data points lying
outside (+/-) an adjustable range. A median filter is applied after
masking of potential astrophysical events, such as giant planet
transits, stellar flares, and microlensing. After removing the median,
the residual light curve is examined for points lying further than a
pre-set value. In the subsequent transit search phase for Kepler, flagged points
are filled ("gapped") via interpolation. However, light curves
available in the archive at MAST do not have outliers removed; the
data is unaltered for user interpretation.

**Performance and cautions**

The Kepler data pipeline was originally optimized for transit
searches. We note here some precautions for working with the
conditioned data (PDC).

Kepler is more sensitive then any previous photometer producing
near-continuous time series. The mission is also exploring a
variability domain not previously accessible. Therefore, we are
encountering subtleties in the data and the data processing not seen
before. 

Users are reminded to compare the calibrated light curve (PA) to the
corrected light curves (PDC), to ascertain the reliability of any
astrophysical signature in your data. Following are examples of
specific situations found in PDC output of which the user should be
aware:

(a)   Fails to identify and correct a source-specific discontinuity. <br/>
(b)   Poor detrending may introduce noise into complex lightcurves. <br/>
(c)   May identify a stellar eclipse as a flux discontinuity. <br/>
(d)   Fail to accurately track slowly rising or declining flux levels over a quarter. If this linear term is correlated with centroid motion times series, the linear term may be removed from the data. <br/>
(e)   Positive outliers which are not flagged as real events. PDC may tag these events as discontinuities, and attempt to correct. 

<img class="img-responsive" style="min-width:97%;" src="images/PDC_example_Jenkinsb_fig3.jpg">

Output of PA (top curve) and PDC (bottom curve) for a variable star
observed during Q1. This source displays periodic behavior with ~1%
peak-to-peak amplitude on a timescale of ~5 days. The figures show
that the overall source variability is preserved by PDC. Systematic
noise introduced by an onboard heater can be seen as the short period
wiggles in the upper light curves. This noise is removed by PDC as the
noise signal is correlated with ancillary engineering data.

Kepler is sensitive to an enormous volume of variability phase
space. Overall, the corrected light curves are
excellent probes of the underlying variations on a wide range of
sources. In broad terms, users should be cognizant of three types of
phenomena for which the validity of the corrected light curves warrant
caution:

(1) Low amplitude (10s-100s PPM) variability with periods > 10 days. <br/>
(2) Strongly episodic variable stars, such as cataclysmic binaries. PDC may flag eruptive phenomena as discontinuities, or attempt a fit which may unintentionally modify the data. <br/>
(3) Complex light curves, exhibiting multiple varying components, for
example and eclipsing binary with one or both components also
variable.

### Calibration of Kepler data

#### Orbit

Kepler is in an Earth-trailing heliocentric orbit, which insured a
thermally stable environment and provided the ability to remain on a
single pointing for the duration of the prime Kepler
mission. Quarterly rolls were performed – one roll every 93 days – to
reorient the solar arrays. With each roll, the stars in the field of view land on different regions of the detector relative to their pre-roll position, introducing quarterly discontinuities in the light curves.

#### Field of view

The Kepler photometer consists of 21 CCD modules (each with two 2200x1024
pixel CCDs).  Each module covers 5 square degrees on the sky.  The full 116
square degree field of view on the sky is illustrated below.  Tables that contain the corners of each Kepler CCD
module are available for download ([ascii](data/morc_2_ra_dec_4_seasons.txt) and [Microsoft Excel](data/morc_2_ra_dec_4_seasons.xls)).
Corners are provided in J2000 celestial coordinates for all four seasonal roll rotations.

<img class="img-responsive" style="min-width:97%;" src="images/Keplerfieldofviewstarchart.gif">

#### Instrument response

The primary instrument aboard Kepler is the focal plane array
consisting of 21 science and 4 Fine Guidance Sensor CCD modules. Field
flattener lenses on each module map the spherical telescope image
surface onto the flat CCD chips, and define the overall wavelength
bandpass. Each science module is an array of 2200x2048
pixels. These 21 modules each have 4 output channels, for a total of
84 channels and 94.6 million active pixels that view the sky, with
additional masked real pixels and virtual pixels for collection of
collateral data.  As of May 2014, two of the modules are no longer in
working order.

<img class="img-responsive" style="min-width:97%;" src="images/kepler_CCDarray.jpg">
<img class="img-responsive" style="min-width:97%;" src="images/kepler_focalplane1.jpg">

The Kepler focal plane detectors and the optical elements within the
Kepler telescope are illustrated above (from the [Kepler Instrument Handbook](data/documentation/KSCI-19033-001.pdf)).

The Kepler photometer utilizes one broad bandpass, ranging from 420
to 900 nm. Tables containing the Kepler instrument
response curve in [hi-res](data/kepler_response_hires1.txt) and
[low-res](data/kepler_response_lowres1.txt) tabulations are available
for download. The shape of the bandpass, shown below, was chosen to contain most
of the optical spectrum. This response curve was
derived during pre-flight testing and
represents the laboratory calibration of the Kepler photometer. 

<img class="img-responsive" style="min-width:97%;" src="images/kepler_response1.jpg">

<img class="img-responsive" style="min-width:97%;" src="images/kepler_response2.jpg">

The above plot shows the optical element components of the Kepler Instrument Response compared
to approximate M5 and G2 stellar spectra. The total photometer spectral response is a combination of the
transmission functions of all optical elements, including the Schmidt
corrector, the primary mirror assembly, the field flatterner lenses on
each CCD module, and the wavelength dependent quantum efficiency of
the detectors. The front surfaces of the field flatteners are
anti-reflection coated; a bandpass filter coating was applied to the
back surfaces. At long wavelengths the coating was designed to minimize
fringing.

<img class="img-responsive" style="min-width:97%;" src="images/kepler_bandpass_jason1.jpg">

The above figure shows a comparison of the Kepler, MOST, CoRoT and Johnson response
curves (kindly provided by Jason Rowe and extracted from
2009IAUS..253..121R). The transmission functions for the Johnson B,V,R,I
filters have been scaled to peak at 100% transmission. The
spectrum for an A2V star is shown in cyan, which peaks in the UV and
the spectrum for a M2V star is shown in orange which peaks in the
infrared. The two spectra have been scaled to have equal flux in the
Johnson V filter.

#### Pixel response function

Kepler has an image scale of 3.98 arcseconds per pixel and a pixel
size of 27 × 27 microns.

The design requirements for Kepler emphasize photometric stability
and minimizing noise sources. Users should recognize that
the optimum focal plane geometry for flux collection will not in
principle provide the most compact point spread function, as is
usually desired for imaging experiments. 

The Kepler point spread function varies considerably across the focal
plane due primarily to the Schmidt optics, which provide a large FOV
approximately 16° in diameter. The Project quantifies the total
response of the instrument to incident light in terms of its pixel
response function (PRF), which represents the observed appearance of point
sources. The PRF is a combination of the optical design, focus
setting, CCD detector mechanical and electronic properties, and the
temporal sequence of spacecraft pointing stability during an
observation. Not only does the PRF depend on location within the
focal plane, as defined by a source's CCD channel, row and column
location, but also depends on the intrapixel location of the source
centroid (peak incident light). A detailed summary of the
characteristics and modeling of the PRF is provided by [Bryson et al.
(2010)](http://adsabs.harvard.edu/abs/2010ApJ...713L..97B).

Users should note that light curves are produced using optimal aperture photometry in the
 PA module via straightforward addition of the flux within the optimal source aperture. No PRF-fitting is involved in this photometry, but
  each source's optimal aperture is defined by the interpolated PRF at
  the source location, coupled with the source brightness and a model
  of the background.

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

During the commissioning period for Kepler, the focus was adjusted, and the
resulting PRFs measured, using a large set of test stars. Shown below is a representation of the PRF at two locations in the focal
plane. On the left: a PRF from near the edge; on the right: a PRF near
the center. The pixelated image is shown below and a contoured version
above. (Adapted from [Bryson et al.
(2010)](http://adsabs.harvard.edu/abs/2010ApJ...713L..97B)).

<img class="img-responsive" style="min-width:97%;" src="images/bryson_prfs1.jpg">

For K2, image quality continues to vary with position in the focal plane, with the 95% encircled energy diameter ranging from 3.1 to 7.5 pixels and a median of 4.2 pixels. The percentage of point-source flux concentrated in the center pixel is between 20% and 62%, with a median value of 45%.

**Vignetting**

Vignetting affects the PRF at increasing
distance from the center of the FOV, a consequence of the Schmidt
optical design and large FOV. Somewhat less than half of the active
FOV is unvignetted, and another ~30% is affected, but considered
usable. Vignetting is negligible within 4.6° of the center, and
increases to ~11% at the edge of the FOV at 6.94 degrees off-axis. The
area of sky which is vignetted < 11% is 151.2 square degrees, and the
sky area imaged onto active pixels with < 11% vignetting is 101 square
degrees since there are gaps between modules, a gap between the two
CCDs on each module, and inactive areas on each CCD. 

#### Backgrounds

Source photometry is affected by both celestial and instrumental
backgrounds. During nominal science data collection, pixels designated
as background are measured in addition to target pixels. These data
are used to correct the photometry within the Photometric Analysis (PA)
pipeline module. For Kepler, a separate set
of background apertures are collected across the focal plane, and a
background measure is derived from these pixels. Users should note that the
pipeline does not use pixels within the source aperture to measure the
local background.

**Components**

Celestial backgrounds arise from a number of sources, both from
spatially smooth, diffuse light which affects all pixels in the
aperture, and from transient events, which affect a few pixels:

* Zodiacal light, produced by sunlight scattered from dust in the
ecliptic plane.
* Diffuse scattered starlight, produced by dust in the Galaxy. In the
  fixed field of view for the
  Kepler mission, the Galactic component shows a spatial gradient,
  increasing at lower Galactic latitudes. 
* Unresolved starlight. Given the 4x4 arcsec dimensions of the
  pixels, some light in the aperture arises from faint field stars. As
  with the diffuse Galactic emission, the contribution from unresolved
  starlight increases with decreasing Galactic latitude. 
* Cosmic ray impacts which corrupt individual pixels. The pipeline
   flags and removes cosmic ray events from the pixel counts,
  within the PA pipeline module. Each cosmic ray event is
  replaced with a temporally local average of the pixel's time series
  without the cosmic ray pixel events. 
* Surrounding sources, i.e. the residual wings of the PSFs produced by nearby
  stars which may overlap the PSF of the target. A correction for contaminating flux in the source aperture
  produced by surrounding sources is applied within the PDC pipeline module - a single valued subtraction, termed the crowding metric. In
  ideal situations the PSFs of neighboring stellar sources would not
  change over time, expect for possible intrinsic source
  variabilty. Observers should be aware that spacecraft operations may
  induce changes in the source PSFs, through focus changes, and
  spacecraft motions (jitter and drift). Motion of the source center
  during an observing season, even at the millipixel level, will
  induce variations in the contaminating flux, introducing small
  levels of noise into the light curve. </br>

Instrumental backgrounds include the detector bias level (also termed
black level), which is removed in the CAL pipeline module, scattered light, unexpected electronic
issues discovered during pre-flight characterization of the detectors,
and some features seen during early flight operations,
e.g., "Argabrightening", an anomalous full-field illumination. Spatially varying backgrounds produced by the detector
electronics are fully described in the [Kepler Instrument Handbook](data/documentation/KSCI-19033-001.pdf). 

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
management, background pixels are selected,
avoiding stars and locations affected by charge bleeds.

Background pixels are calibrated in the same manner as source pixels
in the CAL pipeline module. Background channel maps are generated in
PA; interpolated background values are then subtracted from the pixel
values prior to aperture photometry.

A measure of the celestial background in the Kepler FOV is provided in
the Kepler data release notes. The figure below shows the
background flux time series for the Q0+Q1 observing season, derived
from the reprocessed data released on 2010 June 15. The curves show
average over all mod.outs (CCD channels), the modules furthest from
(mod.out 2.4 = channel 4) and nearest to (mod.out 24.4 = channel 84)
the Galactic plane. The vertical offset is produced by the
spatially-dependent Galactic emission; the horizontal trend is caused
by variation in the zodiacal light. The narrow spikes visible in all 3
curves are Argabrightening events. From this plot, a few items are
evident:

* The temporal and FOV-averaged value background value is ~2.7 × 10−5
  electrons per cadence. This value corresponds to the expected signal
  from a star with Kp ~ 18.3.
* The difference in background counts produced by viewing
perpendicular to the Galactic plane is about a factor of 1.8.

<img class="img-responsive" style="min-width:97%;" src="images/kepler_background_Q0+1.jpg">

 The treatment of the background by the pipeline for
crowded sources may not be optimal. Users should inspect the FOV around sources using a Kepler full-frame
image to check for nearby bright sources which may affect a target. Also note saturated stars in
the same (+/-1) column to check for charge
bleeds.  Users may wish to contruct their own background estimates
using the background pixel files available on the data archive at MAST.

#### Signal-to-noise properties

The following plot provides an ensemble comparison of Kepler
three-wheel fine-point precision (red), K2 two-wheel coarse-point
precision (green) and K2 two-wheel fine-point precision (blue). The
red lines are carefully-selected quiet G dwarfs, falling upon
arbitrary modules of the Kepler detector.

<img class="img-responsive" style="min-width:97%;" src="images/Feb2014Precision.png">

The limiting factor for observations of faint sources is set by source
confusion, rather than the photometric accuracy computed for isolated
sources. Users wanting to observe objects with Kepler magnitudes fainter
than 17.0 should carefully examine the field around their source and
estimate the contamination from the PSFs of surrounding objects. Note
that an estimate of the crowding metric is provided for most sources
brighter than Kp = 17.0 in the data archive at MAST (under the
field labeled "Contamination"). Contamination is defined as (1 - crowding_value), where the
crowding value was derived when the target catalogs were created. A value of 0 implies no contamination, 1 implies essentially
all background, i.e., complete contamination of the source by
surrounding objects. For fainter sources, observers can estimate the
contamination using imagery from databases like the Digital Sky Survey
or [UKIRT](data-access.html#keplerukirt), supplemented
with the Kepler or K2 Full Frame Images (FFIs) as the latter become
available.

For bright sources, the observed signal in the central pixel(s) will
increase linearly until the well depth is reached. Beyond that level,
charge will bleed into adjacent pixels in the column containing that
source. However, even when the central pixel is saturated, the target
aperture can extend along the bleed column, preserving most or all of
the signal from the source. 

#### Flux calibration

Each target observed by Kepler or K2 had or has a pre-set observing aperture uploaded to the
spacecraft. These apertures are defined in terms of the number of
pixels and shape of the array. The brighter a source, the larger the
aperture needed to collect the photons for an optimal detection of
that source. Aperture size is primarily defined by the source's Kepler
magnitude (Kp), a measure of the source intensity as observed through
the wide Kepler bandpass.

The Kepler Science Team conducted an extensive observing program
  prior to launch in order to classify stars in the FOV. The
  fundamental goal was to develop a list of FGKM dwarf stars as the
  primary source list for exoplanet detection. Objects were observed
  in the SDSS griz bands. This photometry, along with 2MASS data form
  the basis of the Kepler Input Catalog.  The Project constructed a set of stellar spectral
  synthesis models covering a range of effective temperature, gravity
  and mean abundance, and derived g,r,i,Kp magnitudes by convolving
  the filter response functions with the models. Using correlations
  between these values, Kepler magnitudes are estimated from the
  observed SDSS magnitudes using empirical formulae.
  
An approximate
  estimate of Kp can be derived using the following expression, which
  is based on the empirical relations used by the Kepler Stellar
  Classification Program. A user can convert B,V into
SDSS g,r using the transformation derived by Smith et al. (2002 ApJ 123,
2121, Table 7), shown in line 1 and 2 below.  If SDSS g,r values are available, the conditional
statements in line 3 and 4 below can be used.

(1) g   =   0.54 B   +   0.46 V   −   0.07 <br/>
(2) r   =   −0.44 B   +   1.44 V   +   0.12 <br/> 
(3) if   ( g − r )   ≤   0.8    then    Kp   =   0.2 g   +   0.8 r <br/>
(4) if   ( g − r )   >   0.8     then    Kp   =   0.1 g   +   0.9 r <br/>

This expression is accurate to about ±0.2 mag for stars hotter than
3500 K. For M stars, users are cautioned that systematic errors may
exceed 0.6 mag, i.e. Kp returns magnitudes that are too
faint.

Given a calibration of (B−V) color with spectral type (effective
temperature), a Kepler magnitude can be estimated. Values for (Kp−V)
are presented below for main-sequence stars, based on the above
relation. This color can be applied to stars whose apparent Johnson V
magnitude is known to obtain Kp, with the caveat that for stars cooler
than M0, the estimated Kp may be too faint.

<table class="table table-striped table-hover" style="max-width:10em;">
  <thead>
    <tr>
      <th>Spectral Type</th>
      <th>B-V</th>
      <th>Kp-V</th>
    </tr>
  </thead>

  <tdata>
      <tr>
      <td>O3</td>
      <td>-0.33</td>
      <td>+0.16</td>
      </tr>
	  
     <tr>
      <td>B0</td>
      <td>-0.28</td>
      <td>+0.15</td>
      </tr>

     <tr>
      <td>B5</td>
      <td>-0.16</td>
      <td>+0.12</td>
      </tr>

     <tr>
      <td>A0</td>
      <td>-0.01</td>
      <td>+0.08</td>
      </tr>

     <tr>
      <td>A5</td>
      <td>+0.13</td>
      <td>+0.05</td>
      </tr>

     <tr>
      <td>F0</td>
      <td>+0.28</td>
      <td>+0.01</td>
      </tr>

     <tr>
      <td>F5</td>
      <td>+0.46</td>
      <td>-0.03</td>
      </tr>

     <tr>
      <td>G0</td>
      <td>+0.60</td>
      <td>-0.06</td>
      </tr>

     <tr>
      <td>G5</td>
      <td>+0.67</td>
      <td>-0.08</td>
      </tr>
 
    <tr>
      <td>K0</td>
      <td>+0.85</td>
      <td>-0.13</td>
      </tr>
	  
	     <tr>
      <td>K5</td>
      <td>+1.15</td>
      <td>-0.29</td>
      </tr>

   <tr>
      <td>M0</td>
      <td>+1.55</td>
      <td>-0.43</td>
      </tr>

</tdata>
</table>

#### Astrometry

Source coordinates are provided by the Kepler Input Catalog
(KIC) or the Eplictic Plane Input Catalog (EPIC) for K2. Astrometric calibration of
the source centroids occurs in the PA pipeline
module. Precise centroids of sources within the target aperture
permits correction of the photometry for spacecraft motions during the
observing season.

The focal plane array contains significant gaps between the detectors,
designed to exclude very bright stars from falling into photo-active
pixels (for the Kepler mission).  These gaps will cause some sources,
which appear to lie on the FOV, to actually be not observable. K2 observers should carefully check to see if their
proposed sources land on active silicon using the [K2fov tool](software.html#k2fov).

**Source astrometry**

The source of the astrometry depends on which
catalog (or catalogs) contain data for that source.  Those catalogs are listed here, with an estimate
of their positional accuracy.  Additional information can be found in
the documentation for the KIC and the EPIC.

  1. Kepler Stellar Classification Program; 50 milliarcseconds, data obtained closer to the Kepler epoch, minimizing proper motion offsets 
  2. Hipparcos; 10 milliarcseconds 
  3. Tycho-2; for V brighter than 8.0; 20 milliarcseconds 
  4. UCAC2; 40 milliarcseconds 
  5. 2MASS; 70 milliarcseconds 
  6. USNO-B1.0; 200 milliarcseconds

**Observed astrometry**

Image centroids are calculated as part
of the calibration pipeline, within the PA pipeline module. PA computes flux-weighted mean centroids for all stars, which
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

The full frame images were designated as engineering data by
the Project, and no astrometric calibration was initally
intended. MAST developed an astrometric solution for the 8 Golden
full-frame images, using the public astrometry.net tool, developed by
Blanton, Hogg, Lang, Mierle & Rowies. These 8 FFIs were taken under
ideal pointing and thermal stability at the start of the mission, and
are available at the data archive at MAST.

**Astrometric science with Kepler**

The high signal-to-noise ratios achieved with Kepler permit a high
level of astrometric accuracy, despite the large pixel scale and large
field of view. In principle the Kepler data can be used to determine
parallaxes and proper motion for tens of thousands of stars, and
explore more subtle motions, hinting at planetary companions. Based on
analysis of the Q0+Q1 data, [Monet et al. (2010)](http://adsabs.harvard.edu/abs/2010arXiv1001.0305M) provide an estimate of Kepler's
astrometric precision of ~4 milliarcseconds over a single 30 minute
observation (1 long cadence).

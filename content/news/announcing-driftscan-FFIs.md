Title: Announcing experimental driftscan Full Frame Images
Date: 2018-06-01 08:00
Author: Michael Gully-Santiago


We recently carried out a short pilot program on a new, experimental data collection
mode for the Kepler Space Telescope.  We collected Full Frame
Images (FFIs) while the field of view was drifting at ~0.3-0.5 arcseconds
per second, much higher than during normal science operations.  We are calling
the resulting images *driftscan Full Frame Images*.  These images may facilitate
in-situ focal plane characterization and self-calibration, ultimately useful for scene modeling
and Point Spread Function (PSF) photometry in crowded regions like star clusters or in extended objects.

Five driftscan FFIs we acquired on May 10-11, 2018, during the K2 Campaign 17 (C17) Deep Space
Network (DSN) downlink, after all C17 science data had been safely telemetered
and spare DSN time remained.  In this configuration, the spacecraft antenna points
towards Earth; driftscan FFIs are telemetered back immediately after acquisition.

Driftscanning will produce long overlapping star-trails on the FFI, rather
than conventional sharp point-sources.  The star trails extend over ~150 +/- 20
pixels, corresponding to an average drift rate of ~0.35 arcseconds per second.
The direction of pointing of the telescope was not known a-priori, but can
 in principle be derived from the distinct constellation pattern of star trails.  

The driftscan FFIs were acquired with the same combined exposure time as
conventional 30-minute Long Cadence FFIs, *i.e.* 270 onboard-coadded
integrations with 6.02s exposure time and 0.52s readout time per
integration.  The DFFIs were collected within 16 minutes to 5 hours of the
previous frame, such that star trails can be seen moving across module
boundaries from frame-to-frame.

The star trail line segments possess substructure suggestive of non-constant
image motion.  A longer-than-average dwell time of a point source causes regions of
"burn-in", while shorter-than-average dwell times cause relative dearths in flux.  The
resulting undulations appear in all the star trail line segments for a given
driftscan FFI.  The line segment substructures could also arise from the
shutterless image array transfer process occurring in phase with constant
image motion, yielding a "beating" phenomenon within pixel boundaries.

The driftscan FFIs may enhance flat-field calibration of the Kepler focal
plane, since the relative response of adjacent pixels can be derived by
identifying local departures from the expected star trail illumination pattern.
Other uses for driftscan FFIs may eventually include solar system science and
short-timescale (few seconds) variations of bright astrophysical sources.

This data should be considered experimental, and will not be
pipeline-processed due to its irregular star trail patterns.

The image below shows a portion of one channel of one driftscan FFI.  The
raw driftscan FFIs will soon be available on the MAST archive as FITS files with
similar file format as conventional raw FFIs.  A link to the data will be updated
 here when available.

Two presentations available online summarize the [motivation for FFI driftscans](https://docs.google.com/presentation/d/1qvK2vxBs1kMth0pgf-fBW4T1iGtU3e1-xCrVgHmMHxU/edit?usp=sharing),
and [preliminary FFI analysis](https://speakerdeck.com/gully/k2-driftscan-ffi-analysis).


<a href="images/driftscan_FFI_demo.png"><img class="img-responsive" style="max-width:600px;" src="images/driftscan_FFI_demo.png" alt="driftscan FFI demo"></a>

Title: Problem with Kepler and K2 short cadence pixel calibration
Date: 2016-02-04 13:00
Author: Geert Barentsen

A K2 Guest Observer notified the Kepler Science Center in November 2015
of a puzzling difference between the short- and long-cadence
calibrated pixel data for a specific K2 target.

After investigation, the problem was traced to an accounting error
for the short-cadence collateral smear data.
Under some conditions, these data are passed incorrectly
between the spacecraft and the ground, causing smear values to be
assigned to the wrong columns within a target’s aperture.

In these cases, the pipeline’s pixel-level calibration routine
applies an erroneous smear correction.


### Impact

The issue has been present since launch and affects both the target pixel
files and the light curves of approximately
half of all short-cadence targets in all releases to date,
i.e. Kepler Data Releases 1-24 and K2 Data Releases for Campaigns 0-5.
A list of all the affected targets is attached below.

Since the smear signal is often small compared to the target signal,
the effect is negligible for many targets.
However, the smear signal is scene-dependent,
so time-varying signals can be introduced into an affected target
by the other stars falling on the same CCD column.

To assess the impact on affected targets,
users should inspect the calibrated target pixels
(see Section 2.3.2 of the [Kepler Archive Manual](https://archive.stsci.edu/kepler/manuals/archive_manual.pdf)).
An improperly corrected smear signal may show up as an anomalously bright,
or dark, column in the calibrated target pixel image.
Comparison of the short-cadence pixel image with the long-cadence pixel image
(which is not affected by this problem)
can be used to estimate the magnitude of any contaminating signal.


### Solution

The Kepler pipeline has been amended to ensure that the 
correct smear data is used at all times. 
All affected data will be corrected as follows:

 * All upcoming K2 data releases will be corrected from the start,
 beginning with Campaign 6. (The release of C6 short cadence data will be delayed by approximately two weeks as a result.)
 * Reprocessing of K2 Campaigns 0-5 will occur over the coming months. The expected release dates will be listed here when known.
 * Data from the prime Kepler mission will be corrected as part of the scheduled reprocessing with pipeline release 9.3 (DR25). Corrected target pixel files are expected to be available in Summer 2016.


###  More information 

The project has released an erratum document describing the issue and
its impact in more detail.
The document is accompanied by a list of all the affected targets:

* [KSCI-19080-001.pdf](data/documentation/KSCI-19080-001.pdf)
* [kepler_bad_short_cadence_target_list.csv](data/documentation/kepler_bad_short_cadence_target_list.csv)
* [k2_bad_short_cadence_target_list.csv](data/documentation/k2_bad_short_cadence_target_list.csv)

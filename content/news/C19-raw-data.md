Title: K2 Campaign 19 raw data available
Date: 2018-10-16 10:00
Author: Geert Barentsen

The Kepler spacecraft has successfully downloaded Campaign 19 data to Earth.
To enable users to make use of the current visibility of the Campaign 19 field
from the ground, the raw cadence data files have been made public immediately
via the [K2 data archive at MAST](http://archive.stsci.edu/missions/k2/raw_cadence_data/). 

The use of the raw, uncalibrated data files requires an intimate understanding
of their format and caveats (see the [kadenza tool](https://github.com/KeplerGO/kadenza)).
For scientific investigations that are not time-critical,
we recommend that users wait for the calibrated and quality-controlled
data products to become available in approximately 3 months.

Campaign 19 included TRAPPIST-1.
Uncalibrated Target Pixel Files for this planet system have been created using 
[kadenza](https://github.com/KeplerGO/kadenza) and are available
via [DOI 10.5281/zenodo.1464259](http://doi.org/10.5281/zenodo.1464260):

* Long cadence: [k2c19-trappist1-lc-raw-tpf.fits.gz](
https://zenodo.org/record/1464260/files/k2c19-trappist1-lc-raw-tpf.fits.gz) (1 MB)
* Short cadence: [k2c19-trappist1-sc-raw-tpf.fits.gz](https://zenodo.org/record/1464260/files/k2c19-trappist1-sc-raw-tpf.fits.gz) (25 MB)

The Campaign 19 data are shorter and somewhat less stable than previous K2 Campaigns.
Owing to Kepler's low fuel pressure, the [spacecraft's configuration had to be modified](k2-campaign-19-status-update.html) at the start of Campaign 19 to compensate for the unusual behavior exhibited by one of the thrusters.
The Campaign started collecting data on Aug 30, achieved its nominal
pointing on Sep 7, and was ended on Sep 26 in response to 
a [further degradation in the spacecraft's pointing performance](k2-campaign-19-ended-to-downlink-data.html).

Title: Reprocessed data for K2 Campaign 1 now available
Date: 2016-12-06 14:00
Author: Geert Barentsen

The original data release for K2 Campaign 1 in 2014
used a prior version of the pipeline (v9.2)
which only produced "Type-1" FITS Target Pixel Files.
The Campaign has now been re-processed using the mature 
version of the pipeline (v9.3)
which updates the pixel files to "Type-2" TPFs
([differences detailed here](/k2-data-release-notes.html#type1v2)). 
The new release also adds long-cadence lightcurves,
cotrending basis vectors, and collateral products such as smear data.

The re-processing also corrects a [short cadence calibration
bug](/problem-with-kepler-and-k2-short-cadence-pixel-calibration.html). 
Short cadence targets with significantly improved calibration
are identifed in the
[list of affected targets at the MAST](http://archive.stsci.edu/missions/k2/catalogs/K2_scrambled_short_cadence_collateral_target_list.csv).

Finally, the [C1 data release notes](/k2-data-release-notes.html#k2-campaign-1)
have been updated to include more details on the data characteristics,
and to explain issues associated with the first few days of data
which were taken before a pointing tweak.

The reprocessed Campaign 1 data are now available from the
[K2 data archive at MAST](https://archive.stsci.edu/k2).
Campaigns 0 and 2 are currently undergoing a similar reprocessing effort
which is expected to be completed in early 2017,
at which point all Campaigns will have been processed using the same version
of the pipeline.

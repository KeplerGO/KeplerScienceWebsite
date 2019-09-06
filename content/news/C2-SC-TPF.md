Title: Corrected C2 Short-Cadence TPFs Released
Date: 2019-09-06 12:00
Author: Jeff Coughlin

Previously we announced that [some recently reprocessed short-cadence target pixel files from C2R, C3R, and C5R were incorrectly calibrated](incorrect-pixel-level-calibration-of-short-cadence-tpfs-for-some-c2r-c3r-and-c5r-targets.html). We estimated that of the 474 short-cadence targets in those campaigns, 175 were possibly affected at any level, and ~25% of those 175 were affected at a non-negligible level.

At the time of that announcement, there was correctly calibrated data available for all affected C3 and C5 targets from previous processings that researchers could use if any of their targets were affected. However, there was no correctly-calibrated previous processing available for C2.

Starting today, correctly processed target pixel files for all 54 short-cadence C2 targets are [now available from MAST in this directory](https://archive.stsci.edu/missions/k2/target_pixel_files/old_release_bundles/c2/old_release_files/). These data were produced by an older version of the pipeline right before the start of the [global uniform reprocessing effort](k2-uniform-global-reprocessing-underway.html) that were never delivered to MAST, until now. This data is described in the [Data Release 34 Pipeline Release Notes](k2-pipeline-release-notes.html#data-release-34) &mdash; in brief, compared to the most recent C2 data ([Data Release 21](k2-pipeline-release-notes.html#data-release-21)) produced as part of the uniform reprocessing effort, it lacks the more sophisticated pixel-level calibration technique ("Dynablack") and does not have rolling band flags in the FITS files.

Researchers whose targets are affected by the [incorrect calibration](incorrect-pixel-level-calibration-of-short-cadence-tpfs-for-some-c2r-c3r-and-c5r-targets.html) are advised to use these files. Of the 54 short-cadence C2 targets, 44 were affected at any level, [as listed in this file](/data/documentation/k2_reproc_c2_c3_c5_bad_short_cadence_target_list.csv).

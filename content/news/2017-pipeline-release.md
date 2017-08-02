Title: Open source release of the Kepler data processing pipeline
Date: 2017-08-01 16:00
Author: Geert Barentsen

The source code for the official Kepler data processing pipeline
has been released to the public under the NASA Open Source License,
and made available for download via the GitHub repository at [https://github.com/nasa/kepler-pipeline](https://github.com/nasa/kepler-pipeline).
The release is accompanied by a [Source Code Roadmap](https://github.com/nasa/kepler-pipeline/raw/master/kscrm.pdf) (pdf)
which presents an overview of the various pipeline components
found in the source code directory tree.

Users interested in the development of the underlying algorithms
should refer to the [Kepler Data Processing Handbook](https://archive.stsci.edu/kepler/manuals/KSCI-19081-002-KDPH.pdf) (pdf) which, together with the source code,
represents the documentation of the algorithms used
to produce the final target pixel files, light curves, and list of transit Threshold Crossing Events ([TCEs](https://exoplanetarchive.ipac.caltech.edu/docs/Kepler_TCE_docs.html)) for the final Data Release 25 of Kepler's original mission in the Cygnus field (DR25).

A separate codebase, called the RoboVetter, was used to classify the TCEs into planet candidates and false positives for Kepler's DR25 planet catalog.
This code is available in a separate repository at [https://github.com/nasa/kepler-robovetter](https://github.com/nasa/kepler-robovetter) and will be described in a forthcoming paper led by Susan Mullally et al (in prep).

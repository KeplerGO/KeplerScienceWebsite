Title: Kepler and K2 data products
Save_as: data-products.html

[TOC]

There are two archives for *official* Kepler and K2 data products -
the [Exoplanet Archive](http://exoplanetarchive.ipac.caltech.edu/)
which is hosted at the
[NASA Exoplanet Science Institute (NExScI)](http://nexsci.caltech.edu/)
and the
[Mikulski Archive for Space Telescopes (MAST)](https://archive.stsci.edu/)
which is hosted at the
[Space Telescope Science Institute (STScI)](http://www.stsci.edu/). The
Exoplanet Archive primarily hosts data related to the Kepler and K2 mission planet searches while the MAST is responsible for hosting time series data and spacecraft calibration products for Kepler and K2. 

In the following sections we list the main products from Kepler and
K2, and we describe a few of the products in some detail.  For tools
and tips on
inspecting and analyzing Kepler or K2 data, [users should check out this page](software.html).

## Documentation

We encourage users of Kepler and/or K2 data to read through the
documentation associated with the Kepler and K2 data products.
There is documentation specific to the [Kepler data products](https://archive.stsci.edu/kepler/data_products.html) and to the
[K2 data products](https://archive.stsci.edu/k2/data_products.html).
Users of K2 data should note that much of the Kepler documentation is
also relevant to K2.  Additional documentation can be found
[here](https://archive.stsci.edu/kepler/documents.html) or can be downloaded directly by following the links
below.

* [Kepler Archive Manual](http://archive.stsci.edu/kepler/manuals/archive_manual.pdf)
* [Kepler Instrument Handbook](data/documentation/KSCI-19033-001.pdf) and [Supplement](data/documentation/KSCI-19033-001_supplement.tar)
* [Kepler Input Catalog (KIC)](http://adsabs.harvard.edu/abs/2011AJ....142..112B)
* [Kepler Data Characteristics Handbook](http://archive.stsci.edu/kepler/manuals/Data_Characteristics.pdf)
* [Kepler Data Processing Handbook](http://archive.stsci.edu/kepler/manuals/KSCI-19081-001_Data_Processing_Handbook.pdf)
* [Kepler Data Release Notes](data-products.html#kepler-data-release-notes) 
<br/>
* [K2 Ecliptic Plane Input Catalog (EPIC)](https://archive.stsci.edu/k2/epic.pdf)
* [K2 Data Release Notes](data-products.html#k2-data-release-notes)

## Kepler product overview

The [Kepler mission page at MAST](https://archive.stsci.edu/kepler/) contains the latest news and updates
on Kepler products. The following Kepler data products and catalogs are available
through MAST and can be downloaded
[here](https://archive.stsci.edu/kepler/data_products.html):

**Data products at MAST**

* Long and short cadence target pixel files
* Long and short cadence light curves
* Data validation time series files
* Full frame images (calibrated and uncertainty files)
* Cotrending basis vectors files
* Pixel response function files
* Artifact removal pixel files
* Background pixel files
* Long and short cadence collateral files
* Reverse clock files
* Ancillary engineering files
* Latest SPICE kernels (bsp an tsc binary files)

**Catalogs at MAST**

* Kepler Input Catalog (KIC)
* KIC joined with characteristics table
* Revised stellar parameters of Kepler targets (Q1-Q16)
* Revised stellar parameters of Kepler targets (Q1-Q17)
* Kepler Objects of Interest (KOI)
* Kepler/GALEX cross match catalog
* False positive working group tables
* Observed KIC targets by quarter

The
[Kepler mission page at NExScI](http://exoplanetarchive.ipac.caltech.edu/docs/KeplerMission.html)
contains the following products and also details the instructions for
requesting a Kepler number for new planets discovered in the
Kepler data:

**Data products at NExScI**

* KOI activity tables
* Threshold-crossing events and data validation tables
* Stellar information for observed Kepler targets
* Ccompleteness and reliability products

### Kepler data release notes

The prime Kepler mission operated from 2009 May 2 until 2013 May 8,
when a second reaction wheel failed on the spacecraft.  During its
four years of operation, the spacecraft completed a 90 degree roll every 3 months to
optimize solar panel efficiency.  Kepler operations are therefore divided into four quarters each year, separated by the quarterly rolls of the spacecraft.  The table
below lists each operational quarter, the corresponding Guest
Observer (GO) program cycle, the beginning and end dates for data
collection, and the date the data was ingested at the [MAST
archive](https://archive.stsci.edu/kepler/).

Note that Kepler long cadence (30-min) images and light curves are stored in files that
span a quarter. Short cadence (1-min) images and light curves are
stored in files that span a month.

The latest data release notes describe [Data Release 24 for Quarters
0-17](https://archive.stsci.edu/kepler/release_notes/release_notes24/KSCI-19064-002DRN24.pdf).  [Earlier release notes for individual quarters can be found at MAST](https://archive.stsci.edu/kepler/data_release.html).

<table class="table table-striped table-hover" style="max-width:40em;">
  <thead>
    <tr>
      <th>Operational quarter</th>
      <th>GO cycle</th>
      <th>Start</th>
      <th>Stop</th>
      <th>Data archived</th>
    </tr>
  </thead>

  <tdata>

  <tr>
      <td>0</td>
	  <td>N/A</td>
      <td>2009 May 02</td>
      <td>2009 May 11</td>
      <td>2009 Oct 21</td>
      </tr>

    <tr>
      <td>1</td>
	  <td>N/A</td>
      <td>2009 May 13</td>
      <td>2009 Jun 15</td>
      <td>2009 Oct 23</td>
    </tr>

    <tr>
      <td>2</td>
	  <td>1</td>
      <td>2009 Jun 20</td>
      <td>2009 Sep 16</td>
      <td>2010 Jan 15</td>
      </tr>

    <tr>
      <td>3</td>
	  <td>1</td>
      <td>2009 Sep 18</td>
      <td>2009 Dec 16</td>
      <td>2010 Apr 15</td>
      </tr>

    <tr>
      <td>4</td>
	  <td>1</td>
      <td>2009 Dec 19</td>
      <td>2010 Mar 19</td>
      <td>2010 Aug 04</td>
      </tr>

    <tr>
      <td>5</td>
	  <td>1</td>
      <td>2010 Mar 20</td>
      <td>2010 Jun 23</td>
      <td>2010 Oct 23</td>
      </tr>

    <tr>
      <td>6</td>
	  <td>2</td>
      <td>2010 Jun 24</td>
      <td>2010 Sep 22</td>
      <td>2011 Jan 23</td>
      </tr>


    <tr>
      <td>7</td>
	  <td>2</td>
      <td>2010 Sep 23</td>
      <td>2010 Dec 22</td>
      <td>2011 Apr 23</td>
      </tr>

    <tr>
      <td>8</td>
	  <td>2</td>
      <td>2010 Dec 22</td>
      <td>2011 Mar 24</td>
      <td>2011 Jul 24</td>
      </tr>

    <tr>
      <td>9</td>
	  <td>2</td>
      <td>2011 Mar 19</td>
      <td>2011 Jun 27</td>
      <td>2011 Nov 18</td>
      </tr>

    <tr>
      <td>10</td>
	  <td>3</td>
      <td>2011 Jun 28</td>
      <td>2011 Sep 27</td>
      <td>2012 Jan 27</td>
      </tr>

    <tr>
      <td>11</td>
	  <td>3</td>
      <td>2011 Sep 29</td>
      <td>2012 Jan 04</td>
      <td>2012 May 04</td>
      </tr>


    <tr>
      <td>12</td>
	  <td>3</td>
      <td>2012 Jan 05</td>
      <td>2012 Mar 28</td>
      <td>2012 Jul 28</td>
      </tr>

    <tr>
      <td>13</td>
	  <td>3</td>
      <td>2012 Mar 29</td>
      <td>2012 Jun 27</td>
      <td>2012 Oct 23</td>
      </tr>

    <tr>
      <td>14</td>
	  <td>4</td>
      <td>2012 Jun 28</td>
      <td>2012 Oct 03</td>
      <td>2013 Feb 03</td>
      </tr>

    <tr>
      <td>15</td>
	  <td>4</td>
      <td>2012 Oct 05</td>
      <td>2013 Jan 11</td>
      <td>2013 May 06</td>
      </tr>

    <tr>
      <td>16</td>
	  <td>4</td>
      <td>2013 Jan 12</td>
      <td>2013 Apr 08</td>
      <td>2013 Aug 02</td>
      </tr>

    <tr>
      <td>17</td>
	  <td>4</td>
      <td>2013 Apr 09</td>
      <td>2013 May 08</td>
      <td>2013 Dec 09</td>
      </tr>
	  
</tdata>
</table>

## K2 product overview

The [K2 mission page at MAST](https://archive.stsci.edu/k2/) contains
the latest news and updates on K2 products. The following K2 data
products and catalogs are available through MAST and can be downloaded
[here](https://archive.stsci.edu/k2/data_products.html):

**Data products at MAST**

* Long and short cadence target pixel files
* Long cadence light curves (and some user-provided light curves)
* Full frame images (calibrated and uncertainty files)
* Cotrending basis vectors files
* Artifact removal pixel files
* Background pixel files
* Long and short cadence collateral files
* Ancillary engineering files
* Latest SPICE kernels (bsp and tsc binary files)
* Two-wheel concept engineering test data (some HLSP light curves
exist)

**Catalogs at MAST**

* Ecliptic Plane Input Catalog (EPIC)
* Thruster firings for Campaign 1 and Campaign 2
* Published K2 exoplanets

The
[K2 mission page at NExScI](http://exoplanetarchive.ipac.caltech.edu/docs/K2Mission.html)
contains an interactive table of K2 targets and also details the instructions for
requesting a K2 number for new planets discovered in the K2 data.

### K2 data release notes

K2 long cadence (30-min) images are available for each Campaign.
Light curves produced by the Project Office are available starting in
Campaign 3.  Short cadence (1-min) images are also available for each
Campaign, but no light curves are provided.  The relevant data release notes
for each Campaign are linked in the table below.  The pipeline release
notes for K2 are
[available here](http://keplerscience.arc.nasa.gov/K2/pipelineReleaseNotes.shtml),
which detail deviations from the pipeline used for Kepler.

<table class="table table-striped table-hover" style="max-width:40em;">
  <thead>
    <tr>
      <th>Campaign</th>
      <th>Release Note</th>
      <th>Date</th>
      <th>Pipeline Processing Version</th>
    </tr>
  </thead>

  <tdata>

      <tr>
      <td>C0</td>
      <td><a href="http://keplerscience.arc.nasa.gov/K2/C0drn.shtml">C0 DRN</a></td>
      <td>2014 Sep 09</td>
      <td>9.2</td>
      </tr>

      <tr> 
      <td>C1</td>
      <td><a href="http://keplerscience.arc.nasa.gov/K2/C1drn.shtml">C1 DRN</a></td>
      <td>2014 Dec 24</td>
      <td>9.2</td>
      </tr>

      <tr>
      <td>C2</td>
      <td><a href="http://keplerscience.arc.nasa.gov/K2/C2drn.shtml">C2 DRN</a></td>
      <td>2015 Apr 02</td>
      <td>9.2</td>
      </tr>

      <tr>
      <td>C3</td>
      <td><a href="http://keplerscience.arc.nasa.gov/K2/C3drn.shtml">C3 DRN</a></td>
      <td>2015 Jul 17</td>
      <td>9.3</td>
      </tr>

      <tr>
      <td>C4</td>
      <td><a href="http://keplerscience.arc.nasa.gov/K2/C4drn.shtml">C4 DRN</a></td>
      <td>2015 Sep 02</td>
      <td>9.3</td>
      </tr>

</tdata>
</table>

## Main data products

A few of the data products from Kepler and K2 are described
below. For a comprehensive list of available products, see the above
lists for [Kepler](data-products.html#kepler-product-overview) and [K2](data-products.html#k2-product-overview).

### Full frame images (FFIs)

The Kepler detector is a photometer with an array of 42 CCDs or 21 modules. The
Kepler field of view spans 115.6 square degrees over 95 million
detector pixels, with 3.98 x 3.98 arcsec pixels. Science
data downloads for Kepler occurred
approximately once per month. Immediately
before each data download, a 29.4 min image of the entire field of
view was collected and transmitted. [These are the Kepler FFIs, which
can be downloaded from a dedicated data retrieval page at MAST](http://archive.stsci.edu/kepler/ffi/search.php).

For K2, typically only two FFIs are collected per Campaign.  [These can
also be downloaded through MAST](http://archive.stsci.edu/k2/ffi/search.php).

FFI data format is defined in section 2.3.3 of the [Kepler Archive
Manual](http://archive.stsci.edu/kepler/manuals/archive_manual.pdf). Note
that as of May 2014, the Kepler detector has two dead modules (3 and
7). 

<br/>

<img class="img-responsive" style="min-width:97%;" src="images/kepler-fov-full.jpg">

<br/>

### Target pixel files (TPFs)

The Kepler camera takes one exposure every 6.5s. Exposures are summed
onboard and stored at either 1765.5 s (29.4 min) cadence
(a.k.a. 30 min or long
cadence) or 58.89 s cadence (a.k.a. 1 min or short cadence). At these
data collection cadences, the Solid State Recorder onboard the
spacecraft can store only 5.4 million of the 95 million pixels
available. The pixels collected are chosen strategically to provide
postage stamp images centered on the positions of targets of interest. The size of a postage stamp increases with target brightness
and the average yield was 166,000 targets per month for Kepler.  For
K2 the average yield per Campaign is between 10,000 and 20,000 long
cadence targets and 50 to 100 short cadence targets.

A critical concept for understanding artifact issues in Kepler light
curves is that in order to maximize the target yield, postage stamp
sizes and shapes are chosen to maximize the signal-to-noise on the
3-12 hour timescales of exoplanet transits. Postage stamp pixels are
chosen by a calculation that combines the photometry and astrometry
within the Kepler Input Catalog and an [analytical model](http://adsabs.harvard.edu/abs/2010ApJ...713L..97B) for the
detector and optics. Any variation in the position of the target
within the postage stamp or the focus of the telescope will result in
a redistribution of flux within the postage stamp pixels.  Similar
steps are performed for K2 targets.

The target pixel files are the rawest form of target-specific data
available from the Kepler and K2 archives at MAST.  The TPF data format is defined in section 2.3.2 of the [Kepler Archive
Manual](http://archive.stsci.edu/kepler/manuals/archive_manual.pdf). 

<br/>

<img class="img-responsive" style="min-width:97%;" src="images/TPF-FV3.jpg">

<br/>

Typical images stored within a TPF. The left-hand image is stored in a
time-tagged data table and contains calibrated, background-subtracted
and cosmic ray removed pixel fluxes for one specific timestamp. The
right-hand image contains a bitmap that describes the employment of
each pixel in the Kepler/K2 pipeline. Black pixels were not collected by
the spacecraft, yellow are collected but do not contribute to the
photometry stored in the associated light curve file. White pixels are
included in the photometric aperture that maximizes target
signal-to-noise over nominal observations.

### Light curve files

The light curves are derived from the TPFs. There is a one-to-one
correspondence between the files and timestamps and quality flags
within the two products are identical. The primary data within the
light curve file is Simple Aperture Photometry - a summation of the
calibrated pixels in the TPF.

The nominal spacecraft pointing for the
Kepler mission was typically 20 milli-arcsec over 6.5 hours. Noise
(artifacts) manifest from thermally-driven focus changes, pointing
derivatives and differential velocity aberration. Systematic artifacts
within the light curves are associated with these events and are the
result of both time-dependent light losses falling out of the pixel
apertures and time-dependent contamination of neighboring sources
moving around within the pixel apertures. These effects are greater
for K2 as the pointing is not as stable as for Kepler, due to
low-frequency motion due to solar pressure and subsequent thruster
firings. These cause targets to drift across detector pixels and are
the dominant factor in photometric precision from K2 after photon statistics. 

Within the pipeline, artifacts are mitigated for using a derivative of principle component analysis. The product of this analysis is provided within the light curve. It is the prerogative of archive users to determine whether the pipeline mitigation is suitable for their scientific goals or whether manual mitigation will be required.

Light curve files also contain centroid measurements derived from the
TPFs. Since many artifacts are the result of target motion within its
pixel aperture, time-resolved correlations between target flux and
motion provide useful diagnostics of systematic artifacts within the
time series.

The light curve file format is defined in section 2.3.1 of the [Kepler Archive
Manual](http://archive.stsci.edu/kepler/manuals/archive_manual.pdf). Light
curves are available for all quarters of Kepler data, but are only
available (from the Project Office) for Campaign 3 and later for K2.

### Collateral data

Collateral data is collected onboard for the purpose of calibrating
science data. Collateral pixels estimate the bias level, dark current
and charge smear that results from shutter-less camera
operation. Pixels are collected around sparse fields in order to
provide background measures. Format and content of the collateral files is
provided in section 2.3.7 of the [Kepler Archive
Manual](http://archive.stsci.edu/kepler/manuals/archive_manual.pdf). These
files are available for both Kepler and K2.

## Auxiliary data products

Auxiliary data is not collected directly by the spacecraft, but is
derived from spacecraft data. Some of the currently available auxiliary data is
described below.

### Cotrending basis vectors (CBVs)

CBVs are provided for each operational quarter of the mission. These are derived by
the Kepler pipeline from Principle Component Analysis and used to
mitigate for systematic artifacts within the the target light
curves. If Kepler or K2 users see residual systematic problems
within their light curve data, the CBVs can be employed in performing
a manual photometric correction, more tailored towards the users
science. Format and content of the CBV files is provided in
section 2.3.4 of the [Kepler Archive
Manual](http://archive.stsci.edu/kepler/manuals/archive_manual.pdf). [Software for applying the CBVs
to data can be found here](http://keplerscience.arc.nasa.gov/ContributedSoftwareKepcotrend.shtml).

### Pixel response functions (PRFs)

The PRFs model the Point Spread Function (PSF) of the telescope with
the pointing stability of the Kepler spacecraft. The PSF varies across
the detector plane. There are three primary uses of the PRFs that
require fitting to either TPF or FFI data.

Format and content of the PRF files is provided in section 2.3.5 of
the [Kepler Archive
Manual](http://archive.stsci.edu/kepler/manuals/archive_manual.pdf). Note
that PRFs are only available for Kepler.

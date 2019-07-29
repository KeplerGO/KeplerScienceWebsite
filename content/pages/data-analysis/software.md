Title: Kepler/K2 community software tools
Save_as: software.html

[TOC]

## Overview

Below is a list of software tools created by the community for use in preparing for Kepler and K2 observations
and for analyzing the collected data.  Note that these tools are not official NASA software products (with the exception of PyKE).

<table class="table table-striped table-hover" style="max-width:50em;">

<tr>
    <td><a href="/software.html#pyke">PyKE</a></td>
    <td>
        A suite of command-line tools to inspect target pixel files and extract detrended lightcurves.
    </td>
    <td>
        <a href="https://github.com/nasa/Kepler-PyKE">github.com/nasa/Kepler-PyKE</a>
    </td>
</tr>

<tr>
    <td><a href="/software.html#lightkurve">Lightkurve</a></td>
    <td>
        The Lightkurve Python package offers a user-friendly way to analyze the pixels and light curves obtained by Kepler, K2, and TESS.
    </td>
    <td>
         <a href="https://github.com/KeplerGO/lightkurve">github.com/KeplerGO/lightkurve</a>
    </td>
</tr>

<tr>
    <td><a href="/software.html#k2fov">K2fov</a></td>
    <td>
        Checks whether a celestial coordinate falls within the field of view
        of a K2 campaign.
    </td>
    <td>
        <a href="https://github.com/KeplerGO/K2fov">github.com/KeplerGO/K2fov</a>
    </td>
</tr>

<tr>
    <td><a href="/software.html#k2ephem">K2ephem</a></td>
    <td>
        Checks whether a moving Solar System body, e.g. an asteroid or comet,
        falls within the field of view of any K2 campaign.
    </td>
    <td>
        <a href="https://github.com/KeplerGO/K2ephem">github.com/KeplerGO/K2ephem</a>
    </td>
</tr>

<tr>
    <td><a href="http://barentsen.github.io/k2flix/">K2flix</a></td>
    <td>
        Converts target pixel files into movies or animated gifs for quick and easy pixel data inspection.
    </td>
    <td>
        <a href="https://github.com/KeplerGO/k2flix">github.com/KeplerGO/k2flix</a>
    </td>
</tr>

<tr>
    <td><a href="http://k2mosaic.geert.io">K2mosaic</a></td>
    <td>
        Combines target pixel files into wide-field images.
    </td>
    <td>
        <a href="https://github.com/KeplerGO/k2mosaic">github.com/KeplerGO/k2mosaic</a>
    </td>
</tr>

<tr>
    <td><a href="https://github.com/KeplerGO/kadenza">Kadenza</a></td>
    <td>
        Converts raw cadence data from the Kepler spacecraft into astronomer-friendly FITS files.</td>
    <td>
        <a href="https://github.com/KeplerGO/kadenza">github.com/KeplerGO/kadenza</a>
    </td>
</tr>

</table>


A non-exhaustive list of additional community tools is available on
the ["Other software" page](https://docs.lightkurve.org/about/other_software.html) on the documentation website
of the [Lightkurve package](https://docs.lightkurve.org).



## Observation planning

### K2fov

K2fov is a Python package that allows users to check whether a target falls within the field of view of K2.

In particular, the package adds the *K2onSilicon* and *K2findCampaigns* tools to the command line, which allow the visibility of targets to be checked during one or all campaigns, respectively.

The code and documentation is [hosted on Github](https://github.com/KeplerGO/K2fov) and only briefly summarized here.

<h4>Installation</h4>

Users will need to have a working version of Python 2 or 3 installed.
If this requirement is met, K2fov can be installed using pip:

    pip install K2fov

If you have a previous version installed, please make sure you upgrade to the latest version using:

    pip install K2fov --upgrade

It is important to upgrade frequently to ensure that you are using the most up to date K2 field parameters.

<h4>Usage</h4>

Installing K2fov will automatically add a command line tool to your path called *K2onSilicon*, which takes a list of targets as input and writes a new list that indicates the "silicon status" of each target, i.e. whether or not it falls on one of the detectors of the spacecraft's focal plane.

The simplest thing to do is to have a CSV file with columns "RA_degrees, Dec_degrees, Kepmag". Do not use a header.
For example, create a file called mytargetlist.csv containing the following rows:

    178.19284, 1.01924, 13.2
    171.14213, 5.314616, 11.3

The format for the target list is very strict -- you need three
columns: ra, dec, and magnitude.
Headers or other additional columns will cause an execution failure.

You can then check whether each object in the file falls on silicon by calling K2onSilicon from the command line:

    K2onSilicon mytargetlist.csv 1

Where mytargetlist.csv is your CSV file and 1 is the K2 Campaign number.

Running the code will output an updated target list containing the three input columns and an extra column containing either a "0" or "2":

* 0 = Not observable
* 2 = Target is in the K2 field of view and on silicon

The code will also write an image, called targets_fov.png, showing where the targets fall. An example is shown below.
<br/>

<img class="img-responsive" style="max-width:77%;" src="images/K2FOV.png">

<br/>

If instead of checking the targets in a single campaign, you want to understand whether a target is visible in any past or future K2 Campaign, you can use a different tool called *K2findCampaigns*.

For example, to verify whether J2000 coordinate (ra, dec) = (269.5, -28.5) degrees is visible at any point during the K2 mission, type:

    $ K2findCampaigns 269.5 -28.5
    Success! The target is on silicon during K2 campaigns [9].

You can also check a list of targets using the alternative command line tool called *K2findCampaigns-csv*.


### K2ephem

K2ephem is a Python package that allows to check
whether a Solar System body, i.e. a moving asteroid or comet,
falls within the field of view of a K2 campaign.

It provides a command-line tool that will automatically grab the ephemeris
of an object from NASA's JPL/Horizons service and then check its K2 visibility
using *K2fov*.

<h4>Installation</h4>

You need to have a working version of Python 2 or 3 installed.
If this requirement is met, you can install K2ephem using pip

    pip install K2ephem --upgrade

If required, this command will take care of installing
the two required dependencies (*K2fov* and *pandas*).

<h4>Usage</h4>

After installation, you can call *K2ephem* from the command line.
For example, to verify whether comet Chiron can be observed by K2, simply type:

    K2ephem Chiron

Or you can type *K2ephem --help* to see the detailed usage instructions:

    $ K2ephem --help
    usage: K2ephem [-h] [--first campaign] [--last campaign] target

    Check if a Solar System object is (or was) observable by NASA's K2 mission.
    This command will query JPL/Horizons to find out.

    positional arguments:
      target            Name of the target. Must be known to JPL/Horizons.

    optional arguments:
      -h, --help        show this help message and exit
      --first campaign  First campaign to check (default: 0)
      --last campaign   Final campaign to check (default: 18)


## Data analysis

### Lightkurve

Documentation website: [docs.lightkurve.org](https://docs.lightkurve.org).

The lightkurve Python package offers a user-friendly way to analyze astronomical flux time series data, in particular the pixels and lightcurves obtained by Kepler, K2, and TESS.

This package aims to lower the barrier for both students, astronomers, and citizen scientists interested in analyzing Kepler and TESS space telescope data. It does this by providing high-quality building blocks and tutorials which enable both hand-tailored data analyses and advanced automated pipelines.

Lightkurve is an open source community project.
The development [takes place on GitHub](https://github.com/KeplerGO/lightkurve)
and everyone is [invited to contribute](http://docs.lightkurve.org/about/contributing.html).

### PyKE

PyKE is a suite of command-line tools developed to reduce and
analyze Kepler and K2 light curves, TPFs, and FFIs. PyKE tools provide the
user with flexibility to tune pixel extraction and artifact mitigation
for the scientific potential of individual target data. A variety of
other tasks are also included.
PyKE development takes place on its [GitHub repository](https://www.github.com/KeplerGO/PyKE).
We encourage users to participate in the development process by opening
issues, pull requests, or sending us an email.

<h4>PyKE tasks</h4>

A comprehensive list of PyKE tasks is provided here.

<table class="table table-striped table-hover" style="max-width:70em;">

<tr>
    <td>kepbls</td>
    <td>Box Least-Square planet transit detection </td>
</tr>

<tr>
    <td>kepclip</td>
    <td>Remove unwanted time ranges from Kepler time series data </td>
</tr>

<tr>
    <td>kepconvert</td>
    <td>Convert Kepler FITS time series to or from a different file format </td>
    </tr>

<tr>
    <td>kepcotrend</td>
    <td>Remove systematic trends in photometry using cotrending basis vectors </td>
    </tr>

<tr>
    <td>kepdetrend</td>
    <td>Detrend systematic features from Simple Aperture Photometry (SAP) data </td>
    </tr>

<tr>
    <td>kepdiffim</td>
    <td>Difference imaging of pixels within a target mask </td>
    </tr>

<tr>
    <td>kepdraw</td>
    <td>Interactive plotting of Kepler time series data </td>
    </tr>

<tr>
    <td>kepdynamic</td>
    <td>Construct a dynamic (time-dependent) power spectrum from Kepler time series data </td>
    </tr>

<tr>
    <td>kepextract</td>
    <td>Derive a light curve from a target pixel file, with user-defined apertures </td>
    </tr>

<tr>
    <td>kepffi</td>
    <td>Plot sub-areas of Kepler Full Frame Images and define custom target apertures </td>
    </tr>

<tr>
    <td>kepfield</td>
    <td>Superimpose photometric mask and source positions over a target pixel image </td>
    </tr>

<tr>
    <td>kepfilter</td>
    <td>Remove low frequency variability from time-series, preserve transits and flares </td>
    </tr>

<tr>
    <td>kepflatten</td>
    <td>Low bandpass or high bandpass signal filtering </td>
    </tr>

<tr>
    <td>kepfold</td>
    <td>Fold data on a linear ephemeris </td>
    </tr>

<tr>
    <td>kepft</td>
    <td>Calculate and store a Fourier Transform from a Kepler time series </td>
    </tr>

<tr>
    <td>kephead</td>
    <td>Search for and list FITS keywords in Kepler data files </td>
    </tr>

<tr>
    <td>kepimages</td>
    <td>Create a series of separate FITS image files from a Target Pixel File </td>
    </tr>

<tr>
    <td>kepmask</td>
    <td>Plots, creates or edits custom light curve extraction masks for target pixel files </td>
    </tr>

<tr>
    <td>kepoutlier</td>
    <td>Remove or replace data outliers from a time series</td>
    </tr>

<tr>
    <td>keppca</td>
    <td>Pixel-level principal component analysis of time series </td>
    </tr>

<tr>
    <td>keppixseries</td>
    <td>Individual time series photometry for all pixels within a target mask </td>
    </tr>

<tr>
    <td>kepprf</td>
    <td>Fit a PSF model to a specific image within a Target Pixel File </td>
    </tr>

<tr>
    <td>kepprfphot</td>
    <td>Fit a PSF model to time series observations within a Target Pixel File </td>
    </tr>

<tr>
    <td>keprange</td>
    <td>Interactively define and store time ranges via a GUI </td>
    </tr>

<tr>
    <td>kepsff</td>
    <td>Correct aperture photmetry using target motion </td>
    </tr>

<tr>
    <td>kepsmooth</td>
    <td>Smooth Kepler light curve data by convolution</td>
    </tr>

<tr>
    <td>kepstddev</td>
    <td>Calculate Combined Differental Photometric Precision for time series light curve </td>
    </tr>

<tr>
    <td>kepstitch</td>
    <td>Append multiple month short cadence and/or multiple quarter long cadence data</td>
    </tr>

<tr>
    <td>keptimefix</td>
    <td>Correct time stamps in Target Pixel Files to TDB system </td>
    </tr>

<tr>
    <td>keptransit</td>
    <td>Fit planet trasit models to Kepler time-series </td>
    </tr>

<tr>
    <td>keptrial</td>
    <td>Calculate best period and error estimate from Fourier transform </td>
    </tr>

<tr>
    <td>keptrim</td>
    <td>Trim pixels from Target Pixel Files </td>
    </tr>

<tr>
    <td>kepwindow</td>
    <td>Calculate and store the window function for a Kepler time series </td>
    </tr>

</table>

<h4>PyKE history</h4>

<table class="table table-striped table-hover" style="max-width:70em;">
  <thead>
    <tr>
      <th>Date</th>
      <th>Version</th>
      <th>Description</th>
    </tr>
  </thead>

<tdata>

<tr>
    <td style="min-width: 8em;">2010-06-29</td>
    <td>1.0.0 </td>
    <td>Initial software release (MS) </td>
</tr>

<tr>
    <td>2011-07-03</td>
    <td>2.0.0 </td>
    <td>Added support for FITS v2.0 archive files (MS) </td>
    </tr>

<tr>
    <td>2011-07-21</td>
    <td>2.1.0 </td>
    <td>Added kepcotrend tool to package (TB) </td>
    </tr>

<tr>
    <td>2011-08-30</td>
    <td>2.1.1 </td>
    <td>Trapped new behavior of STSCI_PYTHON 2.12 in reading multi-dimension FITS columns (MS) </td>
    </tr>

<tr>
    <td>2011-09-22</td>
    <td>2.1.2 </td>
    <td>Plot style updates to kepdraw and kepsmooth (MS) </td>
    </tr>

<tr>
    <td>2011-10-20</td>
    <td>2.1.3 </td>
    <td>Added short cadence functionality to basis vector cotrending in kepcotrend. Added simple light curve algebra tool kepartih to package (TB) </td>
    </tr>

<tr>
    <td>2012-06-09</td>
    <td>2.2.0 </td>
    <td>Provided greater plotting stability on linux/unix operating systems. Tasks can be executed from within the PyRAF environment or from within a linux/unix shell without compiling against PyRAF or IRAF. Added the kepflatten tool to the task list (MS,TB). </td>
    </tr>

<tr>
    <td>2012-07-02</td>
    <td>2.2.1 </td>
    <td>keparith bug addressed. Fatal error upon PDCSAP photometry arithmetic fixed (TB). </td>
    </tr>

<tr>
    <td>2012-10-01</td>
    <td>2.2.2 </td>
    <td>kepflatten bug addressed: light curve fits no longer tapered after 4,000 timestamps. NaN handling in kepdraw improved for speed. Two options now provided in kepdraw - fast and ugly - slow and pretty (MS). </td>
    </tr>

<tr>
    <td>2012-10-09</td>
    <td>2.2.3 </td>
    <td>kepdraw bug addressed: plottype functionality added to shell-mode operation (MS)
 </td>
</tr>

<tr>
    <td>2012-10-12</td>
    <td>2.2.4 </td>
    <td>kepbls task for transit searching added to package (MS) </td>
 </tr>

<tr>
    <td>2012-10-23</td>
    <td>2.2.5 </td>
    <td>kepsmooth bug addressed: fscale and plotlab functionality added to shell-mode operation (MS) </td>
 </tr>

<tr>
    <td>2012-12-09</td>
    <td>2.3.0 </td>
    <td>Added tasks keptransit and keppca (TB, MS) </td>
 </tr>

<tr>
    <td>2013-02-07</td>
    <td>2.3.1 </td>
    <td>Added kepffi and kepmask functionality to load existing pixel mask defintion. Bug in pixel selection within both tasks and keprange fixed. kepffi adapted in response to format changes to the target tables at MAST (MS) </td>
 </tr>

<tr>
    <td>2013-08-06</td>
    <td>2.4.0 </td>
    <td>Added kepfield and keptimefix tasks. Bug corrections in kepfold (MS,TB)</td>
 </tr>

<tr>
    <td>2013-09-30</td>
    <td>2.5.0 </td>
    <td>Added kepprf, kepprfphot, kepstddev and keptrim tasks. Bug correction to kepcotrend and functionality change to keptimefix (MS,TB) </td>
 </tr>

<tr>
    <td>2014-03-26</td>
    <td>2.5.1 </td>
    <td>Minor adaptations for two-wheel engineering data. Added keptrim (MS)
 </td>
</tr>

<tr>
    <td>2014-06-26</td>
    <td>2.5.2 </td>
    <td>Corrected all tasks for the deprecation of ascardlist() in pyfits 3.1 (MS)</td>
</tr>

<tr>
    <td>2014-09-10</td>
    <td>2.6.2 </td>
    <td>New tools like kepsff (MS) </td>
</tr>

<tr>
    <td>2015-12-16</td>
    <td>2.6.3a </td>
    <td>Bugfixes in kepextract and keppca</td>
</tr>

<tr>
    <td>2017-05-03</td>
    <td>2.6.3 </td>
    <td>PyKE is now installable via the <a href="http://astroconda.readthedocs.io/en/latest/installation.html#legacy-software-stack-with-iraf">Astroconda IRAF Channel</a>
    In addition, the release contains a series of bugfixes related to deprecated dependencies</td>
</tr>


</tdata>
</table>


## Data inspection

A variety of other public software exists for inspection of Kepler and K2 FITS
data.  An incomplete list is provided here. FV can be used to inspect
Target Pixel Files (TPFs) and TOPCAT can be used to inspect light
curves.  DS9, KeplerFFI, and MAST can be used to inspect full-frame images (FFIs).


### K2flix

K2flix enables the pixel data to be visualized
by turning Kepler/K2's Target Pixel Files (TPF) into
contrast-stretched animated gifs or MPEG-4 movies.
K2flix can be used both as a command-line tool or using its Python API.
The tool is hosted and documented on [GitHub](https://github.com/KeplerGO/k2flix).


### K2mosaic

K2mosaic is a command-line tool which allows the postage stamp-sized pixel masks obtained by Kepler and K2 to be stitched together into CCD-sized mosaics and movies. The principal use is to take a set of Target Pixel Files (TPF) and turn them into more traditional FITS image files -- one per CCD channel and per cadence. K2mosaic can also be used to create animations from these mosaics.
The tool is hosted and documented on [GitHub](https://github.com/KeplerGO/K2mosaic).

### KeplerFFI

This FFI inspection tool is used to examine the sources surrounding a
target, assess crowding, identify artifacts, and understand the
effects of the photometric aperture on the light curves. KeplerFFI
also creates a custom pixel mask by allowing users to select pixels
for inclusion within a target aperture. Individual pixels are chosen
interactively by tapping upon them. [This standalone python tool is
available for download here](/ContributedSoftwareKeplerFFI.shtml).


### MAST FFI Viewer

MAST maintains an online FFI display tool, which allows the user to
examine individual channels within an FFI image. Kepler and K2 targets, as
well as 2MASS and GALEX sources located within the frame, are marked
with symbols and are user-selectable. Sources for which the data have been
published or made public are also
indicated. [The Kepler FFI tool can be accessed here](http://archive.stsci.edu/kepler/ffi_display.php). [The K2 FFI tool can be accessed here](http://archive.stsci.edu/k2/ffi_display.php).


### FV

Kepler and K2 Target Pixel Files (TPFs) are provided to the user in the form
of binary FITS tables, one file per target. Each row in the table
contains timestamps, photometric measurements, astrometric
measurements and data quality flags. A format description and content
definition of the TPFs is provided in section 2.3.2 of the [Kepler
Archive Manual](http://archive.stsci.edu/kepler/manuals/archive_manual.pdf). Each row of the photometric columns contains a pixel
image of the target. We have found that the best tool to inspect the
structure and content of the TPF is the GUI-driven tool FV. FV is software that can display and edit FITS format tables and images and is developed and distributed by NASA's High Energy Astrophysics Science and Archive Research Center (HEASARC).  We provide a specific example of TPF product inspection using FV below. [FV can be downloaded here](http://heasarc.nasa.gov/ftools/fv/).

**Load and inspect tabulated data**

* Start up the FV application to open the primary GUI.
* Click on the "Open File..." button in the menu.
* Use the file browser that pops up to navigate the folders on your system.
* Click on the TPF of interest and then the "Open" button. The file summary GUI
will open. Each row in the summary is a data extension within the FITS
file. All header keywords within the extension will be provided if you
click on one of the "Header" buttons. The "Hist" and "Plot" buttons provide histograms and line plots of tabulated data.
* On the summary GUI, click the "All" button to open the table of time-tagged
  data within the TPF.

**Plot target images**

* In the above table, choose a specific row/time and click the "Image" button under the SAP_FLUX column.
* On the summary GUI, click the "Image" button.
* FV will ask whether you want replace the current selected image. Click "No".

<br/>

<img class="img-responsive" style="min-width:97%;" src="images/TPF-FV3.jpg">

<br/>

The above figure shows typical images stored within a TPF. The left-hand image is stored in the time-tagged data table and contains calibrated, background-subtracted and cosmic ray removed pixel fluxes. The right-hand image contains a bitmap that describes the employment of each pixel. Black pixels are not collected, yellow are collected but do not contribute to the photometry stored in the light curve products. White pixels are included in the photometric aperture that maximizes target signal-to-noise over nominal short timescales of observation.

### TOPCAT

Kepler and K2 times-series light curves are provided to the user in the form
of a binary FITS table, one file per target. Each row in the table
contains timestamps, photometric measurements, astrometric
measurements and data quality flags. A format description and content
definition of the Kepler light curve file is provided in section 2.3.1
of the [Kepler
Archive Manual](http://archive.stsci.edu/kepler/manuals/archive_manual.pdf). Below,
we provide a specific example of light curve product inspection using
the Java tool TOPCAT (Tool for Operation on Catalogs and Tables).
[TOPCAT can be downloaded here](http://www.star.bris.ac.uk/~mbt/topcat/).

**Load data and display data table**

* Start up TOPCAT to open the main control GUI. The
left-most icon on the options bar at the top allows the user to open and
inspect light curve files. Other icons provide data table display,
data plotting, filtering and statistics, and output of a variety of
different data formats.
* Click on the "Load New Table" icon (top-left) to open a new GUI. In the "Format" dialog box scroll down and click on "FITS".
* Click on the "Filestore Browser" button to navigate through your directories; choose the desired file by clicking on it.
* The file name will appear in the left-hand window of the main GUI. The
number of rows and columns in the table will appear in the right-hand
area.
* Click on the fourth icon from the left in the primary GUI opens the data table within the FITS file for inspection.

**Plot and save data table**

* Click on the icon labeled "Scatter Plot" at the top of the control window. A plotting GUI opens in which data in the TIME column (col. 1) is plotted versus data in the TIMECORR column (col. 2), the default option.
* In the plot window, the user can select alternative data columns to plot. For the Y-axis data choose, for example the data column SAP_FLUX. The plot will update with simple aperture photometry against time.
* Options for customizing the plot are available using the various
icons located above the plot. For example, at the bottom right of the plot under "Row Subsets", click on the rightmost button to access the Plot Style Editor.
* Save the plot to PDF using icon 4.
* Data can be convered to, e.g., ASCII files using the "Save Table" option (the
second icon from the left at the top of the control window).

### DS9

Kepler and K2 Full Frame Images (FFIs) are provided to the user in the form
of a binary FITS file. There are ~94 million pixels in each FFI. In
order to manage this large number of pixel, the data is divided into
subimages by readout node. There are 84 readouts spread over 21 CCD
modules on the detector plane and therefore there are 84 subimages
stored in 84 FITS extensions within the file. Each FFI is 400 MB in
size. A format description and content definition of the Kepler FFIs
is provided in section 2.3.3 of the [Kepler
Archive Manual](http://archive.stsci.edu/kepler/manuals/archive_manual.pdf). We provide
a specific example of FFI inspection using the SAOImage DS9
tool below. DS9 is an image visualization application,
developed by the Smithsonian Astrophysical Observatory.  [DS9 can be downloaded here]().

**Load FFI images**

* Start DS9
* Under the "File" menu, scroll to the 2nd option, "Open Other", then move the cursor to the right-hand menu and click on "Open Mutli Ext Multi Frames".
* A standard directory dialog box will open; select the desired file
  to open. Click on the image.
* All FFI subimages, one per channel, will open in a tiled view.
* To display a single image from the set, click on it, then under the top-level menu labeled "frame", toggle the "single frame" option.
* Toggle between "tile frames" and "single frame" to view any frame on the image.
* To load a specific single frame of the image set, click on the "Open" option in the menu under "File". Navigate to the relevant folder, then scroll through the folder for the desired image. Enter the name of the image in the box but add an extra qualifier like: *'filename[nn]'*, where *nn* is the HDU or extension number within the FITS file containing the image. The extension number is equivalent to the channel number on the detector mosaic.
* Logarithmic image scaling works best for displaying the full dynamic
  range of the Kepler and K2 images.
* To adjust the contrast, place the cursor in the image pane, and scroll the mouse, while holding down the right button.
* The header keywords for the image can be displayed using the "File"
menu, click on "header". A new window opens asking you to select the
file, click "OK" and another window opens with the header information.

**FFI matching against the DSS**

* Under the "Analysis" menu, choose "Image Servers" and "STSCI-DSS I/II".
* Click the "Retrieve" button.
* Under the "Scale" menu, choose "Linear".
* Under the "Frame" menu, choose "Match", then "Frame", then "WCS".
* Under the "Frame" menu again, click "Blink".

The below image displays the result of the example procedure detailed
above. The image shows a side-by-side comparison of a region within the first Q10 FFI (left) with the same region of the Digitized Sky Survey (right).

<br/>

<img class="img-responsive" style="min-width:97%;" src="images/ds9-dss.jpg">

<br/>

Note: With so many subimages within an FFI file, it is not immediately
obvious with DS9 how to navigate to a specific celestial location. The
simplest method to inspect the region around a specific provided
celestial coordinate or Kepler or K2 target is to use the tool KeplerFFI
(see below).

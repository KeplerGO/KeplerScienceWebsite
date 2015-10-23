Title: Kepler/K2 Guest Observer Office Software
Save_as: software.html

[TOC]

Here is a list of software products created by the Kepler/K2 Guest
Observer Office for use in preparing for Kepler and K2 observations
and for analyzing the collected data. The Guest Observer Office hosts
source code on [Github](https://github.com/keplergo). 

<table class="table table-striped table-hover" style="max-width:40em;">

<tr>
    <td>K2Fov</td>
    <td>A tool to check whether targets are within the field of view for each K2 campaign</td>
    <td><a href="https://github.com/KeplerGO/K2fov">https://github.com/KeplerGO/K2fov</a></td>
</tr>

<tr>
    <td>Kadenza</td>
    <td>Converts raw cadence data from the Kepler spacecraft into astronomer-friendly FITS files.</td>
    <td><a href="https://github.com/KeplerGO/kadenza">https://github.com/KeplerGO/kadenza</a></td>
</tr>

<tr>
    <td>PyKE</td>
    <td>A tool to create light curves with user-chosen pixel apertures and
    cotrend and/or detrend data.</td>
	<td><a href="data/pyke/PyKE.tar">download PyKE</a></td>
	</tr>
	
</table>

### K2fov

K2FOV reads a list of potential target positions (J2000 celestial coordinates) and returns whether they are likely to fall within the field of view of K2 during a specified observing campaign.

The code is hosted on Github. Users will need python and numpy
installed. Users who would like to produce plots like the one below also need to install matplotlib. Users of PyKE will already have these dependencies installed on their system. If you have pip, a python package manager, installed on your machine you can download and install the code by running:

   <i>pip install K2fov</i>

Alternatively, users can download the code package from Github (using the button lower-right labeled Download ZIP), unzip the file in a directory, cd to the directory within a shell and run:

   <i>python setup.py install</i>

There are a few different ways to execute the code within your shell. The simplest method is to download this file, make it executable, and run it:

   <i>./runK2onSilicon.py myTargetList.csv campaignNumber</i>

In the example above you should replace campaignNumber with an
integer, 0 for Campaign 0 or 1 for Campaign 1. The code will output
two files, i) an updated ascii target list with an extra column
flagging targets that land on active silicon, and ii) if matplotlib is
intalled, a plot showing where the proposed targets fall on the focal
plane. The format for the target list is very strict -- you need three
columns: RA in degrees, Declination in degrees and Kepler
magnitude. Headers or other additional columns will cause an execution
failure. The code will output a similar file to the one input but with
an extra column containing either a 0, 1 or 2, where 0 = not on
silicon, 1 = near to the focal plane, and 2 =
target is on active silicon.  Targets near the focal plane (flagged
with 1) but not on active silicon are not
worth proposing, since the position of each K2 Campaign is fixed.

<img class="img-responsive" style="min-width:97%;" src="images/K2FOV.png">

### PyKE

The Kepler archive contains raw and calibrated time-series data in
both light curve and pixel form. This pipelined reduction includes the
removal of time-series trends systematic to the spacecraft and its
environment rather than the targets. For every target there is a level
of subjectivity required to reduce systematics. Differing scientific
goals are likely to have differing requirements for systematic
mitigation. Systematic reduction in the Kepler pipeline is optimized
to yield the highest number of potentially-detectable exoplanet
transits from a sample of 160,000 stars. PyKE, on the other hand, is a
group of python tasks developed for the reduction and analysis of
Kepler pixel-level data and Simple Aperture Photometry (SAP) data of individual targets
with individual characteristics. PyKE was developed to provide
alternative data reduction, tunable to the user's specific science
goals. The main purposes of these tasks are to i) re-extract light
curves from manually-chosen pixel apertures and ii) cotrend and/or
detrend the data in order to reduce or remove systematic noise
structure using methods tune-able to user and target-specific
requirements. Tasks to perform data analysis developed for the
author's science programs are also included. PyKE is an open source
project. Contributions of new tasks or enhanced functionality of
existing tasks by the community are welcome.

**Content**

<table class="table table-striped table-hover" style="max-width:40em;">

<tr>
    <td><a href="http://keplerscience.arc.nasa.gov/ContributedSoftwareKeparith.shtml">keparith</a></td>
    <td>Time-invariant algebra on light curve data </td>
</tr>

</table>



**PyRAF installation**

PyKE is a python-based PyRAF package which can also be executed without PyRAF on the command line of a shell. In order to install and run PyKE as a PyRAF package on your Mac or Linux platform you will need PyRAF to be pre-installed following these instructions. We recommend the Ureka binary install option.

A PyRAF tutorial is provided, explaining functionality and the evolution of IRAF into a python-based scripting language. The Kepler tools have been tested against PyRAF version 2.1.6. Please report any deviant behavior using later versions of these packages.

Download the PyKE package tarball by clicking the button at the top-right of the webpage.
To install the Kepler package first create an empty directory to contain the PyKE package files. The most uniform place for this directory is alongside similar packages in the IRAF tree such as stsdas/ and tables/. If PyRAF has been installed e.g. on a mac using the Ureka instructions on the STScI python page then create a directory called /usr/local/Ureka/variants/common/iraf/kepler. Doing this may require administrator privileges. The command to create a new directory will be sudo mkdir /usr/local/Ureka/variants/common/iraf/kepler. 

The folder /usr/local/Ureka/variants/common/iraf/kepler may already exist. If so, it was installed by the Ureka build and more often than not will contain an older version of the PyKE tools. We recommend you delete the content of that folder before continuing.

Edit the extern.pkg file to define the package within the PyRAF system. The location of this file will typically be /usr/local/Ureka/variants/common/extern.pkg. Edit extern.pkg to include the two lines (again administrator privileges may be needed here):

reset kepler = /usr/local/Ureka/variants/common/iraf/kepler/
task kepler.pkg = kepler$kepler.cl

Change directories to the PyKE root directory /usr/local/Ureka/variants/common/iraf/kepler and unpack the downloaded file PyKE.tar:

% cd /usr/local/Ureka/variants/common/iraf/kepler/
% tar xvf path/PyKE.tar

where path is the location of the downloaded file. The tar operation may require root privilege.

If you are an existing IRAF or PyRAF user, change directory to where your iraf login script 'login.cl' is located (for example, your home directory), and rerun the 'mkiraf' script, which re-initializes the uparm parameter files. 

PyRAF requires that you be using csh or tcsh. If you are not running csh or tcsh change to cshell by typing: 

% csh

**PyRAF execution**

For a full description on getting started go to chapter 2 of the PyRAF tutorial. Here's the short version:

Before running this package for the first time add the Ureka executable files to your path by typing: eval `/Users/still/.ureka/ur_setup !*`. Tip - if you look in your startup file e.g. .cshrc in your home directory, you will find that the Ureka install process has made you a handy alias for this ugly command.
Then create files for the storage of PyRAF environment variables and arguments: Within the working shell type 'mkiraf' and choose 'xterm'.

Fire up PyRAF by typing 'pyraf'.

Load the Kepler package by typing 'kepler'. You should see a welcome
message and a list of available tasks.

**Standalone installation**

There are pros and cons to using PyKE as a PyRAF package. Users can rely on GUI operation and retention of input parameters previously used. On the other hand, installation of PyRAF on linux machines can occassionally be challenging. Users unwilling to attempt PyRAF installation can still use PyKE from within a unix/linux shell on the command line. GUI and parameter retention features are however lost in this operating mode and command line calls to PyKE can often be character strings of long length. A positive however is that calls to PyKE can be easily included within shell scripts. Find installation and execution instructions for shell-based PyKE here.

**Citing PyKE in publications**

Those wishing to cite PyKE in a publication may wish to reference Still & Barclay (2012). An appropriate statementment to include in the acknowledgements is: "This work made use of PyKE (Still & Barclay 2012), a software package for the reduction and analysis of Kepler data. This open source software project is developed and distributed by the NASA Kepler Guest Observer Office".

**History**

**Disclaimers**
No Warranty: THE SUBJECT SOFTWARE IS PROVIDED "AS IS" WITHOUT ANY WARRANTY OF ANY KIND, EITHER EXPRESSED, IMPLIED, OR STATUTORY, INCLUDING, BUT NOT LIMITED TO, ANY WARRANTY THAT THE SUBJECT SOFTWARE WILL CONFORM TO SPECIFICATIONS, ANY IMPLIED WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, OR FREEDOM FROM INFRINGEMENT, ANY WARRANTY THAT THE SUBJECT SOFTWARE WILL BE ERROR FREE, OR ANY WARRANTY THAT DOCUMENTATION, IF PROVIDED, WILL CONFORM TO THE SUBJECT SOFTWARE. THIS AGREEMENT DOES NOT, IN ANY MANNER, CONSTITUTE AN ENDORSEMENT BY GOVERNMENT AGENCY OR ANY PRIOR RECIPIENT OF ANY RESULTS, RESULTING DESIGNS, HARDWARE, SOFTWARE PRODUCTS OR ANY OTHER APPLICATIONS RESULTING FROM USE OF THE SUBJECT SOFTWARE. FURTHER, GOVERNMENT AGENCY DISCLAIMS ALL WARRANTIES AND LIABILITIES REGARDING THIRD-PARTY SOFTWARE, IF PRESENT IN THE ORIGINAL SOFTWARE, AND DISTRIBUTES IT "AS IS."

Waiver and Indemnity: RECIPIENT AGREES TO WAIVE ANY AND ALL CLAIMS
AGAINST THE UNITED STATES GOVERNMENT, ITS CONTRACTORS AND
SUBCONTRACTORS, AS WELL AS ANY PRIOR RECIPIENT. IF RECIPIENT'S USE OF
THE SUBJECT SOFTWARE RESULTS IN ANY LIABILITIES, DEMANDS, DAMAGES,
EXPENSES OR LOSSES ARISING FROM SUCH USE, INCLUDING ANY DAMAGES FROM
PRODUCTS BASED ON, OR RESULTING FROM, RECIPIENT'S USE OF THE SUBJECT
SOFTWARE, RECIPIENT SHALL INDEMNIFY AND HOLD HARMLESS THE UNITED
STATES GOVERNMENT, ITS CONTRACTORS AND SUBCONTRACTORS, AS WELL AS ANY
PRIOR RECIPIENT, TO THE EXTENT PERMITTED BY LAW. RECIPIENT'S SOLE
REMEDY FOR ANY SUCH MATTER SHALL BE THE IMMEDIATE, UNILATERAL
TERMINATION OF THIS AGREEMENT.

**Notices**
Copyright © 2010-2011 United States Government as represented by the Administrator of the National Aeronautics and Space Administration. All Rights Reserved.

[NASA open source agreement](http://keplerscience.arc.nasa.gov/docs/KeplerScienceCommunityToolsNOSA.pdf)

#### Walk-through examples

PyKE is a suite of python software tools developed to reduce and analyze Kepler light curves, TPFs, and FFIs. PyKE tools provide the user with flexibility to tune pixel extraction and artifact mitigation for the scientific potential of individual target data. These examples provide use cases and reduction examples for the reader to follow. Data users are encouraged to experiment with the tunable input parameters for each tool. The procedures outlined in this section will not be optimal for all science, and it will ultimately be up to the user to determine what parameter values optimize scientific return.

PyKE tasks can be called and controlled i) directly from the command line within the PyRAF environment, ii) entirely through GUI-driven operation using the epar function on the command line within the PyRAF environment, or iii) as standalone python scripts called from the command line of a unix/linux shell. For the sake of clarity in these walkthroughs, we provide uniformly the PyRAF GUI task invocations. To get started on each walkthrough - in an xterm (not an OS X terminal window), run the following command in the directory where you have downloaded your Kepler data:
   % mkiraf
setting the terminal type to xterm when asked. Then startup PyRAF and load the PyKE tools in the Kepler package by entering the following commands
   % pyraf
      --> kepler
To execute any task in GUI mode, type epar <taskname>, e.g.
      --> epar kepdraw

* [Extract and cotrend new light curves from Target Pixel Files](http://keplerscience.arc.nasa.gov/PyKEprimerWalkthroughA.shtml)
* [Mitigate motion and focus artifacts by redefining the optimal aperture](http://keplerscience.arc.nasa.gov/PyKEprimerWalkthroughB.shtml)
* [Subjective light curve cotrending using basis vectors](http://keplerscience.arc.nasa.gov/PyKEprimerWalkthroughC.shtml)
* [Removing stellar astrophysics and quarter stitching](http://keplerscience.arc.nasa.gov/PyKEprimerWalkthroughD.shtml)
* [Mitigate K2 motion artifacts by correlating detrended flux with target centroids](http://keplerscience.arc.nasa.gov/PyKEprimerWalkthroughE.shtml)

### Additional tools

A variety of publicly available software exists for inspection of Kepler and K2 FITS
data.  An incomplete list is provided here:

#### FV

Software for display and editing FITS format tables and images, developed and distributed by NASA's High Energy Astrophysics Science
  and Archive Research Center.  Source code or binaries can be
  obtained here.

Kepler Target Pixel Files (TPFs) are provided to the user in the form
of binary FITS tables, one file per target. Each row in the table
contains timestamps, photometric measurements, astrometric
measurements and data quality flags. A format description and content
definition of the TPFs is provided in section 2.3.2 of the Kepler
Archive Manual. Each row of the photometric columns contains a pixel
image of the target. We have found the best tool to inspect the
structure and content of the TPF is the GUI-driven HEASARC tool FV. We
provide a specific example of TPF product inspection using FV. After
starting up the FV application, the primary GUI will open.

**Load data and inspect tabulated data**

Click on the "Open File..." button in the menu.
Use the file browser that pops up to navigate the folders on your system.
Click on the TPF of interest and then the "Open" button.
On the summary GUI, click the "All" button.

The file summary GUI will open, containing the same structure as
illustrated in figure 1. Each row in the summary is a data extension
within the FITS file. All header keywords within the extension will be
provided if you click on one of the "Header" buttons. The "Hist" and
"Plot" buttons provide histograms and line plots of tabulated data.

**Plot target images**
On the table GUI in figure 2, choose a specific row/time and click the "Image" button under the SAP_FLUX column.
On the summary GUI in figure 1, click the "Image" button.
FV will ask whether you want replace the current selected image. Click "No".

<img class="img-responsive" style="min-width:97%;" src="images/TPF-FV3.jpg">

Typical images stored within a TPF. The left-hand image is stored in the time-tagged data table and contains calibrated, background-subtracted and cosmic ray removed pixel fluxes. The right-hand image contains a bitmap that describes the employment of each pixel. Black pixels are not collected, yellow are collected but do not contribute to the photometry stored in the light curve products. White pixels are included in the photometric aperture that maximizes target signal-to-noise over nominal short timescales of observation.

#### TOPCAT

Tool for Operation on Catalogs and Tables, a Java-based interactive graphical viewer and editor for tabular data. TOPCAT can be obtained here.

Kepler times-series light curves are provided to the user in the form
of a binary FITS table, one file per target. Each row in the table
contains timestamps, photometric measurements, astrometric
measurements and data quality flags. A format description and content
definition of the Kepler light curve file is provided in section 2.3.1
of the Kepler Archive Manual. We provide a specific example of light
curve product inspection using the Java tool TOPCAT. After starting up
the TOPCAT application, the main control GUI will open (figure 1). The
left-most icon on the options bar at top allows the user to open and
inspect light curve files. Other icons provide data table display,
data plotting, filtering and statistics, and output of a variety of
different data formats.

**Load data and display data table**

Clicking on the "Load New Table" icon (top-left) will open a new GUI. In the "Format" dialog box scroll down and click on "FITS".
Click on the "Filestore Browser" button to navigate through your directories; choose the desired file by clicking on it.
The file name will appear in the left-hand window of the main GUI. The
number of rows and columns in the table will appear in the right-hand
area.
Clicking the fourth icon from the left in the primary GUI opens the data table within the FITS file for inspection.

**Plot data table**
Click on the icon labeled "Scatter Plot" at the top of the control window. A plotting GUI opens in which data in the TIME column (col. 1) is plotted versus data in the TIMECORR column (col. 2), the default option.
In the plot window, the user can select alternative data columns to plot. For the Y-axis data choose, for example the data column SAP_FLUX. The plot will update with simple aperture photometry against time.
Options for customizing the plot are available using the various icons located above the plot. For example:
Axis titles and XY scale ranges are set using the 3rd icon along the top of the GUI.
Rescale the plot using the arrow icons.
At the bottom right of the plot, under "Row Subsets", click on the rightmost button, to access the Plot Style Editor.
Save the plot to PDF using icon 4.

**Save data table to ASCII*
* Convert data to e.g. ASCII files, using the "Save Table" option - the
second icon from the left at the top of the control window.


#### DS9

SAOImage DS9 is an image visualization application, developed by the Smithsonian Astrophysical Observatory. DS9 can display and compare multiple images together and contains scaling and zoom options. DS9 source code and binaries can be found here.

Kepler Full Frame Images (FFIs) are provided to the user in the form of a binary FITS file. There are 94 million pixels in each FFI. In order to manage this large number of pixel, the data is divided into subimages by readout node. There are 84 readouts spread over 21 CCD modules on the detector plane and therefore there are 84 subimages stored in 84 FITS extensions within the file. Each FFI is 400 MB in size. A format description and content definition of the Kepler FFIs is provided in section 2.3.3 of the Kepler Archive Manual. We provide a specific example of FFI inspection using the DS9 tool.

**Load FFI images**

Start DS9 per your platform-specific method as detailed in the DS9 installation notes.
Under the "File" menu, scroll to the 2nd option, "Open Other", then move the cursor to the right-hand menu and click on "Open Mutli Ext Multi Frames".
A standard directory dialog box should open; navigate to the relevant folder, then scroll through the folder for the desired file. Click on the image.
All FFI subimages, one per channel, will open in a tiled view.
To display a single image from the set, click on it, then under the top-level menu labeled "frame", toggle the "single frame" option.
Toggle between "tile frames" and "single frame" to view any frame on the image.
To load a specific single frame of the image set, click on the "Open" option in the menu under "File". navigate to the relevant folder, then scroll through the folder for the desired image. Enter the name of the image in the box but add an extra qualifier thus: 'filename[nn]', where nn is the HDU or extension number within the FITS file containing the image. The extension number is equivalent to the channel number on the detector mosaic.
Logarithmic image scaling works best for displaying the full dynamic range of the Kepler images.
To adjust the contrast, place the cursor in the image pane, and scroll the mouse, while holding down the right button.
The header keywords for the image can be displayed using the "File"
menu, click on "header". A new window opens asking you to select the
file, click "OK" and another window opens with the header information.

**FFI matching against the DSS**

Under the "Analysis" menu, choose "Image Servers" and "STSCI-DSS I/II".
Click the "Retrieve" button.
Under the "Scale" menu, choose "Linear".
Under the "Frame" menu, choose "Match", then "Frame", then "WCS".
Under the "Frame" menu again, click "Blink".

<img class="img-responsive" style="min-width:97%;" src="images/ds9-dss.jpg">

The result of the example procedure above. A side-by-side comparison of a region within the first Q10 FFI (left) with the same region of the digitized sky survey (right).

Note: With so many subimages within an FFI file, it is not immediately
obvious with DS9 how to navigate to a specific celestial location. The
simplest method to inspect the region around a specific provided
celestial coordinate or Kepler target is to use the tool KeplerFFI
(see below).

#### KeplerFFI

This FFI inspection tool is used to examine the sources surrounding a
target, assess crowding, identify artifacts, and understand the
effects of the photometric aperture on the light curves. KeplerFFI
also creates a custom pixel mask by allowing users to select pixels
for inclusion within a target aperture. Individual pixels are chosen
interactively by tapping upon them. The standalone python tool is
available for download here.

#### MAST FFI Viewer

MAST maintains am online FFI display tool, which allows the user to examine individual channels within an FFI image. Kepler targets, as well as 2MASS and GALEX sources located within the frame are marked with symbols and user-selectable. Sources for which the data have been published or made public are also indicated.

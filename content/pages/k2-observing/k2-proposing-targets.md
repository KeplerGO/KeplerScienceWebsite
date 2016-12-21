Title: K2 proposal preparation
Save_as: k2-proposing-targets.html

[TOC]

There are no guaranteed, or predetermined, targets for any of 
<a href="k2-fields.html">the fields where K2 is pointing</a>.
All targets are proposed by the community 
through the Guest Observer (GO) program. 
This page details the program and its aims.


## Guest Observer program


### Permitted science areas

The K2 GO program welcomes proposals addressing compelling scientific questions 
in **any area of astrophysics and planetary science** 
providing the required observations are amenable 
to the operational characteristics and constraints of the mission. The science motivation may include, but is not limited to, 
exoplanet detection, stellar astrophysics, 
galactic and extragalactic astrophysics, and solar system science. 

All science proposals must be compelling and carefully justified
scientifically and technically. 
Proposers should particularly note that short (1-minute) cadence resources 
and bright (Kp < 9) targets are expensive in pixels and onboard storage 
and have historically been in high demand. 
Proposals for short cadence or bright targets must have a very strong scientific and technical
justification.

Proposers must take into account the difference between science 
that can be achieved exclusively using archived K2 and Kepler data 
and science that requires new observations by K2. 
The K2 GO program is specific to the case of science 
requiring new observations. 
Funding for archival science is instead provided through the Astrophysics Data Analysis Program ([ADAP; ROSES-2016](https://nspires.nasaprs.com/external/solicitations/summary.do?method=init&solId={C8318766-786D-1262-D3C9-9C888D2873CE}&path=closedPast)). 
This includes all Kepler data and archived data from K2 Campaigns. All
proposals to the K2 GO calls therefore must justify 
the need for new observational data within their program. 
However, we welcome proposals that build upon data already collected 
and programs requiring more data to enhance or complete investigations.


### Evaluation criteria

Proposals submitted in response to GO calls will be evaluated 
with respect to the criteria specified 
in Section C.2 of the [NASA Guidebook for Proposers](http://www.hq.nasa.gov/office/procurement/nraguidebook/), which are intrinsic merit,
relevance to the GO solicitation, 
and the realism/reasonableness of the proposed work effort and resources. 
In addition to the factors for intrinsic merit 
given in the NASA Guidebook for Proposers, 
intrinsic merit includes the following factors:

 * The suitability of using the K2 observatory and data products for the proposed investigation;
 * The legacy value of the data collected;
 * The degree to which the investigation uses K2’s unique capabilities;
 * The feasibility of accomplishing the objectives 
of the proposed investigation with the requested observations, 
including the degree to which the proposal satisfies 
K2’s observational constraints; and
 * The feasibility and suitability of the proposed analysis techniques.

All proposals are peer-reviewed and ranked by a panel of professional volunteers, followed by ratification from NASA Headquarters. The members of the peer-review panel will not be disclosed. The deliberations of the panel will be disclosed to PIs only after ratification by the selecting official.

### Availability of funds

There are typically two categories of K2 GO proposals.
They are:

 * Small proposals—proposals requesting fewer than 1000 targets, 
with a budget capped at $50,000.
 * Large proposals—proposals requesting 1000 or more targets, 
with a budget capped at $150,000. 
Large proposals must also include the development and dissemination 
of a value-added community resource product that the proposal will provide at the end of the period of performance of the grant and how that product will be made available to the community.

Funding for selected programs typically starts upon availability 
of Campaign data to the public archive 
at [MAST](http://archive.stsci.edu/k2/). 
Note that there is no exclusive use period associated with any K2 GO data. 


### Eligibility

Application to the K2 GO program is typically open to all investigators,
including those from outside the U.S. 
under NASA’s no-exchange-of-funds policy. 

Investigators who are not affiliated with a U.S. institution 
are not eligible for funding through this program,
but may submit proposals that will be reviewed and ranked 
along with eligible proposals for the purpose of allocating targets.

Co-Investigators (Co-Is) affiliated with a U.S. institution 
are eligible to receive funding under a proposal led by a foreign PI. 
In this scenario, only a single Co-Investigator per proposal will be considered as a lead PI for funding purposes, 
and proposals should identify a lead Co-Investigator within the U.S.

In accordance with Public Law 113--76, Division B, Title V, Section 532, NASA cannot support bilateral participation, collaboration, or coordination with China or any Chinese-owned company or entity, whether funded or performed under a no-exchange-of-funds arrangement. See Section III(c) of the ROSES-2016 NRA for more information on these restrictions. 

## Target selection

### Tools

Pointed observations away from the single stare position of any given field 
cannot be accommodated by K2; Campaign targets are limited to the objects 
available in <a href="k2-fields.html">the fixed field of view</a>. 

Small gaps between the 42 detector CCDs as well as the three dead modules result in additional loss 
of available objects that would otherwise be within the field of view. 
A <a href="http://archive.stsci.edu/k2/epic/search.php">documented target search tool at MAST</a> determines if an object of a particular coordinate 
lies close to the observable field of view. 

The target search tool accesses the Ecliptic Plane Input Catalog (EPIC), 
which provides physical data, coordinates, magnitudes, and colors, 
for sources close to K2 silicon. 
The EPIC is complete only to m<sub>V</sub> ~ 17; 
specifications of the catalog are [documented here](http://archive.stsci.edu/k2/epic.pdf). 

It is the proposer’s responsibility to identify targets 
that are faint or missing from the EPIC. 
K2 collection of valid data relies on the delivery 
of accurate celestial positions and magnitudes of each target. 
Proposals must state the origin for this information, 
especially if it does not come from the EPIC.  Extended targets or
targets with high proper motion should also be noted by the proposer.

Determining whether or not desired targets fall on active regions 
of the focal plane is also the responsibility of the proposer. 
The Kepler & K2 Science Center provides a tool called
[K2fov](software.html#k2fov)
to identify which targets fall upon active silicon. 
Only those targets within the active fields of view should be proposed.

Note that all investigators *must* update their version of 
K2fov to the latest version (v6.2) to take the final field positions of Campaigns 14-15-16 into account. 
K2fov can be updated from the command line using pip:

    pip install K2fov --upgrade

The version number of your K2fov installation may be verified
using the following command:

    python -c "import K2fov; print(K2fov.__version__)"

This must return "6.2.0" or higher. If the number is lower,
or if you see an error message, then your installation of K2fov is outdated
and must be upgraded.
Not upgrading K2fov will lead to unobservable targets being selected!


### Target table

All proposals for targets are required to include a target table 
in a pre-defined format to specify desired observing modes 
and other needed parameters. 

The target tables generally provide all the information required by
the Kepler & K2 Science Center to incorporate GO sources within the observing list. Table fields are described below with an example. If a proposal includes targets within multiple campaign fields, then a separate target table should be prepared for each field.

An example of a valid target table is shown in the image below. <a
href="data/K2/K2-2-propnum-PI.xls">The corresponding .xls file can be downloaded here.</a>

<a href="images/template-target-table.png"><img
src="images/template-target-table.png" class="img-responsive"
alt="Template Target Table"></a>

A definition of each column is included in the below table.

<table class="table table-striped table-hover" style="max-width:70em;">
  <thead>
    <tr>
      <th>Attribute</th>
      <th>Description</th>
    </tr>
  </thead>

<tdata>

<tr>
    <td style="min-width: 10em;">Object </td>
    <td>The Ecliptic Plane Input Catalog (EPIC) ID number. This
    attribute can be determined by using the <a
href="http://archive.stsci.edu/k2/epic/search.php">K2 EPIC Target
    Search</a> page. The EPIC ID is coupled to celestial coordinates and magnitudes. If the proposed target does not have an EPIC ID number please use a unique identifier, common or catalog name for this source, and supply the J2000 celestial coordinates in the Right Ascension and Declination columns of your target table.</td>
</tr>

<tr>
    <td>Right Ascension </td>
    <td>Right Ascension (J2000) of the center of the desired aperture. Celestial coordinates are only required if the target is not listed in the <a
href="http://archive.stsci.edu/k2/epic/search.php">K2 EPIC Target
    Search</a> page. Adhere to decimal degree format. </td>
</tr>

<tr>
    <td>Declination </td>
    <td>Declination (J2000) of the center of the desired aperture. Celestial coordinates are only required if the target is not listed in the <a
href="http://archive.stsci.edu/k2/epic/search.php">K2 EPIC Target
    Search</a> page. Adhere to decimal degree format. </td>
	</tr>

<tr>
    <td>Kp </td>
    <td>The apparent magnitude of the target in the Kepler
    bandpass. The combination of celestial coordinates and magnitude
    are the primary data required by the Kepler & K2 Science Center to calculate target pixel masks. The Kepler magnitude for most sources can be obtained from the <a
href="http://archive.stsci.edu/k2/epic/search.php">K2 EPIC Target
    Search</a> page. If no Kepler bandpass magnitude is provided in the EPIC, <a
href="/the-kepler-space-telescope.html#flux-calibration">it
    can be estimated</a>. If the magnitude entered here is brighter than the EPIC magnitude, then the user-supplied magnitude will be adopted. For highly-variable stars, list the brightest predicted magnitude.
 </td>
</tr>

<tr>
    <td>Cadence Mode </td>
    <td>The observing mode requested. Long cadence (30-minute) mode or Short cadence (1-minute) mode. </td>
	</tr>

<tr>
    <td>&delta;RA </td>
    <td>Proper motion of the target in units of arcsec per year. This information is optional and should only be provided if the proposer disagrees with the proper motion provided in the EPIC. </td>
	</tr>

<tr>
    <td>&delta;Dec </td>
    <td>Proper motion of the target in units of arcsec per year. This information is optional and should only be provided if the proposer disagrees with the proper motion provided in the EPIC. </td>
</tr>

<tr>
    <td>Extent </td>
    <td>The radius of the semi-major axis of an extended target such as a galaxy. To reiterate, this is the radius, NOT the diameter i.e. the furthest distance that structure extends from the target coordinates provided. This column should be ignored if all targets are point sources. </td>
	</tr>

<tr>
    <td>Comments </td>
    <td>If a target is non-standard, provide a brief description of non-standard table entries including: (a) user-supplied magnitude; (b) user-supplied coordinates; (c) extended sources; (d) the amplitude of highly variable stars, (e) high proper motion stars; (f) custom mask requests. Comments should be expanded upon within the text of the science justification of the proposal. </td>
	</tr>
	
</tdata>
</table>

A blank template target table for insertion into the proposal 
can be [downloaded here](data/K2/K2-Cnn-propnum-PINAME.xls). 

Each campaign target table must appear in two places:

1.  Embedded within the body of your uploaded proposal package to NSPIRES.
2.  As a separate electronic file submitted directly to the Kepler & K2 Guest Observer Office.

Instructions on how to provide both versions of the table are detailed below: 

1.  Download the template file written in Microsoft Excel format: <a
href="data/K2/K2-Cnn-propnum-PINAME.xls">K2-Cnn-propnum-PINAME.xls</a>
2.  Populate the table using either Microsoft Excel or the freeware [OpenOffice](http://www.openoffice.org/) package. Insert additional table rows if needed, one per proposed target.
3.  Copy / paste or encapsulate the table into the submission package between the science justification / technical management section and the PI's biography.
4.  Rename the Excel spreadsheet according the format
    K2-Ccampaign-no-propid-PIname.xls, where propid is the proposal ID
    number assigned to the proposal by NSPIRES at the time of
    submission and PIname is the surname of the PI. A separate target
    table should be created for each campaign.  An example would be K2-C04-0097-SMITH.xls
5.  Attach the renamed spreadsheet to an email and send it to the GO
    Office at **keplergo@mail.arc.nasa.gov** before the proposal deadline.

**Special instructions for moving targets**<br/>

If you plan to submit a proposal for a Solar System (moving) target, we recommend that you adhere to the following guidelines:<br/>

1. Only include a single row in your target table for each moving target.  You are not required to include coordinates as long as you provide the name or number of the object exactly as it is known in JPL Horizons. 
2. State (a) the minimum and (b) the ideal number of days during which each target needs to be observed to meet the goals of your scientific investigation. 
3. Provide a rough estimate of the pixel cost corresponding to both the minimum and ideal observing durations for each target.  Please get in touch with us at **keplergo@mail.arc.nasa.gov** if you require assistance with this.

## Solicitations

**The most recent call for K2 GO Cycle 5 proposals, which included <a href="k2-fields.html">Campaigns 14, 15,
and 16</a>,
[was released and made available at NSPIRES](https://nspires.nasaprs.com/external/solicitations/summary.do?method=init&solId={D68A4380-B327-7C96-04CF-02B0FC940DBF}&path=open). The
call is now closed. Details relevant to that call are below.  Stay
tuned for a call for GO Cycle 6.**

We
are requesting the community propose targets to observe
during only these three campaigns. Based on recent estimates of the remaining fuel on the Kepler
 spacecraft, it is anticipated that Campaign 17 and beyond will be conducted
 at risk.  In order to maximize the
 science return from the K2 mission, we changed the position of the field for C16.
 C16 will now involve the Kepler spacecraft observing in the forward-facing direction, and a significant fraction of pixels will
 be dedicated to supernova science.  Proposals covering all other
 areas of astrophysics and planetary science are still encouraged for
 C16.  In particular, we strongly encourage programs that can
 benefit from simultaneous observations from
 Earth. [The final field positions are posted here](k2-fields.html).

### FAQs  

* **What are the proposal deadlines?**<br/>
The deadlines for GO Cycle 5 have passed.  Stay tuned for a call
for GO Cycle 6.
  
* **What are the anticipated dates of the campaigns included in the
current solicitation?**<br/>
Campaign 14: 2017 May 31 - Aug 19 <br/>
Campaign 15: 2017 Aug 23 - Nov 20 <br/>
Campaign 16: 2017 Dec 07 - 2018 Feb 25 <br/>
Start and stop dates for all campaigns are approximate, flexible and
could be overtaken by unanticipated operational events.<br/>

* **Where are the fields located on the sky for the campaigns included in the
current solicitation?**<br/>
The pointings for all K2 campaigns can be found on the <a
href="k2-fields.html">fields page.</a> Proposers
should be aware that changes were made to the pointing for Campaign 16 and should only propose for
 targets that are on active silicon in the updated Campaign 16
 field.  All investigators *must* update their version of the
<a href="software.html#k2fov">K2fov target selection tool</a>
to account for the recent changes to Campaign 16. <br/>

* **Should I submit one proposal or two?**<br/>
  In the interest of efficiency, proposers are requested *NOT* to provide separate proposals with identical science cases for each of the campaigns. If the same science goals are spread across both campaigns, please provide one science justification and two target tables, one for each field.<br/>
  
* **How do I select targets on silicon?**<br/>
  In order to avoid inefficiency for proposers, you are encouraged to
  use the <a href="software.html#k2fov">K2fov tool</a> to
  determine whether your targets fall upon silicon and propose only
  those that do. The precision of this tool is a few 4x4 arcsec
  detector pixels. <br/>

* **Should I apply for targets that do not fall on silicon?**<br/>
  Please, no. Proposing off-silicon targets is a waste of energy for proposers, reviewers and project staff. Use <a href="software.html#k2fov">K2fov</a> and apply only for targets that fall upon silicon (output flag "2").<br/>

* **What is the K2 Ecliptic Plane Input Catalog (EPIC)?**<br/>
  Proposers are asked to submit targets that have been selected from the <a href="http://archive.stsci.edu/k2/epic/search.php">EPIC</a>. The EPIC plays the same role for K2 that the <a href="http://adsabs.harvard.edu/abs/2011AJ....142..112B">Kepler Input Catalog (KIC)</a> played for Kepler target selection. The primary purpose of the catalog is to define photometric apertures for each potential target by providing celestial positions and Kepler bandpass magnitudes. EPIC parameters are produced by source matching existing multi-band catalogs and calculating color corrections for the Kepler bandpass. Documentation describing the compilation of the EPIC is provided <a href="http://archive.stsci.edu/k2/epic.pdf">here</a>.<br/>

* **What type of science targets can be proposed?**<br/>
  There are no constraints on the type of science or science target that can be proposed.<br/>

* **How many targets can be proposed?**<br/>
  Both long cadence (30-min exposure) and short cadence (1-min
  exposure) targets will be observed during each Campaign. There are
  no constraints whatsoever on the number of targets that can be
  proposed. The total long cadence target list is expected to be
  between 10,000 and 20,000 targets per Campaign. Approximately 50 to 100 short cadence targets are anticipated per Campaign.<br/>

* **How many pixels around each target will be collected?**<br/>
  The number of pixels collected for each target depends on the
  target's Kepler magnitude.  For Kp = 12, the target pixel masks include
  approximately 100 pixels.  Extra halos of pixels will be added to K2 masks in order to capture uncertainties in field acquisition (currently a pixel) and pointing drift over time (currently a pixel).<br/>

* **Are there bright or faint magnitude limits?**<br/>
  There are no faint limits upon the brightness of targets that can be
  proposed. Bright targets will be significantly more expensive in
  terms of pixel usage. Targets brighter than 3rd magnitude in the
  Kepler bandpass cannot be observed because charge bleeding along CCD
  pixel columns will fall into collateral pixels of the
  detector. Bright targets (Kp < 9) and short cadence targets require
  strong, compelling science cases.<br/>

* **How do I propose a moving target?**<br/>
 The proposal process is the same for a Solar System or moving target
 as it is for other targets. However, proposers should take note of
 recommendations when creating the [target table for moving targets](k2-proposing-targets.html#target-table).


### Submission process

K2 proposal submission is a 2-step process. Both steps are
mandatory. To propose for Campaigns 14, 15 and 16, investigators are
required to submit Step 1 through the NSPIRES website by <font color='black'>23:59 EST
November 3, 2016</font> and are required to submit Step 2 to the NSPIRES
website by <font color='black'>23:59 EST December 15, 2016</font>. All proposers need to register
with NSPIRES in order to submit both parts of the proposal. The
separation of the proposal into two steps is required in order to
expedite the completion of review administration and target
engineering before the start of Campaign 14. Detailed instructions for
submitting a K2 proposal to the GO call are provided below:

* If new to the NASA Solicitation and Proposal Integrated Review and
  Evaluation System, NSPIRES,
  [register on the NSPIRES website](https://nspires.nasaprs.com/external/aboutRegistration.do).

* Familiarize yourself with the NASA Research Announcement (NRA) Research Opportunities in Space and Earth Sciences Announcement 2016 [(ROSES-2016)](https://nspires.nasaprs.com/external/solicitations/summary.do?method=init&solId={68C12087-132D-3814-9A87-5323BCE6CAB6}&path=open&redirectURL=%2Fexternal%2Fsolicitations%2Fsolicitations.do%3Fmethod%3Dopen%26stack%3Dpush). This document provides an overview of the NRA process and is a compilation of most solicitations within NASA's Science Mission Directorate.

* Read the
  [Cycle 5 K2 Research Announcement](https://nspires.nasaprs.com/external/solicitations/summary.do?method=init&solId={D68A4380-B327-7C96-04CF-02B0FC940DBF}&path=open). New
  amendments to the NRA are publicized at NSPIRES. Check this page
  regularly. 

* [Submit Step 1 of
      the proposal to NSPIRES](http://nspires.nasaprs.com/external/)
      by <font color='black'>23:59 EST November 3, 2016</font>.  [Instructions for
      Step 1 submission can be found here](https://nspires.nasaprs.com/external/viewrepositorydocument/cmdocumentid=498339/solicitationId=%7BD68A4380-B327-7C96-04CF-02B0FC940DBF%7D/viewSolicitationDocument=1/Step-1%20instructions%2002182016.pdf). 

* [Submit Step 2 of
      the proposal to NSPIRES](http://nspires.nasaprs.com/external/)
      by <font color='black'>23:59 EST December 15, 2016</font>. 

*  The generic content of the proposal is described in Sec 2.3 of the
    <a
    href="http://www.hq.nasa.gov/office/procurement/nraguidebook/proposer2016.pdf">2016
    NRA Proposers Guide</a>. Page
    limits and proposal content within the NRA Guide are amended
    within the
    [K2 GO Cycle 5 NRA](https://nspires.nasaprs.com/external/solicitations/summary.do?method=init&solId={D68A4380-B327-7C96-04CF-02B0FC940DBF}&path=open)
    and are summarized in the table below.   The
    right-hand column provides page limits for the package elements. Caveats to the page limits are provided as footnotes. *The page limits on this website override the NRA-generic limits within the handbook.*
    The Scientific/Technical/Management section of the
    Step 2 proposal, which consists of text, tables (excluding the
    target table), and figures must not exceed four pages for
    proposals in the Small category, or six pages for proposals in the
    Large category. An additional 0.5 pages is allowed in Large proposals to describe
    progress the proposers have made to delivering value-added
    community resources.  References and the target table do not count against the four or
    six page
    limit, however, the
completed package uploaded to NSPIRES for the Scientific/Technical/Management
    section must not exceed 15 pages. If a large target
table extends beyond the 15 page limit then truncate the table so that
the page limit is not exceeded and make a note within the proposal
that the table has been truncated. Page limits for the PI and Co-I biographies and
    current and pending support are defined below, and are 
    separate from the 15 page limit for the
    Scientific/Technical/Management section.  PIs should not feel compelled to
meet the page limits, but must submit all items appropriate to their
proposal and should not exceed the page limits as defined below.


<table class="table table-striped table-hover" style="max-width:70em;">
  <thead>
    <tr>
      <th>Required Content for Step 2 Proposals</th>
      <th>Page Limit</th>
    </tr>
  </thead>

<tdata>

<tr>
    <td style="min-width: 5em;">Table of Contents </td>
    <td>1</td>
	</tr>

<tr>
    <td>Scientific Justification/Technical/Management Section, "Small" proposals<sup>†</sup> </td>
    <td>4</td>
	</tr>

<tr>
    <td>Scientific Justification/Technical/Management Section, "Large" proposals<sup>†</sup><sup>&Dagger;</sup> </td>
    <td>6</td>
	</tr>

<tr>
    <td>Target Table </td>
    <td>as needed</td>
	</tr>

<tr>
    <td>References</td>
    <td>as needed</td>
	</tr>

<tr>
    <td>PI Biography </td>
    <td>2</td>
	</tr>

<tr>
    <td>Co-I Biography </td>
    <td>1 per Co-I</td>
	</tr>

<tr>
    <td>Current and Pending Support </td>
    <td>as needed</td>
	</tr>
	
</tdata>
</table>
<sup>†</sup>Includes text, tables, and figures. References and the
required target table do not count against these four or six page limits, but the
target table should be truncated in cases where it would cause this specific
section to exceed 15 pages.<br/>
<sup>&Dagger;</sup>An additional 0.5 pages is allowed in "Large" proposals to describe
    progress the proposers have made to delivering value-added
	community resources, but the Scientific/Technical/Management
	section still must not exceed 15 pages.

In summary, proposers should:

  * Understand the scope of the
        Guest Observer program. Science papers exploiting data from the Kepler and K2 mission can be found [here](publications.html).
  * Familiarize yourself with the [technical documentation](data-products.html#documentation) for the mission.
  * Develop and justify a science concept for observations
          within Campaigns specific to the current GO Cycle <a href="fields.html"></a>.
   * Identify appropriate targets for the proposed observations using the
        <a href="http://archive.stsci.edu/k2/epic/search.php">K2 Target Search</a> page as the primary (but not exclusive) source list. This search page provides for the construction of short or long target lists based upon e.g. celestial cone searches, magnitude and color.
   * Include a [Target Table](k2-proposing-targets.html#target-table)
     as an integral component of the proposal and as a separate
     submission to the Guest Observer Office at **keplergo@mail.arc.nasa.gov**. 
   * Provide the administrative elements of the proposal
          including a proposer biographical information, and a
          statement of current and pending financial support.
   * **Large proposals that anticipate delivery of a data product/products
  to one of the NASA archives (e.g., MAST or the NASA Exoplanet
  Database) for curation must also include a letter of acknowledgement from
  the relevant archive.**
   * **Although a detailed budget is not requested in either Step 1 or
  Step 2 proposals, the Step 2 proposal should include either a
  statement of work or a table summarizing the work effort.  If the
  statement of work is included in the Scientific/Technical/Management
  section it will count against the page limit for that section, but a
  table can be included as a separate section that will not count
  against the Scientific/Technical/Management section page limit .**  The
  statement of work should clearly identify any and all members of the proposing team
  who would receive funding under the proposed investigation. The
  funding amounts will be determined formulaically based on target
  allocation.**
  * **Special instructions for non-US PIs**<br/>
During the submission process, non-US PI-led proposals will need to be
affiliated to a submitting organization. Do this by clicking on the
"Account Mgmt" tab at the top of the NSPIRES page and follow the
instructions. All non-US proposals should use the "Kepler Guest
Observer Office" as your affiliation within NSPIRES. This is simply a
fudge, albeit a required fudge, so that non-US PIs spend no more
effort than this over the institutional endorsements that are
mandatory for US investigators. When completing the proposal, there are a few obscure boxes on the standard form that need your attention. The organization name is "Kepler Guest Observer Office", doing business as the "Kepler Guest Observer Office". The DUNS number is "999999954" and the cage code is "ZZZ54". These details will make sense to you when you see the Step 2 proposal form. 


### Director's Discretionary Time

A small part of the pixel budget may be allocated by the project as Director's Discretionary Targets (DDT),
which is intended to facilitate observations that address
scientific topics missed in the proposal review process.
More information and deadlines are available from the [DDT program page](k2-ddt.html).

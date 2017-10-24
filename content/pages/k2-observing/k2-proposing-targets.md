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
to the operational characteristics and constraints of the mission.
The science motivation may include, but is not limited to, 
exoplanet detection, stellar astrophysics, 
galactic and extragalactic astrophysics, and solar system science. 

All science proposals must be compelling and carefully justified
scientifically and technically. 
Proposers should particularly note that short (1-minute) cadence resources 
and bright (Kp < 9) targets are expensive in pixels and onboard storage 
and have historically been in high demand. 
Proposals for short cadence or bright targets must have a very strong scientific
and technical justification.

Proposers must take into account the difference between science 
that can be achieved exclusively using archived K2 and Kepler data 
and science that requires new observations by K2. 
The K2 GO program is specific to the case of science 
requiring new observations. 
Funding for archival science is instead provided through the
Astrophysics Data Analysis Program ([ADAP; e.g. see ROSES-2017 solicitation](https://nspires.nasaprs.com/external/solicitations/summary.do?method=init&solId={9B644CB9-C0A8-8F23-DE92-FA3837D2F0BD}&path=closedPast)). 
This includes all Kepler data and archived data from K2 Campaigns. All
proposals to the K2 GO calls therefore must justify 
the need for new observational data within their program. 
However, we welcome proposals that build upon data already collected 
and programs requiring more data to enhance or complete investigations.


### Evaluation criteria

Phase-1 proposals consisting of target lists and a scientific justification
that are submitted in response to the K2 GO Cycle 6 call
will be evaluated primarily on the scientific merit and the long-term
legacy value in observing the proposed targets. The Phase-1 proposals
will be peer-reviewed and will support target selection for the
campaigns to be observed in Cycle 6.

Phase-2 proposals submitted via NSPIRES in response
the K2 GO Cycle 6 call will be evaluated 
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

All Phase-2 proposals are peer-reviewed and ranked by a panel
of professional volunteers, followed by ratification from NASA Headquarters.
The members of the peer-review panel will not be disclosed.
The deliberations of the panel will be disclosed to PIs only after ratification
by the selecting official.

### Availability of funds

There are typically two categories of K2 GO proposals.
They are:

 * Small proposals—proposals requesting fewer than 1000 targets, 
with a budget capped at $50,000.
 * Large proposals—proposals requesting 1000 or more targets, 
with a budget capped at $150,000. 
Large proposals must also include the development and dissemination 
of a value-added community resource product that the proposal
will provide at the end of the period of performance of the grant
and how that product will be made available to the community.

Funding for selected programs typically starts upon availability 
of campaign data to the public archive 
at [MAST](http://archive.stsci.edu/k2/). 
Note that there is no exclusive use period associated with any K2 GO data. 

In K2 GO Cycle 6, only Phase-2 proposals are considered for funding.

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
In this scenario, only a single Co-Investigator per proposal will be considered
as a lead PI for funding purposes, 
and proposals should identify a lead Co-Investigator within the U.S.

In accordance with Public Law 113--76, Division B, Title V, Section 532,
NASA cannot support bilateral participation, collaboration,
or coordination with China or any Chinese-owned company or entity,
whether funded or performed under a no-exchange-of-funds arrangement.
See Section III(c) of the ROSES-2017 NRA for more information on these restrictions. 

## Target selection

### Tools

Pointed observations away from the single stare position of any given field 
cannot be accommodated by K2; campaign targets are limited to the objects 
available in <a href="k2-fields.html">the fixed field of view</a>. 

Small gaps between the 42 detector CCDs as well as the three dead modules
result in additional loss of available objects that would otherwise be within
the field of view. 
A <a href="http://archive.stsci.edu/k2/epic/search.php">documented target search tool at MAST</a>
determines if an object of a particular coordinate 
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
K2fov to the latest version (v7.0) to take the final field positions
of Campaigns 17-18-19 into account. 
K2fov can be updated from the command line using pip:

    pip install K2fov --upgrade --no-deps

The version number of your K2fov installation may be verified
using the following command:

    python -c "import K2fov; print(K2fov.__version__)"

This must return "7.0.0" or higher. If the number is lower,
or if you see an error message, then your installation of K2fov is outdated
and must be upgraded.
Not upgrading K2fov will lead to unobservable targets being selected!


### Target table

All proposals are required to include a target table 
in a pre-defined format to specify desired observing modes 
and other needed parameters. 

The target tables generally provide all the information required by
the Kepler & K2 Science Center to incorporate sources within the observing list.
Table fields are described below with an example.
If a proposal includes targets within multiple campaign fields,
then a separate target table should be prepared for each field.

An example of a valid target table is shown in the image below.
<a href="data/K2/K2-2-propnum-PI.xls">The corresponding .xls file can be downloaded here.</a>

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
can be [downloaded here](data/K2/K2-Cnn-PINAME.xls). 

Target tables for each campaign are required to be submitted via email
directly to the Kepler & K2 GO Office for Phase-1 proposals submitted in response to GO Cycle 6.
They do not need to be embedded within the text of the proposal.

For GO Cycle 6 Phase-2 proposals that are submitted via NSPIRES
in order to request funding, a target table for each campaign
must appear in two places:

1.  Embedded within the body of your uploaded proposal package to NSPIRES.
2.  As a separate electronic file submitted directly to the Kepler & K2 GO Office.

Instructions on how to provide both versions of the table are detailed below: 

1.  Download the template file written in Microsoft Excel format: <a
href="data/K2/K2-Cnn-PINAME.xls">K2-Cnn-PINAME.xls</a>
2.  Populate the table using either Microsoft Excel or the freeware [OpenOffice](http://www.openoffice.org/) package. Insert additional table rows if needed, one per proposed target.
3.  Copy / paste or encapsulate the table into the submission package
    between the science justification / technical management section
    and the PI's biography (only required for Phase-2 proposals).
4.  Rename the Excel spreadsheet according the format
    K2-Cnn-PIname.xls, where PIname is the surname of the PI.
    A separate target table should be created for each campaign.
    An example would be "K2-C17-SMITH.xls".
    If you plan on submitting a second proposal, use "K2-C17-SMITH-2.xls".
5.  Attach the renamed spreadsheet to an email and send it to the GO
    Office at **keplergo@mail.arc.nasa.gov** before the proposal deadline.

**Special instructions for moving targets**<br/>

If you plan to submit a proposal for a Solar System (moving) target,
we recommend that you adhere to the following guidelines:<br/>

1. Only include a single row in your target table for each moving target.
You are not required to include coordinates as long as you provide
the name or number of the object exactly as it is known in JPL Horizons. 
2. State (a) the minimum and (b) the ideal number of days
during which each target needs to be observed to meet the goals
of your scientific investigation. 
3. Provide a rough estimate of the pixel cost
corresponding to both the minimum and ideal observing durations for each target.
Please get in touch with us at **keplergo@mail.arc.nasa.gov**
if you require assistance with this.

## Solicitations

**The call for K2 GO Cycle 6 proposals has been
[released and made available at NSPIRES](https://nspires.nasaprs.com/external/solicitations/summary!init.do?solId={7DC22936-4C6A-44FC-74A3-F0C9248DC9DD}&path=open).
Due to the uncertainty in the estimated spacecraft fuel available for the K2 Mission,
which under normal operational conditions, suggest a depletion in the near future,
we are presenting a different proposal submission and target selection process for K2 Cycle 6,
which comprises Campaigns 17, 18, and 19.
We are requesting the community propose targets to observe 
during only these three campaigns.
Note that C17 and C19 involve the Kepler spacecraft observing
in the forward-facing direction.
We strongly encourage programs that can benefit from simultaneous observations
from Earth. [The final field positions are posted here](k2-fields.html).**

### FAQs  

* **What are the proposal deadlines?**<br/>
Phase-1 proposals for Cycle 6 are due October 12, 2017 by 23:59 (EDT). <br/>
Phase-2 proposals for Cycle 6 are due April 19, 2018 by 23:59 (EDT).

  
* **What are the anticipated dates of the campaigns included in the
current solicitation?**<br/>
Campaign 17: 2018 Mar 01 - May 08 <br/>
Campaign 18: 2018 May 12 - Aug 02 <br/>
Campaign 19: 2018 Aug 06 - Oct 10 <br/>
Start and stop dates for all campaigns are approximate, flexible and
could be overtaken by unanticipated operational events.<br/>

* **Where are the fields located on the sky for the campaigns included in the
current solicitation?**<br/>
The pointings for all K2 campaigns can be found on the <a
href="k2-fields.html">fields page.</a>
All investigators *must* update their version of the
<a href="software.html#k2fov">K2fov target selection tool</a>
to account for the final field positions. <br/>

* **Should I submit one proposal or two?**<br/>
  In the interest of efficiency, proposers are requested *NOT* to
  provide separate proposals with identical science cases for each of
  the campaigns. If the same science goals are spread across multiple
  campaigns, please provide one science justification and up to three target tables,
  one for each field.<br/>
  
* **How do I select targets on silicon?**<br/>
  In order to avoid inefficiency for proposers, you are encouraged to
  use the <a href="software.html#k2fov">K2fov tool</a> to
  determine whether your targets fall upon silicon and propose only
  those that do. The precision of this tool is a few 4x4 arcsec
  detector pixels. <br/>

* **Should I apply for targets that do not fall on silicon?**<br/>
  Please, no. Proposing off-silicon targets is a waste of energy for proposers,
  reviewers and project staff.
  Use <a href="software.html#k2fov">K2fov</a> and apply only for targets
  that fall upon silicon (output flag "2").<br/>

* **What is the K2 Ecliptic Plane Input Catalog (EPIC)?**<br/>
  Proposers are asked to submit targets that have been selected
  from the <a href="http://archive.stsci.edu/k2/epic/search.php">EPIC</a>.
  The EPIC plays the same role for K2
  that the <a href="http://adsabs.harvard.edu/abs/2011AJ....142..112B">Kepler Input Catalog (KIC)</a>
  played for Kepler target selection.
  The primary purpose of the catalog is to define photometric apertures
  for each potential target by providing celestial positions
  and Kepler bandpass magnitudes.
  EPIC parameters are produced by source matching existing multi-band catalogs
  and calculating color corrections for the Kepler bandpass.
  Documentation describing the compilation of the EPIC
  is provided <a href="http://archive.stsci.edu/k2/epic.pdf">here</a>.<br/>

* **What type of science targets can be proposed?**<br/>
  There are no constraints on the type of science or science target
  that can be proposed.<br/>

* **How many targets can be proposed?**<br/>
  Both long cadence (30-min exposure) and short cadence (1-min
  exposure) targets will be observed during each campaign. There are
  no constraints whatsoever on the number of targets that can be
  proposed. The total long cadence target list is expected to be
  between 10,000 and 20,000 targets per campaign.
  Approximately 50 to 100 short cadence targets are anticipated per campaign.<br/>

* **How many pixels around each target will be collected?**<br/>
  The number of pixels collected for each target depends on the
  target's Kepler magnitude.  For Kp = 12, the target pixel masks include
  approximately 100 pixels. 
  Extra halos of pixels will be added to K2 masks in order to capture
  uncertainties in field acquisition (currently a pixel)
  and pointing drift over time (currently a pixel).<br/>

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
 as it is for other targets.
 However, proposers should take note of recommendations when creating the
 [target table for moving targets](k2-proposing-targets.html#target-table).


### Submission process

K2 proposal submission for GO Cycle 6, which includes Campaigns 17,
18, and 19, is a different process than has
been previously been used due to the uncertainty in the estimated
spacecraft fuel available.
Target lists and accompanying scientific justifications for these campaigns
are now required to be submitted as part of a Phase-1 submission,
which was not required in prior K2 Cycles.
The Phase-1 submission is designed to enable targets to be selected via peer review
ahead of these campaigns, allowing the Phase-2 deadline for funding proposals
to be postponed until after the successful start of Campaign 17 is confirmed.

To propose specific targets to be observed in Campaigns 17, 18, and/or
19, investigators are
required to submit Phase-1 proposals via email directly to the GO Office by <font color='red'>23:59 EDT
October 12, 2017</font>.
A Phase-1 submission is encouraged, but not mandatory, to qualify for Phase-2.

To propose for funding to support scientific investigations of targets
selected for observations in Campaigns 17, 18 and/or 19, investigators are
required to submit Phase-2 proposals through the NSPIRES website by <font color='red'>23:59 EDT
April 19, 2018</font>. All proposers need to register
with NSPIRES in order to submit a Phase-2 proposal. Note that Phase-2
proposals will only be solicited and accepted upon the successful initiation of
Campaign 17 and if allowed by the spacecraft health and fuel.

**Detailed instructions for submitting a Phase-1 proposal are provided below:**

* Phase-1, for all three campaigns combined, will consist of 2 pages of text for small programs (less than 1000 targets) and 4 pages for large programs (1000 targets or more), including all figures, tables, and references, in a PDF file. The text shall be no smaller than 12-point font. 

* The Phase-1 proposal must include a title, team, and summary,
followed by a body of text which offers a strong scientific justification
of the target list and explains the long-term legacy value of the proposed targets.
Large programs must also include a detailed description of the target selection criteria,
and explain how the target list may be de-scoped if required
by the spacecraft’s limited on-board storage.
<b>Proposers are encouraged to use the Phase-1 proposal template
available [here in Word format](data/K2/k2go6_template.docx)
and [here in Latex format](data/K2/k2go6_template.tex).</b>

* Separate target tables (one per campaign), which do not count toward
  the 2/4-page limit for the scientific justification, must be prepared in the [format specified here](https://keplerscience.arc.nasa.gov/k2-proposing-targets.html#target-table). **Targets in the list must be ordered by priority.**

* Submit a Phase-1 proposal (one PDF document) and all relevant target
      tables (one per campaign) via email directly to the GO Office
      (**keplergo@mail.arc.nasa.gov**) by
      <font color='red'>23:59 EDT October 12, 2017</font>. 

**Detailed instructions for submitting a Phase-2 proposal are provided below:**

* Phase-2 proposals and accompanying target tables must only include
  targets that have been selected as part of Phase-1, the selection
  results of which will be published in February 2018 [here]( https://keplerscience.arc.nasa.gov). Proposers should verify that
  the targets that funding is requested to support have been selected
  for observations in Cycle 6.

* If new to the NASA Solicitation and Proposal Integrated Review and
  Evaluation System, NSPIRES,
  [register on the NSPIRES website](https://nspires.nasaprs.com/external/aboutRegistration.do).

* Familiarize yourself with the NASA Research Announcement (NRA) Research Opportunities in Space and Earth Sciences Announcement 2017 [(ROSES-2017)](https://nspires.nasaprs.com/external/solicitations/summary!init.do?solId={E757EF32-60E6-76AE-A276-21A1F8BA96BB}&path=open). This document provides an overview of the NRA process and is a compilation of most solicitations within NASA's Science Mission Directorate.

* Read the
  [Cycle 6 K2 Research Announcement](https://nspires.nasaprs.com/external/solicitations/summary!init.do?solId={7DC22936-4C6A-44FC-74A3-F0C9248DC9DD}&path=open). New
  amendments to the NRA are publicized at NSPIRES. Check this page
  regularly. 

* [Submit a Phase-2 proposal to NSPIRES](http://nspires.nasaprs.com/external/)
      by <font color='red'>23:59 EDT April 19, 2018</font>. 

*  The generic content of the proposal is described in Sec 2.3 of the
    <a
    href="http://www.hq.nasa.gov/office/procurement/nraguidebook/proposer2017.pdf">2017
    NRA Proposers Guide</a>. Page
    limits and proposal content within the NRA Guide are amended
    within the
    [K2 GO Cycle 6 NRA](https://nspires.nasaprs.com/external/solicitations/summary!init.do?solId={7DC22936-4C6A-44FC-74A3-F0C9248DC9DD}&path=open)
    and are summarized in the table below.   The
    right-hand column provides page limits for the package elements. Caveats to the page limits are provided as footnotes. *The page limits on this website override the NRA-generic limits within the handbook.*
    The Scientific/Technical/Management section of the
    Phase-2 proposal, which consists of text, tables (excluding the
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
      <th>Required Content for Phase-2 Proposals</th>
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
<sup>&Dagger;</sup>Investigations that have broadly similar goals and team members to selected Cycle 1, Cycle 2, or Cycle 3 proposals may use up to an additional 0.5 pages to describe progress they have made to delivering value-added community resources, but the Scientific/Technical/Management
	section still must not exceed 15 pages.

In summary, proposers should:

  * Understand the scope of the
        Guest Observer program. Science papers exploiting data from the Kepler and K2 mission can be found [here](publications.html).
  * Familiarize yourself with the [technical documentation](data-products.html#documentation) for the mission.
  * Develop and justify a science concept for observations
          within Campaigns specific to the current GO Cycle <a href="fields.html"></a>.
   * Identify appropriate targets for the proposed observations using the
        <a href="http://archive.stsci.edu/k2/epic/search.php">K2 Target Search</a> page as the primary (but not exclusive) source list. This search page provides for the construction of short or long target lists based upon e.g. celestial cone searches, magnitude and color.
   * Include a separate
     [Target Table](k2-proposing-targets.html#target-table) for each campaign
     as an integral component of the proposal and as a separate
     submission to the Guest Observer Office at **keplergo@mail.arc.nasa.gov**. 
   * For Phase-2 proposals only, provide the administrative elements of the proposal
          including a proposer biographical information, and a
          statement of current and pending financial support.
   * **For Phase-2 proposals only, large proposals that anticipate delivery of a data product/products
  to one of the NASA archives (e.g., MAST or the NASA Exoplanet
  Database) for curation must also include a letter of acknowledgement from
  the relevant archive.**
   * **Although a detailed budget is not requested in either Phase-1 or
  Phase-2 proposals, the Phase-2 proposal should include either a
  statement of work or a table summarizing the work effort.  If the
  statement of work is included in the Scientific/Technical/Management
  section it will count against the page limit for that section, but a
  table can be included as a separate section that will not count
  against the Scientific/Technical/Management section page limit .**  The
  statement of work should clearly identify any and all members of the proposing team
  who would receive funding under the proposed investigation. The
  funding amounts will be determined formulaically based on target
  allocation.
  * **Special instructions for non-US PIs**<br/>
During the submission process for Phase-2 proposals via NSPIRES, non-US PI-led proposals will need to be
affiliated to a submitting organization. Do this by clicking on the
"Account Mgmt" tab at the top of the NSPIRES page and follow the
instructions. All non-US proposals should use the "Kepler Guest
Observer Office" as your affiliation within NSPIRES. This is simply a
fudge, albeit a required fudge, so that non-US PIs spend no more
effort than this over the institutional endorsements that are
mandatory for US investigators. When completing the proposal, there are a few obscure boxes on the standard form that need your attention. The organization name is "Kepler Guest Observer Office", doing business as the "Kepler Guest Observer Office". The DUNS number is "999999954" and the cage code is "ZZZ54". These details will make sense to you when you see the Phase-2 proposal form. 


### Director's Discretionary Time

A small part of the pixel budget may be allocated by the project
as Director's Discretionary Targets (DDT),
which is intended to facilitate observations that address
scientific topics missed in the proposal review process.
More information and deadlines are available
from the [DDT program page](k2-ddt.html).

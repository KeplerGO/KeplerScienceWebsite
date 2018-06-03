Title: Call for K2 GO Cycle 7 proposals for Campaign 20
Date: 2099-06-01 17:00
Author: Geert Barentsen

The solicitation for K2 Guest Observer Cycle 7 proposals for Campaign 20 
has been [released and made available via NSPIRES](https://nspires.nasaprs.com/external/solicitations/summary!init.do?solId=%7b8A2B07C0-F3D9-677F-0C28-F0E8406FC3CD%7d&path=open).

Campaign 20 will revisit the Taurus-Auriga star-forming region in the
forward-facing mode, enabling simultaneous observations from the ground.
The field contains a large number of very young stars (<10 Myr)
and the Campaign will approximately double the number of young stars previously observed by Kepler.
These new observations will vastly improve the estimation of planet occurence rates at the youngest ages, and also enable young star variability studies over a longer baseline by re-observed stars previously observed in Campaigns 4 (2015) and 13 (2017).


## Target and funding selection process

Similar to the selection process executed for K2 GO Cycle 6,
the solicitation presents a two-phase process:

1. An optional **Phase-1** proposal will enable targets to be
selected for Campaign 20. Phase-1 proposals, including target tables
and a scientific rationale, are requested by **July 19, 2018**
and must be submitted via email to keplergo@mail.arc.nasa.gov.
The scientific rationale must not exceed 2 pages for small programs
(less than 1000 targets) and 4 pages for large programs
(1000 targets or more).

2. If the spacecraft health and fuel allow,
then **Phase-2** proposals for **funding** will be due **January 17, 2019**
via NSPIRES (see Section 7.1.2 of [the solicitation](https://nspires.nasaprs.com/external/viewrepositorydocument/cmdocumentid=610960/solicitationId=%7B8A2B07C0-F3D9-677F-0C28-F0E8406FC3CD%7D/viewSolicitationDocument=1/D.7%20K2%20Cycle%207%20Final%20Text%20Amend%2014%20final.pdf)).
Phase-2 proposals are limited to use observations for targets which have
been selected as part of Phase-1, the selection results of which will
be published in September 2018.
Phase-2 proposals are eligible to receive funding awards
between $30K and $150K, depending on the number of targets used.

Information about the proposal process, including the scope,
evaluation criteria, availability of funds, eligibility,
target selection tools, submission process, and frequently asked questions, is detailed on the [proposal preparation page](/k2-proposing-targets.html).


### K2fov update required

All investigators *must* update their version of the
<a href="software.html#k2fov">K2fov target selection tool</a>
to version 7.0, released on 16 June 2017,
to take the final field positions into account. 

K2fov can be updated from the command line using pip:

    pip install K2fov --upgrade

The version number of your K2fov installation may be verified
using the following command:

    python -c "import K2fov; print(K2fov.__version__)"

This should return "7.0.0" or higher. If the number is lower,
or if you see an error message, then your installation of K2fov is outdated.


### Questions?

Questions regarding this call should be sent to <a href="keplergo@mail.arc.nasa.gov">keplergo@mail.arc.nasa.gov</a>.

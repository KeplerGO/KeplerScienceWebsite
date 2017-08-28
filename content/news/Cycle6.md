Title: Call for K2 GO Cycle 6 proposals for Campaigns 17, 18, and 19
Date: 2017-08-28 07:20
Author: Geert Barentsen

The call for K2 Guest Observer Cycle 6 proposals for Campaigns 17, 18, and 19 
has been [released and made available at NSPIRES](https://nspires.nasaprs.com/external/solicitations/summary!init.do?solId={7DC22936-4C6A-44FC-74A3-F0C9248DC9DD}&path=open).

### New two-phase process

Because spacecraft fuel is expected to run out during one of these Campaigns,
the Cycle 6 call will use a new two-phase submission and
target selection process:

1. An optional **Phase-1** proposal, for all three campaigns (17-19) combined, will enable **targets** to be selected ahead of the observing campaigns.
Phase-1 proposals, including target lists and a scientific rationale (both submitted via email to keplergo@mail.arc.nasa.gov)
are requested by **October 12, 2017**.
The scientific rationale must not exceed 2 pages for small programs
(less than 1000 targets) and 4 pages for large programs
(1000 targets or more).

2. If the spacecraft health and fuel allow,
then **Phase-2 proposals for funding** will be due **April 19, 2018** (via NSPIRES).
Phase-2 proposals are limited to use observations for targets which have
been selected as part of Phase-1, the selection results of which will
be published in February 2018.
Phase-2 proposals are eligible to receive funding awards
between $30K and $150K, depending on the number of targets used.

This revised process allows the allocation of funding to be postponed until after the successful start of Campaign 17 is confirmed in April 2018.

Both Phase-1 and Phase-2 proposals will be peer-reviewed and ranked by professional volunteers.
The ranking of Phase-1 proposals will only inform the target selection, while
the ranking of Phase-2 proposals will only inform the allocation of funding. Submission of the Phase-1 proposals does not obligate proposers to submit a Phase-2 proposal. (In fact Phase-2 proposals will normally only be of interest to US-based investigators that are eligible to receive funding.)

Information about the proposal process, including the scope,
evaluation criteria, availability of funds, eligibility,
target selection tools, submission process, and frequently asked questions, is detailed on the [proposal preparation page](/k2-proposing-targets.html).


### K2fov update required

The [final field positions for Campaigns 17-19
have recently been set](fields-selected-for-k2-campaigns-17-18-and-19.html)
based on community input.
All investigators *must* update their version of the
<a href="software.html#k2fov">K2fov target selection tool</a>
to version 7.0, released on 16 June 2017,
to take the final field positions into account. 

K2fov can be updated from the command line using pip:

    pip install K2fov --upgrade --no-deps

The version number of your K2fov installation may be verified
using the following command:

    python -c "import K2fov; print(K2fov.__version__)"

This should return "7.0.0" or higher. If the number is lower,
or if you see an error message, then your installation of K2fov is outdated.


### Questions?

Questions regarding this call should be sent to <a href="keplergo@mail.arc.nasa.gov">keplergo@mail.arc.nasa.gov</a>.

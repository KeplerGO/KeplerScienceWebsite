Title: K2 Cycle 4: Target selection tools
Date: 2016-01-02 12:00
Author: Geert Barentsen

Proposals for targets to be observed by K2 in Campaigns 11, 12, and 13
are currently being solicited as part of [K2 Guest Observer Cycle 4](call-for-k2-go-cycle-4-proposals-for-campaigns-11-12-and-13.html).
Step 1 submissions for these proposals are due on **February 5, 2016**.

Proposals must be accompanied by a [target table](http://keplerscience.arc.nasa.gov/k2-proposing-targets.html#target-table) which details the objects
to be observed.
To enable the community to select and propose the most interesting targets,
the following resources are available:

* The Ecliptic Plane Input Catalog (**EPIC**) has been updated to include targets for Campaigns 11-13. The catalogs can be [queried online](https://archive.stsci.edu/k2/epic/search.php) or [downloaded in text format](https://archive.stsci.edu/missions/k2/catalogs/) from MAST.
* The **[K2fov](https://github.com/KeplerGO/K2fov)** package has been updated to include the details of fields 11-12-13, along with the preliminary positions of fields 14 through 17. Installing the package adds two executables to the command line, *K2onSilicon* and *K2findCampaigns*, which allow the visibility of targets to be checked during one or all campaigns.  If you have a previous version of K2fov installed, it is crucial that you upgrade to version 3.0 or higher ("pip install K2fov --upgrade").
* A new package called **[K2ephem](https://github.com/KeplerGO/K2ephem)** has been built on top of K2fov to allow the visibility of Solar System bodies, i.e. asteroids and comets, to be checked in a user-friendly way.
* The **sky footprints** of past and future campaigns have been made available
as [machine-readable text files](http://keplerscience.arc.nasa.gov/k2-fields.html#machine-readable-files). These files detail the coordinates of the CCD corners during each Campaign and allow users to create custom visualizations or run custom target selection algorithms.  The footprints are also available in the [MOC data format](k2-fields.html#moc-format) which can be opened and visualized using the [Aladin interactive sky atlas](http://aladin.u-strasbg.fr/).

Please [contact the Guest Observer Office](helpdesk.html) if you have questions.

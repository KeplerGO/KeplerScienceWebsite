Title: Lightkurve is now able to perform a cone search on Kepler/K2 data
Date: 2018-6-04 01:00
Author: Christina Hedges
Summary: The Kepler/K2 GO office lightkurve tool is always updating and evolving. We have now added the functionality to search the archive in a cone search. This will allow users to find nearest neighbors to the target in question.

The new lightkurve tool has a new feature to help users work with Kepler/K2 data. It is now possible to use the `from_archive` tool to perform a cone search around a given target. An example of how to perform the search is given below.

Users can now specify a radius and a number of targets in `from_archive` to return nearest neighbors to a target. This allows you to look for common systematics between neighboring targets, such as rolling band or due to solar system objects such as Mars. This can be used to vet data quality or remove spurious points.

A cone search with `from _archive` can be performed either with `KeplerTargetPixelFile.from_archive()` to find target pixel files, or with `KeplerLightCurveFile.from_archive()` to find light curve files.

<center>
<img src="images/conesearch.png" alt="Cone search with lightkurve" style="width: 100%; height: 100%">
</center>

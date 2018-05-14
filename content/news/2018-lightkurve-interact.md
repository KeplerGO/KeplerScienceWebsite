Title: New in lightkurve: inspecting pixel data using tpf.interact()
Date: 2018-05-11 01:00
Author: Michael Gully-Santiago

The new [lightkurve](http://lightkurve.keplerscience.org) Python package
for Kepler and K2 data analysis, which we [first announced in March](new-kepler-data-analysis-tools-and-tutorials-lightkurve-v10.html),
contains a new feature: `interact()`.

The tool strives to solve a common stumbling block in Kepler data analysis:
"*I see a blip in my lightcurve.  Is it real or instrumental?*"
`interact()` alleviates the guesswork by providing users with an easy-to-use
Python notebook widget to interactively inspect the pixel data
along a lightcurve.

A user can move a slider to rifle through cadences,
while seeing the postage stamp images update in real time.
A red vertical bar highlights the moment in the lightcurve.
Mousing-over individual lightcurve points flashes up a hover-over tool tip
with ancillary metadata about that particular cadence (e.g. quality flags).
The tool offers many avenues for customization,
including zooming, panning, and screen stretch. 

<a href="https://www.youtube.com/watch?v=89_sz-oG4VI">
    <img class="img-responsive" src="images/news/lightkurve-interact.gif" alt="Lightkurve tpf.interact() tool" style="margin:2em;">
</a>


The command `interact()` is a method of the `KeplerTargetPixelFile` class,
meaning that you can simply load in a target pixel file and append `.interact()` to the file as follows:

    :::python
    from lightkurve import KeplerTargetPixelFile
    tpf = KeplerTargetPixelFile.from_archive(target="Trappist-1")
    tpf.interact()

You will need to upgrade your installation of `lightkurve` to the latest version
(v1.0b5) for this to work. This can be done via the command line as follows:

```
$ pip install lightkurve --upgrade
```

We invite you to try out `interact()` today and [let us know if you have any problems by opening a GitHub Issue](https://github.com/KeplerGO/lightkurve/issues/new).

A [**YouTube screencast**](https://youtu.be/89_sz-oG4VI) and a [tutorial in the documentation](http://lightkurve.keplerscience.org/tutorials/1.05-interact-with-lightcurves-and-tpf.html) further illustrate the features of the tool.

<iframe width="800" height='450' src="https://www.youtube.com/embed/89_sz-oG4VI" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

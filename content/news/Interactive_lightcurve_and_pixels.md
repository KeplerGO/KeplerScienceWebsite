Title: Interactively visualize lightcurves and pixel postage stamps
Date: 2018-05-11 01:00
Author: Michael Gully-Santiago



A common stumbling block arises in K2 data analysis: *I see a blip in my K2 lightcurve.  Is it real or instrumental?*  We have recently developed a new software tool to aid in the interpretation of Kepler/K2 lightcurves and help alleviate the guesswork.  The tool visually distinguishes among sources of instrumental artifacts that have distinct appearances in the target pixel file postage stamp images.  

<a href="https://user-images.githubusercontent.com/860227/39730581-4c6b8c68-5217-11e8-92c1-10070faff8ac.gif">
<img class="img-responsive" src="https://user-images.githubusercontent.com/860227/39730581-4c6b8c68-5217-11e8-92c1-10070faff8ac.gif" alt="Interact tool""></a>


A user can move a slider to rifle through cadences, while seeing the postage stamp images update in real time.  A red vertical bar highlights the moment in the lightcurve.  Mousing-over individual lightcurve points flashes up a "hover-over tool tip" with ancillary metadata about that particular candence-- time and quality flags.  The tool offers many avenues for customization, including zooming, panning, and screen stretch.  [**This screencast**](https://youtu.be/89_sz-oG4VI) further illustrates the many features of the tool.  

We are calling the tool simply **interact**, and it appears as part of our [actively developed open source **lightkurve** package](https://github.com/KeplerGO/lightkurve).  The command `interact()` is a method of the `KeplerTargetPixelFile` class, meaning that you can simply read in a target pixel file (either locally or remotely) and simply append `.interact()` to the file; analogously `.plot()` yields a static image plot.

```python
import KeplerTargetPixelFile   
tpf = KeplerTargetPixelFile.from_archive(205913009)   

tpf.interact()   
```

The tool requires some new dependencies: [bokeh](https://bokeh.pydata.org/en/latest/) and [ipywidgets](https://ipywidgets.readthedocs.io/en/latest/).  You will likely need to upgrade your lightkurve installation:

```bash
pip install lightkurve --upgrade
```

We invite you to try out **interact** today, and [please let us know if you have any problems by opening a GitHub Issue.](https://github.com/KeplerGO/lightkurve/issues/new)

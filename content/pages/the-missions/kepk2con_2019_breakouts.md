Title: Kepler & K2 SciCon V Breakout Sessions
Save_as: scicon-2019/breakouts.html

[TOC]

Descriptions of all the Wednesday afternoon breakout sessions are included below.  Note that some strongly suggest downloading software and data before the session since wifi at the hotel will be somewhat limited.  You will be able to sign up for the breakout sessions at registration.

## Schedule

### Part I: March 6th, 13:30-15:00

<table class="table table-striped table-hover" style="max-width:55em;">
<tr>
<td style="width: 20em;"><a href="#soderblom">Opportunities and Limitations of the Cluster Data from Kepler/K2</a></td>
<td style="width: 12em;">David Soderblom (STScI) </td>
<td style="width: 9em;">Room: </td>
</tr>
<tr>
<td style="width: 20em;"><a href="#wang">Data Hack for RVxK2: Battling Stellar Jitter with Simultaneous K2 Photometry and RVs</a></td>
<td style="width: 12em;">Sharon Xuesong Wang (Carnegie DTM)</td>
<td style="width: 9em;">Room: </td>
</tr>
<tr>
<td style="width: 20em;"><a href="#hedges">The Lightkurve package for Kepler & TESS data analysis: tutorials and consulting breakout</a></td>
<td style="width: 12em;">Christina Hedges (NASA Ames)</td>
<td style="width: 9em;">Room: </td>
</tr>
<tr>
<td style="width: 20em;"><a href="#feigelson">Finding Planets in Kepler Lightcurves with R</a></td>
<td style="width: 12em;"> Eric Feigelson (Penn State University)</td>
<td style="width: 9em;">Room: </td>
</tr>
</table>


### Part II: March 6th, 15:30-17:00

<table class="table table-striped table-hover" style="max-width:55em;">
<tr>
<td style="width: 20em;"><a href="#cody">A Crowded Field Photometry Challenge</a></td>
<td style="width: 12em;">Ann Marie Cody (BAERI/NASA Ames)   </td>
<td style="width: 9em;">Room: </td>
</tr>
<tr>
<td style="width: 20em;"><a href="#gully">Modeling Correlated Noise with Gaussian Processes</a></td>
<td style="width: 12em;">Michael Gully-Santiago (NASA Ames) </td>
<td style="width: 9em;">Room: </td>
</tr>
<tr>
<td style="width: 20em;"><a href="#barclay">Community Data Products and Early Science from the TESS Mission</a></td>
<td style="width: 12em;">Tom Barclay (Univ. of Maryland) & Knicole Colon (NASA GSFC) </td>
<td style="width: 9em;">Room: </td>
</tr>
<tr>
<td style="width: 20em;"><a href="#rosenthal">RadVel: The Radial Velocity Fitting Toolkit</a></td>
<td style="width: 12em;">Lee Rosenthal (Caltech)</td>
<td style="width: 9em;">Room: </td>
</tr>
</table>


## Breakout summaries

<h3 id="soderblom">Opportunities and Limitations of the Cluster Data from Kepler/K2</h3>
<p> By providing significant samples of stars of the same age and composition, clusters are fundamental to astrophysics. Kepler and K2 have added greatly to our knowledge of stellar evolution, stellar behavior, and the nature of the clusters themselves. This breakout session will bring together researchers who have worked on clusters with Kepler/K2 or who want to understand better the opportunities that have not yet been explored. A panel will be assembled of people who have worked on Kepler/K2 for the Pleiades, Praesepe, Hyades, M67, star-forming regions, the 4 Kepler-field clusters and so on. Questions to be addressed include:</p>
<ul>
  <li>How well have Kepler/K2 observed the clusters in the fields observed? Aspects include completeness relative to known members; brightness and mass ranges; confusion issues.</li>
  <li>What systematics has Kepler/K2 imposed? For example, the visit durations for K2 were ~80 days, making the detection of rotation periods of 30-40 days problematic. Artifacts in the data make detection of transients difficult.</li>
  <li>What ancillary data are there to add in? Gaia is the obvious example, but there are many other high-quality surveys, as well as targeted projects.</li>
  <li>What do we know about clusters due to Kepler/K2? (5) What gaps still need to be filled to more fully exploit Kepler/K2 cluster data? Does TESS help?</li>
</ul>
<p>Some of the science areas directly relevant to this session include: rotation, activity, asteroseismology, and stellar evolution.</p>
<p><b>Attendee needs:</b> none</p>
<h3 id="wang">Data Hack for RVxK2: Battling Stellar Jitter with Simultaneous K2 Photometry and RVs</h3>
<p>Stellar jitter is the current bottleneck for achieving < 1 m/s radial velocity (RV) precision, and the RVxK2 project (rvxk2.com) addresses this issue with simultaneous RV and photometry with the best cadence and precision available today, provided by a suite of ground-based RV instrument and Kepler. Several members ( > 4) of the RVxK2 team will attend this conference, and we will use the breakout session to work together on RVxK2 papers. In addition, we invite anyone at the conference who's interested in RVxK2 to join us and work on our data (data can be made available to new members upon signing the RVxK2 collaborative agreement and code of conduct). For an overview of the RV data we have collected, please visit rvxk2.com.</p>
<p><b>Attendee needs:</b> laptop but not strictly required</p>
<h3 id="hedges">The Lightkurve package for Kepler & TESS data analysis: tutorials and consulting breakout</h3>
<p>Lightkurve is a community-developed, open-source Python package which offers a user-friendly and accessible way to analyze data from NASA’s Kepler, K2, and TESS missions. The package is supported by a rich syllabus of tutorials which aim to lower the barrier for students, astronomers, and citizen scientists alike to analyze data from NASA’s exoplanet space telescopes (cf.
  <a href= https://docs.lightkurve.org) target="_blank">https://docs.lightkurve.org</a>. This breakout session will start with an introductory tutorial (25 min) which demonstrates the most important features. We will then split the breakout into small groups to focus on particular use-cases, including: (i) custom aperture photometry, (ii) systematics removal, (iii) rolling band identification and removal, and (iv) periodogram and asteroseismology extraction. A developer or expert user will be assigned to each group to help new users get started, provide expert advice, and troubleshoot problems.</p>
<p><b>Attendee needs:</b> laptop with lightkurve installed; attendees can also work through the tutorials before the conference to gain familiarity</p>
<h3 id="feigelson">Finding Planets in Kepler Lightcurves with R</h3>
<p>R is the premier statistical software environment with millions of users and ~100,000 functions covering all of modern statistics. It is particularly strong for the analysis of evenly-spaced time series (missing data permitted). In this hands-on tutorial, we guide you through several steps of the AutoRegressive Planet Search methodology: display of lightcurves, differencing to reduce nonstationarity, ARIMA & ARFIMA modeling of short- & long-memory stochastic processes, and the new Transit Comb Filter to search for transit-like periodicities (Caceres et al. 2019). A variety of time series diagnostics are applied such as: interquartile range to measure noise, autocorrelation function to measure autocorrelation, Durbin-Watson and Ljung-Box tests for autocorrelation, Anderson-Darling test for normality, and the Adjusted Dickey-Fuller test for stationarity. Several graphical presentations are illustrated. Other analysis approaches using R are outlined: Fourier & Lomb-Scargle spectral analysis, wavelet analysis, nonparametric smoothing & interpolation, change point analysis, nonlinear modeling, and time series clustering. Resources for further study of time series analysis with R are provided.</p>
<p>This 1.5 hour hands-on tutorial will introduce participants to:
<ol>
  <li>
    the basics of times series analysis for any light curves with evenly-spaced cadences, missing data permitted;
  <li>
    the outline of the AutoRegressive Planet Search research effort at Penn State and its application to ~150,000 4-year Kepler light curves.
</ol>
<p><b>Attendee needs:</b> Prior to the session, the participant should:
<ol>
  <li> 
    install R on their laptop from <a href=https://www.r-project.org/ target="_blank">https://www.r-project.org/</a>.  This should be quick and simple for MacOS, Linus, and Windows operating systems;
  <li>
    download the contents of this directory: <a href=https://drive.google.com/drive/folders/1-T_dhKVuoktPhZd8i-hpfIZ-5imuGeFW target="_blank">https://drive.google.com/drive/folders/1-T_dhKVuoktPhZd8i-hpfIZ-5imuGeFW</a> which contains 4 files:
      <ul>
        <li>
          <b>R TSA tutorial KepSciConfV.ipynb</b>:  A Jupyter notebook with embedded R scripts
        <li>
          <b>R TSA tutorial KepSciConfV.r</b>:  An ASCII R script with the same information as the Jupyter notebook.  It can be cut-and-pasted into an interactive R console (double-click on the R icon, or type "R" into a terminal). 
        <li>
          <b>KID_001724719_lc.lst</b> and <b>KID_010024701_lc.lst</b>:  Single-column ASCII table giving PDCflux values for these two Kepler ID stars, with 'NA' (Not Available') used for cadences in gaps.
    </ul>
  <li> 
    install Jupyter notebooks, including the R kernel, from the Python anaconda system.  Check that the R kernel is working. This step is optional, as the session can be conducted from an interactive R console.  
    </ol>
<h3 id="cody">A Crowded Field Photometry Challenge</h3>
<p>Kepler is known for its exoplanet discoveries and exquisite variable time series of many different types of stars. Hundreds of thousands of light curves are available from the mission’s pipeline as well as from community teams. Much of the data analysis to date has focused on moderately bright, isolated stars. Precise light curves remain to be extracted from fainter, more crowded targets that exist in star clusters, as well as the galactic bulge. Precision photometry for these objects is challenging, but achievable. To enable breakthrough progress of crowded field photometry, we are organizing a challenge in which participants will be provided in advance with a set of images from K2’s Campaign 9 fields. The goal will be for several teams to produce precision time series photometry on a small set of prespecified variable targets, using methods of their choosing. The breakout session will start with an introductory overview of the problem and potential science (20 mins). Next, a summary will be presented of the participating teams’ results, followed by a group discussion on the merits of the different techniques. To secure the success of the breakout, we will be providing the community with tutorial and data challenge materials ahead of the meeting.</p>
<p><b>Attendee needs:</b> </p>
<h3 id="gully">Modeling Correlated Noise with Gaussian Processes</h3>
<p>Data analysis with Kepler and K2 can be broadly summarized as the quest to distill astrophysical or exoplanetary information from noisy, biased time series data. So far, heuristic methods have been successful in rapidly delivering discoveries in many high or modest signal-to-noise ratio applications. Advanced statistical techniques matter most in the lowest signal-to-noise ratio regimes-- the marginal detections. These margins represent scientific frontiers of understanding: the existence of Earth 2.0, the spin-down behavior of solar-age stars, pulsation amplitudes in faint white dwarfs, the weak extra light from the first moments of a supernova explosion. In all of these low signal-to-noise ratio scenarios, understanding and quantifying noise shares equal footing as understanding the astrophysics of interest. In this clinic, we will offer instructor-led tutorials and hands-on practice for modeling correlated noise, which can arise from either instrumental artifacts (e.g. rolling band) or astrophysical phenomena (e.g. starspot modulation). We will emphasize applications of likelihood-based inference with sampling or optimization. We will show how to get started with several common Python packages for scalable Gaussian Process regression: scipy, George, and celerite. Finally, we will mention new GPU-based frameworks for scaling Gaussian Processes such as GPyTorch.</p>
<p><b>Attendee needs:</b> </p>
<h3 id="barclay">Community Data Products and Early Science from the TESS Mission</h3>
<p>Since beginning science operations in July 2018, TESS is poised to provide a wealth of data on a wide variety of astrophysical objects, ranging from solar system bodies to exoplanets to stars to galaxies. We will provide an overview and update on data products and toolkits available for use by the broader community to enable TESS data analysis. These products and toolkits are supported by both active members of the community and the TESS Guest Investigator Program Office. We will also highlight early science results produced by the community, based on the first few months of TESS data.</p>
<p><b>Attendee needs:</b> none </p>
<h3 id="rosenthal">RadVel: The Radial Velocity Fitting Toolkit</h3>
<p>This tutorial will demonstrate the use of the RadVel Python package to characterize Keplerian orbits of transit-detected planetary systems with radial velocity (RV) data. RadVel can model multi-planet, multi-instrument datasets, while incorporating constraints such as transit ephemerides and secondary eclipse times. It includes several built-in Gaussian process kernels for the treatment of stellar activity, and employs MCMC and Bayesian modeling techniques to precisely determine the posterior distributions of planetary properties. Demonstrations will include how to use RadVel in conjunction with RV, Kepler, and K2 data, to better characterize the masses and orbits of transiting planets. An associated software package, rvsearch, will also be introduced.  Rvsearch is currently under development and can be used for blind RV planet detection in conjunction with RadVel. Rvsearch combines the Bayesian methods and Keplerian fitting tools of RadVel with a periodogram-based algorithm to search for planets in RV datasets, iteratively accepting potential planetary signals until they fail to surpass an empirically calculated threshold for goodness-of-fit. To learn more about RadVel, visit radvel.readthedocs.io.</p>
<p><b>Attendee needs:</b> laptop</p>
<h3 id="contact">Contact</h3>
<p>If you have questions regarding the conference, please send an email to <a href="mailto:keplerscicon@ipac.caltech.edu">keplerscicon@ipac.caltech.edu</a>.</p>

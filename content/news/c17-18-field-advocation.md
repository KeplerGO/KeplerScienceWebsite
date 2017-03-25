Title: Request for input on the Campaign 17 and 18 field placement
Date: 2017-03-25 11:00
Author: Knicole Colon & Geert Barentsen

The fields for K2 Campaigns 17 and beyond have not yet been set.
We strive to optimize these future fields based on potential science.
We are now soliciting feedback from the community on the
placement of fields 17 and 18.

Example options which satisfy K2's pointing constraints are shown below.
When submitting your input, please keep in mind
that we can only shift the field along the ecliptic between these options,
not up or down.

**We ask that all requests for field placements be received by
April 10 and be [submitted via this Google Form](https://docs.google.com/forms/d/e/1FAIpQLSfJ9hfrCBbRKsbHF-0cMO-orQMaijXnC_5pHfezp29Q81wFPg/viewform?usp=sf_link).**
We anticipate announcing the final field positions in early May.


## Campaign 17: Example forward-facing options

Campaign 17 is designated to have a forward-facing field
to enable simultaneous observations from the Earth.
Possible field options are outlined in the table below.

Note that all options have a start date of 3 March 2018,
i.e. 5 days after the end of Campaign 16.
The first option is very short in duration as a result; 
Campaign 16 would have to be cut short by a month to enable
the the C17-C10 overlap option to run for >70 days.

<div class="panel panel-primary" style="max-width:40em;">
  <div class="panel-heading">
    <h3 class="panel-title"> Campaign 17: Example options</h3>
  </div>
  <div class="panel-body">

<table class="table table-striped table-hover">
  <thead>
    <tr>
    <th>Option</th>
    <th>Possible dates</th>
	<th>Max. duration</th>
	<th>Overlap region</th>
    </tr>
  </thead>  
  <tdata>
    <tr>
     <td>1</td>
     <td>Mar 3 - Apr 18,&nbsp;2018</td>
     <td>46 days</td>
     <td>14 modules of C10</td>
    </tr>
    <tr>
     <td>2</td>
     <td>Mar 3 - May 8,&nbsp;2018</td>
     <td>66 days</td>
     <td>14 modules of C6</td>
    </tr>
    <tr>
     <td>3</td>
     <td>Mar 3 - May 23,&nbsp;2018</td>
     <td>81 days</td>
     <td>1 module of C6</td>
    </tr>
</tdata>
</table>

  </div>
  </div>

<a href="images/k2/k2-c17-options.gif">
<img src="images/k2/k2-c17-options.gif" style="max-width:40em;">
</a>


## Campaign 18: Example forward-facing options

The field for Campaign 18 largely depends on the location of the Campaign
17 field as well as whether or not Campaign 18 will be posited as a
forward-facing or backward-facing field. If we allow Campaign 18 to begin 5 days after the end of
each of the three options for Campaign 17 noted above, then we obtain
the following options listed below in the case of a forward-facing field:

<div class="panel panel-primary" style="max-width:40em;">
  <div class="panel-heading">
    <h3 class="panel-title"> Campaign 18: Example options (forward-facing) </h3>
  </div>
  <div class="panel-body">

<table class="table table-striped table-hover">
  <thead>
    <tr>
    <th>Option</th>
    <th>Possible dates</th>
    <th>Max. duration</th>
    <th>Overlap region</th>
    </tr>
  </thead>  
  <tdata>
    <tr>
     <td>1</td>
     <td>Apr 23 - Jul 18, 2018</td>
     <td>86 days</td>
     <td>17 modules of C9*</td>
    </tr>
    <tr>
     <td>2</td>
     <td>May 13 - Aug 09, 2018</td>
     <td>88 days</td>
     <td>9 modules of C7</td>
    </tr>
    <tr>
     <td>3</td>
     <td>May 28 - Aug 25, 2018</td>
     <td>88 days</td>
     <td>none</td>
    </tr>
</tdata>
</table>


* C9 was the microlensing experiment where pixels were primarily collected
  around the Galactic bulge. Therefore, the distribution of targets
  across modules was not uniform in that campaign.

  </div>
  </div>

<a href="images/k2/k2-c18-forward-options.gif">
<img src="images/k2/k2-c18-forward-options.gif" style="max-width:40em;">
</a>


## Campaign 18: Example backward-facing options

And these are the C18 options for the backward-facing geometry,
in which case Earth is kept out of the field but
simultaneous observations from the ground would be challenging:

<div class="panel panel-primary" style="max-width:40em;">
  <div class="panel-heading">
    <h3 class="panel-title"> Campaign 18: Example options (backward-facing) </h3>
  </div>
  <div class="panel-body">


<table class="table table-striped table-hover">
  <thead>
    <tr>
    <th>Option</th>
    <th>Possible dates</th>
    <th>Max. duration</th>
    <th>Overlap region</th>
    </tr>
  </thead>  
  <tdata>
    <tr>
     <td>1</td>
     <td>Apr 23 - Jul 18, 2018</td>
     <td>86 days</td>
     <td>1/2 module of C5</td>
    </tr>
    <tr>
     <td>2</td>
     <td>May 13 - Aug 09, 2018</td>
     <td>88 days</td>
     <td>14 modules of C5 and C16</td>
    </tr>
    <tr>
     <td>3</td>
     <td>May 28 - Aug 25, 2018</td>
     <td>88 days</td>
     <td>2 modules of C14</td>
    </tr>
</tdata>
</table>

  </div>
  </div>

<a href="images/k2/k2-c18-backward-options.gif">
<img src="images/k2/k2-c18-backward-options.gif" style="max-width:40em;">
</a>


## K2fov

The above field options have been configured in the [GitHub version of K2fov](https://github.com/KeplerGO/K2fov) using mock field numbers:

* 171, 172, 173 (C17);
* 181, 182, 183 (C18 forward-facing);
* 184, 185, 186 (C18 backward-facing).

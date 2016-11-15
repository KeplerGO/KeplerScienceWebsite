Title: Small changes to Campaigns 13, 14, and 15
Date: 2016-11-14 21:00
Author: Geert Barentsen

K2 users are alerted to a small but necessary adjustment
to the fields of Campaigns 13, 14, and 15.

To better compensate for the radiation pressure exerted by one of the
spacecraft's low-gain antennae, these fields have been rotated by 0.365°.
This change minimizes the roll drift rate and
hence optimizes fuel usage and photometric precision.

The change affects less than 1% of the sky area covered and is unlikely
to affect most Cycle 5 proposals.
All users are nevertheless encouraged to update the 
<a href="software.html#k2fov">K2fov</a> target selection tool
to version 6.2, released on 14 Nov 2016, which includes the change.

K2fov can be updated from the command line using pip:

    pip install K2fov --upgrade

The version number of your K2fov installation may be verified
using the following command:

    python -c "import K2fov; print(K2fov.__version__)"

This must return "6.2.0" or higher. If the number is lower, or if you see an error message, then your installation of K2fov is outdated and must be upgraded. 

Campaign 16 does not require a change due to the use of a different,
forward-facing spacecraft configuration.

Please [contact the Guest Observer Office](helpdesk.html) if you have questions.

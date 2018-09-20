#!/bin/bash

# Save the KARs
for i in {1..1359}  # Loop through all KAR numbers
do
  mkdir KAR-$i  # Make a directory for the current KAR number
  mkdir ./KAR-$i/Attachments  # Make a sub-directory to save attachments
  /home/jeff/Downloads/wkhtmltox/bin/wkhtmltopdf --cookie JSESSIONID D06D5D55527AA4BDA431F390A9CC6306 --enable-internal-links https://lasp.colorado.edu/kepler-ats/si/jira.issueviews:issue-html/KAR-$i/KAR-$i.html ./KAR-$i/KAR-$i.pdf  # Use wkhtmltopdf to save the html to a pdf. Note you have to specify your own JESSIONID from your currently logged-in session
  pdftotext ./KAR-$i/KAR-$i.pdf ./KAR-$i/KAR-$i.txt  # Make a txt version of the PDF as well.
  wget --load-cookies cookie.txt --reject robots,robots.txt,robots.txt.tmp,KAR-$i.html,KAR-$i.doc,KAR-$i.xml,logout,ViewProfile.jspa,savedfilters.jsp,recenthistory.jsp -A txt,ppt,pptx,pdf,doc,docx,xls,xlsx,xml,out -r -l 0 -nd -P ./KAR-$i/Attachments/ https://lasp.colorado.edu/kepler-ats/browse/KAR-$i  # Get wget to get attachments. Note you have to specify all possible attachement types
done

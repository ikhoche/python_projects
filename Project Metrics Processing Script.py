#!/usr/bin/env python
# coding: utf-8

# This script creates a table from using data from JIRA and calculates how many User Stories and Bugs were Created and Resolved per day per project.



import pandas as pd

df = pd.read_csv(r'C:\Users\ishan.khoche\Documents\Project Metrics\Projec Metrics Dashboard Data_23Oct- Copy.csv') #Load File to be analyzed


fixedversion = df.loc[df['Fixed Version'] == 'ZS Web 2.0Mallorca'] # Enter Fixed Version

bug = fixedversion.loc[fixedversion['Issue Type'] == 'Bug'] 


bug['created date'] = pd.to_datetime(bug['Created']).dt.date 
bug['Created/Resolved'] = 'Created' #add column to mark that these are created bugs
createdBugs = bug.groupby(['created date', 'Fixed Version','Created/Resolved']).size() #Count of Created/Day

bug['resolved date'] = pd.to_datetime(bug['Resolved']).dt.date 
bug['Created/Resolved'] = 'Resolved' #add column to mark that these are resolved bugs
resolvedBugs = bug.groupby(['resolved date', 'Fixed Version','Created/Resolved']).size() #Count of Resolved/Day

#Change name of file below:
createdBugs.append(resolvedBugs).to_csv('ZS Web 2.0Mallorca_bugs.csv') # Create file with bugs created/resolved counts



userstories = fixedversion.loc[fixedversion['Issue Type'] == 'Story'] 


userstories['created date'] = pd.to_datetime(userstories['Created']).dt.date 
userstories['Created/Resolved'] = 'Created' #add column to mark that these are created bugs
createduserstories = userstories.groupby(['created date', 'Fixed Version','Created/Resolved']).size() #Count of Created/Day

userstories['resolved date'] = pd.to_datetime(userstories['Resolved']).dt.date 
userstories['Created/Resolved'] = 'Resolved' #add column to mark that these are resolved bugs
resolveduserstories = userstories.groupby(['resolved date', 'Fixed Version','Created/Resolved']).size() #Count of Resolved/Day

#Change name of file below:
createduserstories.append(resolveduserstories).to_csv('ZS Web 2.0Mallorca_us.csv') # Create file with bugs created/resolved counts













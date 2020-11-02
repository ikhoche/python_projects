#!/usr/bin/env python
# coding: utf-8

# Python Script Structure
# 
# 1. Read the JIRA files 
# 2. Iterate over the JIRA files and clean them up
#     - Affects Version, Fix Version, Component have several columns - get data from them and put into one single column
# 3. Combine the JIRA files into one file and export




def cleanAffectsversion (affects):

    if len(affects) == 1:
        pass
    elif len(affects) == 2:
        nf.loc[nf["Affects Version/s"].isnull(),'Affects Version/s'] = nf["Affects Version/s.1"]
    elif len(affects) ==3:
        nf.loc[nf["Affects Version/s"].isnull(),'Affects Version/s'] = nf["Affects Version/s.1"]
        nf.loc[nf["Affects Version/s"].isnull(),'Affects Version/s'] = nf["Affects Version/s.2"]
    elif len(affects) == 4:
        nf.loc[nf["Affects Version/s"].isnull(),'Affects Version/s'] = nf["Affects Version/s.1"]
        nf.loc[nf["Affects Version/s"].isnull(),'Affects Version/s'] = nf["Affects Version/s.2"]
        nf.loc[nf["Affects Version/s"].isnull(),'Affects Version/s'] = nf["Affects Version/s.3"]
    else:
        print("There are more than 4 Affects Versions")





def cleanFixversion (fix):

    if len(fix) == 1:
        pass
    elif len(fix) == 2:
        nf.loc[nf["Fix Version/s"].isnull(),'Fix Version/s'] = nf["Fix Version/s.1"]
    elif len(fix) ==3:
        nf.loc[nf["Fix Version/s"].isnull(),'Fix Version/s'] = nf["Fix Version/s.1"]
        nf.loc[nf["Fix Version/s"].isnull(),'Fix Version/s'] = nf["Fix Version/s.2"]
    elif len(fix) == 4:
        nf.loc[nf["Fix Version/s"].isnull(),'Fix Version/s'] = nf["Fix Version/s.1"]
        nf.loc[nf["Fix Version/s"].isnull(),'Fix Version/s'] = nf["Fix Version/s.2"]
        nf.loc[nf["Fix Version/s"].isnull(),'Fix Version/s'] = nf["Fix Version/s.3"]
    else:
        print("There are more than 4 Fix Versions")





def addComponentnumber():
    cols = []
    count = 0
    for column in nf.columns:
        if column == 'Component/s':
            cols.append(f'Component/s.{count}')
            count+=1
            continue
        cols.append(column)
    nf.columns = cols





def cleanComponentversion (component):

    if len(component) == 1:
        pass
    elif len(component) == 2:
        nf.loc[nf["Component/s.0"].isnull(),'Component/s.0'] = nf["Component/s.1"]
    elif len(component) ==3:
        nf.loc[nf["Component/s.0"].isnull(),'Component/s.0'] = nf["Component/s.1"]
        nf.loc[nf["Component/s.0"].isnull(),'Component/s.0'] = nf["Component/s.2"]
    elif len(component) == 4:
        nf.loc[nf["Component/s.0"].isnull(),'Component/s.0'] = nf["Component/s.1"]
        nf.loc[nf["Component/s.0"].isnull(),'Component/s.0'] = nf["Component/s.2"]
        nf.loc[nf["Component/s.0"].isnull(),'Component/s.0'] = nf["Component/s.3"]
    elif len(component) == 5:
        nf.loc[nf["Component/s.0"].isnull(),'Component/s.0'] = nf["Component/s.1"]
        nf.loc[nf["Component/s.0"].isnull(),'Component/s.0'] = nf["Component/s.2"]
        nf.loc[nf["Component/s.0"].isnull(),'Component/s.0'] = nf["Component/s.3"]
        nf.loc[nf["Component/s.0"].isnull(),'Component/s.0'] = nf["Component/s.4"]
    elif len(component) == 6:
        nf.loc[nf["Component/s.0"].isnull(),'Component/s.0'] = nf["Component/s.1"]
        nf.loc[nf["Component/s.0"].isnull(),'Component/s.0'] = nf["Component/s.2"]
        nf.loc[nf["Component/s.0"].isnull(),'Component/s.0'] = nf["Component/s.3"]
        nf.loc[nf["Component/s.0"].isnull(),'Component/s.0'] = nf["Component/s.4"]
        nf.loc[nf["Component/s.0"].isnull(),'Component/s.0'] = nf["Component/s.5"]
    elif len(component) == 7:
        nf.loc[nf["Component/s.0"].isnull(),'Component/s.0'] = nf["Component/s.1"]
        nf.loc[nf["Component/s.0"].isnull(),'Component/s.0'] = nf["Component/s.2"]
        nf.loc[nf["Component/s.0"].isnull(),'Component/s.0'] = nf["Component/s.3"]
        nf.loc[nf["Component/s.0"].isnull(),'Component/s.0'] = nf["Component/s.4"]
        nf.loc[nf["Component/s.0"].isnull(),'Component/s.0'] = nf["Component/s.5"]
        nf.loc[nf["Component/s.0"].isnull(),'Component/s.0'] = nf["Component/s.6"]
    





import pandas as pd
import os

folder = 'C:/Users/ishan.khoche/Documents/Project Metrics/JIRA' #Enter path of downloaded JIRA CSV files.

filelist = [file for file in os.listdir(folder) if file.startswith('Jira')]
newdataframe = pd.DataFrame()

for file in filelist:
    file = os.path.join(folder,file)
    nf = pd.read_csv(file, dtype = str)
    addComponentnumber()

    affects = [col for col in nf if col.startswith('Affects')]
    fix = [col for col in nf if col.startswith('Fix')]
    component = [col for col in nf if col.startswith('Component')]
    
    cleanAffectsversion (affects)
    cleanFixversion (fix)
    cleanComponentversion (component)
    
    nf = nf[['Summary','Issue key','Issue id','Issue Type','Status','Project key','Project name','Project type','Project lead','Project description','Project url','Priority','Resolution','Assignee','Reporter','Creator','Created','Updated','Last Viewed','Resolved','Affects Version/s','Fix Version/s','Component/s.0']]
    newdataframe = newdataframe.append(nf)
    newdataframe.to_csv('check.csv')






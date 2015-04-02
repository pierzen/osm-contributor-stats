#!/usr/bin/python
#-*- coding: utf-8 -*-

"""
#========================================================================="
# https://github.com/pierzen/osm-contributor-stats/blob/master/Script-to-run-OsmContributorStats-Module-Extract-Objects-Calculate-Statistics.py
# Pierre Beland, 10-2013
# Example running version 0.1 of OsmContributorStats
# OSM Contributors Histor Statistics, for a specific bbox zone and date range
# STATISTIQUES Historiques, contributeurs OSM pour une zone bbox et paire de dates
#========================================================================="
#========================================================================="
"""
import os
# specify the directory where both OsmApi.py and OsmContributorStats.py are stored
os.chdir('c:\OsmContributorStats\\')
import OsmApi
# Instantiation classe OsmApi
osmApi = OsmApi.OsmApi(debug=False)
import OsmContributorStats
# Instantiation classe OsmContributorStats
ContributorStats = OsmContributorStats.OsmContributorStats(rep='c:\OsmContributorStats\\',lang="en",debug=False)
dir(ContributorStats)

#===============================================================================
# users :  array of contributor ID's or Name by team - if no users, all users in the bbox will be selected
users=[None]*2
users[0] = [""]
users[1] = [""]

"""
Example with nicknames
users=[None]*2
users[0] = ["abc","def","gjol"]
users[1] = ["zyx","avb Yul"]
"""



# Example - Lome, Togo
# The examples below defines a Bbox covering Lome, Togo. The period covered si from 2013-06-26 to 2013-06-27.
  
# Step 1 - Extract History Data  - Extraire les données historiques
ContributorStats.API6_Collect_Changesets(team_from=0,team_to=0,from_date="2013-06-26",
    to_date="2013-06-27",
    min_lon=1.151,max_lon=1.2888,min_lat=6.1288,max_lat=6.2375,
    prefix="osmef-togo-",users=users)

# Step 2 - Statistics from data stored locally	- Statistiques produite à partir des données enregistrées localement
ContributorStats.Changesets_Contributor_Statistics(team_from=0,team_to=0,from_date="2013-06-26",
    to_date="2013-06-27",
    min_lon=1.151,max_lon=1.2888,min_lat=6.1288,max_lat=6.2375,
    prefix="osmef-togo-",users=users)


print "\n-----------------------------------------------------"

ContributorStats.__del__()
del OsmContributorStats

import sys
sys.exit('\n=== Travail complété ===')

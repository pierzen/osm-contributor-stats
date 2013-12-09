#!/usr/bin/python
#-*- coding: utf-8 -*-

"""
#========================================================================="
# OsmContributorStats
# Pierre Beland, 10-2013

# OSM Contribitors Histor Statistics, for a specific bbox zone and date range
# STATISTIQUES Historiques, contributeurs OSM pour une zone bbox et paire de dates
#========================================================================="
#========================================================================="
"""
import os
os.chdir('c:\OsmContributorStats\\')
import OsmApi
osmApi = OsmApi.OsmApi(debug=False)
import OsmContributorStats
# Instantiation classe OsmContributorStats
ContributorStats = OsmContributorStats.OsmContributorStats(rep='c:\OsmContributorStats\\',lang="fr",debug=False)
dir(ContributorStats)

#===============================================================================
# users :  array of contributor ID's or Name by team - if no users, all users in the bbox will be selected
users=[None]*2
users[0] = [""]
users[1] = [""]



# Example - Lome, Togo

# Step 1 - Extract History Data  - Extraire les données historiques
ContributorStats.API6_Collect_Changesets(team_from=0,team_to=0,from_date="2013-06-26",
    to_date="2013-08-14",
    min_lon=1.151,max_lon=1.2888,min_lat=6.1288,max_lat=6.2375,
    prefix="osmef-togo-",users=users)

# Step 2 - Statistics from data stored locally	- Statistiques produite à partir des données enregistrées localement
ContributorStats.Changesets_Contributor_Statistics(team_from=0,team_to=0,from_date="2013-06-26",
    to_date="2013-06-28",
    min_lon=1.151,max_lon=1.2888,min_lat=6.1288,max_lat=6.2375,
    prefix="osmef-togo-",users=users)


print "\n-----------------------------------------------------"

ContributorStats.__del__()
del OsmContributorStats

import sys
sys.exit('\n=== Travail complété ===')

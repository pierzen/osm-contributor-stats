# Osm Contributor Statistics


## How to use this class

You need to import and instantiate OsmApi
You also need to import and instantiate OsmContributorStats

## Functions

The class  	OsmContributorStats.py contains two main functions :

1. API6_Collect_Changesets extracts history data and store locally in a specified directory.

2. Changesets_Contributor_Statistics  produce the statistics from the local directory file.

Array users is used to store the list of contributor osm nicknames by team


Parameters
 team_from and team_to : team to use in the users array
 from_date to to_date : pair of dates for extraction
  min_lon, max_lon, min_lat, max_lat : these four parameters define the bbox zone to extract
  prefix : prefix to use to name history files
  
The file names will be composed using the prefix and the from and to dates.

## Example

See Example-using-OsmContributorStats.py

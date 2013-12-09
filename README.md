# Osm Contributor Statistics


## How to use this Python class to produce contributor statistics

The Script-to-run-OsmContributorStats-Module-Extract-Objects-Calculate-Statistics.py Python script contains instructions to extract objects and calculate statistics.

## Dependancies 
You need to import and instantiate both OsmApi and OsmContributorStats. You should also indicate the directory where the Modules are stored and where the files produced will be stored.

OsmApi is from Etienne Chové. See http://wiki.openstreetmap.org/wiki/PythonOsmApi
OsmContributorStats class module from Pierre Béland, is en enhancement of a first script written by Sebastien Pierrel. From our experience in Haiti (60 trainees in six teams) and with the various French african projects we supported in the summer 2013, various flexibilities were added.
* Differentiate Extract and Statistic functions. The Extract step may take some time. We should also be careful to avoid adding to much burden on the OSM API server. For these reasons, we thought that it would be better to differentiate Extract and Statistic phases.
* Add the possibility to have a various teams. This is useful to follow various classes or groups in the same bbox area.
* when the user array is empty, Changesets for all contributors are extracted.
* For the Statistic phase, it is possible to have a different User's array and then select a portion of the users. Also, Changesets that cover a bbox area 10 times larger then the bbox specified are excluded from the statistics. These are in general bots or Massive edits often covering continents.


## Functions

Two functions are called to extract objects and produce statistics. These are part of OsmContributorStats.py class.

1. API6_Collect_Changesets extracts history data and store locally in a specified directory. List of changesets and List of objects will be stored as Python objects.

2. Changesets_Contributor_Statistics  produce the statistics from the local directory file.

Array users is used to store the list of contributor osm nicknames by team
See Examples in the script


Parameters
 team_from and team_to : team to use in the users array
 from_date to to_date : pair of dates for extraction
  min_lon, max_lon, min_lat, max_lat : these four parameters define the bbox zone to extract
  prefix : prefix to use to name history files
 users : indicate the array of osm contributors to query. If no
The file names will be composed using the prefix and the from and to dates.

## Example

See Example-using-OsmContributorStats.py

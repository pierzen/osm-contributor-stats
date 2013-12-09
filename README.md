# Osm Contributor Statistics


## How to use this Python class to produce contributor statistics

The ***Script-to-Extract-Objects-and-Calculate-Statistics-from-OsmContributorStats-Module.py*** Python script is an example of instructions to extract objects and calculate statistics using the OsmContributorStats Class Module.

## Instructions

You need to import and instantiate both OsmApi and OsmContributorStats. You should also indicate the directory where the Modules are stored and where the files produced will be stored.

OsmContributorStats class module from Pierre Béland, is en enhancement of a first script written by Sebastien Pierrel. From our experience in 2013 in Haiti (60 trainees in six teams) and with various French african projects we supported, various flexibilities were added to the script.
* Differentiate History extraction and Statistic steps as two funcions. The History extraction step may take some time. We should also be careful to avoid adding too much burden on the OSM API server. The possibility to first identify all contributors and later group them for analysis is an other aspect to take into account. For these reasons, we thought that it would be better to differentiate Extract and Statistic phases.
* Add the possibility to compile statistics by teams. This is useful to follow various classes or groups in the same bbox area.
* when the user array is empty, Changesets for all contributors are extracted.
* For the Statistic phase, it is possible to have a different User's array and then select a portion of the users. 
* Possibility to exclude some changesets from either Bots or Massive edits often covering continents. The solution we retained is to exclude Changesets that cover a bbox area 10 times larger then the bbox specified in the Function.


## Functions

Two functions are called to extract objects and produce statistics. These are part of OsmContributorStats.py class.

1. API6_Collect_Changesets extracts history data and store locally in a specified directory. List of changesets and List of objects will be stored as Python objects.

2. Changesets_Contributor_Statistics  produce the statistics from the local directory file.

Array users is used to store the list of contributor osm nicknames by team
See Examples in the script


Parameters
The parameters should be the same for both functions since the file names for read / write are composed using the prefix and the from and to dates.

* team_from and team_to : team to use in the users array
* from_date to to_date : pair of dates for extraction
* min_lon, max_lon, min_lat, max_lat : these four parameters define the bbox zone to extract
* prefix : prefix to use to name history files
* users : indicate the array of osm contributors to query. If no


## Dependancies

* OsmApi.py Author Etienne Chové, source http://wiki.openstreetmap.org/wiki/PythonOsmApi
* OsmContributorStats.py class module Author Pierre Béland Source https://github.com/pierzen/osm-contributor-stats/OsmContributorStats.py. The original script from Sebastien Pierrel (Seb's stats script v0.4 ) produced statistics for objects created. The present scripts produce also statistics for modified and deleted objects. The breakdown of POI's and ways is also provided.


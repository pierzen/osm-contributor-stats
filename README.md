# Osm Contributor Statistics

Version 02.1 August 18 2014

## How to use this Python class to produce contributor statistics

The ***Script-to-Extract-Objects-and-Calculate-Statistics-from-OsmContributorStats-Module.py*** Python script is an example of instructions to extract objects and calculate statistics using the OsmContributorStats Class Module.

CSV Output files show the statistics
[Prefix] of files contains the prefix provided by the user + the date range ex. ebola-2014-08-18-2014-08-18 )
1. Users statistics : [prefix].csv
2. Teams statistics : [prefix]-team.csv
3. Changesets statistics : [prefix]-changeset.csv

File format 1 and two are obsolete and might be deleted in other versions of the script.
File format 3 (by CSV) can be analysed in a spreadsheet and produce statistics with the various variables such as day, user, team. Statistics by date show the progression of an activity. Statistics by user let's see how many contributors up to date.

## Instructions

You need to import and instantiate both OsmApi and OsmContributorStats. You should also indicate the directory where the Modules are stored and where the files produced will be stored.

OsmContributorStats class module from Pierre Béland, is en enhancement of a first script written by Sebastien Pierrel. From our experience in 2013 in Haiti (60 trainees in six teams) and with various French african projects we supported, various flexibilities were added to the script.
* Differentiate History extraction and Statistic steps as two funcions. The History extraction step may take some time. We should also be careful to avoid adding too much burden on the OSM API server. The possibility to first identify all contributors and later group them for analysis is an other aspect to take into account. For these reasons, we thought that it would be better to differentiate Extract and Statistic phases.
* Add the possibility to compile statistics by teams. This is useful to follow various classes or groups in the same bbox area.
* when the user array is empty, Changesets for all contributors are extracted.
* For the Statistic phase, it is possible to have a different User's array and then select a portion of the users. 
* Possibility to exclude some changesets from either Bots or Massive edits often covering continents. The solution we retained is to exclude Changesets that cover a bbox area 10 times larger then the bbox specified in the Function.

## Statistics

Statistics for each contributor and teams are compiled and saved in csv files.

| Statistic type | variable names |
| ------------------------- | ---------------------------------------- |
| number of changesets | changeset |
| objects created | object_c, node_c, way_c, relation_c |
| objects modified | object_m, node_m, way_m, relation_m |
| objects deleted | object_d, node_d, way_d, relation_d |
| POI nodes | poi_total_nodes, node_amenity, node_shop, node_office, node_power, node_place, node_man_made, node_history, node_tourism, node_leisure |
| ways| way_highway, way_waterway, way_building, way_landuse, way_man_made |



## Dependancies

* OsmApi.py Author Etienne Chové, source http://wiki.openstreetmap.org/wiki/PythonOsmApi
* OsmContributorStats.py class module Author Pierre Béland Source https://github.com/pierzen/osm-contributor-stats/OsmContributorStats.py. The original script from Sebastien Pierrel (Seb's stats script v0.4 ) produced statistics for objects created. The present scripts produce also statistics for modified and deleted objects. The breakdown of POI's and ways is also provided.


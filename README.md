## Overview

This repo contains my logbook for all igc recorded flights.  It is intended to be consumed programatically.  The best way to view this is on my website at https://www.scottyob.com/flying

Currently, all non-igc recorded flights live @ https://docs.google.com/spreadsheets/d/1-rd2b-_l5IgavBxVe50O817AjAbI5qAVc0leU2bxUM8/edit?usp=sharing


### Installing and creating the launches database
1. First setup the environment
```
$ python3 -m venv /tmp/launches
$ . /tmp/launches/bin/activate
$ pip install yq
```

2.  Download the launches database from [Paraglidingspots](https://www.paraglidingspots.com/) 

3.  Generate the launches JSON file
```
unzip -p  ~/Downloads/launches.kmz doc.kml | xq | sed 's/kml\://' | jq '[.. | .Placemark? // empty] | flatten | map((.Point | .coordinates | split(",")?) as $c | {name, longitude: ($c[0] | tonumber), latitude: ($c[1] | tonumber) })' > launches.json
```

### Create a list of sites
A lot of launches in this database will look something like 
> TO (SW) Mission...
> TO (WNW-SW) Ed Levin_2

The interesting part of this would be "Mission" or "Ed Levin", so the icea is storing sites.json is to store a list of strings containing site names that are used as a substring match.


## Overview

This repo contains my logbook for all igc recorded flights.  It is intended to be consumed programatically.  The best way to view this is on my website at https://www.scottyob.com/flying

Currently, all non-igc recorded flights live @ https://docs.google.com/spreadsheets/d/1-rd2b-_l5IgavBxVe50O817AjAbI5qAVc0leU2bxUM8/edit?usp=sharing


### Installing and creating the launches database
1. First setup the environment
```
$ python3 -m venv /tmp/launches
$ . /tmp/launches/bin/activate
$ pip install -r requirements.txt
```

2.  Download the launches database from [Paraglidingspots](https://www.paraglidingspots.com/) and unzip it
```
unzip ~/Downloads/launches.kmz
```

3.  Generate the launches JSON file
```
 python gen-launches.py doc.kml > launches.json
```

### Create a list of sites
A lot of launches in this database will look something like 
> TO (SW) Mission...
> TO (WNW-SW) Ed Levin_2

The interesting part of this would be "Mission" or "Ed Levin", so the goal is storing sites.json is to store a list of strings containing site names that are used as a substring match.

See launches.json for the modifications used in the web frontends.
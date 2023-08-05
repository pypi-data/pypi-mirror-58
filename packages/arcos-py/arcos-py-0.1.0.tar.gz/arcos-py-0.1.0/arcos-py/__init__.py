"""Arcos-Py 

Arcos-Py

    >>> from reader import feed
    >>> feed.get_titles()
    ['Logging in Python', 'The Best Python Books', ...]

See https://github.com/realpython/reader/ for more information
"""
import importlib_resources as _resources

#try:
#    from configparser import ConfigParser as _ConfigParser
#except ImportError:  # Python 2
#    from ConfigParser import ConfigParser as _ConfigParser

	
import numpy as np
import pandas as pd
import geopandas as gpd
from shapely.geometry import Polygon, Point
import requests
from pandas.io.json import json_normalize


	
# Version of realpython-reader package
__version__ = "0.1.0"

# Read URL of feed from config file

us_abbr_list = [
    "AK",
    "AL","AR","AZ", "CA","CO","CT","DE","FL","GA",
    "HI",
    "IA","ID","IL","IN","KS","KY","LA","MA","MD","ME","MI","MN","MO","MS","MT","NC","ND",
    "NE","NH","NJ","NM","NV","NY","OH","OK","OR","PA","RI","SC","SD","TN","TX","UT","VA",
    "VT","WA","WI","WV","WY"]

us_48_abbr_list = [
    #"AK",
    "AL","AR","AZ", "CA","CO","CT","DE","FL","GA",
    #"HI",
    "IA","ID","IL","IN","KS","KY","LA","MA","MD","ME","MI","MN","MO","MS","MT","NC","ND",
    "NE","NH","NJ","NM","NV","NY","OH","OK","OR","PA","RI","SC","SD","TN","TX","UT","VA",
    "VT","WA","WI","WV","WY"]

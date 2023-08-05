README
======

[![Build Status](https://travis-ci.com/robotpt/fitbit-reader.svg?branch=master)](https://travis-ci.com/robotpt/fitbit-reader)
[![Downloads](https://pepy.tech/badge/fitbit-reader)](https://pepy.tech/project/fitbit-reader)

A way to access Fitbit daily and intraday steps data.
See `example.py` for usage.

This project uses a different notion of active steps than Fitbit.
From experience, if you are walking for nine minutes, stop for one minute 
(say, at a traffic intersection before you are given the 'walk' prompt), and walk for
another nine minutes, Fitbit will not register your walk as 'active'.
This reader allows you to specify a step frequency that is considered active during a duration (the finest is minutes)
and a number of time periods that can be inactive before ending the activity.

All data returns are in Pandas dataframes.


Setup
-----

### Option 1: Clone the repository

> Best if you want to modify or view the code - note that you can do the following inside of a virtual environment

    git clone https://github.com/robotpt/fitbit-reader
    
An easy way to setup the repository with its dependencies and with your Python path
is to use `pip`.  

    pip install -e fitbit-reader

Tests can be run with the following commands.
    
    cd fitbit-reader
    python3 -m unittest

### Option 2: Use Pip

> Best if you just want to use it

    python3 -m pip install fitbit_reader


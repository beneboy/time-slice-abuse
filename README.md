# time-slice-abuse

An intuitive way of instantiating time or timedelta objects using familiar syntax.

*or*

Create Python datetime.time/datetime.timedelta objects by abusing slices.


Usage
---------

    >>> import timeslice
    >>> t = timeslice.TimeSlice()[19:42:23]
    >>> t
    datetime.time(19, 42, 23)
    >>> d = timeslice.TimeDeltaSlice()[54:89:99]
    >>> d
    datetime.timedelta(2, 27039)
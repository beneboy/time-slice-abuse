from datetime import time, timedelta


class _TimeSliceBase(object):
    @staticmethod
    def time_units_from_slice(val, is_time=True):
        if not isinstance(val, slice):
            raise TypeError("Arg to __getitem__ must be a slice")
        seconds = val.step or 0
        minutes = val.stop
        hours = val.start

        invalid_range = False

        if minutes is None or hours is None:
            invalid_range = True

        if not invalid_range and is_time and (minutes >= 60 or hours >= 24 or seconds >= 60):
            invalid_range = True

        if not invalid_range and (minutes < 0 or hours < 0 or seconds < 0):
            invalid_range = True

        if invalid_range:
            raise ValueError("Please slice only in range [0-23]:[0-59]:[0-59]?.")

        return hours, minutes, seconds


class TimeSlice(_TimeSliceBase):
    def __getitem__(self, val):
        hours, minutes, seconds = self.time_units_from_slice(val)
        return time(hours, minutes, seconds)


class TimeDeltaSlice(_TimeSliceBase):
    def __getitem__(self, val):
        hours, minutes, seconds = self.time_units_from_slice(val, False)
        return timedelta(hours=hours, minutes=minutes, seconds=seconds)

# -*- coding: utf-8 -*-

""" Module summary description.

More detailed description.
"""


class Time:

    def __init__(self, hour, minute, second):
        self.hour = hour + (minute + second//60)//60
        self.minute = (minute + second//60) % 60
        self.second = second % 60

    def __add__(self, other):
        """ Override "+" operation

        :param other:
        :return:
        """
        return Time(self.hour + other.hour, self.minute + other.minute, self.second + other.second)

    def __repr__(self):
        return "%02d:%02d:%02d" % (self.hour, self.minute, self.second)


time1 = Time(12, 53, 23)
time2 = Time(7, 23, 45)
print("time1: %s" % time1)
print("time2: %s" % time2)
print("Sum: %s" % time1 + time2)

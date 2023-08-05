# -*- coding: utf-8 -*-
# author: ethosa
import math


class Point:
    def __init__(self, *args):
        if len(args) == 1:
            if isinstance(args[0], Point):
                self.points = args[0].points
            elif isinstance(args[0], list) or isinstance(args[0], tuple):
                self.points = args[0]
            else:
                self.points = [0, 0]
        elif len(args) == 0:
            self.points = [0, 0]
        else:
            self.points = [i for i in args]

    def euclideanDistance(self, *args):
        r = Point(*args)
        sum_sqr = sum([(self.points[i] - r.points[i])**2 for i in range(len(self.points))])
        distance = math.sqrt(sum_sqr)
        return distance

    def middlePoint(self, pnt):
        pnt1 = Point(self)
        for p in range(len(pnt1.points)):
            pnt1.points[p] = (self.points[p]+pnt.points[p])//2
        return pnt1

    def offset(self, points):
        for i in range(len(points)):
            self.points[i] += points[i]

    def __eq__(self, other): return self.points == other.points

    def __str__(self):
        return "<Point (%s)>" % ", ".join("%s" % i for i in self.points)

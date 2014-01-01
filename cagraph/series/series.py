#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.

# Copyright (C) 2011 Yaacov Zamir <kobi.zamir@gmail.com>
# Author: Yaacov Zamir (2011) <kobi.zamir@gmail.com>

class CaGraphSeries():
    def __init__(self, main_graph, xaxis, yaxis):
        ''' set line default parameters '''
        
        self.graph = main_graph
        self.xaxis = main_graph.axiss[xaxis]
        self.yaxis = main_graph.axiss[yaxis]
        
        self.data = []
    
    def get_xrange(self):
        ''' get max and min values '''
        
        if len(self.data) < 1:
            return
            
        xvals = map(lambda x: x[0], self.data)
        return min(xvals), max(xvals)
        
    def get_yrange(self):
        ''' get max and min values '''
        
        if len(self.data) < 1:
            return
            
        yvals = map(lambda x: x[1], self.data)
        return min(yvals), max(yvals)
    
    def find_point(self, x):
        ''' find data point by x (used in pointers) '''
        
        # index = 0 is usualy the x-axis
        return self.find_point_by_index(value = x, index = 0)
        
    def find_point_by_index(self, value, index):
        ''' find data point by value and index (used in pointers) '''
        
        data = self.data
        distance_data = [((d[index] - value) ** 2, d) for d in data]
        
        min_distance = distance_data[0][0]
        near_point = distance_data[0][1]
        
        for distance_point in distance_data:
            if min_distance > distance_point[0]:
                min_distance = distance_point[0]
                near_point = distance_point[1]
        
        return near_point


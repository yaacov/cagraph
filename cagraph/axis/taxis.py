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

import time
import math

from xaxis import CaGraphXAxis
        
class CaGraphTAxis(CaGraphXAxis):
    def __init__(self, main_graph):
        ''' set y axis default parameters '''
        CaGraphXAxis.__init__(self, main_graph)
        
        self.axis_style.label_format = "%y-%m-%d %H:%M:%S"
        self.axis_style.label_rotate = math.pi * 0.10
        
    def draw_labels(self, level, y_px, d, direction):
        ''' draw axis labels '''
        context = self.graph.context
        axis_style = self.axis_style
        
        # set direction
        if direction == 'top':
            d = -d
        
        # draw tics
        for x in self.tics_iterator(level):
            x_px = self.data_to_px(x)
            time_string  = time.strftime(axis_style.label_format, 
              time.gmtime(x))
              
            context.move_to(x_px, y_px + d)
            context.rotate(axis_style.label_rotate)
            context.show_text(time_string)
            context.rotate(-axis_style.label_rotate)
            

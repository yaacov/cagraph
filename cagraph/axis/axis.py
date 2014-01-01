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

class CaAxisStyle:
    ''' axis stye class '''
    
    def __init__(self):
        ''' set default style '''
        self.title_color = (0, 0, 1)
        
        self.line_color = (0, 0, 0, 1)
        self.line_width = 1.0
        self.num_of_tics = 10.0
        self.num_of_sub_tics = 4.0
        
        self.label_color = (1, 0, 0)
        self.label_format = '%.2f'
        self.label_rotate = 0.0
        
        self.side = 'left'
        self.draw_labels = True
        self.draw_tics = True
        
class CaGraphAxis:
    def __init__(self, main_graph):
        ''' set axis default parameters '''
        self.max = 58.0
        self.min = -11.0
        
        self.axis_style = CaAxisStyle()
        self.graph = main_graph
    
    def tics_iterator(self, level):
        ''' calculate axis tics position '''
        num_of_tics = self.axis_style.num_of_tics
        
        # make steps a clean number
        t_step = (self.max - self.min) / num_of_tics
        t_step_exp = map(int, ("%1.e" % t_step).split('e'))
        t_step = t_step_exp[0] * 10 ** t_step_exp[1]
        
        # set sub tics
        if level == 1:
            t_step /= self.axis_style.num_of_sub_tics
            
        # align min with zero
        n = int(self.min / t_step)
        if n >= 0:
            n += 1
        t = t_step * n
        
        # get tics
        while t <= self.max:
            yield t
            t += t_step
    

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

import pygtk
pygtk.require('2.0')

import gtk, gtk.glade

class CaGridStyle:
    ''' grid stye class '''
    
    def __init__(self):
        ''' set default style '''
        self.line_color = (0.3, 0.7, 0.3, 0.5)
        self.line_width = 0.5
        
        self.zero_line_color = (0, 0.5, 0, 1.0)
        self.zero_line_width = 1.0
        
        self.grid_level = 0
        
class CaGraphGrid():
    def __init__(self, main_graph, xaxis, yaxis):
        ''' set grid default parameters '''
        self.style = CaGridStyle()
        
        self.graph = main_graph
        self.xaxis = main_graph.axiss[xaxis]
        self.yaxis = main_graph.axiss[yaxis]
        
    def draw(self):
        ''' draw grid '''
        level = self.style.grid_level
        context = self.graph.context
        style = self.graph.graph_style
        
        # draw grid lines
        context.set_source_rgba(*self.style.line_color)
        context.set_line_width(self.style.line_width)
        
        # draw xaxis grid lines
        direction = 'bottom'
        d1 = 0
        d2 = style.height - style.margin - style.margin
        y_px = style.margin
        
        self.xaxis.draw_tics(level, y_px, d1, d2, direction)
        
        # draw yaxis grid lines
        direction = 'right'
        d1 = 0
        d2 = style.width - style.margin - style.margin
        x_px = style.margin
        
        self.yaxis.draw_tics(level, x_px, d1, d2, direction)
        
        # draw zero lines
        context.set_source_rgba(*self.style.zero_line_color)
        context.set_line_width(self.style.zero_line_width)
        
        if self.yaxis.min < 0 and  self.yaxis.max > 0:
            y_px = self.yaxis.data_to_px(0)
            
            context.move_to(style.margin, y_px)
            context.line_to(style.width - style.margin, y_px)
            context.stroke()
            
        if self.xaxis.min < 0 and  self.xaxis.max > 0:
            x_px = self.xaxis.data_to_px(0)
            
            context.move_to(x_px, style.margin)
            context.line_to(x_px, style.height - style.margin)
            context.stroke()
            

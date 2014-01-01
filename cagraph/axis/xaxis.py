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

from axis import CaGraphAxis
        
class CaGraphXAxis(CaGraphAxis):
    def __init__(self, main_graph):
        ''' set x axis default parameters '''
        CaGraphAxis.__init__(self, main_graph)
        self.type = 'xaxis'
        
    def data_to_px(self, x):
        ''' calculate position in pixels from data '''
        style = self.graph.graph_style
        
        graph_width = style.width - style.margin - style.margin
        x_in_px = graph_width * (x - self.min) / (self.max - self.min)
        px = style.margin + x_in_px
        
        return px
    
    def px_to_data(self, x):
        ''' calculate position in data units from pixels '''
        style = self.graph.graph_style
        
        graph_width = style.width - style.margin - style.margin
        x_in_data = (self.max - self.min) * (x - style.margin) / graph_width
        data = x_in_data + self.min
        
        return data
        
    def draw_tics(self, level, y_px, d1, d2, direction):
        ''' draw axis tics '''
        context = self.graph.context
        axis_style = self.axis_style
        
        # set direction
        if direction == 'top':
            d1 = -d1
            d2 = -d2
        
        # draw tics
        for x in self.tics_iterator(level):
            x_px = self.data_to_px(x)
            
            context.move_to(x_px, y_px + d1)
            context.line_to(x_px, y_px + d2)
            context.stroke()
    
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
            
            context.move_to(x_px, y_px + d)
            context.rotate(axis_style.label_rotate)
            context.show_text(axis_style.label_format % x)
            context.rotate(-axis_style.label_rotate)
    
    def draw(self):
        ''' draw x axis '''
        context = self.graph.context
        style = self.graph.graph_style
        axis_style = self.axis_style
        
        # set axis y position
        y_px = style.height - style.margin
        if axis_style.side == 'top':
            y_px = style.margin
        
        # draw main axis
        context.set_line_width(axis_style.line_width)
        context.set_source_rgba(*axis_style.line_color)
        
        context.move_to(style.margin, y_px)
        context.line_to(style.width - style.margin, y_px)
        context.stroke()
        
        # draw tics
        if axis_style.draw_tics:
            context.set_source_rgba(*axis_style.line_color)
            
            # level-0 tics
            self.draw_tics(0, y_px, 4, -10, axis_style.side)
            
            # level-1 tics
            self.draw_tics(1, y_px, 0, -5, axis_style.side)
            
        # draw lables
        if axis_style.draw_labels:
            context.set_source_rgb(*axis_style.label_color)
            self.draw_labels(0, y_px, 21, axis_style.side)
        
        # draw title


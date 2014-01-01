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

from line import CaSeriesLineStyle, CaGraphSeriesLine

class CaSeriesAreaStyle(CaSeriesLineStyle):
    ''' line stye class '''
    
    def __init__(self):
        ''' set default style '''
        CaSeriesLineStyle.__init__(self)
        
        self.line_color = (1.0, 0.0, 0.0, 1.0)
        self.fill_color = (1.0, 0.0, 0.0, 0.3)
        self.line_width = 1.0
        self.point_type = 'o'
        
class CaGraphSeriesArea(CaGraphSeriesLine):
    def __init__(self, main_graph, xaxis, yaxis):
        ''' set line default parameters '''
        CaGraphSeriesLine.__init__(self, main_graph, xaxis, yaxis)
        
        self.style = CaSeriesAreaStyle()
        
    def draw_area(self):
        ''' draw area '''
        
        data = self.data
        
        if len(data) == 0:
            return
        
        context = self.graph.context
        style = self.graph.graph_style
        
        context.save()
        
        # set a clip region for the expose event
        context.rectangle(style.margin, style.margin,
            style.width - style.margin - style.margin, 
            style.height - style.margin - style.margin)
        context.clip()
        
        # move to first point
        x_px = self.xaxis.data_to_px(data[0][0])
        y_px = self.yaxis.data_to_px(0)
        context.move_to(x_px, y_px)
        
        # draw area lines
        for point in data:
            x_px = self.xaxis.data_to_px(point[0])
            y_px = self.yaxis.data_to_px(point[1])
            context.line_to(x_px, y_px)
            
        y_px = self.yaxis.data_to_px(0)
        context.line_to(x_px, y_px)
        
        # fill path
        context.close_path()
        context.set_source_rgba(*self.style.fill_color)
        context.fill()
        
        context.restore()
        
    def draw(self):
        ''' draw series '''
        
        self.draw_area()
        self.draw_line()
        self.draw_points()
        

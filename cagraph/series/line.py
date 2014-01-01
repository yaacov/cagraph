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

import math

from series import CaGraphSeries

class CaSeriesLineStyle:
    ''' line stye class '''
    
    def __init__(self):
        ''' set default style '''
        self.line_color = (0.0, 0.0, 1.0, 1.0)
        self.line_width = 1.0
        self.point_type = '+'
        self.point_radius = 3.0
        
class CaGraphSeriesLine(CaGraphSeries):
    def __init__(self, main_graph, xaxis, yaxis):
        ''' set line default parameters '''
        CaGraphSeries.__init__(self, main_graph, xaxis, yaxis)
        
        self.style = CaSeriesLineStyle()
        
    def draw_line(self):
        ''' draw line '''
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
        
        # draw lines
        context.set_source_rgba(*self.style.line_color)
        context.set_line_width(self.style.line_width)
        
        # move to first point
        x_px = self.xaxis.data_to_px(data[0][0])
        y_px = self.yaxis.data_to_px(data[0][1])
        context.move_to(x_px, y_px)
        
        # draw line
        for point in data:
            x_px = self.xaxis.data_to_px(point[0])
            y_px = self.yaxis.data_to_px(point[1])
            context.line_to(x_px, y_px)
            context.stroke()
            
            context.move_to(x_px, y_px)
            
        context.restore()
    
    def draw_point_o(self, x_px, y_px):
        ''' draw o style point '''
        context = self.graph.context
        radius = self.style.point_radius
        
        context.arc(x_px, y_px, radius, 0, 2 * math.pi)
        context.fill()
    
    def draw_point_x(self, x_px, y_px):
        ''' draw x style point '''
        context = self.graph.context
        radius = self.style.point_radius
        
        context.move_to(x_px - radius, y_px - radius)
        context.line_to(x_px + radius, y_px + radius)
        context.stroke()
        
        context.move_to(x_px - radius, y_px + radius)
        context.line_to(x_px + radius, y_px - radius)
        context.stroke()
    
    def draw_point_plus(self, x_px, y_px):
        ''' draw x style point '''
        context = self.graph.context
        radius = self.style.point_radius
        
        context.move_to(x_px - radius, y_px)
        context.line_to(x_px + radius, y_px)
        context.stroke()
        
        context.move_to(x_px, y_px + radius)
        context.line_to(x_px, y_px - radius)
        context.stroke()
        
    def draw_points(self):
        ''' draw points '''
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
        
        # draw lines
        context.set_source_rgba(*self.style.line_color)
        context.set_line_width(self.style.line_width)
        
        # draw line
        radius = self.style.point_radius
        for point in data:
            x_px = self.xaxis.data_to_px(point[0])
            y_px = self.yaxis.data_to_px(point[1])
            
            # draw points
            if self.style.point_type == 'o':
                self.draw_point_o(x_px, y_px)
                
            elif self.style.point_type == 'x':
                self.draw_point_x(x_px, y_px)
                
            elif self.style.point_type == '+':
                self.draw_point_plus(x_px, y_px)
        
        context.restore()
    
    def draw(self):
        ''' draw series '''
        
        self.draw_line()
        self.draw_points()
        

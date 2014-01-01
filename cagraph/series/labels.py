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

from series import CaGraphSeries

class CaSeriesLabelStyle:
    ''' labels stye class '''
    
    def __init__(self):
        ''' set default style '''
        self.label_color = (1.0, 0.0, 1.0, 1.0)
        self.label_rotate = 0
        self.label_font_size = 10
        self.label_padding = 10
        
class CaGraphSeriesLabels(CaGraphSeries):
    def __init__(self, main_graph, xaxis, yaxis):
        ''' set labels default parameters '''
        CaGraphSeries.__init__(self, main_graph, xaxis, yaxis)
        
        self.style = CaSeriesLabelStyle()
    
    def draw_labels(self):
        ''' draw labels '''
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
        context.set_source_rgba(*self.style.label_color)
        
        # draw line
        for point in data:
            x_px = self.xaxis.data_to_px(point[0]) + self.style.label_padding
            y_px = self.yaxis.data_to_px(point[1]) - self.style.label_padding
            text = point[2]
            
            self.graph.draw_text(x_px, y_px, text, 
                color = self.style.label_color, 
                size = self.style.label_font_size, 
                angle = self.style.label_rotate)
            
        context.restore()
    
    def draw(self):
        ''' draw series '''
        
        self.draw_labels()
        

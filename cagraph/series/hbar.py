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

from bar import CaGraphSeriesBar
        
class CaGraphSeriesHBar(CaGraphSeriesBar):
    def __init__(self, main_graph, xaxis, yaxis):
        ''' set bar default parameters '''
        CaGraphSeriesBar.__init__(self, main_graph, xaxis, yaxis)
        
    def draw_bar(self):
        ''' draw bars '''
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
        context.set_line_width(self.style.line_width)
        
        # draw bar
        height = self.style.bar_width
        for point in data:
            x_px = self.xaxis.data_to_px(point[0])
            y_px = self.yaxis.data_to_px(point[1])
            zero_px = self.xaxis.data_to_px(1)
            width = x_px - zero_px
            
            context.set_source_rgba(*self.style.line_color)
            context.rectangle(zero_px, y_px - height / 2.0, width, height)
            context.stroke()
            
            context.set_source_rgba(*self.style.fill_color)
            context.rectangle(zero_px, y_px - height / 2.0, width, height)
            context.fill()
            
        context.restore()


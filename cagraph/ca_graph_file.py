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

import cairo
import pango
import pangocairo

class CaGraphStyle:
    ''' graph style '''
    
    def __init__(self):
        ''' set default style '''
        self.margin = 60
        self.width = 600
        self.height = 600
        self.title_color = (1, 0, 0)
        self.background_color = (1, 1, 1)
        self.auto_range_padding = 0.1
        self.draw_pointer = False
        self.draw_pointer_y = False
        self.pointer_color = (1, 0, 0, 1)
        self.pointer_width = 1.0
        
class CaGraphFile():
    ''' cairo charting class '''
    
    def __init__(self):
        ''' init event handlers and default parameters '''
                
        # add styles
        self.graph_style = CaGraphStyle()
        
        # add axiss
        self.axiss = []
        
        # add grid
        self.grid = None
        
        # add seriess
        self.seriess = []
    
    def draw_to_file(self, filename, width = 600, height = 600):
        ''' draw widget window to png/svg file '''
        
        # get png/svg context
        if filename.endswith('.svg'):
            surface = cairo.SVGSurface (filename, width, height)
        else:
            surface = cairo.ImageSurface (cairo.FORMAT_ARGB32, width, height)
        
        self.context = cairo.Context (surface)
        self.graph_style.width = width
        self.graph_style.height = height
        
        # set a clip region for the expose event
        self.context.rectangle(0, 0, width, height)
        self.context.clip()
        
        self.draw_graph()
        
        if filename.endswith('.svg'):
            surface.finish()
        else:
            surface.write_to_png(filename)
    
    def auto_set_xrange(self, xaxis, include_zero = False):
        ''' auto set the axis range '''
        
        if len(self.seriess) < 1:
            return
        
        style = self.graph_style
        
        x_min, x_max = self.seriess[0].get_xrange()
        for series in self.seriess:
            series_min, series_max = series.get_xrange()
            x_min = min([series_min, x_min])
            x_max = max([series_max, x_max])
        
        if include_zero:
            x_min = min([0, x_min])
            x_max = max([0, x_max])
        
        x_range = x_max - x_min
        self.axiss[xaxis].min = x_min - abs(style.auto_range_padding * x_range)
        self.axiss[xaxis].max = x_max + abs(style.auto_range_padding * x_range)
    
    def auto_set_yrange(self, yaxis, include_zero = False):
        ''' auto set the axis range '''
        
        if len(self.seriess) < 1:
            return
        
        style = self.graph_style
        
        y_min, y_max = self.seriess[0].get_yrange()
        for series in self.seriess:
            series_min, series_max = series.get_yrange()
            y_min = min([series_min, y_min])
            y_max = max([series_max, y_max])
        
        if include_zero:
            y_min = min([0, y_min])
            y_max = max([0, y_max])
        
        y_range = y_max - y_min
        self.axiss[yaxis].min = y_min - abs(style.auto_range_padding * y_range)
        self.axiss[yaxis].max = y_max + abs(style.auto_range_padding * y_range)
    
    def auto_set_range(self, include_zero = False):
        ''' auto set the axis range '''
        
        axiss = self.axiss
        num_of_axiss = len(axiss)
        
        for i in range(num_of_axiss):
            if axiss[i].type == 'xaxis':
                self.auto_set_xrange(i, include_zero)
            else:
                self.auto_set_yrange(i, include_zero)
    
    def draw_text(self, x, y, text, color, 
            size = 10, family = "Sans", angle = 0):
        ''' draw text at x, y '''
        context = self.context
        
        context.save()
        
        # move to x, y
        context.translate(x, y)
        context.rotate(angle)
        
        # create pango context
        pangocairo_context = pangocairo.CairoContext(context)
        pangocairo_context.set_antialias(cairo.ANTIALIAS_SUBPIXEL)

        # set font
        layout = pangocairo_context.create_layout()
        fontname = "%s %d" % (family, size)
        font = pango.FontDescription(fontname)
        layout.set_font_description(font)
        
        # set color
        context.set_source_rgba(*color)
        
        # drow text
        layout.set_text(text)
        pangocairo_context.update_layout(layout)
        pangocairo_context.show_layout(layout)
        
        context.restore()
    
    def draw_graph(self):
        ''' draw widget window to context '''
        context = self.context
        style = self.graph_style
        
        # draw graph title
        
        # draw background
        width = style.width - style.margin - style.margin
        height = style.height - style.margin - style.margin
        
        context.set_source_rgb(*style.background_color)
        context.rectangle(style.margin, style.margin, width, height)
        context.fill()
        
        # draw grid
        if self.grid:
            self.grid.draw()
        
        # draw axiss
        for axis in self.axiss:
            axis.draw()
        
        # draw seriess
        for series in self.seriess:
            series.draw()
    
    def check_xy(self, x, y):
        ''' is x_px,y_px inside graph ? '''
        
        style = self.graph_style
        
        if x < style.margin:
            return False
        if x > (style.width - style.margin):
            return False
        if y < style.margin:
            return False
        if y > (style.height - style.margin):
            return False
        
        return True
        

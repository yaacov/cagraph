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
# Author: Nah, Chong Yeol (2011) <nahchongyeol@gmail.com>

from series import CaGraphSeries

class CaSeriesDNAStyle:
    ''' dna stye class '''
    
    def __init__(self):
        ''' set default style '''
        self.line_color = (0.0, 1.0, 0.0, 1.0)
        self.fill_color = (0.0, 1.0, 0.0, 0.3)
        self.bar_width = 20.0
        self.line_width = 1.0
        
class CaGraphSeriesDNA(CaGraphSeries):
    def __init__(self, main_graph, xaxis, yaxis):
        ''' set dna default parameters
            data form: list of size 3 tuples
                       (x_st, x_fi, y)
        '''
        CaGraphSeries.__init__(self, main_graph, xaxis, yaxis)
        
        self.style = CaSeriesDNAStyle()
    
    def get_xrange(self):
        ''' get max and min values '''

        if len(self.data) < 1:
            return

        xvals = map(lambda x: x[0], self.data)
        _xvals = map(lambda x: x[1], self.data)
        return min(xvals), max(_xvals)
    
    def get_yrange(self):
        ''' get max and min values '''

        if len(self.data) < 1:
            return

        yvals = map(lambda x: x[2], self.data)
        return min(yvals), max(yvals)
    
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
        for x_st, x_fi, y_st in data:
            x_st_px = self.xaxis.data_to_px(x_st)
            x_fi_px = self.xaxis.data_to_px(x_fi)
            y_st_px = self.yaxis.data_to_px(y_st)
            width = x_fi_px - x_st_px
            
            context.set_source_rgba(*self.style.line_color)
            context.rectangle(x_st_px, y_st_px - height / 2.0, width, height)
            context.stroke()
            
            context.set_source_rgba(*self.style.fill_color)
            context.rectangle(x_st_px, y_st_px - height / 2.0, width, height)
            context.fill()
            
        context.restore()
    
    def draw(self):
        ''' draw series '''
        
        self.draw_bar()
        

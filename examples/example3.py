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
import re

import math
import sys
sys.path.insert(0, '../')

from cagraph.ca_graph import CaGraph

from cagraph.axis.xaxis import CaGraphXAxis
from cagraph.axis.yaxis import CaGraphYAxis
from cagraph.axis.taxis import CaGraphTAxis

from cagraph.ca_graph_grid import CaGraphGrid

from cagraph.series.line import CaGraphSeriesLine
from cagraph.series.bar import CaGraphSeriesBar
from cagraph.series.area import CaGraphSeriesArea

class MainWindow:
    def __init__(self):
        # create widget tree ...
        xml = gtk.glade.XML('test.glade')

        # connect handlers
        xml.signal_autoconnect(self)

        # widgets
        self.main_window = xml.get_widget('main_window')
        self.hbox_graph = xml.get_widget('hbox_graph')
        
        # add graph
        self.graph = CaGraph()
        self.hbox_graph.pack_start(self.graph)
        
        # create and add axiss to graph
        xaxis = CaGraphXAxis(self.graph)
        yaxis = CaGraphYAxis(self.graph)
        self.graph.axiss.append(xaxis)
        self.graph.axiss.append(yaxis)
        
        # create and add top axis
        top_axis = CaGraphXAxis(self.graph)
        top_axis.axis_style.side = 'top'
        top_axis.axis_style.draw_labels = False
        self.graph.axiss.append(top_axis)
        
        # create and add right axis
        right_axis = CaGraphYAxis(self.graph)
        right_axis.axis_style.side = 'right'
        right_axis.axis_style.draw_labels = False
        self.graph.axiss.append(right_axis)
        
        # create and add series to graph
        series1 = CaGraphSeriesLine(self.graph, 0, 1)
        series2 = CaGraphSeriesArea(self.graph, 0, 1)
        series3 = CaGraphSeriesLine(self.graph, 0, 1)
        
        self.graph.seriess.append(series2)
        self.graph.seriess.append(series3)
        self.graph.seriess.append(series1)
        
        # set line style
        series1.style.line_color = (1.0, 0.0, 0.0, 1.0)
        series1.style.line_width = 2.0
        series1.style.point_type = ''
        
        series2.style.line_color = (0.0, 1.0, 0.0, 1.0)
        series2.style.fill_color = (0.0, 1.0, 0.0, 0.3)
        series2.style.line_width = 2.0
        series2.style.point_type = ''
        
        series3.style.line_color = (0.0, 0.6, 0.0, 1.0)
        series3.style.line_width = 0.0
        series3.style.point_type = 'o'
        
        # add data to seriess
        for i in range(-360, 720):
            alpha = math.pi * i / 180.0
            
            series1.data.append( (alpha, math.sin(alpha)) )
            series2.data.append( (alpha, math.cos(alpha)) )
        
        for i in range(-360, 720, 20):
            alpha = math.pi * i / 180.0
            
            series3.data.append( (alpha, math.cos(alpha)) )
            
        # automaticaly set axis ranges
        self.graph.auto_set_range()
        
        # add grid
        self.graph.grid = CaGraphGrid(self.graph, 0, 1)
        
        # show wigdet
        self.graph.show()
    
        # draw to file
        self.graph.draw_to_file('example3.svg', 700, 300)
        self.graph.draw_to_file('example3.png', 700, 300)
        
    # signal handlers
    def on_main_window_delete_event(self, widget, obj):
        "on_main_window_delete_event activated"
        gtk.main_quit()
        
# run main loop
def main():
    main_window = MainWindow()
    main_window.main_window.show()
    gtk.main()

if __name__ == "__main__":
    main()


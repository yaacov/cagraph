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

import sys
sys.path.insert(0, '../')

from cagraph.ca_graph import CaGraph

from cagraph.axis.xaxis import CaGraphXAxis
from cagraph.axis.yaxis import CaGraphYAxis
from cagraph.axis.taxis import CaGraphTAxis

from cagraph.ca_graph_grid import CaGraphGrid

from cagraph.series.line import CaGraphSeriesLine
from cagraph.series.hbar import CaGraphSeriesHBar
from cagraph.series.labels import CaGraphSeriesLabels
from cagraph.series.dna import CaGraphSeriesDNA

class MainWindow:
    def __init__(self):
        # create widget tree ...
        xml = gtk.glade.XML('example99.glade')

        # connect handlers
        xml.signal_autoconnect(self)

        # widgets
        self.main_window = xml.get_widget('main_window')
        self.vbox_graph = xml.get_widget('vbox_graph')
        self.label_xy =  xml.get_widget('label_xy0')
        
        # add graph
        self.graph = CaGraph(self.main_window)
        self.vbox_graph.pack_start(self.graph)
        
        # show pointer line
        self.graph.graph_style.draw_pointer = True
        self.graph.graph_style.draw_pointer_y = True
        
        # create and add axiss to graph
        xaxis = CaGraphXAxis(self.graph)
        xaxis.axis_style.label_format = '%d'
        xaxis.axis_style.side = 'top'
        yaxis = CaGraphYAxis(self.graph)
        yaxis.axis_style.draw_labels = False
        yaxis.axis_style.draw_tics = False
        self.graph.axiss.append(xaxis)
        self.graph.axiss.append(yaxis)
  
        # create and add top axis
        top_axis = CaGraphXAxis(self.graph)
        top_axis.axis_style.label_format = '%d'
        top_axis.axis_style.side = 'bottom'
        self.graph.axiss.append(top_axis)
        
        # create and add right axis
        right_axis = CaGraphYAxis(self.graph)
        right_axis.axis_style.side = 'right'
        right_axis.axis_style.draw_labels = False
        right_axis.axis_style.draw_tics = False
        self.graph.axiss.append(right_axis)
                       
        # create and add series to graph
        self.graph.seriess.append(CaGraphSeriesDNA(self.graph, 0, 1))
        self.graph.seriess.append(CaGraphSeriesLabels(self.graph, 0, 1))
        
        # add data to seriess
        self.graph.seriess[0].data = [
            (32.0,40.0,10.0),
            (10.0,15.0,20.0),
            (33.0,50.0,30.0),
            (38,42.0,40.0),
            (55.0,78.0,50.0), 
            (65.0,90.0,60.0),
            (75.0,84.0,70.0)]
        
        self.graph.seriess[1].data = [
            (32.0,10.0,u'sample 89A'),
            (10.0,20.0,u'sample 18'),
            (38,40.0,u'sample 46'),
            (55.0,50.0,u'sample 89B')]
            
        # automaticaly set axis ranges
        self.graph.auto_set_range()

        self.graph.grid = CaGraphGrid(self.graph, 0, 1)
        self.graph.grid.style.line_color = (0, 0.5, 0, 1.0)
        self.graph.grid.style.zero_line_color = (0, 0, 0, 0)

        # show x,y data in a label when the mouse is over the graph
        self.main_window.connect('motion-notify-event', self.motion_notify)
        
        # show wigdet
        self.graph.show()
    
    def motion_notify(self, widget, ev):
    
        # get the data seriess
        series = self.graph.seriess[0]
        
        # check if pointer is inside graph
        if self.graph.check_xy(ev.x, ev.y):
        
            # translate pixels to data
            x = series.xaxis.px_to_data(ev.x)
            y = series.yaxis.px_to_data(ev.y)
            
            # find nearest data point to mouse position
            # index = 2 is the y-axis
            point = series.find_point_by_index(y, 2)
            self.label_xy.set_text("X: %f - %f, Y: %f" % point)
            
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


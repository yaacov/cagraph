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
                
        # create and add series to graph
        self.graph.seriess.append(CaGraphSeriesLine(self.graph, 0, 1))
        self.graph.seriess.append(CaGraphSeriesBar(self.graph, 0, 1))
        
        # add data to seriess
        self.graph.seriess[0].data = [
            (10.0,52.0),(20.0,70.0),
            (30.0,53.0),(40.0,38),
            (50.0,75.0), (60.0,85.0),
            (70.0,65.0)]
        
        self.graph.seriess[1].data = [
            (10.0,42.0),(20.0,50.0),
            (30.0,63.0),(40.0,68),
            (50.0,75.0), (60.0,95.0),
            (70.0,65.0)]
        
        # automaticaly set axis ranges
        self.graph.auto_set_range()
        
        # show wigdet
        self.graph.show()
    
        # draw to file
        self.graph.draw_to_file('example1.svg')
        self.graph.draw_to_file('example1.png')
    
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


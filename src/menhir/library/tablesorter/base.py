# -*- coding: utf-8 -*-

import grok
import megrok.resourcelibrary
from menhir.library.jquery import JQueryBase


class TableSorter(megrok.resourcelibrary.ResourceLibrary):
    grok.name("menhir.library.tablesorter.base")
    megrok.resourcelibrary.depend(JQueryBase)
    megrok.resourcelibrary.directory('resources')
    megrok.resourcelibrary.include('jquery.tablesorter.min.js')


class SimpleTableSorter(megrok.resourcelibrary.ResourceLibrary):
    grok.name("menhir.library.tablesorter.simple")
    megrok.resourcelibrary.depend(TableSorter)
    megrok.resourcelibrary.directory('resources')
    megrok.resourcelibrary.include('simple.sorter.js')

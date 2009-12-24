# -*- coding: utf-8 -*-

from megrok import resource
from hurry.jquery import jquery


class TableSorter(resource.Library):
    resource.name("menhir.library.tablesorter.base")
    resource.path('resources')

    
tablesorter = resource.ResourceInclusion(
    TableSorter, 'jquery.tablesorter.min.js', depends=[jquery])

sortable = resource.ResourceInclusion(
    TableSorter, 'simple.sorter.js', depends=[tablesorter])

dragndrop = resource.ResourceInclusion(
    TableSorter, 'jquery.tablednd_0_5.js', depends=[jquery])

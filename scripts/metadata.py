#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Run this script in the root directory of the datapackage to get metadata
from data
"""
from datapackage import Package, infer

# get meta data with infer function
descriptor = infer('data/**/*.csv')

print(descriptor)

# create package based on derscriptor
p = Package(descriptor)

# add key 'name' to desrciptor with value 'tech...'
p.descriptor['name'] = 'Technology Costs'

p.descriptor['description'] = "Data includes costs and technical parameters."

p.descriptor["contributors"] = [{
    "title": "'Simon Hilpert'",
    "email": "simon.hilpert@uni-flensburg.de",
    "role": "author"
    }
]

p.descriptor["sources"] = [{
    "title": "DIW",
    "path": "https://www.diw.de/documents/publikationen/73/diw_01.c.424566.de/diw_datadoc_2013-068.pdf"
    }
]

# add to description to second field of the first resource
p.descriptor['resources'][1]['schema']['fields'][3]['description'] = "Units in Euro/kW 2010"
p.descriptor['resources'][1]['schema']['fields'][4]['description'] = "Lifetime of plant in years"
p.descriptor['resources'][1]['schema']['fields'][5]['description'] = "Units in percentage per insatalled capacity kW/a"


p.commit()

p.save('datapackage.json')

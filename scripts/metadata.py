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
    }, {
    "title": "'Martin Soethe'",
    "email": "martin.soethe@uni-flensburg.de",
    "role": "author"
    }
]

p.descriptor["sources"] = [{
    "title": "DIW",
    "path": "https://www.diw.de/documents/publikationen/73/diw_01.c.424566.de/diw_datadoc_2013-068.pdf"
    }, {
    "title": "Brown",
    "path": "10.1016/j.energy.2017.06.004"
    },
    {
    "title": "UBA2016",
    "path": "https://www.umweltbundesamt.de/sites/default/files/medien/1968/publikationen/co2-emissionsfaktoren_fur_fossile_brennstoffe_korrektur.pdf"
    },
    {
    "title": "REMod",
    "path": "https://doi.org/10.1016/j.rser.2013.09.012"
    }
]

p.commit()

p.save('datapackage.json')

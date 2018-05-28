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
p.descriptor['name'] = 'technology costs'

# add to description to second field of the first resource
p.descriptor['resources'][0]['schema']['fields'][1]['description'] = 'lifetime of component in years'
p.descriptor['resources'][0]['schema']['fields'][1]['title'] = 'Lifetime of component'



# apply changes to datapackage
p.commit()

# save the metadata
p.save('datapackage.json')

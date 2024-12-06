#!/usr/bin/env python3

"""
Get Star Citizen bindings, and push actionmap names into Joystick Gremlin's config.
In JG config, vjoy have to be labeled: vjoy{number}:js{number}.
Don't forget to update that, if SC change theses.
"""

import xml.etree.ElementTree as ET
import random

SC_xml = "full.actionmaps.xml"

SC_binds = ET.parse(SC_xml).getroot()

first_param = {}
param = {}

#for action in SC_binds.findall('ActionsMaps/ActionProfiles/actionmap'):
for AM in SC_binds.iter('ActionMaps'):
    for AP in AM.iter('ActionProfiles'):
        for actionmap in AP.iter('actionmap'):
            for action in actionmap.iter('action'):
                param_splitted = action.attrib['name'].split('_')
                fparam = param_splitted.pop(0)
                first_param[ fparam ] = True
                for param_str in param_splitted:
                    param[ param_str ] = True

#print( first_param )
#print( f"\t{param}" )

rparam = random.choice( list( first_param.items() ) )[0]
for i in range(0,4):
    ritem = random.choice( list( param.items() ) )[0]
    rparam = f"{rparam}_{ritem}"

print( rparam )
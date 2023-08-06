#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: DIYer22@github
@mail: ylxx@live.com
Created on Sat Dec 28 21:38:05 2019
"""

from boxx import *
from boxx import os

import bpy



def set_inst_map_material():
    objs = [obj for obj in bpy.data.objects if "inst_idx" in obj]
    instn = len(objs)
    for idx_obj, obj in enumerate(objs):
        material_name = "inst_map_material." + obj.name
        material = bpy.data.materials.new(material_name)
        material.use_nodes = True
        bsdf = material.node_tree.nodes["Principled BSDF"]

        bsdf.inputs[0].default_value = (0, 0, 0, 1)
        bsdf.inputs[3].default_value = (0, 0, 0, 1)
        obj.data.materials.append(material)
        for inp_idx in range(4, 17):
            bsdf.inputs[inp_idx].default_value = 0

        if "inst_idx" in obj:
            brightness = (obj["inst_idx"] + 1) / instn
        else:
            brightness = 0.0
        bsdf.inputs[17].default_value = (brightness,) * 3 + (1,)

if __name__ == "__main__":
    pass
    
    
    

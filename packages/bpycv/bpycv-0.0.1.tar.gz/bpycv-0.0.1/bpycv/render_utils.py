#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: DIYer22@github
@mail: ylxx@live.com
Created on Sat Dec 28 21:33:28 2019
"""

from boxx import *
from boxx import inpkg


with inpkg():
    from .select_utils import scene, render

def set_inst_map_render():
    render.engine = "BLENDER_EEVEE"
    scene.eevee.taa_render_samples = 1

    render.image_settings.file_format = "OPEN_EXR"
    render.image_settings.color_mode = "RGBA"
    render.image_settings.color_depth = "32"
    render.image_settings.use_zbuffer = True

if __name__ == "__main__":
    pass
    
    
    

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: DIYer22@github
@mail: ylxx@live.com
Created on Thu Dec 26 18:15:47 2019
"""

from boxx import *
from boxx import np, inpkg

with inpkg():
    from .pseudo_color import heatmap_to_pseudo_color

import OpenEXR


class ExrDict(dict):
    LIMIT_DEPTH = 1e8

    def __getattribute__(self, key):
        if len(key) == 1 and key.upper() in self:
            return self[key.upper()]
        return dict.__getattribute__(self, key)

    def get_rgb(self):
        return np.concatenate(
            [self["R"][..., None], self["G"][..., None], self["B"][..., None]], -1
        )

    def get_rgba(self):
        return np.concatenate(
            [
                self["R"][..., None],
                self["G"][..., None],
                self["B"][..., None],
                self["A"][..., None],
            ],
            -1,
        )

    def get_pseudo_color(self):

        limit_mask = self.z < self.LIMIT_DEPTH
        depth = self.z * limit_mask
        # depth = np.log(depth + 1)
        depth = depth / depth.max()
        depth[~limit_mask] = 1.1
        depth = 1 - depth
        return heatmap_to_pseudo_color(depth)

    def get_depth(self):
        limit_mask = self.z < self.LIMIT_DEPTH
        depth = self.z * limit_mask
        return depth


def parser_exr(exr_path):
    file = OpenEXR.InputFile(exr_path)
    header = file.header()

    h, w = header["displayWindow"].max.y + 1, header["displayWindow"].max.x + 1
    exr = ExrDict()
    for key in header["channels"]:
        assert header["channels"][key].type.__str__() == "FLOAT"
        exr[key] = np.fromstring(file.channel(key), dtype=np.float32).reshape(h, w)
    file.close()
    return exr


def test_parser_exr(exr_path="../tmp_exrs/cycles.exr"):
    return parser_exr(exr_path)


if __name__ == "__main__":
    from boxx import show, timeit, mg

    exr_path = "tmp_exr.exr"
    exr_path = "../tmp_exrs/untitled.exr"
    exr_path = "/tmp/blender/tmp.exr"
    exr = parser_exr(exr_path)
    rgb = exr.get_rgb()
    show - rgb
    z = exr.z
    a = exr.a
    za = z * a
    depth = exr.get_pseudo_color()
    show - depth

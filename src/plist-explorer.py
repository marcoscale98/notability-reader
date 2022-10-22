import os
import plistlib
import struct
import numpy as np


def unpack_struct(string, fmt):
    return struct.unpack(f'{len(string) // 4}{fmt}', string)


def unpack_colors(string):
    sublists = list(string)
    return [list(i) for i in [sublists[i:i + 4] for i in range(0, len(sublists), 4)]]


if __name__ == '__main__':
    filename = os.path.relpath("../bdb_transazioni/Session.plist")
    with open(filename, "rb") as fp:
        pl = plistlib.load(fp)
        data = pl['$objects'][8]
        points = data['curvespoints']
        curvesnumpoints = data['curvesnumpoints']
        curveswidth = data['curveswidth']
        curvescolors = data['curvescolors']
        curvesfractionalwidths = data['curvesfractionalwidths']
        eventTokens = data['eventTokens']
        unpacked_points = unpack_struct(points, 'f')
        unpacked_numpoints = unpack_struct(curvesnumpoints, 'i')
        unpacked_curveswidth = unpack_struct(curveswidth, 'f')
        unpacked_curvescolors = list(curvescolors)
        unpacked_curvesfractionalwidths = unpack_struct(curvesfractionalwidths, 'f')
        unpacked_eventTokens = unpack_struct(eventTokens, 'f')
        # Now we have unpacked all of the points, time to do the rest

import plistlib
import struct
import numpy as np


def unpack_struct(string, fmt):
    return struct.unpack(f'{len(string) // 4}{fmt}', string)


def unpack_colors(string):
    sublists = [x for x in string]
    return [list(i) for i in [sublists[i:i + 4] for i in range(0, len(sublists), 4)]]


if __name__ == '__main__':
    with open("../bdb_transazioni/Session.plist", "rb") as fp:
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
        unpacked_curvescolors = [x for x in curvescolors]  # List of sublists of RGBA values
        unpacked_curvesfractionalwidths = unpack_struct(curvesfractionalwidths, 'f')
        unpacked_eventTokens = unpack_struct(eventTokens, 'f')
        # Now we have unpacked all of the points, time to do the rest

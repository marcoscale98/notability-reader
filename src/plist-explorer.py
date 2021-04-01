import subprocess
import plistlib
import struct


def unpack_struct(string, fmt):
    return struct.unpack(f'{len(string) // 4}{fmt}', string)


with open("../bdb_transazioni/Session.plist", "rb") as fp:
    pl = plistlib.load(fp)
    data = pl['$objects'][8]
    points = data['curvespoints']
    curvesnumpoints = data['curvesnumpoints']
    curveswidth = data['curveswidth']
    curvescolors = data['curvescolors']
    unpacked_points = unpack_struct(points, 'f')
    unpacked_numpoints = unpack_struct(curvesnumpoints, 'i')
    unpacked_curveswidth = unpack_struct(curveswidth, 'f')
    unpacked_curvescolors = [x for x in curvescolors]
    print(curvescolors)

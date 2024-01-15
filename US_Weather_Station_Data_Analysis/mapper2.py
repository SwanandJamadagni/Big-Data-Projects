#!/usr/bin/env python
import sys

out_d = {}

for l in sys.stdin:
    l = l.strip()
    (station, sky_ch, q) = (l[4:10], l[70:75], l[75:76])
    if(station != '999999' and sky_ch != '99999' and q in ['0','1','4','5','9']):
        print '%s,%s' % (station, sky_ch)

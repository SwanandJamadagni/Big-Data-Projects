#!/usr/bin/env python
import sys

s_vdist_dict = {}

for l in sys.stdin:
    l = l.strip()
    (station, v_dist, q) = (l[4:10], l[78:84], l[84:85])
    if(station != '999999' and v_dist != '999999' and q in ['0','1','4','5','9']):
        s_vdist_dict[station] = str(s_vdist_dict.get(station,''))+str(v_dist)+','

for k in s_vdist_dict:
    out = str(k)+','+str(s_vdist_dict[k])
    if out[-1] == ',':
        out = out[:-1]
        
    print(out)

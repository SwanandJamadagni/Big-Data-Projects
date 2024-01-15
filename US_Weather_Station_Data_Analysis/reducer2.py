#!/usr/bin/env python
import sys

out_d = {}

for l in sys.stdin:
    l = l.strip()
    l = l.split(',')
    st = l[0]
    sch = []
    sch.append(l[1])
    c = out_d.get(st,'')
    out_d[st] = list(c)+sch

for k in out_d:    
    out_d[k] = list(set(out_d[k]))

for k in out_d:
    for i in out_d[k]:
        print '%s\t%s' % (k, i)

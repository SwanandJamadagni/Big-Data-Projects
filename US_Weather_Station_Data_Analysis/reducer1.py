#!/usr/bin/env python
import sys

out_d = {}

for l in sys.stdin:
    l = l.strip()
    l = l.split(',')
    st = l[0]
    dl = l[1:]
    c = out_d.get(st,'')
    out_d[st] = list(c)+dl

for k in out_d:
    dl = out_d[k]
    recs = len(dl)
    s = 0
    for r in dl:
        s = s+int(r)
    a = s/recs
    
    print '%s\t%s' % (k, a)

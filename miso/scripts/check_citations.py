#!/usr/bin/env python3
"""List every issue the guide cites, with its state in miso/source/issues.json.

Usage: python3 miso/scripts/check_citations.py [issues.json]

Run it after merge_issues.py. It shows, for each cited issue: state, closing date,
last activity in the export, and the pages that cite it. Issues absent from the
export are listed apart, so a fresh export can be requested. Standard library only.
"""
import glob, json, re, sys
path = sys.argv[1] if len(sys.argv) > 1 else 'miso/source/issues.json'
data = {i['number']: i for i in json.load(open(path))}
snap = max([i['createdAt'] for i in data.values()] + [c['createdAt'] for i in data.values() for c in i['comments']])
cites = {}
for f in sorted(glob.glob('docs/*.md')):
    for n in set(re.findall(r'UNopenGIS/7/issues/(\d+)', open(f).read())):
        cites.setdefault(int(n), []).append(f.split('/')[-1][:-3])
print('export snapshot ends at', snap[:10])
missing = []
for n in sorted(cites):
    i = data.get(n)
    if not i:
        missing.append(n); continue
    last = max([i['createdAt']] + [c['createdAt'] for c in i['comments']])
    print('#%d %-6s closed=%s last=%s comments=%d  %s' % (n, i['state'], (i['closedAt'] or '-')[:10], last[:10], len(i['comments']), ','.join(cites[n])))
if missing: print('not in the export (refresh it):', missing)

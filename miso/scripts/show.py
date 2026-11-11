#!/usr/bin/env python3
"""Print one issue thread from miso/source/issues.json, truncated. Usage: show.py NUMBER [maxchars]"""
import json, sys
d = {i['number']: i for i in json.load(open('miso/source/issues.json'))}
i = d[int(sys.argv[1])]; m = int(sys.argv[2]) if len(sys.argv) > 2 else 500
print('#%d %s [%s] %s..%s labels=%s' % (i['number'], i['title'], i['state'], i['createdAt'][:10], (i['closedAt'] or '')[:10], [l['name'] for l in i['labels']]))
print('BODY:', i['body'][:m].replace('\n', ' '))
for c in i['comments']:
    print('-', c['createdAt'][:10], c['author']['login'], ':', c['body'][:m].replace('\n', ' '))

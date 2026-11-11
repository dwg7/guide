#!/usr/bin/env python3
"""Index Qiita API v2 exports in miso/source/qiita-USER-N.json. Usage: qiita_index.py USER"""
import json, glob, sys
u = sys.argv[1]
items = [x for f in sorted(glob.glob('miso/source/qiita-%s-*.json' % u)) for x in json.load(open(f))]
items.sort(key=lambda x: x['created_at'])
for x in items:
    print(x['created_at'][:10], len(x['body']), x['likes_count'], ','.join(t['name'] for t in x['tags'])[:40], '|', x['title'][:70], '|', x['url'].split('/')[-1])

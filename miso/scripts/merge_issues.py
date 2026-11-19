#!/usr/bin/env python3
"""Merge a newer `gh issue list` export into miso/source/issues.json (by issue number).

Refresh recipe (run on a machine with gh access; an incremental export is enough):

    gh issue list -R UNopenGIS/7 --state all --limit 2000 \
      --search "updated:>=2026-11-01" \
      --json number,title,state,labels,author,assignees,createdAt,closedAt,body,comments > issues-new.json
    python3 miso/scripts/merge_issues.py issues-new.json

Standard library only. Prints the numbers added and updated.
"""
import json, sys
base_path = 'miso/source/issues.json'
base = {i['number']: i for i in json.load(open(base_path))}
new = json.load(open(sys.argv[1]))
added, updated = [], []
for i in new:
    (updated if i['number'] in base else added).append(i['number'])
    base[i['number']] = i
json.dump(sorted(base.values(), key=lambda i: i['number']), open(base_path, 'w'), ensure_ascii=False)
print('added', sorted(added)); print('updated', sorted(updated)); print('total', len(base))

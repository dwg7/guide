#!/usr/bin/env python3
"""Summarise miso/source/issues.json (gh issue list export). Standard library only."""
import json, sys, collections as C
d = json.load(open(sys.argv[1] if len(sys.argv) > 1 else 'miso/source/issues.json'))
last, cnt = {}, C.defaultdict(C.Counter)
for i in d:
    ev = [(i['createdAt'], i['author']['login'])] + [(c['createdAt'], c['author']['login']) for c in i['comments']]
    for t, u in ev:
        last[u] = max(last.get(u, ''), t); cnt[t[:4]][u] += 1
print('issues', len(d), 'open', sum(i['state'] == 'OPEN' for i in d))
for y in sorted(cnt): print(y, cnt[y].most_common(8))
print('last activity:', sorted(((t[:10], u) for u, t in last.items() if cnt['2026'][u] or t > '2026'), reverse=True)[:15])
for u in ['albertkun','ShogoHirasawa','mapconcierge','ubukawa','asahina820','kenjiyoshidahome2026-bit','k96mz','smellman']: print(u, last.get(u,'')[:10])

#!/bin/sh
# Fetch the Qiita articles used as background (public API v2, no token) into miso/source/.
# Usage: sh miso/scripts/fetch_qiita.sh   (writes qiita-T-ubu-N.json and qiita-k96mz-N.json; git-ignored)
mkdir -p miso/source
for u in k96mz T-ubu; do
  for p in 1 2 3; do
    curl -sS "https://qiita.com/api/v2/users/$u/items?page=$p&per_page=100" -o "miso/source/qiita-$u-$p.json"
  done
done

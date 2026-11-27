# 引き継ぎ（会話の圧縮・再開用）

最終更新: 2026-11-27。次のセッションは、この文書、`AGENTS.md`、`miso/dwg7.md`、`miso/FOLLOW-UP.md` の順に読めば再開できる。

## 何のリポジトリか

dwg7 の公開ガイド（GitHub Pages、`main` の `/docs`、公開 URL は https://dwg7.unopengis.org/guide/）。中核は 5 ページ（`docs/` の 5 点、`docs/index.md` が入口）。内部の材料庫は `miso/dwg7.md`（miso 形式。`check_miso.py` はエラー 0、警告 4。警告は未作成の参照パスの類）。

## ユーザーの方針（hfu）

- 最優先は**ロジック**。連鎖「問い → 実験 → 条件つきの結果 → レビューと訂正 → 再利用」で記述する。
- 英文は**肯定形**、短く、具体的（Elements of Style の精神）。否定語（not、no、never、without、cannot、nor）を残さない。GitHub の語（`not planned`）や引用した選択肢の名前は例外。
- `dwg7` は常に小文字。個人名より役割（contributor、owner）。
- 確認できないことは書かない。確認できない提案は「このガイドは〜を勧める」と明示する。要約を介した情報は、そう明記する。
- 各ターンで、やったことを報告し、次のターンの提案をする。ユーザーの指示があればそれを優先する。
- `main` への push は、区切りごとに随時してよい（ユーザーの許可あり）。作業ブランチは `claude/eloquent-euler-b2w67t`。`git push origin claude/eloquent-euler-b2w67t:main`（fast-forward）で反映してきた。PR は作っていない。
- 外部への投稿（Issue、コメント、メール）は、依頼がない限りしない。下書きまで。

## いまの状態（2026-11-27、すべて push 済み）

- 5 ページを、Issue（993 件、2026-11-11 のエクスポート）と dwg7 組織のリポジトリの記録に基づいて書き直した。5 Minutes（連鎖、10 の習慣、三つの自己記述、リポジトリ群）、Onboarding（6 つの道、各道に実在の Issue と公開リポジトリ 3 件）、Good First Experiments（14 件。検証済み: 4 部分、5、9、10、13。再現待ち: 6、7、8、14）、Field Guide（Q1〜Q24）、Monthly Snapshot（テンプレートと 4 つの作例: #1003、#1027 のミッション通信速度、cvalda、#1036 のドローン）。
- `CONTRIBUTIONS.md`、`miso/FOLLOW-UP.md`（週次の追従）、`miso/scripts/`（`merge_issues.py`、`check_citations.py`、`analyze.py`、`show.py`、`qiita_index.py`、`fetch_qiita.sh`）。
- 公開 URL を `dwg7.unopengis.org/guide/` に訂正済み（当初の `dwg7.opengis.org` は名前解決できなかった）。

## ローカルのデータ（git 管理外。消えたら再生成）

- `miso/source/issues.json`: `gh issue list -R UNopenGIS/7 --state all --limit 2000 --json number,title,state,labels,author,assignees,createdAt,closedAt,body,comments > issues.json`。この環境では GitHub の API が拒否されるため、ユーザーに実行してもらい、アップロードされた（2026-11-11 時点、993 件）。以後の更新分は `merge_issues.py` で統合する。**2026-11-18 以降の更新は、まだ統合していない**（下記）。
- `miso/source/qiita-*.json`: `sh miso/scripts/fetch_qiita.sh`（208 本。ubukawa は T-ubu、k96mz）。
- 外部リポジトリの読み取り用の clone（`/home/user/dwg7/{miso,cvalda,cafebabe,browse/*}`）は、`git clone --depth` で再取得できる（匿名の公開リポジトリのみ）。
- Jekyll の確認ビルド: `ruby <gem path>/jekyll-3.10.0/exe/jekyll build -s docs -d <scratchpad>/site --baseurl ""`（`gem install jekyll jekyll-relative-links jekyll-optional-front-matter jekyll-seo-tag webrick`）。

## この環境の制約

- `gh` と GitHub API は、検索（`gh api search/...`）を除き拒否される。GitHub の HTML ページは `curl` で 403。公開ページは、取得エージェント（`web-fetch`）で読める（長いページは要約を介すので、完全な確認にはエクスポートが要る）。
- 外部のコードのビルドと実行（tippecanoe の `make`、cvalda のスクリプト）は、自動判定で拒否された。回避しない。該当する実験（6、7、8、14）は「再現待ち」と Status 行で明記している。
- `add_repo` の push 付きの接続は拒否された。読み取りは匿名の `git clone` で足りる。
- 他のエージェント（`cvalda` など）には、同じアカウントの一覧にいない限り連絡できない。cvalda の担当エージェントは、guide の担当への質問を 2 件残している。回答案は `miso/dwg7.md` の `/open-questions/cvalda-onboarding-answers`（外部には投稿していない。hfu 経由）。

## 未了・次の候補（優先順）

1. **Issue のエクスポートを再取得して統合する。** `issues-new.json`（更新分、コマンドは `merge_issues.py` の冒頭）を受け取り、`merge_issues.py` → `check_citations.py`。#1028（11-17 の週次）は全文が未確認（要約を介した部分あり）。#1031〜#1037、2026-11-26 の一斉 closed（13 件）、#740 と #976（open）の最新を反映する。
2. #1011 と #997 を全文読み、ferspas の停止の経緯を miso に連鎖で記録する。
3. cafebabe の `patterns/`（39 ファイル）から、Field Guide に生きる知見を拾う。
4. README を読んでいないリポジトリ（maplibre-gl-atlas、kaga0、bvmap、kataribe）の確認。
5. Qiita の各主題の残りの本文（約 150 本）の精読。
6. Field Guide Q22（アプリのリポジトリの登録手順）は「このガイドの提案」のまま。cafebabe の保守者に確認するとよい。
7. 実験 4・6・7・8・14 の再現（許可があれば）。
8. ラベルの定義文書の有無（リポジトリ側の確認に API 権限が要る）。

## 確認済みの重要な事実（再確認が不要なもの）

- dwg7 は、UN Open GIS Initiative の Domain Working Group 7（Smart Maps）。主要メンバー（2026 年の発言）は 6 名。公開記録は Issue と、dwg7 組織の 27 件のプロジェクト（cafebabe の `PROJECTS.md`）。
- 週次ミートアップ: 12:30–12:55 JST、火曜（165 件中 164 件）、開始前のコメントが 163 件すべてにある。
- `priority/*` の閉じるまでの中央値: MUST 14 日、SHOULD 23 日、MAY 32 日。
- 非公開のリポジトリ: `m3xx-fleet-ops`（guide は公開の `m3xx-fleet` にリンク）。リンクの前に `git ls-remote` で匿名に読めることを確認する。
- ferspas57 は 2026-09-18 から停止（README の冒頭に理由）。

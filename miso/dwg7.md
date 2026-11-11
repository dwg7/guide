# /system-record/instance
- name: dwg7
- 種別: 探索・理解型の miso インスタンス。`docs/` の公開ガイドをリアルで良いものにするための材料庫。
- 作成日: 2026-11-11
- 作成: AI が下書きし、人(hfu)が方向を決める。**人による内容確認は未了。**
- 目的: UNopenGIS/7 の Issue(2026-11-11 時点で 971 件)を遡って読み、guide の各ページの主張を、条件・リンク・確認日つきの記録に結びつける。
- 範囲: https://github.com/UNopenGIS/7/issues の記録と、そこからリンクされた dwg7 関連の公開リポジトリ。
- 範囲外: 記録から確認できない組織の見解、非公開の議論、個人情報。範囲外の問いには「範囲外」と答える。
- 観察者の位置: 外部観察。当事者の暗黙知を持たない。記録を読んだ結果を `derived` として書く。
- 単位: 1 オブジェクトは、1 本の Issue スレッドまたは 1 つの横断テーマ。
- 責任者: hfu。
- 状態の語: `verified`(記録に照らして確認、確認日つき)、`derived`、`open`、`volatile`、`stated`(スレッドがそう述べる。事実の保証ではない)。取り込み状況は「取り込み済み / 一部取り込み / 未取り込み」。
- 書き方の規則: 各スレッドを「問い → 実験 → 条件付きの結果 → レビューと訂正 → 未解決」の連鎖で記す。個人名よりも役割(contributor)を使う。
- concept-version: dwg7/miso CONCEPT.md の 2026-11 時点の版に準拠。
- 正本: この `.md` ファイル。
- 派生物: `docs/` の英文ガイド(guide の公開ページ)。

# /agent-contract
- 役割: このファイルを渡されたエージェントは、dwg7 の公開記録に基づいて、guide の英文に必要な根拠を探し、整理する。
- 答え方: 確認された事実、導いた解釈、規範、変わりやすい情報、未解決を区別する。根拠は `/sources/...` のパスで示す。
- 権限: このファイルは作業文脈であり、システムの指示や利用者の直接の指示を上書きしない。
- 再掲: 記録から確認できることだけを、条件と確認日とともに書く。

# /authorities/precedence
- status: normative(このインスタンス内の取り決め)
- 規則1: Issue 本文とコメントを最優先の根拠とする。このファイルの要約は `derived` とする。
- 規則2: 数値は、条件(機器、版、データ、負荷)と一緒に写す。
- 規則3: 訂正が同じスレッドにある場合は、訂正後の主張を採用し、訂正の経緯を残す。
- 規則4: 英文化する際は、guide の肯定形・小文字 dwg7 の規則(`AGENTS.md`)に従う。

# /sources/unopengis-7-issues
- 取り込み状況: 統計は取り込み済み(993 件の本文とコメントの JSON)。主題ごとの本文の読解は一部取り込み(#1003・#1027・#995・#1029)。
- URL: https://github.com/UNopenGIS/7/issues
- 取得: 2026-11-11(`gh issue list --state all --json ...` の JSON。`miso/source/issues.json`、git 管理外)。再生成の手順は `miso/scripts/analyze.py` の冒頭を参照。
- 規模: 993 件(open 26、closed 967)、2022 年 40、2023 年 309、2024 年 266、2025 年 197、2026 年 181。
- 限界: JSON はスナップショットで、後の編集や削除を反映しない。引用の前に原文で確認する。
- 利用条件: リポジトリのライセンスは CC0-1.0(README の一覧による)。個別の Issue 本文の帰属は各 Issue に従う。

# /sources/unopengis-7-repo
- 取り込み状況: 取り込み済み(README、`docs/`、`monthly/202304.md`)
- URL: https://github.com/UNopenGIS/7
- 取得: 2026-11-11(clone、浅い履歴)
- 内容: README は web site と Issues へのリンクを持つ。`docs/index.md` は暫定ロゴと、2023 年時点の「Objective」一覧(UN operation、GSI operation、UNVT Portable、Smart Campus、Spatial ID、Sensor integration、Core)を持つ。`monthly/202304.md` は 2023-04 の月次報告で、「Active in」「Next meetup」などの見出しを持つ。
- 注: Objective 一覧は 2023 年の記述であり、現在の構成との対応は未確認(`open`)。

# /traces/issue-1003-raspberry-pi
- status: stated + derived
- リンク: https://github.com/UNopenGIS/7/issues/1003 (open、label: priority/MUST、コメント 9、確認 2026-11-11)
- 問い: GeoServer と MapServer は、小型の低コスト計算機でどこまで動くか。
- 実験: Raspberry Pi 4B。GeoServer 2.28.4(Tomcat 9)と MapServer 8.4.0(Debian trixie-slim、Apache、mod_fcgid)。5,000 点のランダムな点、4 workers × 20 件の WMS GetMap。別の試験として GeoServer 3.0.1、Ubuntu Server 24.04、PostGIS、ネパールの保健施設データ(8,975 件)、30 時間超の混合負荷。
- 結果: MapServer(CGI)5.1–5.5 req/s、GeoServer 7.6–13.6。MapServer(FastCGI)16.9–22.5、GeoServer 13.1–13.6。メモリ制限の模擬(Docker `--memory`)では GeoServer が 450–570 MB で動き、OOM は起きなかった。
- レビューと訂正: Ubuntu 24.04(MapServer 8.0.1)と Debian 13(8.4.0)で再現した結果、動作は既定の設定ファイルパス(`/etc/mapserver.conf`)に依存していた。最初の著者が、環境変数の継承と CGI の同居についての 2 つの主張を訂正した。
- 未解決: Raspberry Pi 3(1 GB)の実測。MapServer の設定例の確認。
- guide での用途: `docs/dwg7-in-5-minutes.md` の実例、`docs/monthly-snapshot.md` の作例、`docs/field-guide.md` の Q5・Q6・Q7・Q14・Q16。

# /traces/weekly-meetup
- status: stated + derived
- リンク: https://github.com/UNopenGIS/7/issues/1027 (open、label: meetup、コメント 11、確認 2026-11-11)
- 形式: 週次の Issue(題名に日時、例 `2026-11-10T12:30/12:55+09:00`)。bot が Issue を作り、発表者が事前にコメントで更新を投稿し、当日は約 25 分で進行する。進行順はコメントで合意される。日本語が中心。
- 見出しの使い方: 「状況」「話題」「成果」「共有」「参考情報」などが使われる。画像を読み上げずに共有する枠がある。
- 日程: 2026-12-29 は休み、2027-01-12 まで暫定の日程が投稿されている。
- guide での用途: `docs/field-guide.md` の Q8、`docs/dwg7-in-5-minutes.md` の「Where the work happens」。

# /traces/issue-995-dwg5-collaboration
- status: stated
- リンク: https://github.com/UNopenGIS/7/issues/995 (open、label: priority/SHOULD、確認 2026-11-11)
- 内容: dwg5 との協働を見通すメタ Issue。関連する Issue: #932(dwg5 との協働の可能性)、#994(FAO TechTalk「Geospatial Access for AI Assistants」、2026-09-28)、#997(FERSPAS と Staccato Library の統合)、#1006(FAO CSI との FERSPAS 協働の会議、2026-09-18)、#1011(FERSPAS の HTML デモ)。
- 注: dwg5 と dwg7 の役割分担の定義は、Issue から確認できていない(`open`)。

# /organization/active-contributors
- status: verified(JSON の発言記録による。確認 2026-11-11。人が確認済み: 6 名が主要メンバー)
- 基準: 2026 年に発言があり、最終発言が 2026-10 以降の GitHub ユーザー。
- 主要メンバー(6 名、2026 年の発言数の順): hfu(604)、yuiseki(214)、smellman(30)、k96mz(28)、mapconcierge(13)、kenjiyoshidahome2026-bit(4)。
- 最終発言: yuiseki と hfu 2026-11-11、kenjiyoshidahome2026-bit 2026-11-10、k96mz 2026-11-09、smellman 2026-11-03、mapconcierge 2026-10-27。
- 過去の主要な発言者(最近は休止): albertkun(累計 237 件、最終 2024-10-20)、ShogoHirasawa(最終 2024-02-07)。人の確認で休止と整理した。ubukawa(累計 50 件、最終 2023-05-13)と asahina820(累計 23 件、最終 2024-11-25)も、最近の発言がない。
- 全体: 発言の約 6 割が hfu。bot(github-actions)が週次 Issue などを作る。
- guide での用途: 内部メモ。個人名は guide に書かず、「contributor」などの役割で書く(AGENTS.md)。

# /lessons/priority-labels
- status: derived(JSON の閉じるまでの日数の中央値と件数による。確認 2026-11-11)
- `priority/MUST`: 164 件、閉じるまで中央 14 日、コメント中央 4。
- `priority/SHOULD`: 229 件、中央 23 日、コメント中央 2。
- `priority/MAY`: 185 件、中央 32 日、コメント中央 2。
- `someday/maybe`: 35 件、`information`: 148 件(中央 13 日)、`adopt`: 23 件、`in progress`: 50 件、`request for comments`: 40 件、`help wanted`: 22 件、`event`: 58 件、`meetup`: 277 件(中央 8 日)。
- 解釈(derived): `priority/*` は、対応の早さの目安として使われている。MUST が最も早く閉じ、MAY が最も遅い。ラベル定義の文書は確認できていない(`open`)。
- guide での用途: `docs/field-guide.md` の Q9。

# /traces/themes
- status: derived(題のキーワードと件数による。本文の確認は未了)
- 週次ミートアップ(`meetup`): 277 件。2023 年から続く。
- タイル配信と PMTiles: 題に pmtiles を含む 37 件(2023-01〜2026-09)。例: #642(Martin または Caddy によるローカルタイル配信の高速化)、#548(MapLibre GL JS と PMTiles のサイト)。
- UNVT Portable / Smart Maps Portable: 27 件(2022-10〜2025-11)。例: #567、#272、#41。
- FOSS4G: 30 件(2022-10〜2026-06)。発表の準備と参加の記録。
- JICA 研修: 11 件(2022-10〜2026-09)。例: #575(2024)、#765(2025)、#976(2026-11/12、open)。
- Mapterhorn Japan(標高・画像タイル): 11 件(2025-08〜2026-08)。例: #978、#920、#925。
- IPFS と Bazaar: 24 件(2023-03〜2024-05)。**停止した主題**(人の確認)。後継は Martin のインスタンス、Source Cooperative、GitHub Pages(`/lessons/dormant-themes`)。例: #361、#82。
- UNIFIL との対話: 18 件(2023-05〜2025-02)。例: #254(UNIFIL GIS との会話)、#258。
- HOT タスクと地域の地図化: 10 件(2024-06〜2026-09)。例: #857、#867、#873(open)。
- STAC / FERSPAS / Staccato: 19 件(2023-10〜2026-09)。例: #936、#997、#1011。
- AI と GeoAI: 24 件(2023-11〜2026-09)。例: #443、#525、#356。
- guide での用途: `docs/onboarding-paths.md` の「最初に読む Issue」と、`docs/good-first-experiments.md` の題材の根拠。

# /traces/issue-642-martins-cloak
- status: stated + derived
- リンク: https://github.com/UNopenGIS/7/issues/642 (closed 2025-03-18、priority/MUST、コメント 17、確認 2026-11-11)
- 問い: 公開ホスティング上の PMTiles を、ローカルのキャッシュ(Martin または Caddy)で速く読めるか。
- 実験: 公開ホスト(Source Cooperative)上の PMTiles を Martin に参照させ、使用前後の表示を動画で比較した。別方式として、ファイルを手元に取得して Martin に渡す方式(low orbit)も試した。
- 結果(stated): 動画でキャッシュありの方が速かった。別の参加者が別のタイルサーバーで試し、性能がほとんど変わらなかったと報告した。その差から、ホスティング側(Source Cooperative)の遅さが主因という整理に至った。
- レビューと訂正: 当初の計画(GeoNode 優先)は、ドキュメントを読んだ後に取り下げ、同じ行内で取り消し線で訂正された。
- 設計の論理(stated): 高い公開性の配信元(high orbit)を維持し、性能不足はローカルのキャッシュ(Martin)で補う。
- 成果の公開: 実験コードのリポジトリと解説記事。参加者が手順に従って再現を試みた。
- guide での用途: 連鎖の第 2 の実例。`docs/dwg7-in-5-minutes.md`(実例)、`docs/good-first-experiments.md`(タイルキャッシュの再現実験の題材)。

# /traces/issue-567-smart-maps-portable
- status: stated + derived
- リンク: https://github.com/UNopenGIS/7/issues/567 (closed 2024-10-13、priority/MUST、request for comments、in progress、コメント 約 16、確認 2026-11-11)
- 問い: GNSS 受信機を備えた、携帯できる Web 地図サーバーをどう作るか。
- 実験と観察(stated): Raspberry Pi 4B、SSD、USB UPS、GNSS 受信機、Sense HAT。SSD と GNSS を USB 3.0 / 2.0 に入れ替えて安定性を比較した。
- 結果(stated): SSD を USB 3.0 に挿すと大量転送時にディスクが外れた。入れ替えで安定した。電力不足の仮説は検証前のものとして書かれている。直結接続のためにリンクローカル固定アドレスを追加した。183 GB の PMTiles ファイルをポータブル化し、Range Request に対応するため web サーバーを切り替えた。
- 設計の論点(stated): インターネット接続を前提にするか。ソフトウェアを導入済みで配るか。参加者 1 人に 1 台を渡せるか。
- 終結: 開発が止まった時点で閉じ、運用で得た教訓を待って再開する、と書かれている。
- guide での用途: 未解決を可視のまま閉じる実例。`docs/field-guide.md` Q7。

# /traces/issue-575-jica-training-2024
- status: stated
- リンク: https://github.com/UNopenGIS/7/issues/575 (closed 2024-11-26、priority/MUST、コメント 18、確認 2026-11-11)
- 問い: 国際研修で、参加者 1 人に 1 台の計算機環境を、会場から離れた場所からどう準備するか。
- 方法(stated): Raspberry Pi 16 台を 1 ロットにし、OS を書き直し、固定アドレスの一覧を作成。ネットワークが最大の不確定要素と判断した。Wi-Fi ルーターを使う方式と、Pi 自身を AP にする方式を比較した。
- 結果(stated): Pi を AP にすると、8 台目あたりで不安定になった。ルーターを使う方式に戻し、全機の設定を完了した。
- 毎年の形: 講義は毎年行われ、2025 年(#765)と 2026 年(#976、open)に続く。
- guide での用途: 国際・公共セクターの実務者の経路(onboarding)に、研修という接点の実例を示す。

# /traces/issue-920-mapterhorn-imagery-japan
- status: stated
- リンク: https://github.com/UNopenGIS/7/issues/920 (closed 2026-08-25、priority/SHOULD、コメント 22、確認 2026-11-11)
- 起点: 外部プロジェクト(mapterhorn)の Issue(mapterhorn/mapterhorn#266)で歓迎された貢献。
- 内容(stated): 国土地理院のシームレス写真を z2〜z18 まで取得し、PMTiles 化して再配布した。合計 1,935,326 枚(z2–z15 の時点)。z18 は約 400 GB と見積もられ、先に z18.pmtiles を用意する方針に変わった。torrent と Source Cooperative の両方でホストした。公開元への大量アクセスを減らすことが、再配布の理由として明記されている。
- 役割分担: 取得と変換を行う contributor と、ホスティングを整える contributor が、同じスレッドで進捗率を共有した。
- guide での用途: 外部プロジェクトへの貢献と、公開リソースへの配慮の実例。

# /traces/issue-254-unifil-gis
- status: stated(個人情報を除いて要約)
- リンク: https://github.com/UNopenGIS/7/issues/254 (closed 2023-08-27、priority/MUST、request for comments、コメント 約 10、確認 2026-11-11)
- 内容(stated): 国連ミッションの GIS 担当との対話を、候補時刻の相談、参加者の事前メモ、議事録、次回の予定、扱う言語カテゴリの検討までを、1 つのスレッドで記録した。大規模言語モデルを使うパイロットの可能性が議題だった。
- guide での用途: 組織外の相手との対話も、公開記録の連鎖(問い、メモ、議事録、次の一歩)で進める例。個人名や所属は guide に書かない。

# /traces/issue-361-global-elevation-tiles
- status: stated
- リンク: https://github.com/UNopenGIS/7/issues/361 (closed 2024-05-02、priority/MUST、コメント 11、確認 2026-11-11)
- 問い: オープンな全球標高タイルを PMTiles で用意し、IPFS でも配れるか。
- 経緯(stated): 他の contributor の記事(NASADEM からの標高タイルの作り方、大規模・小規模)を足場にし、同じ contributor が手元のバックアップからのパッケージ提供を申し出た。試験サイトのリポジトリを作り、高ズームの合成スクリプトを公開し、地球を西から回って進捗を画像で記録した。
- 動機(stated): 別の Issue(#359、デジタルツイン)で良い地形が必要になり、優先度を上げた。
- 派生: 同じ流れが後の `gel.pmtiles`(#747)や、Mapterhorn 系の作業(#920)につながる。
- guide での用途: 「他者の公開記事を足場にして、成果物を公開し、進捗を画像で残す」連鎖の実例。IPFS・Bazaar 主題(24 件、2023-03〜2024-05)の代表。

# /traces/issue-936-staccato
- status: stated
- リンク: https://github.com/UNopenGIS/7/issues/936 (closed 2026-07-15、priority/MAY、information、コメント 9、確認 2026-11-11)
- 問い: 企業環境の生成 AI が Web 地図を直接使えないとき、地図の意図をどう受け渡すか。
- 提案(stated): 二段階の構成。企業内の「Staff」AI が利用者の問いを自然文の依頼にし、インターネット側の「Cartographer」が地図を作る。両者の間に、参照用の「Library」(Martin によるカタログ)を置く。ADR(設計判断の記録)形式で書かれ、状態は「提案中」。
- 進展(stated): 設計文書のリポジトリを作成。Library の第一実装で、空のカタログを配り続ける致命的バグを修正し、候補 12,603 件の生データを、迷わないようにキュレーションする方針を立てた。User → Staff → Cartographer が end-to-end で動いたと報告。「アグリゲーターは不要」という設計判断も記録した。
- 終結: 「概念として定着した」としてクローズ。
- 関連: #995(dwg5 との協働)、#997、#1011。
- guide での用途: AI を使う人の経路(AI Builder)の実例。設計判断を ADR とスレッド内の進捗報告で公開する方法。

# /traces/issue-443-geoai-collaboration
- status: stated(個人名と所属は除外)
- リンク: https://github.com/UNopenGIS/7/issues/443 (closed 2024-05-27、priority/SHOULD、request for comments、コメント 11、確認 2026-11-11)
- 内容(stated): ある contributor の AI ハッカソン受賞(GPU クラウドの一定期間の利用権が賞品)を起点に、dwg5(GeoAI)との窓口を探し、連絡チャネルへの参加を段取りし、翌週には Smart Maps の周辺で扱う言語を尋ねる依頼につながった。
- guide での用途: dwg5 との接点の始まりの記録(2024-04)。窓口の作り方(既存の参加者に依頼し、活動の履歴で招待元を確認する)の実例。個人名や所属は guide に書かない。

# /traces/issue-857-hot-task
- status: stated
- リンク: https://github.com/UNopenGIS/7/issues/857 (open、priority/MAY、コメント 7、確認 2026-11-11)
- 問い: 地図作成タスクの進行を、外部(HOT Tasking Manager)の公開データでどう観察できるか。
- 方法(stated): 静かにコメントを集める場として Issue を使い、監視用のデータとサイトを作り、2 時点(2026-02-10 と 2026-02-22)を色分けして重ねた。参加を促す時期を別 Issue で合意した。
- 結果(stated): 2026-04-27 時点で、対象範囲の「地図作成」は 94% 完了、「検証」は 3 月末で 20%、4/24 で 35%。2026-05-20 に、全タスクが「地図作成完了」になったことを確認した。次の段階は「検証」の完了。
- 勧め(stated): 隅の小さい区画から試す。全体のグリッドはベンチマークの可能性がある。
- guide での用途: 観察と小さな参加の実例。`docs/onboarding-paths.md`(Documentation, Data, or Community Contributor)の最初の一歩。同系統: #867、#873(open)。

# /traces/issue-625-foss4g-2025
- status: stated
- リンク: https://github.com/UNopenGIS/7/issues/625 (closed 2025-11-25、event、priority/MUST、コメント 6、確認 2026-11-11)
- 内容(stated): 国際会議(FOSS4G 2025、オークランド)への参加を、提出、発表予定、スライドの公開、参加後の感想の置き場(別 Issue #825)という順で記録した。2023 年の前回(#47、#191)でも、投稿から準備までを Issue で進めた。
- guide での用途: 外部への発信が、公開記録の延長として行われる実例。FOSS4G 主題(30 件、2022-10〜2026-06)の代表。

# /traces/issue-999-stars-martin
- status: stated(#934 と #999 の読解)
- リンク: https://github.com/UNopenGIS/7/issues/934 (Martin の Web UI を有効化、closed 2026-06-19)、https://github.com/UNopenGIS/7/issues/999 (closed 2026-09-10、priority/SHOULD、確認 2026-11-11)
- 現在の配信構成(stated): Martin の独自配信サーバー「stars」でタイルを配信し、大容量の PMTiles(768 GB と 425 GB)の配信元を Source Cooperative に集約した。切り替え前に、ローカルファイルを一時退避してタイル取得を確認し、バイト単位の一致(ハッシュ)を確認し、1 週間コメントを待った。結果として、ローカルの使用率が 76% から 13% に下がった。利用者側の TileJSON URL とスタイル定義は変わらなかった。
- 論理(stated): 公開性の高い配信元(Source Cooperative)を正本にし、Martin のインスタンスが配信を受け持つ。#642 の high orbit / low orbit の構成が、運用に定着した形。
- guide での用途: 運用の実例。変更前の検証、コメント期間、利用者への影響なしの確認という手順。

# /lessons/dormant-themes
- status: verified(人の確認: 2026-11-11 の指示)+ derived(JSON の件数による)
- IPFS と Bazaar(題に ipfs または bazaar を含む 24 件、2023-03〜2024-05、最後の題は 2024-05-05)は、活動が止まった主題である。2025 年以降に本文やコメントで IPFS に触れる Issue は 2 件(#889、#765)にとどまる。
- 後継(人の確認): Martin のインスタンス(stars など)、Source Cooperative、GitHub Pages。
- 書き方の規則: guide は IPFS・Bazaar を現在の活動として書かず、経緯として書く。「2023–2024 に試され、配信は Martin、Source Cooperative、GitHub Pages に移った」と日付つきで書く。
- 一般化: 止まった主題は、後継と移行の理由を記録する。これも踏み跡の一部である。
- 他の主題の状態(derived): UNVT/Smart Maps Portable は、#567 が 2024-10 に停止したが、UNVT Portable の系は継続中(2026-11-10 の記事、`/lessons/lineage-qiita-unvt`)。UNIFIL は最後の題が 2025-02。活動中かどうかは、本文の確認と人の確認を経て記す(`open`)。

# /lessons/lineage
- status: derived(Issue と Qiita 記事 208 件の索引・抜粋による。確認 2026-11-11。人の確認は未了)
- 内部メモ。guide には載せない。
- 出典: Qiita の公開記事(API v2 の取得): ubukawa のアカウント(T-ubu)120 件(2021-11〜)、k96mz 88 件(2024-04〜)。記事の主題は、ubukawa が vectortile 57%・unvt 47%・MapLibre 24%、k96mz が unvt 72%・vectortile 51%・Node.js 25%。索引は `miso/scripts/qiita_index.py`。
- 系譜 1(2018〜): UN Vector Tile Toolkit(unvt)。ubukawa の 2022-04 の記事は、unvt を「2018 年に hfu が立ち上げ、UN Open GIS Initiative の活動の一つ」と述べ、ツールを「生産・スタイル・ホスト・最適化・消費」の 5 段階で整理している(stated)。この 5 段階で、実務者が一段ずつ記事を書く習慣があった。
- 系譜 2(2021〜2022): 小型機での配信。Raspberry Pi 上のベクトルタイルサーバー(2021-12、2022-12)。mbtiles を Node.js/Express で配る。持ち出す(portable)という発想がここで始まる。
- 系譜 3(2022): 標高と点群。小縮尺の RGB 標高タイル(2022-05)、NASADEM の取得(2022-10)、点群から voxel タイル(2022-08/09)。後の全球標高タイル(#361、2023-12〜)の下地。
- 系譜 4(2023-01〜): PMTiles。tippecanoe の PMTiles 対応(2022-12 末)から数日で、unvt/nanban を使う作成手順の記事が出た(2023-01-07)。同月に Issue #50「PMTilesについての考察」が立つ。
- 系譜 5(2023〜2024): IPFS と Bazaar、Smart Maps Portable、研修用の Raspberry Pi 16 台(#575)。配信を「持ち運ぶ」「分散する」方向。
- 系譜 6(2024〜): 学びの連鎖。k96mz の記事(2024-08)は、ubukawa の演習記事とリポジトリ(charites-init)を使った練習の記録である。先行者の記事を足場に、後続が自分の環境で再現して記録する。これは `/lessons/recurring-logic` のパターン 9(足場にして始める)の人づてのかたち。
- 系譜 7(2025〜2026): Martin、Source Cooperative、GitHub Pages への配信の移行(#642、#999)、PMTiles を使う produce 系ツールの更新(k96mz、2026-03/04/10)、AI と GeoAI(#936 ほか)。
- 発展の論理(derived): 作る → 持ち出す → 分散する → 正本を公開して Martin で配る、と進んだ。各段階で「何が配信のボトルネックか」という問いが変わり、解は前の段階の成果(PMTiles、Raspberry Pi)を使い続けた。
- 初期の経緯(`/lessons/lineage-qiita-unvt` で一部補った): unvt の公開は 2018 年。2021 年にコミュニティの記事が増えた。立ち上げ時の動機は未確認(`open`)。UN Open GIS Initiative 全体との関係も未確認。
- guide での用途: なし(内部の理解のため)。ただし `docs/good-first-experiments.md` の題材は、この系譜の「手を動かせる地点」から選んだ。

# /traces/issue-740-coordinate-transformation
- status: stated
- リンク: https://github.com/UNopenGIS/7/issues/740 (open、priority/MAY、コメント 1、確認 2026-11-11)
- 問い: 日本の座標変換パラメータ(tky2jgd.par)や、他国(ヨルダン)の変換パラメータを、オープンソースが使える形式に変換できるか。
- 計画(stated、本文): 6 段階。(1)パラメータファイルの構造と内容を調べる。(2)NTv2 形式を調べる。(3)対応するオープンソース(PROJ、GDAL)を特定する。(4)変換ツールを探すか作る。(5)変換して、対象ソフトで試す。(6)データ入手の状況に応じて優先順位を調整する(ヨルダンの方が先に入手できれば優先する)。
- 更新(stated、2026-09-10 のコメント): POS2JGD を既存のオープンソースに接続するなら、短期は PROJ の general grid shift 用 GeoTIFF、長期は変形モデルが妥当と整理した。手順は、par → tif → `+proj=gridshift`。PROJ が水平グリッドで GeoTIFF、CTable2、NTv2 を扱うことが前提。
- 状態: open。2026-09-10 の更新後、実装の報告はない(2026-11-11 時点、`open`)。
- guide での用途: Student or Researcher の道の最初の一歩(研究課題として読める open の問い)。

# /traces/issue-1014-ferspas-semantic-search
- status: stated
- リンク: https://github.com/UNopenGIS/7/issues/1014 (open、priority/SHOULD、コメント 0、本文 327 字、確認 2026-11-11)
- 内容(stated): FAO FERSPAS の 1,921 件のコレクションに、全文検索と意味検索ができるページを公開した。全文検索は元から FAO のサイトにあり、意味検索が新規要素。ソースコードは準備中(2026-09-21)。
- 確認(2026-11-11): ページ(`stac.yuiseki.net/fao-ferspas/search/`)は応答 200。
- guide での用途: AI Builder の道の最初の一歩(利用して、問いと結果を記録する)。

# /lessons/lineage-qiita-unvt
- status: stated(記事の本文の記述)+ derived。確認 2026-11-11。読了: 12 本(ubukawa 8 本、k96mz 6 本の導入と結び)。
- 内部メモ。guide には載せない。
- 記事の実践(stated): ubukawa は 2021 年末のベクトルタイルのアドベントカレンダーに、生産・ホスト・最適化・消費と、分野を変えて記事を寄せたと書く(2021-12-08)。unvt の道具を「非公式のカタログ」として紹介する(2022-04)。2021-10-22 に UNVT Storytelling Workshop が開かれた(2021-11-07 の記事)。
- 企業環境との接続(stated): ubukawa の記事は、ArcGIS Online など企業環境で、外部のベクトルタイルを使う方法を 2021-11 から追った。GitHub Pages に置いた静的タイルを ArcGIS Online で使う(2021-11-28)、認証(Azure AD)の試行(2021-12-17、開発環境のみ)、国土地理院が 2022-03-28 に公開した ArcGIS REST API 実装ツール(unvt/itoma)の検証(2022-04)。k96mz は 2025-01 に、この系の記事を自分の環境で再現した。
- 持ち出しの原型(stated): ubukawa は 2022-11 に、インターネットなしの Wi-Fi アクセスポイントとして Raspberry Pi を使う実験を記録し、「地図サーバー作成に一歩近づいた」と結んだ(2022-11-28)。2024 の Issue(#567、#575)で、Pi を AP にした場合の不安定さが記録されたこととつながる。
- 標高データの年(stated): 2022-05 に MapLibre GL JS が Terrain 3D に対応した後、1 年間に使った無料の標高データ 4 種を、解像度・範囲・登録の要否・注意点の表にまとめた(2022-12-12)。
- 運用の学び(stated): k96mz の記事は、運用中の `produce-gsc-small`(国連データと OSM データから、ズームレベル 0〜5 のタイルを作るコード)を読み解く(2024-10)。国連の Clear Map のタイル構造を、charites でレイヤに分解して観察した(2024-09)。
- 配信の移行(stated): 2026-04 の記事で、k96mz は unvt のタイル配信(coesite4)を MBTiles から PMTiles に移す計画を「今後の展開を考えて」と書く。認証と取得制限を持つため、まず範囲取得(Range Request)を使わない方式で実装した。2026-10 に charites で PMTiles を使い、2026-11-05 にスタイルファイルとともにホストする方法を記した。
- Portable は続いている(stated、訂正): k96mz は 2026-11-10 に「Raspberry Pi 5 の設定 (UNVT Portable)」を書いた。#567 は停止したが、UNVT Portable の系は現在も続く。`/lessons/dormant-themes` の他主題の記述は、この点で補う。
- 学びの文化(derived): 記事の「謝辞」と「参考にしたページ」の節で、先行者への言及が習慣になっている。k96mz は ubukawa の演習の記事とリポジトリを使って練習する。後続が先行の作業を再現し、結果を自分の環境の条件つきで記録する。
- 未精読: 各主題の残りの記事の本文(約 150 本)。主題ごとの精読は `/lessons/lineage-qiita-*` に記録済み(unvt、日本のデータ、標高と引き継ぎ)。

# /traces/un-system-contacts
- status: stated(Issue の題と本文による。確認 2026-11-11。人の確認は未了)
- 内部メモ。guide には載せない。個人名は役割に置き換えた。件数は Issue の題・本文・コメントでの語の出現による(derived)。
- 接点の経路(窓口)は、記録から次の 7 種に分けられる。
  1. **UN Open GIS Initiative の月例会議(VTC)。** 題に `UN Open GIS Monthly` を含む Issue が 2022-12 から 2026-08 まで続く(#46 2022-12-21、#101、#140、#170、#213、#230、#281、#430、#483、#520、#566、#650、#741、#764、#797、#975 2026-08-19 ほか、計 18 件)。報告の場として使われ、2022-12 には「UN EC ハッカソンの成果を月例で報告する」(#42)ことが予定された。
  2. **国連の Microsoft Teams のチャット。** UNIFIL の GIS 担当との最初の対話の招待文に、Teams のチャットで話が始まったことが書かれている(#254、2023-08-24)。dwg5 との連絡も Teams の部屋で始まった(#443、2024-04)。
  3. **UN-GGIM と国連地理空間ネットワーク。** 2023-08 に、One UN Geospatial Situation Room の概念資料を読んで協働の可能性を整理した(#227)。災害に関する作業部会へシナリオ演習の概念(to-go)を提案した(#257、2023-08、同時期に一人がタスクグループの責任者)。UN-GGIM-AP の事務局が UN Smart Maps サイトへのリンクを設けた(#268、2023-09-07)。UN-GGIM 第 15 会期の資料を NotebookLM で分析した(#751、2025-07)。
  4. **国連グローバル・サービス・センター(UNGSC)。** 題に現れるのは、訪問予定(#682、2025-04 起票、2025-06-25 予定、主目的は UNVT Portable の実装評価、2025-07-15 に閉じた)。題に UNGSC などを含まない言及は 2022-11 から 2026-05 まで 28 件ある。
  5. **国連の会議・ウェビナー。** UN Mappers のウェビナー(#401、2024-02)、UN Maps Conference(#468、2024-05-20/24、2 名が遠隔参加)、UN 2.0 Week(#719、2025-06)、UN Mappers Mappy Hour(#726 2025-06-27、#748 2025-07-25)。
  6. **機関の公開プラットフォームと募集。** UNDP GeoHub(PMTiles を登録する方法の検討 #713 2025-05、OSM の JICA 事務所抽出を GeoHub に #714 2025-05)、UNDP Digital X Catalogue(応募 #860 2026-02、掲載案を受領 2026-02-19、関連 #890 2026-04)。
  7. **担当者とのオンライン会議。** FAO CSI(FERSPAS)との会議(#1006 2026-09-18)と FAO での TechTalk(#994 2026-09-28)。ミッションの GIS 担当との 30 分の Teams チャット(#982、2026-09-12 21:00 JST、Raspberry Pi の利用について)。
- 機関別の時系列(stated)
  - **UNIFIL(2023-08〜2024-02)。** #250(2023-08-18、DRC とレバノンの LLM パイロットの戦略: 基本語彙として誤情報・偽情報・憎悪表現を確認)。#254(2023-08-25 17:00 JST の最初の対話、議事録つき、同じ週に再会予定)。#255(傘 Issue、2023-08-25)。#256〜#264(2023-08-25〜29、原則案、言語カテゴリ、典型的プロンプト、対象地域、想定利用者、「地図を出さない」案)。#285(2023-10、会議の再調整。東京とベイルートの時差と昼休みを考慮して日本時間 20〜22 時を提案。2024-02-27 に閉じた)。#274(2023-09、Issue の整理)。最後の UNIFIL 言及は 2024-01。
  - **FAO(2023-01〜2026-09)。** 2026-09 に集中する: #994(2026-09-28 16:30 JST、FAO CSI での TechTalk「Geospatial Access for AI Assistants」。Staccato の話)。#997(FERSPAS と Staccato Library の統合、2026-09-03)。#1006(2026-09-18 16:30 JST、FAO CSI との FERSPAS 協働の会議。dwg7 側が初期検討結果を共有する予定)。#1011(HTML デモ、2026-09-18)。#1013(ferspas-udf、open)。#1014(FERSPAS semantic search、1,921 件のコレクションの意味検索、open)。#995 は dwg5 との協働をまとめる傘で、FERSPAS を含む。
  - **UNDP(2025-05〜2026-04)。** GeoHub への PMTiles 登録(#713: tilestats を PMTiles に埋め込む必要があり、公開済みファイルで成功)。OSM の JICA 事務所抽出(#714)。Digital X Catalogue(#860: 応募名「Smart Maps for Development」、2026-02-19 に掲載案を受領)。
  - **dwg5(GeoAI)(2024-04〜2026-09)。** #443(2024-04、Teams の部屋への参加の段取り)、#932・#995(2026)、#994(2026-09)。
  - **ミッションの GIS 担当(2026-08〜11)。** #979(2026-08-25、Raspberry Pi の接続について、週末の 30 分の会議を設定する計画)、#982(2026-09-12 21:00 JST、ジュバ側 14:00 の会議の段取り)。#1027 のコメント(2026-11-11): 国連 PKO のミッション(UNMISS)の各サイト周辺の通信速度を公開データで調査した。通信は可能だが速度にムラがあり、100 MB の PMTiles のダウンロードに 30 分かかる地域もある、と述べる。データには偏りがあると前提を明記。
  - **その他(情報共有)。** UNHCR の GIS コアデータベースの書き出しツール(#358、2023-12)、世界銀行の City Planning Labs の調査(#526、2024-06)、DRC とレバノンの LLM パイロット(#250)。UNMISS の旧称的な言及(2022-12〜2023)は模擬国連の演習シナリオ(MUNDO)に由来する可能性が高く、実際の接触とは確認できない(`open`)。
  - **国との二国間・研修(参考)。** ブータンの来訪者のための国別研修の一環としての講義(#305、2023-12-13): 「NSDI の実装に向けた能力構築に UN Smart Maps Group は何ができるか」という質問を受け、技術指向のグループであることを踏まえて技術指向のワークショップを返答の方向にした(stated)。
- 学び(stated): #304(2023-12-12)の振り返りで、「提示した内容がやや技術的に難しすぎる。細部を省略して議論可能な内容にする必要がある」「オープンな Web 地図を運営している組織は圧倒的に少数」と記録された。
- 未確認(`open`): 各接触の発端(誰が誰に連絡したか)の多くは、Issue 外(Teams、メール)にある。実際に面会・会議が行われたかの確認は、Issue の議事録の有無による。UNGSC 訪問(#682)の実施内容。

# /traces/meetings-timeline
- status: stated(題の日付と、ラベル `event` の Issue による。確認 2026-11-11)
- 注: 題の日付は予定または実施。Issue が closed でも、実施の確認は本文・コメントによる。
- 2022: FOSS4G Thailand 2022 の基調講演準備(#2)、State of the Map Asia での UNVT Portable 発表準備(#6)、ジブチの同僚向け動画(#7)。
- 2023: ベース・レジストリ利活用研究会(#91、03-13)。FOSS4G 2023 コミュニティ審査(#95)。FOSS4G 2023 プリズレンの UNVT Portable ワークショップ(#112)、発表「Smart Maps for the UN and for All」(#184、06-29)。FOSS4G Asia 2023(#284)。地理情報システム学会での話題提供(#293)。国土地理院での講義の連続(2023-11-29 に #297〜#301、12-01 に #300)。研修の講義(#302 12-07 タイル配信、#303 12-11 OSM、#304 12-12 UN Open GIS Initiative、#305 12-13 ブータン)。
- 2024: 紛争評価の地理空間技術に関する国際ワークショップ(#372、02-19)。OpenGeoCommunity シンポジウム(#373、02-20)。ジオ展(#375、04-19)。人道マッパソン(#385、04-24/26)。UN Maps Conference(#468、05-20/24)。Understanding Risk Global Forum 姫路(#381、06-16/21)。ISPRS TC IV 基調講演(#594、10-24)。FOSS4G Perth(#604、10-23)。FOSS4G Belém(#386、12-01/08)。FOSS4G-Asia Bangkok(#387、12-15/18)。
- 2025: NLP2025 チュートリアル(#621、03-10)。UN 2.0 Week(#719、06-09/13)。UNGSC 訪問(#682、06-25)。ティモール・レステのワークショップ(#732、06-26、CNDG と JICA 主催、スライド公開、2025-06-26 に終了を記録)。UN Mappers Mappy Hour(#726、#748)。FOSS4G 2025 オークランド(#625、11 月)。
- 2026: FOSS4G-Asia 2026(#689、01-22/27)。CNG Japan 2026(#928、08-24)。UN Open GIS Featured Presentation「Staccato」(#961、08-19、実施完了を 08-25 に記録)。FOSS4G 2026 ワークショップ(#947、08-31)。放送の状況認識に関する発表(#962、09-16)。FAO CSI との会議(#1006、09-18)と TechTalk(#994、09-28)。
- 定例: 週次ミートアップ(`meetup`、2022 から 277 件)。月例(UN Open GIS Monthly、2022-12〜2026-08 に確認できる 18 件の題)。

# /traces/jica-training-timeline
- status: stated(題と本文による。確認 2026-11-11)
- 背景(stated、#976): 国土地理院は JICA の課題別研修(測量・地図作成)を長年実施している。海外の政府機関の技術者が対象。1959 年から続き、受入実績は 1000 名超(国土地理院の国際協力ページの記述として引用されている)。dwg7 は、その一部の講義を担当する。
- 2022: #12(2022-10-29 起票)。UNVT Portable による研修の支援。2022-11-02 に Web 地図の演習、2022-12 に UN Open GIS Initiative の講義。実施の記録は 2022-12-08。
- 2023: #243(2023-08-15)。既存の資源と権限を活用した 12 月のつくばでのワークショップの計画。内部の検討資料を作り、共有した。講義の予定: 12-07 タイル配信、12-11 OSM、12-12 UN Open GIS Initiative(#302〜#304)。12-13 はブータンの来訪者のための国別研修(#305)。
- 2024: #552(2024-07)で Smart Maps Portable の研修利用を計画し、#575(2024-08-18〜11-26)に統合した。研修員 1 人に 1 台を渡す形を想定し、Raspberry Pi 16 台を 1 ロットにして準備した。会場が遠いため、リモートから準備し、会場に移設した。#505(2024-06)は JICA と OpenStreetMap のウガンダの情報。
- 2025: #704(2025-05)で、JICA の Co-creation, Innovation, and Circulation Initiative として Quick Mapping Project が採択され、dwg7 の資源提供という形で準備を始めた。do-ocracy の分散型の進め方は dwg7 と同じと記す。#714(2025-05、OSM の JICA 事務所抽出を UNDP GeoHub に)、#724(パンフレット)、#729(JICA の Q Day 1、2025-07、日程変更あり)、#732(ティモール・レステ、2025-06-26)。#765(2025-08〜12): 研修の日程。2025-11-10 AM 国土地理院の Web 提供技術、PM 国連オープン GIS イニシアティブ、11-13 Web 提供技術、12-18 OpenStreetMap。研修用 UNVT Portable は設定済みで、接続情報を講義資料に入れた。#824(2025-11): JICA QMP シエラレオネを支える高解像度 WebP Terrarium PMTiles の開発。
- 2026: #976(2026-08-12 起票、open)。講義日は 2026-11-25、11-26、12-14。#1010(2026-09-18 起票、open): 11-25 13:00〜16:30 の「国連オープン GIS イニシアティブ」を、概念編(13:00)、Unix 編(14:15)、Initiative 編(15:30)の 3 部にする案。伝えたいことは「自分で技術を使い、その実践を他者とつなぎ、公務へ持ち帰るという働き方がある」(stated)。
- 流れ(derived): 2022 は機材と演習の支援、2023 は講義の連続と国別研修、2024 は 1 人 1 台の機材の準備(#575)、2025 は Quick Mapping Project と研修日程の統合、2026 は講義を概念・実技・Initiative の 3 部に構成。毎年、研修の準備の知見が、次の年の Portable と配信構成に反映された(#567 → #575 → #765)。
- guide での用途: `docs/onboarding-paths.md` の International and Public-Sector Practitioner の道に、研修という接点の実例(#575、#976、#1010)。個人名と所属の詳細は guide に書かない。

# /lessons/lineage-genai
- status: derived(Issue の題・本文・コメントの検索と、代表スレッドの読解による。確認 2026-11-11。人の確認は未了)
- 内部メモ。guide には載せない。
- 件数(Issue の本文・コメントに語が現れるスレッド数、年別): ChatGPT/GPT/OpenAI 76(2023: 37、2024: 15、2025: 13、2026: 11)、LLM 74(28/28/7/11)、生成 AI 64(5/18/19/22)、GeoAI 43(14/12/6/11)、Copilot 41(3/5/19/14)、agent/エージェント 55(11/7/11/26)、Claude 37(2025: 10、2026: 27)、MCP 7(2025: 6、2026: 1)、Gemini 11。最初の出現: LLM 2023-02-28、ChatGPT 2023-03-09、Copilot 2023-05-26、Gemini 2024-05-07、Claude と MCP 2025-01-21。
- 段階 1(2023-02〜05): 関心の芽。自然言語処理の学会参加の報告(#85)。hfu は、自然言語と地理空間の組合せは地名・住所のジオコーディングが主流で有償サービスになりやすい、と整理した(stated)。ベクトルタイルから説明文を生成する案(#103)と、自然言語からスタイルを生成する案(#104)が 2023-03 に出た。#103 は 2024-01 に「まだ着手できていない」と記録されて閉じた。
- 段階 2(2023-04〜05): ChatGPT を道具として使う。dwg7 の戦略を ChatGPT に尋ねたプロンプトと回答の共有(#118)。国連向けの対話型文書探索システム TRIDENT が「GeoAI」になったと報告(#141、2023-05)。MUNDO(模擬国連)を「Smart Maps Assistant」に改名する提案(#163)。
- 段階 3(2023-08〜11): 文脈を渡す。「Smart Maps Group 標準の背景プロンプト」(#228、2023-08〜11)。英語の草案のあと、日本語版が出て、hfu が「使っている」と報告した。ミッションの GIS 担当との対話(#254)と、LLM パイロットの戦略(#250)、典型的なプロンプトの例示(#259)。TRIDENT Agent の更新で、モデルを text-davinci-003 から gpt-3.5-turbo に切り替えると指示への従順さが下がり、性能低下が確認された(#314、stated)。
- 段階 4(2024): ローカルとオープン。ollama でインターネットなしの代替(#415)、国内機関の取り組みの紹介(#432)、タイ GISTDA の事例(#446)、FOSS4G 向けの指示データセット(#451)、Discord ボット(#472、#485)。AI ハッカソン受賞を機に dwg5 との窓口を作った(#443)。2024-11、システム全体がオープンソースであることを理由に、OSAID(オープンソース AI 定義)に適合し、llama.cpp や ollama で動く基盤モデルが必要と整理(#631)。自作のモデル系列が厳密には適合しないと判明した点も同じスレッドで記録された(stated)。#631 は 2026-07 に閉じた。
- 段階 5(2025): 企業環境の制約と自律エージェント。Geo-Voyager(自律エージェント、#639)、空間知能の調査(#721)、planetiler-ai(惑星規模のカスタム地図を作る AI エージェントの概念実証、#743)。Microsoft Copilot に Web 地図を調整させる(#775、2025-09〜11): 地図の知識を持たない人が、1 ファイルの HTML を Copilot に渡して自然言語で編集する、というニーズが出発点。
- 段階 6(2026): 設計の言語化。AI エージェント向けの CLI(osmcli、#855)、エージェントが計算資源を要求できる環境(NEREID、#865)。「サイト生成プロンプト」の育成(#869、2026-02〜05)。GIS の agent harness design への再定義(#902、2026-05): AI に自由に地図を作らせるのではなく、データ、タイルスキーマ、スタイル、ビルド、検証、プレビューを、型のあるワークフロー、検証器、サンドボックス、フィードバックループとして設計する(stated)。プロンプトに書くのは「サイトの構造」ではなく「サイトの問い」(#927)。Staccato(#936、2026-06〜07)と UN Open GIS での招待発表(#961、2026-08-19)。Staff ロールのプロンプトの実験(#983)。
- 発展の論理(derived): (1)聞く → (2)文脈を渡す(背景プロンプト) → (3)エージェントにする → (4)オープンな基盤を求める → (5)企業環境の制約に気づく → (6)制約を設計に変える(Staff と Cartographer の分離、harness、問いをプロンプトにする)。各段階の学びは、同じ Issue の中で訂正として記録された(モデル切替後の性能低下、OSAID 適合の再確認)。
- miso との接続(derived): #228 の背景プロンプトは、「作業文脈を毎回渡す」発想の源流の一つである。miso(旧称 kcaim)は、これを 1 つの Markdown ファイルに収める方法として発展した(`dwg7/miso` の CONCEPT)。
- guide での用途: なし(内部の理解のため)。`docs/field-guide.md` の AI の項(Q19)を更新するときの根拠。

# /lessons/lineage-qiita-japan-data
- status: stated + derived(ubukawa の記事 24 本の題と 5 本の導入による。確認 2026-11-11。人の確認は未了)
- 内部メモ。guide には載せない。
- 主題(stated): 日本の公開地図データを、ベクトルタイルにして使えるようにする実務の記録。対象は、法務省の登記所備付地図(地図 XML、G 空間情報センターが 2022 年度から公開)、e-Stat の小地域(町丁・字等)と人口集中地区、不動産情報ライブラリのタイル、国土数値情報の地価公示。期間は 2023-05〜2025-07。
- 手順の型(stated): ダウンロード(Windows PowerShell、G 空間情報センターの API)→ 変換(GDAL、のちに mojxml-rs)→ ベクトルタイル化(tippecanoe、PMTiles)→ 重ね合わせ(MapLibre、国土地理院のベクトルタイル)。2025-05 の記事は、変換に新しいプログラムを使って「昨年よりずいぶん早くなった」と記す。
- データ品質の実務(stated、再現可能な分析): 各年度のパッケージ数を数えた(2022 年度 2,070、2023 年度 2,005、2024 年度 2,010 ファイル。2025 年度は 2,006)。公共座標系と任意座標系の割合を市区町村別に数え(R)、都道府県ごとの投影法を調べた(2024-02)。地番リストの新旧比較で変化を見つけ、筆界未定地を抽出した(2024-07、2024-12)。位置がずれた区画を見つけ、QGIS で直す方法を試した(2025-06、2025-07)。ファイル名の重複と文字化けの注意を記した(2024-06)。リストは公開リポジトリに置かれた。
- 学びの型(derived): 毎年同じ手順を記事にし、数え方を変えずに年度を比べる。ここに「条件を添えた数値」と「訂正の可視化」の習慣が、個人の記事でも同じ形で現れる。
- dwg7 の Issue との接続(derived): 2024 年度版の PMTiles が公開ホスティング(Source Cooperative)に置かれ(`MojMap_amx_2024.pmtiles`、#713)、UNDP GeoHub への登録の試験に使われた。海外の事例として、タイの地籍データを扱う作業(#695、2025-04、測地系の変換に苦労し見通しがついたと記録)が、関連プロジェクト(amx)の Issue を参照して始まった。
- guide での用途: `docs/onboarding-paths.md` の Geospatial Practitioner の道と、`docs/good-first-experiments.md` の「データの品質を数える」実験の題材候補(件数を年度間で比べる)。記事は日本語であり、リンクと要約にとどめる。
- 未確認(`open`): amx プロジェクトと dwg7 の組織上の関係(Issue と記事からは、同じ contributor が両方で作業していることだけが分かる)。

# /lessons/lineage-qiita-elevation-and-handover
- status: stated + derived(ubukawa の標高・点群・衛星画像の 25 本と、k96mz の Node.js 学習ノート 28 本の題と抜粋による。確認 2026-11-11)
- 内部メモ。guide には載せない。
- 標高・点群・衛星画像(ubukawa、2022-05〜2023-06 と 2025-02): 2022-05 に MapLibre GL JS が Terrain 3D に対応したのを受けて、標高データから RGB 標高タイルを作る記事が続いた(地球地図、AW3D30、SRTM、NASADEM。2022-05〜10)。標高データの一括ダウンロードの記事(2022-07、2022-10)。点群(OpenDroneMap)から voxel タイルを作る記事(2022-08/09、pdal と tippecanoe。元データは約 5.5 GB の LAZ)。MODIS と Sentinel-2 から小縮尺ラスタタイルを作る記事(2022-12、2023-01)。初心者向けのダウンロードの記事(2022-10、2025-02)。2022-12-12 のまとめが 4 種の標高データを比べた。
- うまくいかなかった経験の共有(stated): 2022-06-01 の記事は、Terrain 3D でブラウザのメモリ使用量が増えすぎ、「結局、原因はわからなかった」と書き、「上手く行かなかった経験をメモしておく」ことを趣旨とする。2022-09-30 の記事は「今の課題をメモしておく」と、高さのオフセットが合わない現象を観察として書く。原因不明のまま観察を公開する習慣である。dwg7 の Issue で「仮説を持っている」と書き、検証後に更新する習慣(#567)と同じ形。
- 引き継ぎ(stated): k96mz の記事(2024-08〜2026-03)は、Node.js のモジュール(stream、child_process、winston、better-queue、mbtiles、tilebelt、express-session、axios、pg など)と、unvt の運用リポジトリ(onyx 2024-11-13、coesite 2024-12-07、marble 2025-01-29)を、一つずつ「理解する」形で解説する。onyx は複数の MBTiles から配信するルーティング、coesite は Microsoft の認証つき配信(ubukawa の記事によると 2021-04 以前のチュートリアルに基づく)、marble は ArcGIS Online 向けの配信。
- 訂正の可視化(stated): k96mz は 2024-11-13 に、以前の記事のサーバーの選定(CentOS 7)が「不適切だった」と書き、RHEL 8 互換の Rocky Linux 8 で書き直した。旧記事の末尾のエラーの原因かもしれない、とも書く。
- 運用の引き継ぎの型(derived): 先行者のコードを、行ごとに解説し、自分の環境で動かし、記事にする。2026-03 以降は、produce 系の運用コードのリファクタリングに進み、2026-04 には配信を MBTiles から PMTiles に移す計画を述べた(`/lessons/lineage-qiita-unvt`)。引き継ぎは、読む → 再現する → 改良する、の順に進んだ。
- guide での用途: なし(内部の理解のため)。ただし、Onboarding の「学びの連鎖」(先行者の記事を足場にする)の事実の裏づけ。

# /lessons/recurring-logic
- status: derived(上の 6 件の読解から。確認 2026-11-11)
- パターン 1: 条件を付けた主張。機器、版、データ量、負荷が数値の隣に書かれる(#1003、#567)。
- パターン 2: 仮説と検証の分離。「仮説を持っている」と書き、検証後に結論を更新する(#567 の電力不足、#1003 の設定ファイル)。
- パターン 3: 訂正の可視化。取り消し線や、同スレッド内の訂正コメントで残す(#642、#1003)。
- パターン 4: 設計の論理を言語化する。選択の理由を箇条書きで述べる(#642 の high orbit / low orbit、#567 の論点)。
- パターン 5: 再現の招待。コードと手順を公開し、参加者が試して質問する(#642)。
- パターン 6: 未解決を残して閉じる。再開の条件を書く(#567)。
- パターン 7: 外部への配慮。公開元への負荷を減らす設計理由を書く(#920)。
- パターン 8: 設計判断を ADR とスレッド内の進捗報告で公開し、「概念として定着した」と判断してから閉じる(#936)。
- パターン 9: 他者の公開記事や外部プロジェクトの Issue を足場にして始める(#361、#920)。
- パターン 10: 静かな観察の場を作り、2 時点の比較で変化を示す(#857)。
- (パターン 7 の原文)公開元への負荷を減らす設計理由を書く(#920)。
- guide での用途: `docs/dwg7-in-5-minutes.md` の「The method in one chain」と `docs/field-guide.md` の習慣の根拠。

# /inventory/issues-open-2026-11-11
- status: volatile(次の確認で更新する)
- 取り込み状況: 一覧のみ取り込み済み。本文は #1003、#995、#1027、#1029 以外は未取り込み。
- 一覧(番号 / 題 / ラベル):
  - 1029 / a dwg7 guide / waiting/assign, waiting/triage
  - 1028 / Smart Maps Meetup Weekly 2026-11-17 / meetup
  - 1027 / Smart Maps Meetup Weekly 2026-11-10 / meetup
  - 1023 / 5cm オルソ (Waterloo, Sierra Leone) の研究 / priority/MAY
  - 1021 / 100g 超ドローン DJI Mini 4 Pro の半自律飛行によるオルソ画像構築 / information
  - 1016 / Risk Data Library / information
  - 1014 / FERSPAS semantic search / priority/SHOULD
  - 1013 / ferspas-udf / priority/SHOULD
  - 1010 / UN Open GIS Initiative (JICA Knowledge Co-creation Program) 2026-11-25 / priority/MUST
  - 1003 / GeoServer / MapServer on a Raspberry Pi / priority/MUST
  - 995 / 5 + 7: Collaboration of DWG 5 and DWG 7 / priority/SHOULD
  - 976 / JICA 課題別研修 2026 dwg7 関連講義 / priority/MUST
  - 963 / Dutch Portolan Demo / information
  - 952 / sakasa - Japan mirror and distribution experiment for Maperhorn / priority/MUST
  - 891 / Deep-dive into CNG / priority/MUST
  - 873, 867, 857 / HOT Task(ヴィエンチャン、フリータウン東端、Hill Cot) / priority/MAY
  - 830 / CSDI Hong Kong / adopt, priority/MAY
  - 783 / Planetarble / in progress, priority/SHOULD
  - 768 / MapLibre and UN Smart Maps Group: use cases / priority/MAY
  - 740 / Reverse-engineer coordinate transformation / priority/MAY
  - 593 / OpenLandMap / adopt, priority/MAY
  - 580 / Dateno Registry / information
  - 578 / Adopt Geodata incubation / priority/MAY, someday/maybe
- 注: open は 26 件。一覧に現れたのは 25 件で、残り 1 件は 2 ページ目にある(`open`)。

# /inventory/issues-backlog
- status: open
- 全体: 993 件。統計と主題の分類(題ベース)は取り込み済み。本文の読解は 4 件。
- 次に取り込む順序(案):
  1. open 26 件の本文を連鎖(問い → 実験 → 結果 → 訂正 → 未解決)で記録する。
  2. 主題ごとの代表スレッドを読み、`/traces/` に記録する。済み(代表 10 件): #642、#567、#575、#920、#254、#361、#936、#443、#857、#625。全 10 主題で代表スレッドを 1 件ずつ記録した。
  3. 全期間の時系列を `/traces/timeline` に作る。
- 注: 2023 年以前の記録は Objective 構成が異なる可能性がある(`open`)。

# /sources/qiita-contributors
- 取り込み状況: 索引と、unvt・ArcGIS・Portable・標高・PMTiles 系の 12 本の導入と結びを精読。残りの約 190 本は索引のみ。
- URL: https://qiita.com/T-ubu (ubukawa、120 件)、https://qiita.com/k96mz (88 件)
- 取得: 2026-11-11(Qiita API v2、未認証。`miso/source/qiita-*.json`、git 管理外)
- 利用条件: 各記事の著者の著作物。guide では要約と記事へのリンクにとどめ、本文は転載しない。

# /inventory/guide-claims
- status: verified / derived / suggestion の別を主張ごとに付けた台帳。確認 2026-11-11。
- 凡例: `verified` = JSON またはスレッド本文で確認した。`derived` = 件数や中央値など、JSON からの計算。`suggestion` = 記録に根拠がなく、ガイドが勧めると明示した。`partial` = 一部だけ確認した。
- 一括の確認(2026-11-11): 週次の 12:30–12:55 JST の枠は 167 件の題にあり、日付が読める 165 件のうち 164 件が火曜(最初の 2022-11-16 のみ水曜)。#1027 のコメントはすべて、会議開始より前に投稿されていた(derived)。#932 の題は「Seek possibilities for collaboration with DWG 5 -Geo AI」。FERSPAS の検索ページ(#1014 の URL)は応答 200。

## dwg7-in-5-minutes
- dwg7 は UN Open GIS Initiative の Domain Working Group 7、Smart Maps — verified(リポジトリの README と docs/index.md)
- #1003 の連鎖(条件、数値、再現、訂正、次の測定)— verified(スレッド全文)
- 10 の習慣と各リンク(#1003、#567、#642、#936、#920、#361、#857)— verified(各スレッドの該当コメント)
- 週次ミートアップ(火曜 12:30 JST、25 分、事前コメント)— verified。12:30 枠でコメントのある 163 件すべてに、開始前のコメントが 1 件以上あり、開始前の割合の中央値は 3 分の 2(derived)。「合意された順」は #1027 の 1 スレッドによる。ページでは「順に進む」と書き換えた。
- 277 件の meetup と 167 件の 12:30 枠 — derived
- ラベルの閉じるまでの中央値 14・23・32 日 — derived
- 2025〜2026 の新規 Issue の 3 分の 2 が日本語を含む — derived(題と本文の先頭 500 字の判定)
- 現在の構成(PMTiles、Source Cooperative、Martin)— verified(#642、#999)
- 小型機の持ち運び(#567、#575)、Staccato(#936)、dwg5(#995)— verified
- IPFS が 2023〜2024 に試され、配信が移った — derived(題の件数)+ 人の確認(あなたの指示)
- 「国際・公共の地理空間業務は検証可能な主張を必要とする」— suggestion。見出しを「Why this guide reads the method this way」に改め、「このガイドの見方」と明示した。

## onboarding-paths
- #857、#1003、#642、#936、#1014、#575、#254、#976、#361、#740、#1027 の説明 — verified。#740(本文 6 段階の計画と 2026-09-10 の 1 コメント)と #1014(本文 327 字、コメントなし)は全文を読んだ。#1014 の「全文検索は元からあり、意味検索が新規要素」「ソースコードは準備中」は本文の記述。
- #1014 の検索ページが使える — verified(応答 200、2026-11-11)。
- 各道の「小さな貢献」と「1 週間後」— suggestion(このガイドの設計)。冒頭に「このガイドの提案」と明示した。

## good-first-experiments
- 実験 5(206)、9(charites)、10(rio-rgbify)— verified(実機、2026-11-11)。
- 実験 4(sha256sum)— partial(ダウンロードは未確認)。
- 実験 6、7、8 — Status 行で未再現と明記。
- 各実験の元スレッド・記事 — verified(リンクと本文)。

## field-guide
- Q1 閉じた 967 件のうち 919 件にコメント — derived
- Q2 リポジトリの説明 — verified(リポジトリ ページ、WebFetch)
- Q3 外部プロジェクト(#920、#857)— verified
- Q4〜Q14 の各スレッド記述 — verified(#642、#567、#1003、#936、#920、#999、#361、#857)
- Q15 週次ミートアップ — verified + partial(上記)
- Q16 ラベル — derived(定義の文書は未確認)
- Q17 言語 — derived + suggestion(英語の要約コメント)
- Q18 #575 の物流 — verified
- Q19 AI — verified(#936、#1014)+ suggestion(開示と確認)
- Q20 公開の範囲 — suggestion

## monthly-snapshot
- #1003 の作例 — verified(スレッド全文)
- 2026 年 11 月の作例(#1027 の 2026-11-11 のコメント)— verified(コメント全文)。引用レポート本体は未読(partial)。
- 研修講義の日付(#976、#1010)— verified(open Issue)。#1014、#1023 は open — verified。

## 空いている根拠(次の作業)
1. (解消)事前コメントは 163 件で確認した。順の合意は #1027 のみ。
2. (解消)#740 と #1014 は全文を読んだ(`/traces/issue-740-coordinate-transformation`、`/traces/issue-1014-ferspas-semantic-search`)。
3. ラベルの定義文書の有無 — リポジトリの `.github` やラベル説明を確認する(API 権限が必要)。
4. 実験 4・6・7・8 の再現。
5. (解消)見方として明示した。

# /open-questions/guide-claims
- status: open
- guide の Field Guide Q10・Q15・Q17・Q18 は、記録で確認できていない提案である。取り込みを進め、根拠が見つかれば `verified` として書き換え、見つからなければ削除する。
- ラベルの意味は `/lessons/priority-labels` で導いた。定義文書の有無は未確認。
- dwg5 と dwg7 の役割分担は、記録から確認できていない。

# /acceptance-tests/t01-what-is-dwg7
- query: dwg7 とは何か。英語 1 段落で、記録に基づいて答えよ。
- expected: UN Open GIS Initiative の Domain Working Group 7、Smart Maps、公開記録(Issue)を通じて問い・実験・結果・訂正を共有する、という趣旨。
- requires: /sources/unopengis-7-repo, /traces/issue-1003-raspberry-pi, /traces/weekly-meetup
- result: untested

# /acceptance-tests/t02-example-thread
- query: dwg7 の方法を示す実例を 1 つ挙げ、問い・実験・結果・訂正・未解決を条件つきで答えよ。
- expected: #1003 の連鎖。数値は条件と一緒に示す。
- requires: /traces/issue-1003-raspberry-pi
- result: untested

# /acceptance-tests/t03-onboarding-per-path
- query: 地理空間の実務者が最初に読むべき Issue と、最初の小さな貢献は何か。
- expected: 実在の Issue への具体的なリンクと、その Issue に対する 1 つの再現可能な行動。
- requires: /inventory/issues-backlog
- result: untested(実在の Issue の取り込みが必要)

# /acceptance-tests/t04-labels
- query: `priority/MUST` と `priority/SHOULD` は、記録の中でどのように使い分けられているか。
- expected: 実際の Issue 群の使われ方に基づく導出。
- requires: /lessons/priority-labels
- result: partial(閉じるまでの日数から導出済み。定義文書は未確認)

# /acceptance-tests/t05-domain-themes
- query: 過去 12 か月の Issue から、dwg7 の主な主題を 5 つに分類して答えよ。
- expected: 題とラベルに基づく分類と、各主題の代表 Issue。
- requires: /inventory/issues-backlog
- result: untested(2 ページ目以降の取り込みが必要)

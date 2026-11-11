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
- 他の主題の状態(derived): UNVT/Smart Maps Portable は最後の題が 2025-11(#567 は 2024-10 に停止)。UNIFIL は最後の題が 2025-02。活動中かどうかは、本文の確認と人の確認を経て記す(`open`)。

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

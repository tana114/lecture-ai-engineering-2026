# 第6回 解答

## 演習

<!-- [tool call] の行は、表示された行をそのまま貼り付けてください。終わらなかった STEP は、空欄のままでかまいません。 -->

- STEP 1 のツールの名前：glossary_search_glossary
- STEP 2 の [tool call]：glossary_search_glossar({'query': '3 レベル'})
- STEP 3 の [tool call]：[fetch_fetch]
  Fetches a URL from the internet and optionally extracts its contents as markdown.
- STEP 4 の [tool call]：[aws_aws___read_documentation]
  [aws_aws___search_documentation]
  [aws_aws___list_regions]
  [aws_aws___get_regional_availability]
- 気づき・疑問：

## 宿題

<!-- 基礎・実装・発展のどれか1つに取り組めば完了です。 -->

- 取り組んだレベル： 実装 
- やったこと：
  tools.pyに make_quiz(lecture: int) -> str を定義し、該当する回が存在しない場合は、「第{lecture}回の用語集に用語がないため、確認問題を作れません。」という文字を返すシンプルな関数を用意した。
  サーバーへの適用はmcp_server.pyに server.tool()(tools.make_quiz) を1行追加するのみ。
- 結果：

> 第2回の確認問題をお届けします！復習にぜひ活用してくださいね。
**【第2回 確認問題】**
Q. 「量子化」の意味は？
（答えのヒント）
モデルの重みのデータ型（ビット数）に着目してみましょう。精度をある程度保ちながら、メモリ使用量や計算量を効率化するための技術です。
関連する回：第2回
--- trace ---
[tool call]   glossary_make_quiz({'lecture': 2})
[tool return] glossary_make_quiz -> {"question": "「量子化」の意味は？", "answer": "モデルの重みを少ないビット数（例：16ビットから4ビット）で表し、メモリ使用量や計算量を減らす技術。精度は少し下がることがある。"}…
[usage] 入力 5,658 tokens / 出力 107 tokens / モデル応答 2 回



> 第99回の用語集に該当する用語が登録されていないため、確認問題を作成することができません。
（関係する回：第99回）
--- trace ---
[tool call]   glossary_make_quiz({'lecture': 99})
[tool return] glossary_make_quiz -> 第99回の用語集に用語がないため、確認問題を作れません。…
[usage] 入力 5,622 tokens / 出力 50 tokens / モデル応答 2 回

- 気づき・疑問：
簡素な関数を定義し、サーバーにtoolとして設定するだけで、LLMが用途や機機を判断して適切に利用できることを確認した。
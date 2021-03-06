# 開発メモ

## 注意点
* postgresのdocker imageは、version 11でないと install しているdjango(psycopg2かも?)のバージョンと合わない。
* djangoのDB backendは`postgresql_psycopg2`
* postgresの環境変数は以下の指定が必要で、同じ設定をdjangoのDBにもする必要がある。
    ```
    environment:
    - POSTGRES_USER=django_db_user
    - POSTGRES_PASSWORD=password1234
    - POSTGRES_DB=django_db
    ```
* 新たに立ち上げるときは（別のPCなど）、`./postgres_data`を空っぽにして接続しないとpostgresqlが立ち上がらない
* makemigrationsするときは、`accounts`と`webmarkdowns`のmigrationsディレクトリを空っぽにする
  * `__init__.py`を消さないように注意する


## 今後の開発方針
* DB内のmarkdownを呼び出す度にHTML化すると、djangoから受け取ったブラウザのでjsの処理（Django内でのデータの受け渡しなども）が大変なのでDB上にHTMLを保存してそれを呼び出すことにする
* いまのindexページをdetail-pageにする
  * detailは編集可にする
  * 日時と作成者を表示する
* index pageにprojectから作ったカードを置いて、各プロジェクトの記事へ飛ぶようにする
* 各プロジェクトの記事は一度に20個ぐらい見えるようにする
  * ページネーションを追加する
  * 日時と作成者を表示する
* 記事一覧を表示できるようにする
  * 全部とプロジェクト毎
  * ページネーションを追加する
  * 日時と作成者を表示する
* 新規作成ページを追加する
  * 新規作成ページはどこからでも飛んでこれるようにする
  * 新規作成時に記事名とプロジェクトを選択する
  * 日時とユーザは自動で追加する
  * 直でmdとhtmlはダウンロードできるようにする（もうあるか・・・）
  * DBには「保存」ボタンで保存する
  * # pj-pk:プロジェクトのPK
# art-pk:記事のpk
# 新規はページにフォームを設けてprojectを指定させる
# プロジェクト内で新規作成するときは別のプロジェクトに飛ばない様に固定値で処理する
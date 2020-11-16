# 開発メモ

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
  * 
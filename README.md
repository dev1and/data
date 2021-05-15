# Target

情報集取の対象となるリストを管理するためのレポジトリです。
[Devland](https://dev1and.com)はこちらのリストから定期的にデータを集取しています。

## Directory

拡張性のために以下のディレクトリ構成を持っています。

**注意**
> 今現在は、国内のみ情報を集取しています。

```
.
└── ja // 言語
    ├── individual.yaml
    ├── news.yaml
    ├── platform.yaml
    ├── security.yaml
    └── team.yaml
```

| 対象 | ファイル名 | 説明 |
| ---| --- | --- |
| 個人ブログ | individual.yaml | Qiita, Zennは除外 |
| ニュース | news.yaml | |
| フラットフォーム | platform.yaml | Qiita, Zenn, Githubなど |
| セキュリティー | security.yaml | |
| 企業ブログ | team.yaml | |

## Data Structure

| 名前 | 必須 | 説明 |
| ---| --- | --- |
| name | ○ | 会社名(英語)、お名前など<br />※ 許可された文字: 半角スペース(` `)、半角数字(`0-9`)、半角英語(`a-zA-Z`)、特殊文字(`-` `_`) |
| alias | | 会社名(英語)などをカタカナや漢字で表現 |
| url | ○ | Blog URL |
| rss | ○ | RSS URL |
| crawler | | Cralwer名 <br /> ※ 注意: `Platform`のみ使用|
| twitter | | |
| facebook | | |
| github | | |
| linkedin | | |
| youtube | | |
| instagram | | |
| speakerdeck | | |

例:
```yaml
- name: Devland
  url: https://dev1and.com
  rss: https://dev1and.com/rss.xml
```

## Contributing

対象をリストに追加する時には以下のルールを守った上、PRをお願いいたします。

1. リストに追加したい対象がRSSで配信をしているか確認をします。
2. `Data Structure`に沿って対象をリストに追加します。
3. 追加した上、`name`を基準にアルファベット順で対象を並び替えてください。
    例:
    ```yaml
    # Before
    - name: b
      url: ...
      ...
    - name: a
      url: ...
      ...

    # After
    - name: a
      url: ...
      ...
    - name: b
      url: ...
      ...
    ```
4. URL末尾の`/`は削除してください。
    例:
    ```yaml
    # Before
    url: https://dev1and.com/

    # After
    url: https://dev1and.com
    ```

## Notice

MasterにMergeしてからサイトに反映されるまでは時間がかかります。
数日経っても情報が取得できてない場合は、[Issue](https://github.com/dev1and/target/issues)または[Gitter](https://gitter.im/dev1and/community)からお知らせください。

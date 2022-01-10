# End of Life(EOL)

EOLの対象となるリストを管理します。
[Devland](https://dev1and.com)はこちらのリストから定期的にデータを取集しています。

## Directory

拡張性のために以下のディレクトリ構成を持っています。

**注意**
> 今現在は、国内のみ情報を取集しています。

```
.
└── [Programming Language].yaml # 言語(e.g php.yaml)
```

## Data Structure

| 名前      | 必須 | タイプ   | 説明 |
| ---      | --- | ---    |  --- |
| name     | ○   | string |  言語またはフレームワークの名前 |
| category | ○   | string | `language` または `framework` |
| url      | ○   | string | EOLページURL  |
| releases | ○   | array  | リリース情報 |
| releases.version         | ○   | string  | Major(Minor)バージョン名 |
| releases.url             | ○   | string  | Release Note、Supported Versions、Change Log URL |
| releases.initail_release | ○   | string(YYYY-mm-dd)  | 初期リリース日 |
| releases.active_support  | ○   | string(YYYY-mm-dd) | 開発期限日 |
| releases.security_support| ○   | string(YYYY-mm-dd)  | セキュリティーサポート期限日 ※ 決まってない場合は空白|
| releases.latest          | ○   | string(Major.Minor.Patch)  | 最新バージョン ※ 決まってない場合は空白|
| releases.lts             | ○   | boolean | Long Term Support有無 |

例:
```yaml
- title: "PHP"
  category: "language"
  url: "https://www.php.net/supported-versions.php"
  releases:
    - version: "8.1"
      url: "https://www.php.net/ChangeLog-8.php#PHP_8_1"
      initail_release: "2021-11-25"
      active_support: "2023-11-25"
      security_support: "2024-11-25"
      latest: "8.1.1"
      lts: true
    - version: "8.0"
      url: "https://www.php.net/ChangeLog-8.php#PHP_8_0"
      initail_release: "2020-11-26"
      active_support: "2022-11-26"
      security_support: "2023-11-26"
      latest: "8.0.14"
      lts: true
    - version: "7.4"
      url: "https://www.php.net/ChangeLog-7.php#PHP_7_4"
      initail_release: "2019-11-28"
      active_support: "2021-11-28"
      security_support: "2022-11-28"
      latest: "7.4.27"
      lts: true

- title: "Laravel"
  category: "framework"
  url: "https://laravel.com/docs/releases"
  releases:
    - version: 8.x
      url: "https://laravel.com/docs/8.x/releases"
      initail_release: "2020-09-08"
      active_support: "2022-07-26"
      security_support: "2023-01-24"
      latest: "8.78.0"
      lts: false
    - version: 7.x
      url: "https://laravel.com/docs/7.x/releases"
      initail_release: "2020-03-03"
      active_support: "2020-10-06"
      security_support: "2021-03-03"
      latest: "7.30.6"
      lts: false
    - version: 6.x
      url: "https://laravel.com/docs/6.x/releases"
      initail_release: "2019-09-03"
      active_support: "2022-01-25"
      security_support: "2022-09-06"
      latest: "6.20.43"
      lts: true
    - version: "5.8"
      url: "https://laravel.com/docs/5.8/releases"
      initail_release: "2019-02-26"
      active_support: "2019-08-26"
      security_support: "2020-02-26"
      latest: "5.8.38"
      lts: false
    - version: "5.5"
      url: "https://laravel.com/docs/5.5/releases"
      initail_release: "2017-08-30"
      active_support: "2019-08-30"
      security_support: "2020-08-30"
      latest: "5.5.50"
      lts: true

...
```

## Contributing

対象をリストに追加する時には以下のルールを守った上、PRをお願いいたします。

1. 各言語に合わせてEOL情報を追加してください。
2. 配列の中には言語が一番上に宣言されるようにしてください。

## Notice

MasterにMergeしてからサイトに反映されるまでは時間がかかります。
数日経っても情報が取得できてない場合は、[Issue](https://github.com/dev1and/target/issues)または[Gitter](https://gitter.im/dev1and/community)からお知らせください。

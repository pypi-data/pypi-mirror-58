# 概要

AWS CLIをMFAの認証付きで利用する場合、少々手間がかかるので、
MFA認証済みのクレデンシャルを発行する手順を自動化するツールを作成

依存するライブラリ一覧

* boto3
* PyInquirer

# インストール方法

```
$ pip install aws-mfa-util
```

# 使い方

まず、動作の前提条件は下記です。

* ~/.aws/credentialファイルが存在する
* ~/.aws/credentialファイル内に適切なプロファイルが設定されている
* ~/.aws/credentialファイル内に、適切なmfa_serialが設定されている

具体的には、下記のような設定が最低限必要です。

```
[testA]
aws_access_key_id=abcde1234
aws_secret_access_key=abcde1234
mfa_serial=arn:aws:iam::12345678:mfa/test1
```


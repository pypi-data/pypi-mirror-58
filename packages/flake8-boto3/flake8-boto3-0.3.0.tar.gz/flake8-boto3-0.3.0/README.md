# flake8-boto3

flake8-boto3 is a plugin for flake8 with checks specifically for [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html), written by [r2c](https://r2c.dev). This plugin is available by default in our program analysis tool, [Bento](https://bento.dev).

## Installation

```
pip install flake8-boto3
```

Validate the install using `flake8 --version`.

```
> flake8 --version
3.7.9 (flake8-boto3: 0.2.2, mccabe: 0.6.1, pycodestyle: 2.5.0, pyflakes: 2.1.1)
```

## List of Warnings

`r2c-boto3-hardcoded-access-token`: This check detects the use of a hardcoded access token for any of the `aws_access_key_id`, `aws_secret_access_key`, `aws_session_token` keyword arguments.
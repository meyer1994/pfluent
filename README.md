# Pfluent

[![Build Status](https://travis-ci.com/meyer1994/pfluent.svg?branch=master)](https://travis-ci.com/meyer1994/pfluent)
[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)

Thin wrapper around `subprocess` to use [fluent][1] syntax.

## Table of Contents

- [About](#about)
- [Install](#install)

## About

Just because I think it is nicer to write:

```py
Runner('git')\
    .arg('commit')\
    .arg('-m', '"message"')\
    .run(check=True)
```

Instead of:

```py
args = ['git', 'commit', '-m', '"message"']
subprocess.run(args, check=True)
```

## Install

```
pip install pfluent
```

[1]: https://en.wikipedia.org/wiki/Fluent_interface

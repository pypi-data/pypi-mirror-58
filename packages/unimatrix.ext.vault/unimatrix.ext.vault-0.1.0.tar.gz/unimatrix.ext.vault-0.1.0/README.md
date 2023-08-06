# Unimatrix Vault Client Library

## Synopsis

The Unimatrix Vault subsystem maintains secrets, such as
passwords and private keys, on the behalf of Unimatrix One
users. This Python package provides a client library that
exposes a simple API for most common operations.

```
import os

import ioc


secret_id = '00000000-00000000-00000000-00000000'
service = ioc.require('VaultService')
with service.asymmetric(secret_id) as fp:
    assert os.path.exists(fp)


assert not os.path.exists(fp)
```


## Installation

```
pip3 install unimatrix.ext.vault
```

## Features

- Remove sensitive data immediately from the local
  system after use.
- Django integration through the `python-ioc` module.


## License

GPLv3

![Cryptemis](images/cryptemis.png)
# Cryptemis ![PyPI](https://img.shields.io/pypi/v/cryptemis) [![Repository Size](https://img.shields.io/github/repo-size/0x01h/cryptemis)](https://pypi.python.org/pypi/ansicolortags/) [![GitHub License](https://img.shields.io/github/license/0x01h/cryptemis?style=flat-square)](https://pypi.python.org/pypi/ansicolortags/)
Minimalist symmetric AES image encryption module for paranoids.

[![asciicast](https://asciinema.org/a/289434.png)](https://asciinema.org/a/289434)

## Installation
```bash
pip3 install cryptemis
```

## Command Line Interpreter (CLI)
```bash
export PASS=my_super_password

# Encrypt an image.
cryptemis my_image.png $PASS

# Decrypt an image.
cryptemis -d my_image.png $PASS

# Keep filenames same after encryption/decryption.
cryptemis -kfn my_image.png $PASS
cryptemis -kfn -d my_image.png $PASS
```

## Module
```python
from cryptemis import Cryptemis


KEEP_FILENAME = False
PASSWORD = 'my_super_password'
IMAGE_FILENAME = 'my_image.png'
ENCRYPT = True
DECRYPT = False

cryptemis = Cryptemis()
cryptemis.img_file_processor(KEEP_FILENAME, PASSWORD, IMAGE_FILENAME, ENCRYPT, DECRYPT)
```

## PyPI
https://pypi.org/project/cryptemis/

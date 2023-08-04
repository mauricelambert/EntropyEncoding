# EntropyEncoding

## Description

This package implements an encoding to bypass entropy antivirus check.

## Requirements

This package require:
 - python3
 - python3 Standard Library

## Installation

```bash
python3 -m pip install EntropyEncoding
```

```bash
git clone "https://github.com/mauricelambert/EntropyEncoding.git"
cd "EntropyEncoding"
python3 -m pip install .
```

## Usages

```python
from EntropyEncoding import *

encoded_shellcode = entropy_encode(b"shellcode_payload")
print(encoded_shellcode)

entropy_decode(encoded_shellcode) == b"shellcode_payload"

print(shannon_entropy)
```

## Links

 - [Pypi](https://pypi.org/project/EntropyEncoding)
 - [Github](https://github.com/mauricelambert/EntropyEncoding)
 - [Documentation](https://user.github.io/info/python/security/EntropyEncoding.html)

## License

Licensed under the [GPL, version 3](https://www.gnu.org/licenses/).

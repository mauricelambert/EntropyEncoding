![EntropyEncoding logo](https://mauricelambert.github.io/info/python/security/EntropyEncoding.gif "EntropyEncoding logo")

# EntropyEncoding

## Description

This package implements an encoding to bypass entropy antivirus check.

I have researched about entropy bypass techniques and found people who use adding low-entropy data to bypass entropy check. I think adding data can be optimized and more efficient with a simple entropy encoding to reduce entropy score.

Adding low-entropy data:
 1. you get a larger file
 2. you do not change payload entropy (if the antivirus software splits the file for entropy calculation, it will probably have high entropy on a payload chunk)

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

print(shannon_entropy(b"shellcode_payload"))
encoded_shellcode = entropy_encode(b"shellcode_payload")
print(encoded_shellcode)

entropy_decode(encoded_shellcode) == b"shellcode_payload"

print(shannon_entropy(encoded_shellcode))
```

Tests results:

```
~# python3 EntropyEncoding.py
Entropy for non-encoded secrets: 4.521591372417719
Entropy for non-encoded encrypted secrets: 7.951320327821406
Entropy for entropy-encoded encrypted secrets: 5.774096152750044
Entropy for non-encoded exe: 5.22055339277441
Entropy for non-encoded encrypted exe: 7.914685739354301
Entropy for entropy-encoded encrypted exe: 5.759477906043907
~# 
```

## Links

 - [Pypi](https://pypi.org/project/EntropyEncoding)
 - [Github](https://github.com/mauricelambert/EntropyEncoding)
 - [Documentation](https://user.github.io/info/python/security/EntropyEncoding.html)

## License

Licensed under the [GPL, version 3](https://www.gnu.org/licenses/).

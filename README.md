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

payload = b"shellcode_payload    0000111122223333444455556666777788889999AAAABBBBCCCCDDDDEEEEFFFF" * 120
key = bytes([0,255,127,55,155,25,225,10,220,40,190,26,100,70,90,45,235,32,64,128,215,28,46,158,123,13,8,5,168,191,69])

encrypted_payload = bytes([key[i % len(key)] ^ x for i, x in enumerate(payload)])

print(shannon_entropy(encrypted_payload))  # 7.753825816757683, good encryption or compression have an entropy score > 7.9 and < 8
                                           # Malicious entropy is detected by antivirus software when entropy score is greater than ~= 7.2
                                           # This encrypted payload will be detected as malicious entropy by antivirus software
encoded_shellcode = entropy_encode(encrypted_payload)
encoded2_shellcode = entropy_encode2(encrypted_payload)
print(encoded_shellcode)
print(encoded2_shellcode)

assert entropy_decode(encoded_shellcode)   == encrypted_payload
assert entropy_decode2(encoded2_shellcode) == encrypted_payload

print(shannon_entropy(encoded_shellcode))  # 5.770760744294572, entropy score is smaller than 7.2, antivirus software will not detect this payload with entropy checks
print(shannon_entropy(encoded2_shellcode)) # 5.767383412620195, entropy score is smaller than 7.2, antivirus software will not detect this payload with entropy checks

r"""
I get entropy score from Windows executable, average score is ~= 5 (so 5.7 can be a legitimate entropy score):
>>> from glob import iglob
>>> from statistics import mean
>>> from EntropyEncoding import *
>>> entropy = []
>>> for a in iglob(r"C:\Windows\System32\*.exe"): entropy.append(shannon_entropy(open(a, "rb").read()))
...
>>> max(entropy)
7.932014219115418
>>> min(entropy)
1.6379445326685684
>>> mean(entropy)
5.063622509688209
>>>
"""
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
 - [Documentation](https://mauricelambert.github.io/info/python/security/EntropyEncoding.html)

## License

Licensed under the [GPL, version 3](https://www.gnu.org/licenses/).

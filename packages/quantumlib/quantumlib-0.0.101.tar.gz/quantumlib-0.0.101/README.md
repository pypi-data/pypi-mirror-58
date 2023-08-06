# Quantum functions for Python

Experimental library for quantum calculations.

<img src="https://img.shields.io/pypi/v/quantumlib.svg" />
<img src="https://img.shields.io/badge/license-MIT-green.svg" />
<img src="https://img.shields.io/badge/python-3.5%20%7C%203.6%20%7C%203.7-blue.svg" />

## Examples

### Integer factorization

```python3
from quantumlib import shor

shor.factorize(123) # returns prime factors of given integer
```

### Find collisions for a custom function

Easily breaks AES256, RSA2048, SHA256 or whatever

```python3
from hashlib import sha256
from quantumlib import grover

data = sha256('Piece of cake!'.encode())

result = grover.find_collision(sha256, data)

print(result) # outputs "Piece of cake!"
```

## Install

```
pip3 install quantumlib
```

## Requirements

* 8192-qubits QPU
* sense of humor

Enjoy! :)

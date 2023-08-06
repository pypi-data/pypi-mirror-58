# Quantum functions for Python

Experimental library for quantum calculations.

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

## Install

```
pip3 install quantumlib
```

## Requirements

* 8192-qubits Quantum FPU
* sense of humor

Enjoy! :)

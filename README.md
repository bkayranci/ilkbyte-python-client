# Ilkbyte Python Client

## Installation
```terminal
pip install ilkbyte
```

## Usage
```python
from ilkbyte.client import Ilkbyte
ilkbyte = Ilkbyte(
    host='https://api.ilkbyte.com/',
    secret_key='SECRET',
    access_key='ACCESS'
)

print(ilkbyte.get_all_servers())
```

## Development
```terminal
pip install -r requirements.txt
```

## Test
```terminal
python -m unittest
```

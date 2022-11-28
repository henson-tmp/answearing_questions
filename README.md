# Question answering system
This system reads a question and tries to find an answer for it on Wikipedia.

## Setup
```bash
./setup.sh

Success
```

## Usage
```bash

cd question_answering
python3 __main__.py
Question: Polska największe miasto
Article title  Polska
{'score': 0.968022346496582, 'start': 982, 'end': 990, 'answer': 'Warszawa'}
```

```bash
cd question_answering
python -m question_answering
```

```bash
cd question_answering
qa
```
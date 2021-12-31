# pyristocloud

<div align="center">

[![Build status](https://github.com/riklus/pyristocloud/workflows/build/badge.svg?branch=master&event=push)](https://github.com/riklus/pyristocloud/actions?query=workflow%3Abuild)
[![Python Version](https://img.shields.io/pypi/pyversions/pyristocloud.svg)](https://pypi.org/project/pyristocloud/)
[![Dependencies Status](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)](https://github.com/riklus/pyristocloud/pulls?utf8=%E2%9C%93&q=is%3Apr%20author%3Aapp%2Fdependabot)

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Security: bandit](https://img.shields.io/badge/security-bandit-green.svg)](https://github.com/PyCQA/bandit)
[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/riklus/pyristocloud/blob/master/.pre-commit-config.yaml)
[![Semantic Versions](https://img.shields.io/badge/%20%20%F0%9F%93%A6%F0%9F%9A%80-semantic--versions-e10079.svg)](https://github.com/riklus/pyristocloud/releases)
[![License](https://img.shields.io/github/license/riklus/pyristocloud)](https://github.com/riklus/pyristocloud/blob/master/LICENSE)
![Coverage Report](assets/images/coverage.svg)

API Wrapper per ristoCoud™, Opera4u unitn.

</div>

PyRistoCloud è un semplicissimo wrapper API per verificare se i posti a mensa sono liberi ed effettuare le prenotazioni. Niente di fancy.

## Installazione

```bash
pip3 install git+https://github.com/riklus/PyRistoCloud.git
```

## Esempio

```python3
from pyristocloud import pyRc

rc = pyRc.Api()
logged = rc.login("nome.cognome@studenti.unitn.it", "pass")

if logged:
  print("Login effettuato!")
else:
  print("Errore login.")
  exit()
```

Per altri esempi visita [cartella esempi](https://github.com/riklus/PyRistoCloud/tree/main/examples)

## Makefile usage

[`Makefile`](https://github.com/riklus/pyristocloud/blob/master/Makefile) contains a lot of functions for faster development.

<details>
<summary>1. Download and remove Poetry</summary>
<p>

To download and install Poetry run:

```bash
make poetry-download
```

To uninstall

```bash
make poetry-remove
```

</p>
</details>

<details>
<summary>2. Install all dependencies and pre-commit hooks</summary>
<p>

Install requirements:

```bash
make install
```

Pre-commit hooks coulb be installed after `git init` via

```bash
make pre-commit-install
```

</p>
</details>

<details>
<summary>3. Codestyle</summary>
<p>

Automatic formatting uses `pyupgrade`, `isort` and `black`.

```bash
make codestyle

# or use synonym
make formatting
```

Codestyle checks only, without rewriting files:

```bash
make check-codestyle
```

> Note: `check-codestyle` uses `isort`, `black` and `darglint` library

Update all dev libraries to the latest version using one comand

```bash
make update-dev-deps
```

<details>
<summary>4. Code security</summary>
<p>

```bash
make check-safety
```

This command launches `Poetry` integrity checks as well as identifies security issues with `Safety` and `Bandit`.

```bash
make check-safety
```

</p>
</details>

</p>
</details>

<details>
<summary>5. Type checks</summary>
<p>

Run `mypy` static type checker

```bash
make mypy
```

</p>
</details>

<details>
<summary>6. Tests with coverage badges</summary>
<p>

Run `pytest`

```bash
make test
```

</p>
</details>

<details>
<summary>7. All linters</summary>
<p>

Of course there is a command to ~~rule~~ run all linters in one:

```bash
make lint
```

the same as:

```bash
make test && make check-codestyle && make mypy && make check-safety
```

</p>
</details>

<details>
<summary>8. Docker</summary>
<p>

```bash
make docker-build
```

which is equivalent to:

```bash
make docker-build VERSION=latest
```

Remove docker image with

```bash
make docker-remove
```

More information [about docker](https://github.com/riklus/pyristocloud/tree/master/docker).

</p>
</details>

<details>
<summary>9. Cleanup</summary>
<p>
Delete pycache files

```bash
make pycache-remove
```

Remove package build

```bash
make build-remove
```

Delete .DS_STORE files

```bash
make dsstore-remove
```

Remove .mypycache

```bash
make mypycache-remove
```

Or to remove all above run:

```bash
make cleanup
```

</p>
</details>

## 🛡 License

[![License](https://img.shields.io/github/license/riklus/pyristocloud)](https://github.com/riklus/pyristocloud/blob/master/LICENSE)

This project is licensed under the terms of the `GNU GPL v3.0` license. See [LICENSE](https://github.com/riklus/pyristocloud/blob/master/LICENSE) for more details.


### Esclusione di responsabilità
Non mi assumo, né espressamente né tacitamente, la responsabilità per l’utilizzo di questo software.  
Non sono affiliato in **alcun** modo a Opera o a ristoCoud™.   
Questo è un progetto nato per puro svago, e in **alcun** modo intende recare danno o problemi, di qualsiasi natura o entità, a Opera o a ristoCoud™ o a terzi.

## 📃 Citation

```bibtex
@misc{pyristocloud,
  author = {riklus},
  title = {API Wrapper per ristoCoud™ di Opera4u unitn.},
  year = {2021},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/riklus/pyristocloud}}
}
```

## Credits [![🚀 Your next Python package needs a bleeding-edge project structure.](https://img.shields.io/badge/python--package--template-%F0%9F%9A%80-brightgreen)](https://github.com/TezRomacH/python-package-template)

This project was generated with [`python-package-template`](https://github.com/TezRomacH/python-package-template)

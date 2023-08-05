# Verminator

[![Latest](https://img.shields.io/pypi/v/verminator.svg)](https://pypi.python.org/pypi/verminator)
[![Status](https://img.shields.io/pypi/status/verminator.svg)](https://pypi.python.org/pypi/verminator)
[![PyV](https://img.shields.io/pypi/pyversions/verminator.svg)](https://pypi.python.org/pypi/verminator)

TDC image Version control tERMINATOR.

## Install

Requires Python 3.5+:
```bash
pip install -U verminator -i http://172.16.1.161:30033/repository/pypi/simple/ --trusted-host=172.16.1.161
```
Or from source code
```bash
python setup.py install
```

## Usage

**First, update product version ranges in `/path/to/product-meta/instances/releases_meta.yaml`**

### Validate instance releases

```bash
verminator validate /path/to/product-meta/instances
```

For specific instance, say inceptor

```bash
verminator validate -c inceptor /path/to/product-meta/instances
```

### Create a new OEM

1. Replace `tdc-` with oem prefix say `gzes-` in release_meta.yaml
2. Update instance releases
```bash
verminator genoem -o gzes /path/to/product-meta/instances
verminator validate -o gzes /path/to/product-meta/instances
```

### Create a new version

New version of a product line, say `sophon`
```bash
verminator genver -v sophon-2.2.0-final /path/to/product-meta/instances
```

For specific instance, say inceptor
```bash
verminator genver -c inceptor -v transwarp-6.0.1-final /path/to/product-meta/instances
```

### For OEM

If you are working on an OEM branch, make sure env `export OEM_NAME=xxx` set or command option `-o xxx` is given on the subcommand like `validate` and `genver`.

### Update History

See `HISTORY`

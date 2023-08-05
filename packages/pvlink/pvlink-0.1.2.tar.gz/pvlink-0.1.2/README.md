
# pvlink

[![Build Status](https://travis-ci.org//pvlink.svg?branch=master)](https://travis-ci.org//pvlink)
[![codecov](https://codecov.io/gh//pvlink/branch/master/graph/badge.svg)](https://codecov.io/gh//pvlink)


ParaView-Web RemoteRenderer in Jupyter

## Installation

You can install using `pip`:

```bash
pip install pvlink
```

Or if you use jupyterlab:

```bash
pip install pvlink
jupyter labextension install @jupyter-widgets/jupyterlab-manager
```

If you are using Jupyter Notebook 5.2 or earlier, you may also need to enable
the nbextension:
```bash
jupyter nbextension enable --py [--sys-prefix|--user|--system] pvlink
```

# pypi_template
Template repository for pypi.



## How to use

Open https://github.com/idleuncle/pypi_teamplate/generate to create your new pypi project.

### Build

```
make clean && make build
```

### Upload to test.pypi.org
```
make upload-test
```

### Install from test.pypi.org

```
make install-test
```


### Upload to pypi.org

```
make upload
```

### Install from pypi.org

```
make install
```

### Install from local

```
pip install .
```

### Install from github

```
pip install git+https://github.com/your_name/your_lib.git
```

# SHYNT

The code SHYNT solves the neutron transport equation by using the response matrix method. To install SHYNT and all the dependencies it is recommended to use a virtual environment, after cloning the repository:

```shell
$ ls
shynt-repo
```

```shell
$ python -m venv shynt-venv
$ source shynt-venv/bin/activate
```

```shell
$ cd path/to/shynt-repo
$ pip install -r requirements.txt
```
The `PYTHONPATH` enviroment variable needs to be modified as well, in the .bashrc file:

```shell
# PYTHON PATH MODIFICATION
SHYNT=/path/to/shynt-repo
PYTHONPATH="$SHYNT:$PYTHONPATH"
export PYTHONPATH

```

After the instalation of all python dependencies and the modification to the `PYTHONPATH` the files in the examples directory can be run.

```shell
$ cd examples
$ python pin.py
```

After running the file `python.py` a set of serpent files will be generated, if the _res.m files don´t exist the code automatically run the generated serpent files using the alias `sss2.1.32` that corresponds to the Serpent version 2.1.32. Once the montecarlo simulations finish the response matrix method is used to solve the neutron transport equation.





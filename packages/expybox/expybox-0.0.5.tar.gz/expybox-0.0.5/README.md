[![Documentation Status](https://readthedocs.org/projects/expybox/badge/?version=latest)](https://expybox.readthedocs.io/en/latest/?badge=latest)

# ExpyBox
ExpyBox is a Jupyter notebook toolbox for model interpretability/explainability.
It lets you create interactive Jupyter notebooks to explain your model.

## Usage
This package is meant to be used inside of Jupyter notebook, other usage makes little to no sense.
First you need to import and instantiate the ExpyBox class:

```python
from expybox import ExpyBox
expybox = ExpyBox(predict_function, train_data, kernel_globals=globals())
```

Now you can use the supported interpretability methods, like this:
```python
expybox.lime()
```
which creates a form like this:


## Instalation
Because of *alibi* package ExpyBox requires **64-bit** Python 3.7 or higher. 
It is also recommended to create separate virtual enviroment - you can use Pythons 
[venv](https://docs.python.org/3/library/venv.html).

Otherwise the installation process is the same as for other packages, just use pip:
```bash
pip install expybox
``` 



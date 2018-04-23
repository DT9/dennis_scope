# ScopeAR Printer

This printer prints pretty ascii art in the form of X's and Trees.

### Prerequisites

You need python and virtualenv to run the printer.

With just python intalled, you can install virtualenv like this:
```
pip install virtualenv
```

### Installing

Setup packages.
```
virtualenv -p python3 venv
source ./venv/bin/activate
pip install -r requirements.txt
```

Auto-generate python docs with Sphinx.
```
cd docs
sphinx-apidoc -f -o source/ ../src
make html
```

Creating a tree sample
```
cd src
python tree.py 5
```

Creating a X sample
```
cd src
python x.py 5
```

## Running the tests

These tests cover constructing, building, and printing of said printer.
From the project root, you may run:

```
nosetests tests
```


## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Dennis Truong** - *Initial work* - [dt9](https://github.com/dt9)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Keith from ScopeAR 

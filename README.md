# python-page-object-selenium-example

This is an example implementation of the automation test framework written in pytest & selenium. Designed in Page Object Patten.
The cases were written on dummy e-commerece web site https://www.saucedemo.com/ that was designed for practising automation techniques. 

### To run tests you need to

#### Install all requirements from requirements.txt
```sh
pip install -r requirements.txt
```

#### Run all tests
```sh
pytest tests/
```

#### Run tests with included allure reporting
```sh
pytest tests/ --alluredir=<reports_directory>
```
#### and after tests finish run:
```sh
allure serve <reoprts_directory>
```

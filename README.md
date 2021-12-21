# python-page-object-selenium-example

This is example implementation of the automation test framework written in pytest & selenium.

This project was created in PageObject Pattern. The cases were written on dummy e-comerece web site https://www.saucedemo.com/.


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

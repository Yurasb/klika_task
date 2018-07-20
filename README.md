# KlikaTech test task
This is test task for KlikaTech

## Requirements
Project is created using Ubuntu 18 (should work with 16 as well),
Python 3.6 (using `virtualenv`) and Chrome browser.
Chromedriver for Selenium is required for sure.

## Local running
Follow steps below to run locally.

#### Preparation
You need `Allure` to generate fancy report and `tox` to build virtual environment.

>sudo apt-add-repository ppa:qameta/allure
>sudo apt-get update 
>sudo apt-get install allure

>sudo pip install tox

#### Launch
Simply run `tox` command from root project folder. This will prepare virtual environment,
launch tests, generate Allure report and open it via your default browser.

## Framework notes
Main issue is precision for operations with float numbers. 
Due to difference in float processing between Python and JS, such tests became flaky.
In order to reduce number of flaky tests, I restricted precision by 3 symbols after point.
Helped a bit, but issue is still there.

## Areas for improvement
+ Flaky tests due to precision - maybe some other way to eliminate this issue is needed
+ Parametrization - could be more elegant

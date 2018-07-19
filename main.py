import pytest


pytest.main(
    ['./tests/', '--junitxml=./test_report.xml', '--alluredir=./test_report/']
)

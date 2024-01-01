# this file is same we have to give the by default we have to create
import pytest


# (scope="class") > if you provide this then fixture will work as beforeclass and afterclass
@pytest.fixture
def setup():
    print(
        ' <<<<<<<<<<<<<<<<<<< i am fixture will be executing only once and will be shared to each every class >>>>>>>>>>>>>>>>>')
    yield
    print(' <<<<<<<<<<<<<<<<<<< i am last just like beforeclass >>>>>>>>>>>>>>>>>')


@pytest.fixture()
def dataload():
    print('user profile data to be loaded !!')
    return ['atul', 'arya', 'atul.arya@993']


# here we want to execute test in every browsers
@pytest.fixture(params=[('chrome','atul','arya'), 'firefox', 'Edge'])
def crossBrowser(request):
    return request.param

import pytest


# this is local fixture but ideally we define fixtures in conftest file to be used by all the sub classes
@pytest.fixture()
def setup1():
    print('i will be executed first !! same as before mthod ')
    yield
    print(' i will be executing last after the method execution !! same as tear down ')


# @pytest.mark.skip
# # here we have to pass argument as fixture name
# def test_fixturedemo(setup1):
#     print(' i am method which will be executed after the fixture !!')
#
# @pytest.mark.skip
# def test_method(setup1):
#     print(' hello i am method 2 !! ')



def test_global_fixture(setup):
    print(' global fixture test')




def test_global_fixture2(setup):
    print(' global fixture test 2')
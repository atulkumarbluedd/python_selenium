# any pytest should start with test_ only or end with test_
# every line of code should be in functions
# method name should always start with test_
import pytest

# @pytest.mark.skip
@pytest.mark.sanity
def test_firstProgramme():
    print('hello')

''' execute using cmd
1. to get more verbose use 
py.test -v
2. to get console logs i.e. print statements etc 
py.test -v -s
-s  >> logs in output
-v >> more info
-k >> method name execution

3. here we can have same name of 2 methods in python but it is not a good practice as it overrides with latest method
4. we can also execute specific tests from pytest file as well provide file name as well 
py.test 01_pytest_basis_test.py -v -s
5. How to run selected test case from different files >> py.test -k credit -v -s
6. marking or tagging or grouping test cases >> >py.test -m sanity  -v -s
@pytest.mark.smoke
7. how to skip one test >> @pytest.mark.skip
8. if you want to run the test but don't want to be reported passed or failed, basically execution count will be increased
@pytest.mark.xfail




'''


@pytest.mark.smoke
def test_creditcard():
    assert "hello" in "klkl" 'falied because the strings are not equal !!'





@pytest.mark.xfail
def test_xfail():
    print('xfail demo !! it will not be reported whether it failed or passed !')



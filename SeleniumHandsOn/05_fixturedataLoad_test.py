import pytest

@pytest.mark.usefixtures('dataload')
class TestExample2:
    def test_editProfile(self,dataload): # you will be forced to pass fixture name as it is returning the data
        print(dataload)
        print(dataload[1])
        print(dataload[2])



import pytest

from SeleniumHandsOn.BaseClass import BaseClass


@pytest.mark.usefixtures('setup')
class TestExample(BaseClass):

    def test_fixturedemo1(self):
        log=   self.getLogger()
        log.info('hello i am comming from logger')
        print(' i will execute steps in fixture demo1')
    def test_fixturedemo2(self):
        print(' i will execute steps in fixture demo2')
    def test_fixturedemo3(self):
        print(' i will execute steps in fixture demo3')

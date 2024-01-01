from SeleniumHandsOn.BaseClass import BaseClass


class TestExmples3(BaseClass): # this is inheritance as here we have provided BaseClass as parameter so we can use all the methods present in the BaseClass
   def test_editProfile(self):
       print('this is logging demo ')
       log=self.getLogger()
       log.info(' hi this is info')


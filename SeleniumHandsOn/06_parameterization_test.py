import pytest


# this test will be executed in all the 3 browsers which we have defined in crossbrowser fixture

def test_crossbrowser( crossBrowser):  # crossBrowser it is fxture name
    print(crossBrowser)

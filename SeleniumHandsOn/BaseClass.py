import inspect
import logging


class BaseClass:

    def getLogger(self):
        loggername=inspect.stack()[1][3] # this we have added because when we are running then it is taking baseclass as test name so to fix we have added this
        logger = logging.getLogger(loggername)  # it will catch file name for which we are generating logs or test case name

        fileHandler = logging.FileHandler('logFile.log')
        formatter = logging.Formatter(
            '%(asctime)s :%(levelname)s : %(name)s: %(message)s')  # this is format in which format we want to print
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # filehandler object >> where you want to print the logs in which file

        logger.setLevel(
            logging.DEBUG)
        return logger

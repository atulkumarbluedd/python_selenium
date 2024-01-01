import logging


def test_loggingDemo():
    logger = logging.getLogger(__name__)  # it will catch file name for which we are generating logs or test case name

    fileHandler = logging.FileHandler('logFile.log')
    formatter = logging.Formatter(
        '%(asctime)s :%(levelname)s : %(name)s: %(message)s')  # this is format in which format we want to print
    fileHandler.setFormatter(formatter)

    logger.addHandler(fileHandler)  # filehandler object >> where you want to print the logs in which file

    logger.setLevel(logging.INFO)  # read online why we use it, here we have used info then below level will be printed but debug will not be preinted
    logger.debug("A debug statement is executed ")
    logger.info("information statement ")
    logger.warning(" something is in warning mode !")
    logger.error(" A mejor error occurred ")
    logger.critical(" critical issue occured !!")

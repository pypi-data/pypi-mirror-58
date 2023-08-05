
import logging
import os

class CsLogging:
     def __init__(self,fname,level=logging.DEBUG,format='[%(levelname)s] %(asctime)s: %(message)s'):

          logger = logging.getLogger(__name__)
          logger.basicConfig(filename,level,format)
          if(level > logging.DEBUG): logging.getLogger().addHandler(logging.StreamHandler())

     def debug(msg):
          logger.debug(msg)

     def info(msg):
          logger.info(msg)

     def warning(msg):
          logger.warning(msg)


from mlops_uno.logger import logging

#logging.info("This is a demo of the logger module.")

from mlops_uno.exception import CustomException
import sys

# logging.info("This is a demo script to show how to use the logger in mlops_uno package.")

try:
    a = 1 / 0  # This will raise a ZeroDivisionError
except Exception as e:
    raise CustomException(e, sys)

# for errors and exceptions, we can use the link below:
#https://docs.python.org/3/tutorial/errors.html
"""
This module contains the logger to be used in section 1.
"""

import logging, sys, os

def setup_custom_logger() -> logging.Logger:
    """Setups the custom logger to be used globally.

    This should only be called by get_logger()

    Returns:
        The logger to be used in the script.
    """
    logging.basicConfig(filename=os.getcwd() + '\\output.log',
                            filemode='a',
                            format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                            datefmt='%H:%M:%S',
                            level=logging.DEBUG)
    log = logging.getLogger()
    log.setLevel(logging.DEBUG)

    stdout_handler = logging.StreamHandler(sys.stdout)
    log.addHandler(stdout_handler)
    return log

def get_logger() -> logging.Logger:
    """Returns the logger to be used.

    Returns:
        The logger to be used in the script.
    """
    # existing logger made
    if logging.getLogger('root').hasHandlers():
        return logging.getLogger('root')
        
    # no existing loggers made
    else:
        logging.basicConfig(filename=os.getcwd() + '\\output.log',
                                filemode='a',
                                format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                                datefmt='%H:%M:%S',
                                level=logging.DEBUG)
        log = logging.getLogger()
        log.setLevel(logging.DEBUG)

        stdout_handler = logging.StreamHandler(sys.stdout)
        log.addHandler(stdout_handler)

        return log

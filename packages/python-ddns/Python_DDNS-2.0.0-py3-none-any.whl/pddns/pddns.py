"""Python client for ddns services"""
import configparser
import argparse
import os
import sys
import socket
import logging

from .providers import cloudflare


def make_logger(name, loglevel):
    """Makes the logger"""
    logger = logging.getLogger(name)
    logger.setLevel(loglevel)
    formatter = logging.Formatter(
        '%(levelname)s - %(name)s - %(asctime)s - %(message)s',
        '%Y-%m-%d %H:%M:%S')  # Built in formatting
    fh = logging.FileHandler("{}.log".format(name), mode='w')
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    ch = logging.StreamHandler()
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    return logger


def get_ip():
    """
    Gets the ip address of the system
    Shamlessly taken from stackoverflow
    https://stackoverflow.com/a/28950776/11542276
    """

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('1.1.1.1', 1))
        host = s.getsockname()[0]
    finally:
        s.close()
    return host


def quick_test(log):
    """Tests to make sure the config is readable"""
    CONFIG = configparser.ConfigParser()
    CONFIG.read("config.conf")
    if CONFIG == 0:
        raise FileNotFoundError
    log.debug(
        {section: dict(CONFIG[section]) for section in CONFIG.sections()}
        )
    log.info("Test Completed Successfully")
    return 0


def initialize(log):
    """Renames config file"""
    dn = os.path.dirname(os.path.realpath(__file__))
    try:
        os.rename(os.path.join(dn, "config.dist.conf"),
                  os.path.join(dn, "config.conf"))
        log.info("File renamed successfully")
        return 0
    except FileNotFoundError:
        log.info("Error: File not found.\nFiles are: {}"
                 .format(os.listdir(dn)))
        return 1


def main():
    """
    Main function that does all the work
    Will be re done with parse arg
    """
    parser = argparse.ArgumentParser(prog="pddns",
                                     description="DDNS Client")
    parser.add_argument('-t', '--test', default=False, action="store_true",
                        help='Tests to make sure the config is readable')
    parser.add_argument('-i', '--initialize',
                        default=False, action="store_true",
                        help="Renames the dist config")
# Logging function from https://stackoverflow.com/a/20663028
    parser.add_argument('-d', '--debug', help="Sets logging level to DEBUG.",
                        action="store_const", dest="loglevel",
                        const=logging.DEBUG, default=logging.WARNING)
    parser.add_argument("-v", "--verbose", help="Sets logging level to INFO",
                        action="store_const", dest="loglevel",
                        const=logging.INFO)
    args = parser.parse_args()

    log = make_logger("PDDNS", args.loglevel)
    log.info("Starting up")
    log.debug(args)

    if args.initialize:
        sys.exit(initialize(log))

    if args.test:
        sys.exit(quick_test(log))

    CONFIG = configparser.ConfigParser()
    CONFIG.read("config.conf")
    cloudflare(get_ip(), CONFIG, log)


if __name__ == "__main__":
    main()

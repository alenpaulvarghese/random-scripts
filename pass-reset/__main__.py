#!/usr/bin/python3
# (c) AlenPaulVarghese
# -*- coding: utf-8 -*-
from pathlib import Path
import logging
import gnupg
import os

__home__ = str(Path.home())
# passphrase of the old gpg key.
__passphrase__ = ""
__gpgdirectory__ = __home__ + "/.gnupg"
__passdirectory__ = __home__ + "/.password-store"
# ID of the new gpg key.
__newkeyid__ = ""


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('pass-reset')
logging.getLogger("gnupg").setLevel("WARNING")


def decrypt_files(path, gpg: gnupg.GPG):
    for files in os.listdir(path):
        actual_path = path + "/" + files
        if os.path.isfile(actual_path):
            if files.endswith(".gpg"):
                logger.debug(f"decrypting: {actual_path}")
                with open(actual_path, "rb") as reader:
                    print(gpg.decrypt_file(reader, passphrase=__passphrase__, output=actual_path).status)
                logger.debug(f"encrypting: {actual_path}")
                with open(actual_path, "rb") as reader:
                    print(gpg.encrypt_file(reader, recipients=__newkeyid__, output=actual_path).status)
        else:
            decrypt_files(actual_path, gpg)


def main():
    logger.info(f"set gpg directory {__gpgdirectory__}")
    logger.info(f"set pass directory {__passdirectory__}")
    gpg = gnupg.GPG(gnupghome=__gpgdirectory__)
    logger.info("gpg loaded now testing recipient")
    a = gpg.encrypt("This is a test", recipients=__newkeyid__, output="test.gpg")
    if not a.ok:
        logger.fatal(f"gpg failed due to: {a.status}")
    else:
        logger.info(f"gpg says: {a.status}")
        os.remove("test.gpg")
    os.chdir(__passdirectory__)
    input("press anykey to proceed? ")
    decrypt_files(os.getcwd(), gpg)


if __name__ == "__main__":
    main()

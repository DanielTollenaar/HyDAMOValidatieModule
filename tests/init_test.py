"""
Test voor __init__.py
"""

from hydamo_validation.__init__ import (__author__,
                                        __copyright__,
                                        __credits__,
                                        __version__,
                                        __license__,
                                        __maintainer__,
                                        __email__,
                                        __status__)

author = "Het Waterschapshuis"
copyright = "Copyright 2021, Het Waterschapshuis"
credits = ["D2HYDRO", "HKV", "HydroConsult"]
version = "0.9.0"

license = "MIT"
maintainer = "Daniel Tollenaar"
email = "daniel@d2hydro.nl"
status = "testing"


def test_author():
    assert __author__ == author


def test_copyright():
    assert __copyright__ == copyright


def test_credits():
    assert __credits__ == credits


def test_version():
    assert __version__ == version


def test_license():
    assert __license__ == license


def test_maintainer():
    assert __maintainer__ == maintainer


def test_email():
    assert __email__ == email


def test_statusl():
    assert __status__ == status

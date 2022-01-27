import sys

from numpy   import ndarray
from os.path import abspath
from os.path import expanduser
from os.path import isfile

sys.path.append(abspath(""))
sys.path.append(abspath("src"))
sys.path.append(abspath("../src"))

from griddingmachine import update_GM
from griddingmachine import query_collection
from griddingmachine import request_LUT


def test_update():
    update_GM()
    assert isfile(expanduser("~") + "/GMCollections" + "/Artifacts.toml")


def test_querry():
    file_path = query_collection('VCMAX_2X_1Y_V1')
    assert isfile(file_path)


def test_request():
    vcmax,error = request_LUT('VCMAX_2X_1Y_V1', 35.1, 115.2)
    assert type(vcmax) == float
    assert type(error) == float

    lai,err = request_LUT('LAI_MODIS_2X_1M_2001_V1', 35.1, 115.2)
    assert type(lai) == ndarray
    assert type(err) == ndarray

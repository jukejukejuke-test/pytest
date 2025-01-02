from xml.etree.ElementInclude import include

import pytest
import requests
from config import (SERVICE_URL)


def test_getting_posts():
    response = requests.get(url=SERVICE_URL)
    assert response.status_code == 200


test_getting_posts()

import os
import pytest


# @pytest.mark.usefixtures("cleandir")  # Via decorator
class TestDirectoryInit(object):
    pytestmark = pytest.mark.usefixtures("cleandir")  # Via mark call

    def test_cwd_starts_empty(self):
        assert os.listdir(os.getcwd()) == []
        with open("myfile", "w") as f:
            f.write("hello")

    def test_cwd_again_starts_empty(self):
        assert os.listdir(os.getcwd()) == []

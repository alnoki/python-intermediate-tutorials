import pytest
pytestmark = pytest.mark.glob("module", x=1)


@pytest.mark.glob("class", x=2)
class TestClass(object):
    @pytest.mark.glob("function", x=3)
    def test_something(self):
        pass

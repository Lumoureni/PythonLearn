import pytest

@pytest.mark.api
def test_a():
    assert 1==1

class Test:
    @pytest.mark.e2e
    def test_b(self):
        assert 1 == 2
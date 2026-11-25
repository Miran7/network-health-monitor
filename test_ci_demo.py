from monitor import get_check

def test_ci_demo():
    result = get_check("https://example.com")

    assert result["status"] == "DOWN"




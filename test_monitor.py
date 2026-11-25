from monitor import get_check, check_service
from unittest.mock import patch
import requests


def test_connection_error():
    with patch("monitor.requests.get") as mock_get:

        mock_get.side_effect = requests.exceptions.ConnectionError(
            "Connection refused"
        )

        result = check_service("http://127.0.0.1:8000/not_found_123")

        assert result["status"] == "DOWN"
        assert result["http_code"] == "N/A"
        
def test_timeout():
    with patch("monitor.requests.get") as mock_get:

        mock_get.side_effect = requests.exceptions.Timeout(
            "Timeout"
        )
        

        result = check_service("http://127.0.0.1:9999")

        mock_get.assert_called_once_with(
                            "http://127.0.0.1:9999",
                            timeout=5
                                )

        assert result["status"] == "DOWN"
        assert result["http_code"] == "N/A"
        assert result["duration_ms"] >= 0

        

def test_default_status():
    result = get_check("https://example.com")

    assert result["status"] == "DOWN"



def test_service_up():

    with patch("monitor.requests.get") as mock_get:

        mock_get.return_value.status_code = 200

        result = check_service("https://example.com")

        assert result["status"] == "UP"
        assert result["http_code"] == 200

def test_service_down():
    with patch("monitor.requests.get") as mock_get:

        mock_get.return_value.status_code = 500

        result = check_service("http://127.0.0.1:9999")
        
        assert result["status"] == "DOWN"
        assert result["http_code"] == 500
#
#
#
























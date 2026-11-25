import requests
import time

def check_service(url):
    check = get_check(url)
    start = time.perf_counter()

    try:

        response = requests.get(url, timeout=5)


    except requests.exceptions.RequestException as error:
        print(f"Request failed: {error}")

    else:
        check["http_code"] = response.status_code
        if 200 <= check["http_code"] < 400:
            check["status"] = "UP"

    end = time.perf_counter()
    duration_mss = (end - start) * 1000
    check["duration_ms"] = duration_mss

    return check

def get_check(url):
    check = {
        "url": url,
        "status": "DOWN",
        "http_code": "N/A",
        "duration_ms": 0
    }
    return check
def main():
    check_service("https://example.com")
    services = [
        "https://example.com",
        "http://127.0.0.1:8000",
        "http://127.0.0.1:9999",
        "http://127.0.0.1:8000/not_found_123"
    ]
    service_results = []

    for url in services:
        result = check_service(url)
        service_results.append(result)

    number_of_result = len(service_results)


    print("\n-------------------------")
    print("NETWORK MONITORING REPORT")
    print("-------------------------\n")


    for result in service_results:

        print(f"Service Results: {result['url']}")
        print("HTTP Status:", result["http_code"])
        print(f"Status: {result["status"]}")
        print(f"Response Time: {int(result["duration_ms"])} ms\n")


    up_counter = 0
    down_counter = 0
    for result in service_results:
        if result["status"] == "UP":
            up_counter += 1
        else:
            down_counter += 1
    if up_counter!= 0 or number_of_result !=0:
        availability_rate= up_counter / number_of_result * 100

    print("-------------------------\n")
    print(f"Total Services: {number_of_result}")
    print(f"Up: {up_counter}")
    print(f"Down: {down_counter}")
    print(f"Availability: {availability_rate:.2f}%")

if __name__ == "__main__":
    main()


# print(f"Target: {end_check['url']}")
#
#
#























        























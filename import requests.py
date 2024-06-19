import requests
import time

def check_application_status(url):
    try:
        response = requests.get(url)
        # Check if the response status code is within 200-299 indicating success
        if response.status_code >= 200 and response.status_code < 300:
            return True, response.status_code
        else:
            return False, response.status_code
    except requests.exceptions.RequestException as e:
        # If an exception occurs (e.g., connection timeout, DNS resolution error)
        return False, None

def main():
    url = "https://www.orchidengg.ac.in/"  # Replace with your application URL
    while True:
        is_up, status_code = check_application_status(url)
        if is_up:
            print(f"Application is UP! Status code: {status_code}")
        else:
            if status_code:
                print(f"Application is DOWN! Status code: {status_code}")
            else:
                print("Application is DOWN! Connection error or timeout occurred.")
        
        # Wait for some time before checking again (e.g., every 60 seconds)
        time.sleep(60)

if _name_ == "_main_":
    main()
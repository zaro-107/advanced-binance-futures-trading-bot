from time import sleep

def retry_request(func, retries=3):

    for attempt in range(retries):

        try:
            return func()

        except Exception:

            sleep(1)

    raise Exception("Request failed")
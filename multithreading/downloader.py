import threading
import requests
import time

def logger(func):
    def wrapper(*args, **kwrgs):
        start_time = time.time()
        result = func(*args, **kwrgs)
        end_time = time.time()
        total_time = end_time - start_time
        print(f"⏱️ Total time taken: {total_time:.2f} seconds")
        return result
    return wrapper


def fetch_url(url):
    try:
        response = requests.get(url)
        print(f"{url} fetched with status code: {response.status_code}")
        # You can add logic to save content or process it here
    except Exception as e:
        print(f"Error fetching {url}: {e}")

@logger
def process(urls):
    threads = []
    for url in urls:
        thread = threading.Thread(target=fetch_url, args=(url,))
        thread.start()
        threads.append(thread)
    print("All downloads completed.")
    # Wait for all threads to complete
    for thread in threads:
        print(thread)
        thread.join()
        
    return threads


if __name__ == "__main__":

    urls = [
        "https://example.com/image1.jpg",
        "https://example.com/file.pdf",
        "https://example.com/video.mp4",
        # Add more URLs
    ]
    print(process(urls))

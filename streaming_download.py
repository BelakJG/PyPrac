import os.path

import requests
import time
import hashlib

def get_file_md5(file_path):
    with open(file_path, "rb") as file:
        digest = hashlib.file_digest(file, "md5")
    return digest.hexdigest()

url = "https://ash-speed.hetzner.com/1GB.bin"
local_filename = "1GB.bin"
file_hash = "5fa2035a209e73f5727a72aafd332916"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

start = time.perf_counter()
bytes_written = 0
try:
    with requests.get(url, stream=True, headers=headers, timeout=15) as response:
        response.raise_for_status()
        with open(local_filename, "wb") as file:
            for chunk in response.iter_content(chunk_size=1024 * 1024):
                if chunk:
                    file.write(chunk)
                    bytes_written += len(chunk)
    end = time.perf_counter()
    elapsed_time = end - start
    Mb_written = bytes_written * 8 / 1000000
    print(f"Downloaded {bytes_written / 1000000:.2f} MB in {elapsed_time:.2f} seconds")
    print(f"Download speed: {Mb_written / elapsed_time:.2f} Mbps")
    print(f"Checking if file hash matches {file_hash}")
    print("MD5 hash matches!" if get_file_md5(local_filename) == file_hash else "MD5 Mismatch")
except Exception as e:
    print(f"Error: {e}")

if os.path.exists(local_filename):
    os.remove(local_filename)
    print(f"{local_filename} deleted!")

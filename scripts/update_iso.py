import requests
from bs4 import BeautifulSoup
import os
from tqdm import tqdm


# Windows 10 ISOs have to be manually installed and updated

# Check if string is float number
def isfloat(value): 
    return value.replace('.', '').isdigit()

# Get the latest ubuntu iso and downloading it to the iso folder
def ubuntu():
    release_url = 'https://releases.ubuntu.com/'
    release_req = requests.get(release_url)
    soup = BeautifulSoup(release_req.text, 'html.parser')
    recent_release = ''
    for link in soup.find_all('a'):
        release_number = (link.get('href'))[:-1]
        is_float_bool = isfloat(release_number)
        # Get last true in link
        if is_float_bool == True:
            recent_release = release_number
    # Check if the iso is already downloaded
    if os.path.isfile(f"iso/ubuntu-{recent_release}-desktop-amd64.iso"): 
        print(f'Ubuntu {recent_release} is already downloaded')
    else:
        iso_url = f'https://releases.ubuntu.com/{recent_release}/ubuntu-{recent_release}-desktop-amd64.iso'

        iso_req = requests.get(iso_url, stream=True)
        path = f"iso/ubuntu-{recent_release}-desktop-amd64.iso"
        with open(path, 'wb') as f:
            total_length = int(iso_req.headers.get('content-length'))
            with tqdm(total=total_length, unit='B', unit_scale=True, unit_divisor=1024) as pbar:
                for chunk in iso_req.iter_content(chunk_size=1024):
                    pbar.update(len(chunk))


        print(f'Ubuntu {recent_release} is downloaded')

ubuntu()
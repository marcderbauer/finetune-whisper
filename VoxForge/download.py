from bs4 import BeautifulSoup
import requests
from tqdm import tqdm


with open ("VoxForge/VoxForge Repository.html", "r", encoding="utf-8") as f:
    forge = f.read()
soup = BeautifulSoup(forge, 'html.parser')

links = {link.contents[0]:link.get('href') for link in soup.find_all('a')}
links = {name:link for name, link in links.items() if link.endswith(".tgz")}

for name, url in tqdm(links.items()):
    result = requests.get(url)
    with open (f"VoxForge/VoxForge Repository_files/downloads/{name}", 'wb') as f:
        f.write(result.content)
    # Ends with an error after downloading all the files?
    # Files are there though...
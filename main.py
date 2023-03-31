from bs4 import BeautifulSoup
import requests
import platform
import os
import py7zr
import git
import shutil

def main():
    print("Provide your license key (https://keymaster.fivem.net)")
    lickey = input("~ % ")
    print("\nProvide your steam web api key (http://steamcommunity.com/dev/apikey)")
    steamapi = input("~ % ")
    # checking if os is Windows or Linux
    system = platform.system()
    if system == "Windows":
        windows(lickey, steamapi)
    else:
        linux(lickey, steamapi)

def windows(lickey, steamapi):
    file_path = os.path.abspath(os.path.dirname(__file__))
    # getting latest recommended build for Windows
    URL = 'https://runtime.fivem.net/artifacts/fivem/build_server_windows/master/'
    with requests.Session() as s:
        soup = BeautifulSoup(s.get(URL).content, "html.parser")
    relative_path = soup.find_all("div", {"class": "panel-block"})[0].next_element.next_element['href']
    latest_stable_url = os.path.join(URL, relative_path[2:])
    # creating necessary directories
    os.makedirs(os.path.join(file_path, "FXServer", "server"), exist_ok=True)
    # downloading server files
    req = requests.get(latest_stable_url)
    filename = latest_stable_url.split('/')[-1]
    with open(os.path.join(file_path, "FXServer", "server", filename), 'wb') as output_file:
        output_file.write(req.content)
    print('\nDownloading Completed')
    # extracting files from server.7z
    with py7zr.SevenZipFile(os.path.join(file_path, "FXServer", "server", "server.7z"), 'r') as archive:
        archive.extractall(path=os.path.join(file_path, "FXServer", "server"))
    # deleting server.7z after extraction
    os.remove(os.path.join(file_path, "FXServer", "server", "server.7z"))
    print("\nServer files extracted correctly")

    # cloning official cfx-server-data
    git.Repo.clone_from("https://github.com/citizenfx/cfx-server-data.git", os.path.join(file_path, "FXServer", "cfx-server-data"))
    print("\ncfx-server-data cloned successfully")

    # copying server.cfg and writing inputted data to it
    shutil.copyfile(os.path.join(file_path, "server.cfg"), os.path.join(file_path, "FXServer", "cfx-server-data", "server.cfg"))

    with open(os.path.join(file_path, "FXServer", "cfx-server-data", "server.cfg"), 'r') as file:
        content = file.read()
    # Replace string
    content = content.replace("changeme", f'"{lickey}"')
    content = content.replace('set steam_webApiKey""", f'set steam_webApiKey "{steamapi}"')
    # Write new content in write mode 'w'
    with open(os.path.join(file_path, "FXServer", "cfx-server-data", "server.cfg"), 'w') as file:
        file.write(content)

    print("\nprocess completed, you're good to go ;D")

def linux(lickey, steamapi):
    # getting latest recommended build for Linux
    URL = 'https://runtime.fivem.net/artifacts/fivem/build_proot_linux/master/'
    with requests.Session() as s:
    soup = BeautifulSoup(s.get(URL).content, "html.parser")
    relative_path = soup.find_all("div", {"class": "panel-block"})[0].next_element.next_element['href']
    latest_stable_url = os.path.join(URL, relative_path[2:])
    # creating necessary directories
    os.makedirs("/home/ubuntu/FXServer/server", exist_ok=True)
    # downloading server files
    req = requests.get(latest_stable_url)
    filename = latest_stable_url.split('/')[-1]
    with open(os.path.join("/home/ubuntu/FXServer/server", filename), 'wb') as output_file:
    output_file.write(req.content)
    print('\nDownloading Completed')
    # extracting files from fx.tar.xz
    os.system("cd /home/ubuntu/FXServer/server/ && tar xf fx.tar.xz")
    # deleting fx.tar.xz after extraction
    os.remove("/home/ubuntu/FXServer/server/fx.tar.xz")
    print("\nServer files extracted correctly")
    # cloning official cfx-server-data
    git.Repo.clone_from("https://github.com/citizenfx/cfx-server-data.git", "/home/ubuntu/FXServer/cfx-server-data")
    print("\ncfx-server-data cloned successfully")

    # copying server.cfg and writing inputted data to it
    shutil.copyfile("/home/ubuntu/server.cfg", "/home/ubuntu/FXServer/cfx-server-data/server.cfg")

    with open("/home/ubuntu/FXServer/cfx-server-data/server.cfg", 'r') as file:
        content = file.read()
    # Replace string
    content = content.replace("changeme", f'"{lickey}"')
    content = content.replace('set steam_webApiKey ""', f'set steam_webApiKey "{steamapi}"')
    # Write new content in write mode 'w'
    with open("/home/ubuntu/FXServer/cfx-server-data/server.cfg", 'w') as file:
        file.write(content)

    print("\nprocess completed, you're good to go ;D")
if name == "main":
    main()
                              

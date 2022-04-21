from bs4 import BeautifulSoup
import requests
import platform
import os
os.environ["GIT_PYTHON_REFRESH"] = "quiet"
import py7zr
import git
import shutil


def main():
    print("Provide your license key (https://keymaster.fivem.net)")
    lickey = input("~ % ")
    print("\nProvide your steam web api key (http://steamcommunity.com/dev/apikey)")
    steamapi = input("~ % ")
    #checking if os is windows or linux
    os = platform.system()
    if os == "Windows":        
        windows(lickey, steamapi)
    else:
        linux(lickey, steamapi)

def windows(lickey, steamapi):
    file_path = os.path.abspath(os.path.dirname(__file__))
    #getting latest recommended build for windows
    URL = 'https://runtime.fivem.net/artifacts/fivem/build_server_windows/master/'
    soup = BeautifulSoup(requests.get(URL).content, "html.parser")
    relative_path = soup.find_all("div", {"class": "panel-block"})[0].next_element.next_element['href']
    latest_stable_url = "{}{}".format(URL, relative_path[2:])
    #creating necessery directories
    os.mkdir(f"{file_path}/FXServer")
    os.mkdir(f"{file_path}/FXServer/server")
    #downloading server files
    req = requests.get(latest_stable_url)
    filename = latest_stable_url.split('/')[-1]  
    with open(f"{file_path}/FXServer/server/{filename}",'wb') as output_file:
        output_file.write(req.content)
    print('\nDownloading Completed')
    #extracting files from server.7z
    with py7zr.SevenZipFile(f"{file_path}/FXServer/server/server.7z", 'r') as archive:
        archive.extractall(path=f"{file_path}/FXServer/server")
    #deleting server.7z after extraction
    os.remove(f"{file_path}/FXServer/server/server.7z")
    print("\nServer files extracted correctly")

    #cloning official cfx-server-data
    git.Git(f"{file_path}/FXServer/").clone("https://github.com/citizenfx/cfx-server-data.git")
    print("\ncfx-server-data cloned successfully")

    #copying server.cfg and writing inputed data to it
    shutil.copyfile(f"{file_path}/server.cfg", f"{file_path}/FXServer/cfx-server-data/server.cfg")

    with open(f"{file_path}/FXServer/cfx-server-data/server.cfg", 'r') as file:
        content = file.read()
        content1 = file.read()
    # Replace string
    content = content.replace("changeme", f'"{lickey}"')
    content1 = content.replace('set steam_webApiKey ""', f'set steam_webApiKey "{steamapi}"')
    # Write new content in write mode 'w'
    with open(f"{file_path}/FXServer/cfx-server-data/server.cfg", 'w') as file:
        file.write(content)
        file.write(content1)

    print("\nprocess completed ure good to go ;D")

def linux(lickey, steamapi):
    #getting latest recommended build for windows
    URL = 'https://runtime.fivem.net/artifacts/fivem/build_proot_linux/master/'
    soup = BeautifulSoup(requests.get(URL).content, "html.parser")
    relative_path = soup.find_all("div", {"class": "panel-block"})[0].next_element.next_element['href']
    latest_stable_url = "{}{}".format(URL, relative_path[2:])
    #creating necessery directories
    os.mkdir("/home/ubuntu/FXServer")
    os.mkdir("/home/ubuntu/FXServer/server")
    #downloading server files
    req = requests.get(latest_stable_url)
    filename = latest_stable_url.split('/')[-1]  
    with open(f"/home/ubuntu/FXServer/server/{filename}",'wb') as output_file:
        output_file.write(req.content)
    print('\nDownloading Completed')
    #extracting files from fx.tar.xz
    os.system("cd /home/ubuntu/FXServer/server/ && tar xf fx.tar.xz")
    #deleting fx.tar.xz after extraction
    os.remove("/home/ubuntu/FXServer/server/fx.tar.xz")
    print("\nServer files extracted correctly")

    #cloning official cfx-server-data
    git.Git("/home/ubuntu/FXServer/").clone("https://github.com/citizenfx/cfx-server-data.git")
    print("\ncfx-server-data cloned successfully")

    #copying server.cfg and writing inputed data to it
    shutil.copyfile("/home/ubuntu/server.cfg", "/home/ubuntu/FXServer/cfx-server-data/server.cfg")

    with open("/home/ubuntu/FXServer/cfx-server-data/server.cfg", 'r') as file:
        content = file.read()
        content1 = file.read()
    # Replace string
    content = content.replace("changeme", f'"{lickey}"')
    content1 = content.replace('set steam_webApiKey ""', f'set steam_webApiKey "{steamapi}"')
    # Write new content in write mode 'w'
    with open("/home/ubuntu/FXServer/cfx-server-data/server.cfg", 'w') as file:
        file.write(content)
        file.write(content1)

    print("\nprocess completed ure good to go ;D")

if __name__ == "__main__":
    main()

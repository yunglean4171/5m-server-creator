
# 5m-server-creator (python 3.7.9)
## Preview: https://youtu.be/PhzwK4rsikg

## Script create FXServer directory and downloads latest artifacts for specified OS (windows or linux), then clones official fivem cfx-server-data repo and creates server.cfg with changed license key and steam web api key provided by user.

## Build with:
- Beautiful Soup
- GitPython
- py7zr
- requests

### Windows installation:
0. Install git on your pc: https://git-scm.com/downloads
1. [Download Python](https://www.microsoft.com/en-us/p/python-37/9nj46sx7x90p?activetab=pivot:overviewtab)
2. Install pip by running this commands:
```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
```
```
python get-pip.py
```
3. Install required packages by running this command:
```
pip install -r requirements.txt
```
4. Start app by running this command:
```
python3 main.py
```

### Linux installation:

0. Run this command to clone repo to your linux vps:
```
git clone https://github.com/yunglean4171/5m-server-creator.git
```
1. If python is not installed follow this [guide](https://phoenixnap.com/kb/how-to-install-python-3-ubuntu)
2. Install pip by running this commands:
```
sudo apt install python3-pip
```
3. Install required packages by running this command:
```
pip install -r requirements.txt
```
4. Start app by running this command:
```
python3 main.py
```

# Contributing
If you have some ideas that you want to suggest please make a [pull requests](https://github.com/yunglean4171/5m-server-creator/pulls) and if you found some bugs please make an [issue](https://github.com/yunglean4171/5m-server-creator/issues). Every contribution will be appreciated.

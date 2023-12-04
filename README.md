# NAO PLANNING CHALLENGE 2022 - ROBOerTo Bolle

### Authors:
Pietro Tellarini 	pietro.tellarini2@studio.unibo.it 
<br> Giorgia Bravi 	giorgia.bravi2@studio.unibo.it

### Github repository:
https://github.com/PtrTella/RoboErto

### Files and folders:
- [_FOLDER_] NAOMoves: containing all moves 
- [_FOLDER_] Music: containing song files .wav 
- [_FOLDER_] Videos: containing sample videos
- readme.md
- main.py
- coreography.py
- library.py
- music_play.py


# Setup:

To be able to excecute the project Python3 and Python2 must be installed. This project is tested on Python2 v. 2.7.15 and Python3 v. 3.12.0.

Python2 is used to run the NAOqi SDK, while Python3 is used for the rest of the project. To download and extract naoqi, follow this [guide](http://doc.aldebaran.com/2-5/dev/community_software.html#retrieving-software)


- Create a Python Virtual Enviroment.
```
python3 -m venv [name]
```
- Access it running the "activate" script in the Bin folder.
```
source [name]/bin/activate
```
- Use PIP to install the requirements
```
python3 -m pip install -r requirements.txt
```
# To run the Code:
- Open Coreographe->Edit->Preferences and Select the **NAO H25 (V40) Robot Model**.
- Run The Code:

```
python3 main.py
```
- **IMPORTANT:** python2 is the alias for python2.7 in the main.py file. If your python2 is not 2.7, you need to change the alias in the main.py file.

- Follow the instructions. If you want another song, you need to add it in the "Music" folder as a .wav file.

- Enjoy the coreography!


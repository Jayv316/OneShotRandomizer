input("This program will only work if its run in the same directory as the OneShot folder (Steam/steamapps/common)\nThe program might not work if it's not run with administrator permissions. (open the program/console window as an administrator)\nThis program changes game files. It will make a backup of the changed files when run. The backup is placed in the same directory as the program and is named 'Audio_backup'.\nTo restore the game's files from the backup, rename the backup folder to 'Audio' and drag it into the OneShot game folder. You can also verify the game's files through Steam.\nPress enter/return to continue.")
print("Loading..")
import os
from random import randint
from sys import exit as sysexit
from shutil import rmtree, copy, SameFileError
def makefolder(target):
    try:
        os.mkdir(f"{os.getcwd()}/{target}")
    except FileExistsError:
        pass
    except:
        input(f"There was an error with making a folder. Try deleting the target folder ({target})")
        sysexit()
if os.path.exists(os.getcwd() + "/OneShotTemp"):
    rmtree(os.getcwd() + "/OneShotTemp")
print("Loaded!")
responses = ["y", "yes", "n", "no"]
detail = input("Do you want to see it happen? (yes/no)\n")
if not detail.lower() in responses:
    while not detail.lower() in responses:
        detail = input("Do you want to see it happen? (yes/no)\n")
if detail.lower() == "y" or detail.lower() == "yes":
    detail = True
elif detail.lower() == "n" or detail.lower() == "no":
    detail = False
rlong = input("Do you want to randomize long sound effects? (may cause lag ingame. yes/no)\n")
if not rlong.lower() in responses:
    while not rlong.lower() in responses:
        rlong = input("Do you want to randomize long sound effects? (may cause lag ingame. yes/no)\n")
if rlong.lower() == "y" or rlong.lower() == "yes":
    rlong = True
elif rlong.lower() == "n" or rlong.lower() == "no":
    rlong = False
print("Preparing...")
bgmpath = "./OneShot/Audio/BGM"
if rlong:
    bgspath = "./OneShot/Audio/BGS"
mepath = "./OneShot/Audio/ME"
sepath = "./OneShot/Audio/SE"
bgm = os.listdir(bgmpath)
if rlong:
    bgs = os.listdir(bgspath)
me = os.listdir(mepath)
se = os.listdir(sepath)
bgmlen = len(bgm)
sfxlen = [len(bgs) if rlong else 0, len(me), len(se)]
files = []
if rlong:
    for file in bgs:
        files.append(f"{bgspath}/{file}")
for file in me:
    files.append(f"{mepath}/{file}")
for file in se:
    files.append(f"{sepath}/{file}")
makefolder("OneShotTemp")
makefolder("OneShotTemp/Audio")
makefolder("OneShotTemp/Audio/BGM")
makefolder("OneShotTemp/Audio/BGS")
makefolder("OneShotTemp/Audio/ME")
makefolder("OneShotTemp/Audio/SE")
print("Ready!")
print("Making sound backup...")
makefolder("Audio_backup")
makefolder("Audio_backup/BGM")
makefolder("Audio_backup/BGS")
makefolder("Audio_backup/ME")
makefolder("Audio_backup/SE")
for file in files:
    try:
        copy(f"{os.getcwd()}/{file[1:]}", f"{os.getcwd()}/Audio_backup/{file[file.rfind('io/')+2:]}")
    except FileExistsError or SameFileError:
        pass
for file in bgm:
    try:
        copy(f"{os.getcwd()}/{bgmpath[2:]}/{file}", f"{os.getcwd()}/Audio_backup/BGM/{file}")
    except FileExistsError or SameFileError:
        pass
print(f"Backup made! (./Audio_backup)")
print("Randomizing sfx...")
usedsfx = []
for file in files:
    choice = randint(0, len(files)-1)
    if choice in usedsfx:
        while choice in usedsfx:
            choice = randint(0, len(files)-1)
            if not choice in usedsfx:
                break
    copy(f"{os.getcwd()}/{file[1:]}", f"{os.getcwd()}/OneShotTemp{files[choice][9:]}")
    if detail:
        print(f"{file[file.rfind('/')+1:]} changed to {files[choice][files[choice].rfind('/')+1:]}")
    usedsfx.append(files.index(files[choice]))
print("Randomized sfx!")
print("Randomizing music...")
usedmus = []
for file in bgm:
    choice = randint(0, len(bgm)-1)
    if choice in usedmus:
        while choice in usedmus:
            choice = randint(0, len(bgm)-1)
            if not choice in usedsfx:
                break
    copy(f"{os.getcwd()}/{bgmpath[2:]}/{file}", f"{os.getcwd()}/OneShotTemp/Audio/BGM/{bgm[choice]}")
    if detail:
        print(f"{file} changed to {bgm[choice]}")
    usedmus.append(bgm.index(bgm[choice]))
print("Randomized music!")
print("Cleaning up...")
rmtree(f"{os.getcwd()}/{bgmpath[2:]}")
if rlong:
    rmtree(f"{os.getcwd()}/{bgspath[2:]}")
rmtree(f"{os.getcwd()}/{mepath[2:]}")
rmtree(f"{os.getcwd()}/{sepath[2:]}")
os.mkdir(bgmpath)
if rlong:
    os.mkdir(bgspath)
os.mkdir(mepath)
os.mkdir(sepath)
nbgmpath = "./OneShotTemp/Audio/BGM"
if rlong:
    nbgspath = "./OneShotTemp/Audio/BGS"
nmepath = "./OneShotTemp/Audio/ME"
nsepath = "./OneShotTemp/Audio/SE"
nbgm = os.listdir(nbgmpath)
if rlong:
    nbgs = os.listdir(nbgspath)
nme = os.listdir(nmepath)
nse = os.listdir(nsepath)
for file in nbgm:
    copy(f"{nbgmpath}/{file}", f"{bgmpath}/{file}")
if rlong:
    for file in nbgs:
        copy(f"{nbgspath}/{file}", f"{bgspath}/{file}")
for file in nme:
    copy(f"{nmepath}/{file}", f"{mepath}/{file}")
for file in nse:
    copy(f"{nsepath}/{file}", f"{sepath}/{file}")
rmtree(f"{os.getcwd()}/OneShotTemp")
print("Done!")
if detail:
    print(f"Changed {bgmlen} music files to {len(os.listdir(bgmpath))} and {sfxlen[0]+sfxlen[1]+sfxlen[2]} sound effect files to {len(os.listdir(bgspath)) if rlong else 0 + len(os.listdir(mepath)) + len(os.listdir(sepath))}\nThe values should be equal. If they aren't, something probably went wrong. Thats why backups are made! (Audio_backup)")
    input()
sysexit()
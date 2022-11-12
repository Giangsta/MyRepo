import shutil
import re
import os

def rename_file(destination, str, season):
    file = str.split("\\")[-1]
    parts = re.split(r'[][.]', file)
    name = [i for i in parts if i][0]
    type = [i for i in parts if i][-1]
    episode = [i for i in parts if i][2].strip()[-2:]
    out_file = "{0}\\{1}\\Season {2}\\{1} - s{2}e{3}.{4}".format(destination, name, season, episode, type)
    return out_file

def ss_rename_file(destination, str, season, index):
    file = str.split("\\")[-1]
    parts = re.split(r'[][.]', file)
    name = [i for i in parts if i][0]
    type = [i for i in parts if i][-1]
    episode = "{:02d}".format(index)
    out_file = "{0}\\{1}\\Season {2}\\{1} - s{2}e{3}.{4}".format(destination, name, season, episode, type)
    return out_file

def dirPath(destination, str, season):
    file = str.split("\\")[-1]
    parts = re.split(r'[][.]', file)
    name = [i for i in parts if i][0]
    out_file = "{0}\\{1}\\Season {2}".format(destination, name, season)
    return out_file    

def Main(source, destination, number, option):
    source_files = []

    for root, dirs, files in os.walk(source):
        for file in files:
            source_files.append(os.path.join(root,file))


    for index, source_file in enumerate(source_files):
        ss_destination_file = ss_rename_file(destination, source_file, number, index+1)
        destination_file = rename_file(destination, source_file, number)
        path = dirPath(destination, source_file, number)
        if not os.path.exists(path):
            os.mkdir(path)
        if option == 1:
            shutil.copyfile(source_file, ss_destination_file)
        elif option == 0:
            shutil.copyfile(source_file, destination_file)

if __name__ == "__main__":
    # 0 = [One Pace][XXX-XXX] {ARC} {##} [###p][########].mkv
    # 1 = [One Pace] Chapter 700-701 [###p][########].mkv
    option = 0 # Set option as per video file name format ^^
    source = r"C:\Users\Simon\Documents\One Pace\[One Pace][603-653] Fishman Island [720p]" # Set source location
    destination = r"C:\Users\Simon\Documents\Plex\TV Shows" # Set destination location
    season = 26 # set season number
    Main(source, destination, season, option)

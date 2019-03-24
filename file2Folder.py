#!/usr/bin/env python
# coding: utf-8

import os
import shutil
import sys


def createFolder(fullPathName):
    try:
        if not (os.path.isdir(fullPathName)):
            os.makedirs(os.path.join(fullPathName))
    except OSError as e:
        if e.errno != errno.EEXIST:
            print("Failed to create directory!!!!!")
            raise

def moveToFolder(path, fileName, seperator) :
    split_list = fileName.split(seperator)
    if (len(split_list) < 2):
        return False

    folderName = split_list[0].strip()

    destPath = path + '\\' + folderName
    createFolder(destPath)
    srcFile = path + '\\' + fileName
    destFile = destPath + '\\' + fileName
    print(srcFile+ '->' + destFile)
    #shutil.move(srcFile, destFile)
    return True

def main(path, sep):
    print("=== " + path + '===' )
    file_list = os.listdir(path)
    count = 0
    for file in file_list:
        fullFilename = os.path.join(path, file)
        if os.path.isfile(fullFilename):
            if moveToFolder(path, file, sep) == True :
                count = count + 1
    print("=====" + str(count) + "files moved" + "====")

if __name__ == "__main__":
    if len(sys.argv) != 3 :
        print("invalid argument")
    main(sys.argv[1], sys.argv[2])





#!/usr/bin/env python
# coding: utf-8

import os.path
import shutil
import sys
from optparse import OptionParser


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
    shutil.move(srcFile, destFile)
    return True

def main(path, sep, ext):
    print("=== " + path + '===' )
    file_list = os.listdir(path)
    count = 0

    if ext == None :
        for file in file_list:
             fullFilename = os.path.join(path, file)
             if os.path.isfile(fullFilename):
                 if moveToFolder(path, file, sep) == True :
                     count = count + 1
    else:
        ext = ext.lower()
        for file in file_list:
            fullFilename = os.path.join(path, file)
            if os.path.isfile(fullFilename):
                fname, fext = os.path.splitext(fullFilename)

                if len(fext) == 0 :
                    continue

                if fext[1:].lower() == ext :
                    if moveToFolder(path, file, sep) == True :
                        count = count + 1

    print("=====" + str(count) + "files moved" + "====")

if __name__ == "__main__":
    option = OptionParser(usage='%prog', version='%prog 1.0')

    option.add_option('-s', '--seperator', dest='sep', type='string', help='Input seperator string.')
    option.add_option('-e', '--ext', dest='ext', type='string', help='Input file ext string.')

    (options, args) = option.parse_args()

    print ('option 정보 : %s' % options)
    print ('args 정보 : %s' % args)

    if (options.sep == None) :
        options.sep = '-'

    if len(args) == 1 :
        main(args[0], options.sep, options.ext)
    else:
        print("Input process path")

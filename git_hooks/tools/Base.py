#!/usr/bin/env python
import subprocess, sys, os

ROOT = "./"

def checkResult(result, file):
    if result == 1:
        print(file + ": Nastal problem ve volani gitu")
    elif result != 0:
        print(file + ": Neznama chyba")
    if result != 0:
        sys.exit(result)

################################################################################################################
# walk all scripts in given path and call them. Exit on fatal error
def callScriptsInDirectory(directoryPath):
    if os.path.isdir(directoryPath):
        for item in os.listdir(directoryPath):
            file = os.path.join(directoryPath, item)
            if os.path.isfile(file):
                fileName, fileExtension = os.path.splitext(file)
                if fileExtension == ".py":
                    checkResult(subprocess.call(["python", file] + sys.argv[1:], shell = True), item)
                elif fileExtension == ".sh":
                    checkResult(subprocess.call(["sh", file] + sys.argv[1:], shell = True), item)

#!/usr/bin/env python
# common methods that use git
import os, sys, subprocess

ROOT = "./"

################################################################################################################
# calls command and returns output from standard output
def call(command):
    return subprocess.check_output(command.split(" "), stderr = subprocess.STDOUT).decode("utf-8")

################################################################################################################
# this method applies callbackFunction to all files staged for commit, than re-adds the files by calling git add
def applyToStagedFiles(callbackFunction, extension):
    try:
        # Check all files in the staging-area:
        gitStatus = call("git status --porcelain -uno")

        # Sort all pro files staged to commit:
        for line in gitStatus.splitlines():
            elements = line.split()
            if any(s in elements[0] for s in ("M", "R", "A")): # apply only to (M)odified, (R)enamed or (A)dded files
                path = os.path.join(ROOT, elements[-1])     # the result file should be the last item in the git status output
                if path.endswith(extension):
                    callbackFunction(path)
                    subprocess.call(["git", "add", path])  # we have to call git add on the modified file to commit the changes

    except subprocess.CalledProcessError:
        # There was a problem calling "git status".
        sys.exit(1)

################################################################################################################
# this method applies callbackFunction to all files in the last commit
def applyToCommitedFiles(callbackFunction, extension):
    try:
        # Check all files in the staging-area:
        commitedFiles = call("git diff-tree --name-only --no-commit-id -r HEAD")

        for line in commitedFiles.splitlines():
            path = os.path.join(ROOT, line)     # the result file should be the last item in the git diff-tree output
            if path.endswith(extension) and os.path.isfile(path):
                callbackFunction(path)
                subprocess.call(["git", "add", path])  # we have to call git add on the modified file to commit the changes

    except subprocess.CalledProcessError:
        # There was a problem calling "git diff-tree".
        sys.exit(1)

################################################################################################################
# this method returns branch name of the HEAD
def getBranchName():
    try:
        branchName = call("git rev-parse --abbrev-ref HEAD")
        branchName = branchName.strip()
        return branchName

    except subprocess.CalledProcessError:
        # There was a problem calling "git rev-parse".
        sys.exit(1)

################################################################################################################
# this method returns hash of the HEAD commit
def getHeadShortHash():
    try:
        branchHash = call("git rev-parse --short HEAD")
        branchHash = branchHash.strip()
        return branchHash

    except subprocess.CalledProcessError:
        # There was a problem calling "git rev-parse".
        sys.exit(1)

################################################################################################################
# this method returns commit message of given commit
def getCommitMessage(commit = "HEAD"):
    try:
        message = call("git log --format=%B -n 1 " + commit)
        return message.strip()

    except subprocess.CalledProcessError:
        sys.exit(1)

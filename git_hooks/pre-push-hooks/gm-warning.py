#!/usr/bin/env python
import tkinter.messagebox
import sys

def createMessageBox(branch):
    """ Creates GUI question to confirm push to a branch """
    root = tkinter.Tk()  # create window
    root.withdraw()
    question = tkinter.messagebox.askquestion(f'Push to grandmaster',
                                              f'Do you really want to push commit directly to {branch}? \r\n'
                                              f'This should only be done when merging integration branch with blocked calendar Merge to GM.')
    result = question == 'yes'
    root.destroy()
    return result


stdin = []
for line in sys.stdin:
    stdin.append(line)

if len(stdin) > 0:
    data = stdin[0].split(" ")
    if len(data) == 4 and data[2].endswith("grandmaster"):
        print("Pre-push hook: Please confirm push to grandmaster in the dialog.", flush=True)
        result = createMessageBox(data[2])
        if not result:
            sys.exit(1)

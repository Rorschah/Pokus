#!/usr/bin/env python
import sys
sys.path.append('./git_hooks')
import tools.Base

tools.Base.callScriptsInDirectory("./git_hooks/pre-push-hooks/")

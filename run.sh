#!/bin/bash

#Note that we assume that we are running from the directory that where
#everything is located.  If you want to move this script, set the $SCRIPT_DIR
#variable some other way

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd $SCRIPT_DIR

source $SCRIPT_DIR/venv/bin/activate
python $SCRIPT_DIR/main.py

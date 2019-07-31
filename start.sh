#!/bin/sh

source ~/venvs/asmt_rolls/bin/activate
setsid sqlite_web -p 7070 -H 0.0.0.0 -r -x ~/workspace/asmt_rolls/asmt.sqlite3 &
deactivate

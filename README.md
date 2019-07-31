== Notes ==

Use sqlite-web to view database in a browser.

```
yum install python3 pip3 sqlite
mkdir -p ~/venvs
python3 -m venv ~/venvs/asmt_rolls
source ~/venvs/asmt_rolls/bin/activate

sqlite_web -p 7070  -H 0.0.0.0 -x asmt.sqlite3
```

Sometimes files will have ^L when viewed in vim, to remove these characters,
do `:%s/^L//g`. You can make the ^L character by hitting Ctrl-l.

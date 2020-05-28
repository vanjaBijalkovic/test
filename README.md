# Backend Startkit
Template to get my favourite SQL stack up and running


![diagram](https://github.com/mekanix/backend-startkit/raw/master/backend.png)

## Forking
The `name.py` is special! Although it ends with .py, it is read by shell scripts and CBSD/Reggae `Makefile` (if you're using it). Because it's not regular Python file, it has some limitations. It should consist of one line:

```
app_name="application"  # noqa: E225
```

There must be no space around `=` in the previous example, otherwise shell scripts won't work. The `noqa` part prevents `flake8` failing the test, because it normally requires spaces around `=`.

On fork, edit `name.py` and rename `application` directory acordingly.

install requirements:

$ pip3 install -r req.txt

run on port 8080:

$ python3 wsgi.py

run tests:

$ python3 -m pytest .

run and create migrations (you will need to manually override some lines):

$ python -m flask migration create {name}

remove redundant change_field() lines in /migrations/name_0001.py etc...

$ python -m flask migration run

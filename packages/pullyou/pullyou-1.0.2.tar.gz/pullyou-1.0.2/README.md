PullYou is a tool for opening the PR associated with a given git hash.

Install
--------
```
pip3 install pullyou
```

Usage
--------
```
$ pullyou 2aaf764552e012ac33cd7b2d6

$ pullyou 2aaf76455 --repo transcom/mymove
```

Auth
------
If accessing a private repository, create a github personal access token with the `repo` scope and drop it in ~/.github_token as `username:token`

Releasing
-------------
```
$ python setup.py sdist bdist_wheel
$ twine upload dist/* [-r testpypi]
$ rm -rf dist/*
* tag the release
* bump the version number
```

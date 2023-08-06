# pypi-downloader

This project can be used to mirror the pypi index using the new warehouse API.

This project consists of three scripts:

1. the main single threaded script pypi-downloader.py
1. a multithreaded version of the main script, pypi-downloader-mt.py
1. a helper script to get the current list of packages from the pypi index site currently located at: <https://pypi.org/>

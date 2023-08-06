#!/usr/bin/env python3
import cgi
import cgitb
import os
import subprocess

# enable detailed error messages
cgitb.enable()

# set content type
print("Content-type:text/html\r\n\r\n")

# run the Python file and capture output
result = subprocess.run(['python3', 'your_python_file.py'], stdout=subprocess.PIPE)

# print the output
print(result.stdout.decode())

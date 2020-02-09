# Notes
* Make sure to make notifications to php.ini file to disable the disable_functions, or comment it out.
This is necessary to allow shell_exec or exec() functions to run the script.
* Add www-data to sudoers file:
```
www-data ALL=(ALL) NOPASSWD: ALL
```
* Add to the python files:
```
#!/bin/env/python3
```
* Make all Python files executables via:
```
sudo chmod +x filename.py
```

# Prerequisites
* Apache2
```
sudo apt install apache2
```
* PHP
```
sudo apt install php
```
* Python-dev
```
sudo apt install python-dev
```
* Python3-dev
```
sudo apt install python3-dev
```
* Setuptools
```
pip install setuptools
```
* Wheel
```
pip install wheel
```
* Requests : Making HTTP(S) requests
```
pip install requests
```
* Numpy
```
pip install numpy
```
* Matplotlib
```
pip install matplotlib
```
* JSON
```
pip install json
```
* Scikit-learn
```
pip install scikit-learn
```

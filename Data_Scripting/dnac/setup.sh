#! /bin/bash

echo "Cloning Github Repo"
git clone https://github.com/taltechmentor/scripts.git

echo "Changing Directory"
cd scripts 

echo "Creating Python Virtual Environment"
python3 -m venv venv 

echo "Activating Virtual Environment"
source venv/bin/activate 

python3 -m pip install -r requirements.txt


echo "Running Script"
python3 interface-SpeedReport.py 

echo "Opening Project in Visual Studio Code"
code .
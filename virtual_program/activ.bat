deactivate
call env/Scripts/activate.bat
python -m pip install --upgrade pip
pip freeze > requirement.txt
cmd

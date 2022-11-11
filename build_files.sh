#build_files.sh
pip install virtualenv
virtualenv venv 
source venv/bin/activate
pip install -r requirements.txt
python3.10 manage.py collectstatic

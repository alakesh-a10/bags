#build_files.sh
pip install virtualenv
virtualenv venv 
source venv/bin/activate
pip install -r requirements.txt
python manage.py collectstatic

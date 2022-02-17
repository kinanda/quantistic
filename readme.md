# Important
Only install Python 3.8
Only install Rasa 2.8.6

# How to install
python -m venv env
.\env\Scripts\activate
pip install --upgrade pip
pip install -r .\requirements.txt

# How to make Django migrations
python .\manage.py makemigrations dashboard --name add_path

# How to start Django app
cd C:\Users\Kinanda\Documents\Django\quantistic
.\env\Scripts\activate
python .\manage.py runserver

# How to start Rasa app
cd C:\Users\Kinanda\Documents\Django\rasa
.\env\Scripts\activate
rasa train
rasa run --credentials ./credentials.yml  --enable-api --model ./models --endpoints ./endpoints.yml --cors "*"

# How to start Packetriot
C:\Users\Kinanda\Documents\Packetriot\pktriot.exe start

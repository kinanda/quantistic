# Important
Only install Python 3.8<br/>
Only install Rasa 2.8.6<br/>

# How to install
python -m venv env<br/>
.\env\Scripts\activate<br/>
pip install --upgrade pip<br/>
pip install -r .\requirements.txt<br/>

# How to make Django migrations
python .\manage.py makemigrations dashboard --name add_path<br/>

# How to start Django app
cd C:\Users\Kinanda\Documents\Django\quantistic<br/>
.\env\Scripts\activate<br/>
python .\manage.py runserver<br/>

# How to start Rasa app
cd C:\Users\Kinanda\Documents\Django\rasa<br/>
.\env\Scripts\activate<br/>
rasa train<br/>
rasa run --credentials ./credentials.yml  --enable-api --model ./models --endpoints ./endpoints.yml --cors "*"<br/>

# How to start Packetriot
C:\Users\Kinanda\Documents\Packetriot\pktriot.exe start<br/>

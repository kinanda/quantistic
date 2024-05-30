# Prerequisites
- Install Python 3.8.x (manual installation; download and install at python website)<br/>
- Install VSCode and open quantistic project folder (e.g. C:\Users\Kinanda\Documents\Django\quantistic)<br/><br/>

# Setup: Install quantistic project (VSCode Terminal)
- Copy paste line by line into terminal, wait until each command finish:<br/><br/>
cd C:\Users\Kinanda\Documents\Django\quantistic (replace with your quantistic path)<br/>
python -m venv env<br/>
.\env\Scripts\activate<br/>
pip install --upgrade pip<br/>
pip install -r .\requirements.txt<br/>
python manage.py migrate<br/>
python manage.py createsuperuser<br/><br/>

# Run: Start quantistic app (Open VSCode Terminal)
- Copy paste line by line into terminal, wait until each command finish:<br/><br/>
cd C:\Users\Kinanda\Documents\Django\quantistic (replace with your quantistic path)<br/>
.\env\Scripts\activate<br/>
python .\manage.py runserver<br/><br/>
- Access app via browser: http://127.0.0.1:8000/<br/><br/>

# Optional: Packetriot command
- Copy paste line by line into cmd:<br/><br/>
C:\Users\Kinanda\Documents\Packetriot\pktriot.exe --config C:\Users\Kinanda\.pktriot\config.json start<br/><br/>
- Access app via browser: https://amazing-lake-73054.pktriot.net/<br/><br/>

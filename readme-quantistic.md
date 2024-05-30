# Prerequisites
- Only install Python 3.8.x (manual installation; download and install at python website)<br/>
- Only install Rasa 2.8.6 (automatic installation; ignore this)<br/><br/>
- Open 2 instances of VSCode:<br/>
  - VSCode #1 for rasa
  - VSCode #2 for quantistic<br/><br/>

# Setup Step #1: Install rasa project (VSCode #1 Terminal)
- Copy paste line by line into terminal, wait until each command finish:<br/><br/>
cd C:\Users\Kinanda\Documents\Django\rasa (replace with your rasa path)<br/>
python -m venv env<br/>
.\env\Scripts\activate<br/>
pip install --upgrade pip<br/>
pip install -r .\requirements.txt<br/><br/>

# Setup Step #2: Install quantistic project (VSCode #2 Terminal)
- Copy paste line by line into terminal, wait until each command finish:<br/><br/>
cd C:\Users\Kinanda\Documents\Django\quantistic (replace with your quantistic path)<br/>
python -m venv env<br/>
.\env\Scripts\activate<br/>
pip install --upgrade pip<br/>
pip install -r .\requirements.txt<br/>
python manage.py migrate<br/>
python manage.py createsuperuser<br/><br/>

# Setup Step #3: Initialize quantistic database (VSCode #2 Terminal)
- Copy paste all lines into terminal:<br/><br/>
python manage.py shell<br/>
from chatbot.models import Method, Flowchart, SamplingMethod, SamplingFlowchart<br/>
method1 = Method(name="Chi-Square Test One and Two Sample", description="Chi-Square Test One and Two Sample")<br/>
method2 = Method(name="Regression Analysis", description="Regression Analysis")<br/>
method3 = Method(name="Fmax Test, Brown & Smythe's Test or Bartlett's Test", description="Fmax Test, Brown & Smythe's Test or Bartlett's Test")<br/>
method4 = Method(name="Pearson's R", description="Pearson's R")<br/>
method5 = Method(name="Spearman's Rank Correlation", description="Spearman's Rank Correlation")<br/>
method6 = Method(name="Student's Unpaired T-Test or Paired T-Test", description="Student's Unpaired T-Test or Paired T-Test")<br/>
method7 = Method(name="Mann-Whitney U or Wilcoxon Rank Sums Test", description="Mann-Whitney U or Wilcoxon Rank Sums Test")<br/>
method8 = Method(name="ANOVA Test", description="ANOVA Test")<br/>
method9 = Method(name="Kruskal-Wallis Test", description="Kruskal-Wallis Test")<br/>
method1.save()<br/>
method2.save()<br/>
method3.save()<br/>
method4.save()<br/>
method5.save()<br/>
method6.save()<br/>
method7.save()<br/>
method8.save()<br/>
method9.save()<br/>
flowchart1 = Flowchart(path="2", method=Method.objects.get(pk=1))<br/>
flowchart2 = Flowchart(path="111", method=Method.objects.get(pk=2))<br/>
flowchart3 = Flowchart(path="121", method=Method.objects.get(pk=3))<br/>
flowchart4 = Flowchart(path="1121", method=Method.objects.get(pk=4))<br/>
flowchart5 = Flowchart(path="1122", method=Method.objects.get(pk=5))<br/>
flowchart6 = Flowchart(path="12211", method=Method.objects.get(pk=6))<br/>
flowchart7 = Flowchart(path="122121", method=Method.objects.get(pk=6))<br/>
flowchart8 = Flowchart(path="122122", method=Method.objects.get(pk=7))<br/>
flowchart9 = Flowchart(path="122221", method=Method.objects.get(pk=8))<br/>
flowchart10 = Flowchart(path="122222", method=Method.objects.get(pk=9))<br/>
flowchart11 = Flowchart(path="12221", method=Method.objects.get(pk=8))<br/>
flowchart1.save()<br/>
flowchart2.save()<br/>
flowchart3.save()<br/>
flowchart4.save()<br/>
flowchart5.save()<br/>
flowchart6.save()<br/>
flowchart7.save()<br/>
flowchart8.save()<br/>
flowchart9.save()<br/>
flowchart10.save()<br/>
flowchart11.save()<br/>
smethod1 = SamplingMethod(name="Convenience Method", description="Convenience Method")<br/>
smethod2 = SamplingMethod(name="Quota Samples", description="Quota Samples")<br/>
smethod3 = SamplingMethod(name="Judgemental Samples", description="Judgemental Samples")<br/>
smethod4 = SamplingMethod(name="Stratified Sampling", description="Stratified Sampling")<br/>
smethod5 = SamplingMethod(name="Simple Random Sampling", description="Simple Random Sampling")<br/>
smethod6 = SamplingMethod(name="Cluster Sampling", description="Cluster Sampling")<br/>
smethod1.save()<br/>
smethod2.save()<br/>
smethod3.save()<br/>
smethod4.save()<br/>
smethod5.save()<br/>
smethod6.save()<br/>
sflowchart1 = SamplingFlowchart(path="aa", method=SamplingMethod.objects.get(pk=1))<br/>
sflowchart2 = SamplingFlowchart(path="ab", method=SamplingMethod.objects.get(pk=2))<br/>
sflowchart3 = SamplingFlowchart(path="ac", method=SamplingMethod.objects.get(pk=3))<br/>
sflowchart4 = SamplingFlowchart(path="ba", method=SamplingMethod.objects.get(pk=4))<br/>
sflowchart5 = SamplingFlowchart(path="bb", method=SamplingMethod.objects.get(pk=5))<br/>
sflowchart6 = SamplingFlowchart(path="bc", method=SamplingMethod.objects.get(pk=6))<br/>
sflowchart1.save()<br/>
sflowchart2.save()<br/>
sflowchart3.save()<br/>
sflowchart4.save()<br/>
sflowchart5.save()<br/>
sflowchart6.save()<br/>
quit()<br/><br/>

# Run Step #1: Start rasa app (VSCode #1 Terminal)
- Copy paste line by line into terminal, wait until each command finish:<br/><br/>
cd C:\Users\Kinanda\Documents\Django\rasa (replace with your rasa path)<br/>
python -m venv env<br/>
.\env\Scripts\activate<br/>
rasa train<br/>
rasa run --credentials ./credentials.yml  --enable-api --model ./models --endpoints ./endpoints.yml --cors "*"<br/><br/>

# Run Step #2: Start quantistic app (Open VSCode #2 Terminal)
- Copy paste line by line into terminal, wait until each command finish:<br/><br/>
cd C:\Users\Kinanda\Documents\Django\quantistic (replace with your quantistic path)<br/>
.\env\Scripts\activate<br/>
python .\manage.py runserver 127.0.0.1:8080<br/><br/>

# Run Step #3: How to access app
- access app via browser: http://127.0.0.1:8080/<br/>
- access admin dashboard via browser: http://127.0.0.1:8080/admin<br/><br/>

# Extra Tips: Command to implement Django migrations
- In case you want to change database model, you need to create and apply a migration<br/>
- Copy paste line by line into terminal, wait until each command finish:<br/><br/>
python .\manage.py makemigrations accounts --name insert_migration_name_here<br/>
python .\manage.py makemigrations chatbot --name insert_migration_name_here<br/>
python .\manage.py makemigrations dashboard --name insert_migration_name_here<br/>
python manage.py migrate<br/><br/>

Python </br>
Classe & Objects </br>
OOPS - Python </br>
Git - Gitgub </br>
Python UnitTest - pyTest </br>
Reporting - pip install allure-pytest </br>

<b>How to execute</b></br>
python -m pytest com\py\train\test</br>

<b>How to execute with xml report generated</b></br>
python -m pytest com\py\train\test --junitxml=result.xml</br>

<b>Sharing result online</b></br>
python -m pytest --pastebin=all com\py\train\test --junitxml=result.xml

<b>Generating result log</b></br>
python -m pytest --pastebin=all --resultlog=log com\py\train\test --junitxml=result.xml 

<b>Generating allure report</b></br>
python -m pytest --alluredir=. com\py\train\test
allure generate .
allue open   "OR" allure serve
     


<b>pyTest execution help</b></br>
https://docs.pytest.org/en/latest/usage.html#sending-test-report-to-online-pastebin-service

default:
	@cat makefile

env:
	python3 -m venv env; . env/bin/activate; pip install --upgrade pip

update: env
	. env/bin/activate; pip install -r requirements.txt

ygainers.html:
	sudo google-chrome-stable --headless --disable-gpu --dump-dom --no-sandbox --timeout=5000 'https://finance.yahoo.com/markets/stocks/gainers/?start=0&count=200' > ygainers.html

ygainers.csv: ygainers.html
	python -c "import pandas as pd; from datetime import datetime; from pytz import timezone; raw = pd.read_html('ygainers.html'); tz = timezone('US/Eastern'); now = datetime.now(tz); raw[0].to_csv(f'ygainers_{now.year}_{now.month}_{now.day}_{now.hour}_{now.minute}.csv')"

wsjgainers.html:
	sudo google-chrome-stable --headless --disable-gpu --dump-dom --no-sandbox 'https://www.wsj.com/market-data/stocks/us/movers' > wsjgainers.html

wsjgainers.csv: wsjgainers.html
	python -c "import pandas as pd; from datetime import datetime; from pytz import timezone; raw = pd.read_html('wsjgainers.html'); tz = timezone('US/Eastern'); now = datetime.now(tz); raw[0].to_csv(f'wsjgainers_{now.year}_{now.month}_{now.day}_{now.hour}_{now.minute}.csv')"

lint:
	pylint bin/normalize_csv.py
	pylint get_gainer.py
	pylint bin/base.py
	pylint bin/factory.py
	pylint bin/yahoo.py
	pylint bin/wsj.py

test: lint
	pytest -vv tests

gainers:
	python get_gainer.py ${SRC}

final_git_push: lint test
	git push

clean:
	rm ygainers.html; rm wsjgainers.html

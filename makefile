CC = python3
MAIN = main.py

default: run

run: 
	$(CC) $(MAIN)

install: requirements.txt
	pip3 install -r requirements.txt

clean:
	rm -rf geckodriver.log

all:
	@echo "make run-selenium"
	@echo "make run-webdriver"

run-selenium:
	java -jar selenium-server-standalone-2.24.1.jar &
	sleep 1
	python selenium/test.py

run-webdriver:
	python webdriver/test.py

install-libs:
	apt-get install python firefox
	wget http://selenium.googlecode.com/files/selenium-server-standalone-2.24.1.jar

clean:
	find ./ -name *.pyc -exec rm -f {} \;
	rm *.txt


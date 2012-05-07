
all:
	@echo "make run-hello-world"
	@echo "make run-fibonacci"
	@echo "make run-django"
	@echo "make install-libs"
	@echo "make install-django"

run-hello-world:
	python hello-world/hello-world.py

run-fibonacci:
	python fibonacci/fibonacci.py

run-django:
	cd djangodemo && python manage.py syncdb && python manage.py runserver

install-libs:
	apt-get install python

install-django:
	rm -rf git-django/
	git clone https://github.com/django/django.git git-django
	cd git-django && python setup.py install
	rm -rf git-django/

clean:
	find ./ -name *.pyc -exec rm -f {} \;
	rm -f djangodemo/demodb


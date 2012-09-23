
all:
	@echo "make run-css"
	@echo "make run-less"
	@echo "make run-sass"
	@echo "make run-stylus"
	@echo "make install-libs"

run-css:
	firefox css/index.html

run-less:
	firefox less/index.html

run-sass:
	sass -t compressed --update sass/style.sass
	firefox sass/index.html

run-stylus:
	stylus -c stylus/style.styl
	firefox stylus/index.html

clean:
	rm -f sass/style.css
	rm -f stylus/style.css
	rm -rf .sass-cache

install-libs:
	apt-get install firefox npm nodejs libhaml-ruby1.8
	npm install stylus -g


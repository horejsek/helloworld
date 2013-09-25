
all:
	@echo "make run-html"
	@echo "make run-jade"
	@echo "make clean"
	@echo "make install-libs"

run-html:
	cd html; chromium-browser index.html

run-jade:
	cd jade; jade index.jade; chromium-browser index.html

clean:
	rm -f jade/index.html

install-libs:
	npm install jade --global

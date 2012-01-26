
all:
	@echo "make run-hello-world"
	@echo "make run-fibonacci"
	@echo "make clean"
	@echo "make install-libs"

run-hello-world:
	coffee -cb hello-world/hello-world.coffee
	rhino hello-world/hello-world.js

run-fibonacci:
	coffee -cb fibonacci/fibonacci.coffee
	rhino fibonacci/fibonacci.js

clean:
	rm -f ./*/*.js

install-libs:
	apt-get install nodejs coffeescript

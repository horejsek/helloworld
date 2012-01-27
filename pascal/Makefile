
all:
	@echo "make run-hello-world"
	@echo "make run-fibonacci"
	@echo "make clean"
	@echo "make install-libs"

run-hello-world:
	fpc hello-world/hello-world.p
	./hello-world/hello-world

run-fibonacci:
	fpc fibonacci/fibonacci.p
	./fibonacci/fibonacci

clean:
	find ./*/* -type f -not -name *.p | xargs rm -f

install-libs:
	apt-get install fp-compiler

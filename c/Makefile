
all:
	@echo "make run-hello-world"
	@echo "make run-fibonacci"
	@echo "make clean"
	@echo "make install-libs"

run-hello-world:
	gcc hello-world/hello-world.c -o hello-world/hello-world
	./hello-world/hello-world

run-fibonacci:
	gcc fibonacci/fibonacci.c -o fibonacci/fibonacci
	./fibonacci/fibonacci

clean:
	rm -f ./hello-world/hello-world ./fibonacci/fibonacci

install-libs:
	apt-get install gcc

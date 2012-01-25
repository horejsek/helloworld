
all:
	@echo "make run-hello-world"
	@echo "make run-fibonacci"
	@echo "make clean"
	@echo "make install-libs"

run-hello-world:
	g++ hello-world/hello-world.cpp -o hello-world/hello-world
	./hello-world/hello-world

run-fibonacci:
	g++ fibonacci/fibonacci.cpp -o fibonacci/fibonacci
	./fibonacci/fibonacci

clean:
	rm -f ./hello-world/hello-world ./fibonacci/fibonacci

install-libs:
	apt-get install g++


all:
	@echo "make run-hello-world"
	@echo "make run-fibonacci"
	@echo "make clean"
	@echo "make install-libs"

run-hello-world:
	cd hello-world; javac HelloWorld.java; java HelloWorld

run-fibonacci:
	cd fibonacci; javac Fibonacci.java; java Fibonacci

clean:
	rm -f ./*/*.class

install-libs:
	apt-get install openjdk-6-jdk

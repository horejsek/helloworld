
all:
	@echo "make run-hello-world"
	@echo "make run-fibonacci"
	@echo "make clean"
	@echo "make install-libs"

run-hello-world:
	cd hello-world; ghc hello-world.hs; ./hello-world

run-fibonacci:
	cd fibonacci; ghc fibonacci.hs; ./fibonacci

clean:
	rm -f ./*/*.hi ./*/*.o

install-libs:
	apt-get install ghc


all:
	@echo "make run-hello-world"
	@echo "make clean"
	@echo "make install-libs"

run-hello-world:
	nasm -f elf hello-world/hello-world.asm
	ld hello-world/hello-world.o -o hello-world/hello-world
	./hello-world/hello-world

clean:
	find ./*/* -type f -not -name *.asm | xargs rm -f

install-libs:
	apt-get install nasm

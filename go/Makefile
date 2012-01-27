
GO_DIR=~/go
GO_COMPILER=$(GO_DIR)/bin/8g
GO_LINKER=$(GO_DIR)/bin/8l

all:
	@echo "make run-hello-world"
	@echo "make run-fibonacci"
	@echo "make clean"
	@echo "make install-libs"

run-hello-world:
	$(GO_COMPILER) -o hello-world/hello-world.8 hello-world/hello-world.go
	$(GO_LINKER) -o hello-world/hello-world hello-world/hello-world.8
	./hello-world/hello-world

run-fibonacci:
	$(GO_COMPILER) -o fibonacci/fibonacci.8 fibonacci/fibonacci.go
	$(GO_LINKER) -o fibonacci/fibonacci fibonacci/fibonacci.8
	./fibonacci/fibonacci

clean:
	find ./*/* -type f -not -name *.go | xargs rm -f

install-libs:
	apt-get install bison gawk gcc libc6-dev make
	apt-get install python-setuptools python-dev build-essential
	easy_install mercurial
	hg clone -u release https://go.googlecode.com/hg/ ~/go
	cd ~/go/src/; ./all.bash

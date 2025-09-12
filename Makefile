.PHONY: build
build:
	@ python3 -m pip install -r MacUSB/requirements.txt && \
	  pyinstaller MacUSB.spec && \
	  printf '\e[42m Success \e[0m\n'

.PHONY: clean
clean:
	@ rm -rf ./dist && \
	  rm -rf ./build && \
	  printf '\e[42m Success \e[0m\n'

.PHONY: rebuild
rebuild :
	@ make clean && \
	  make build
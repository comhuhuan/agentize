.PHONY: install build compile watch clean package

# Make the targets runnable from any working directory:
# `make -f vscode/Makefile build`
VSCODE_DIR := $(patsubst %/,%,$(dir $(abspath $(lastword $(MAKEFILE_LIST)))))

install:
	npm --prefix $(VSCODE_DIR) install

compile: install
	npm --prefix $(VSCODE_DIR) run compile

build: compile

watch: install
	npm --prefix $(VSCODE_DIR) run watch

clean:
	rm -rf $(VSCODE_DIR)/out $(VSCODE_DIR)/.vscode-test

package: compile
	# Produces a .vsix in $(VSCODE_DIR).
	npm --prefix $(VSCODE_DIR) exec --yes -- @vscode/vsce package

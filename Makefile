.PHONY: all clean install uninstall

all:
	python3 -m build -n

install:
	python3 -m pip install --find-links dist gptest

uninstall:
	python3 -m pip uninstall -y gptest

clean:
	@rm -rf dist *.egg-info

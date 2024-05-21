all:
	@python3 -m build -n .

clean:
	@rm -rf dist UNKNOWN*

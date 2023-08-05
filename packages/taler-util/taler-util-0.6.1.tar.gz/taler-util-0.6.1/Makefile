include config.mk

.SILENT: all
all: dist
	$(echo) "This is a python project, no compilation at this step required."
	$(echo) "Run make install to install global."
	$(echo) "Run make install-user to install for the current user."
	$(echo) ""
	$(echo) "If you want to update your installation, use make update."

# you need SOURCE_DATE_EPOCH at least at the 1980s when
# your default SOURCE_DATE_EPOCH in env is 1.
.PHONY: dist
dist:
	$(env) SOURCE_DATE_EPOCH=315532800 $(python) setup.py sdist bdist_wheel

install: all
	(cd dist; $(env) SOURCE_DATE_EPOCH=315532800 $(python) -m pip install taler-util)

uninstall:
	(cd dist; $(env) SOURCE_DATE_EPOCH=315532800 $(python) -m pip uninstall taler-util)

install-user:
	(cd dist; $(env) SOURCE_DATE_EPOCH=315532800 $(python) -m pip install --user --no-index --find-links=. taler-util)

uninstall-user:
	(cd dist; $(env) SOURCE_DATE_EPOCH=315532800 $(python) -m pip uninstall taler-util)

update:
	(cd dist; $(env) SOURCE_DATE_EPOCH=315532800 $(python) -m pip install --upgrade --no-index --find-links=. taler-util)

pypi: dist
	$(env) SOURCE_DATE_EPOCH=315532800 $(python) -m twine upload dist/*

check:
	$(tox) || echo "error: you have to install tox"

pretty:
	$(find) . -type f -name '*.py' -or -name '*.py.in' -print0 | $(xargs) -0 $(yapf) -i 2>&1 || true

clean:
	$(rm) -rf __pycache__ *~

dist:
	python setup.py sdist;
	python setup.py bdist_wheel --universal --bdist-dir /tmp/bdist_wheel

dist2:
	python setup.py sdist;
	python setup.py bdist_wheel --bdist-dir /tmp/bdist_wheel

egg:
	python setup.py bdist_egg

clean:
	rm -rf build dist BioFtParse.egg-info 

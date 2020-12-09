dist:
	python setup.py sdist;
	python setup.py bdist_wheel --universal --bdist-dir /tmp/bdist_wheel

dist2:
	python setup.py sdist;
	python setup.py bdist_wheel --bdist-dir /tmp/bdist_wheel

egg:
	python setup.py bdist_egg

testpypi: dist
	twine upload -r testpypi dist/*

pypi: dist
	twine upload dist/*

clean:
	rm -rf build dist BioFtParse.egg-info

install:
	python setup.py install

.PHONY: docs
setup:
	rm -rf build
	rm -rf dist
	python setup.py bdist_wheel
install:
	pip uninstall initpkg -y
	pip install --find-links=dist  --no-cache-dir initpkg
test:
	rm -rf $(name)
	initpkg $(name)

publish:
	make setup
	git tag $(version)
	git push origin $(version)
	twine upload dist/*

docs:
	rm -rf docs/_build && sphinx-apidoc -o docs <template> && cd docs && make html
VERSION = 1.7.6

build:
	hatch clean
	hatch build

tag:
	git tag v$(VERSION)
	git push --tags
publish:	
	twine upload dist/*
 
	

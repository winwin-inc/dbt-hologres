VERSION = 1.7.8

build:
	hatch clean
	hatch build

tag:
	echo "version = '$(VERSION)'" > dbt/adapters/hologres/__version__.py
	git add -u  
	git commit -m "tag: v$(VERSION)"
	git tag v$(VERSION)
	git push --tags
publish:	
	twine upload dist/*
 
	

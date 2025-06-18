VERSION = 1.9.8a1

tag:
	echo "version = '$(VERSION)'" > source/dbt/adapters/hologres/__version__.py
	git add -u  
	git commit -m "tag: v$(VERSION)"
	git tag v$(VERSION)
	git push --tags

build:
	hatch clean
	hatch build


publish:	
	twine upload dist/*
 
	

VERSION = 1.7.8b

tag:
	echo "version = '$(VERSION)'" > dbt/adapters/hologres/__version__.py
	git add -u  
	git commit -m "tag: v$(VERSION)"
	git tag v$(VERSION)
	git push --tags

build:
	hatch clean
	hatch build


publish:	
	twine upload dist/*
 
	

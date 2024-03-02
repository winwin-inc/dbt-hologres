VERSION=1.7.8

tag:
	echo "version = '$(VERSION)'" > dbt/adapters/hologres/__version__.py
	git add -u  
	git commit --allow-empty -m "Release $release"
	git tag -a $(VERSION) -m "Version $(VERSION)"
e:	
	git push --tags

build:
	hatch clean
	hatch build


publish:	
	twine upload dist/*
 
	

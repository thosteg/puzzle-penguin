.PHONY: doc
doc:
	helpers/create_readme.sh

.PHONY: publish
publish: doc
	git add README.md
	git commit -m "README.md: updated"
SHELL := /bin/bash -euo pipefail

.DEFAULT_GOAL := all

all: create.tag push.tag

.PHONY: install.python.reqs
install.python.reqs:
	$(shell pip install -r ./hacks/requirements.txt)

.PHONY: create.tag
create.tag:
ifeq (, $(GIT_TAG))
	@echo "must define a tag"
endif
	@echo "updating addons with tag: $(GIT_TAG)"
	@python ./hacks/python/repository_ref_labeler.py --ref $(GIT_TAG) --path ./templates/
 	@git commit -a ${GIT_TAG} -m "${GIT_TAG}"

.PHONY: push.tag
push.tag:
ifeq (, $(GIT_TAG))
	@echo "must define a tag"
endif
	echo "pushing tag: ${GIT_TAG}"
 	@git push origin ${GIT_TAG}
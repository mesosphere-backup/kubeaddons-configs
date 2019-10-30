SHELL := /bin/bash -euo pipefail

.DEFAULT_GOAL := all

GIT_COMMIT := $(shell git rev-parse "HEAD^{commit}")
GIT_TAG ?= $(shell git describe --tags --abbrev=7 "$(GIT_COMMIT)^{commit}" --exact-match 2>/dev/null)


all: create.tag push.tag

.PHONY: create.tag
create.tag:
ifeq (, $(GIT_TAG))
	@echo "must define a tag"
endif
	@echo "updating addons with tag: ${GIT_TAG}"
	@$(shell python ./hack/version_labeler.py --version $(GIT_TAG) --path ./templates)
# 	@git commit -a ${GIT_TAG} -m "${GIT_TAG}"

.PHONY: push.tag
push.tag:
ifeq (, $(GIT_TAG))
	@echo "must define a tag"
endif
	echo "pushing tag: ${GIT_TAG}"
# 	@git push origin ${GIT_TAG}
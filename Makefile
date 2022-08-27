SCRIPTS_DIR = scripts
WIP_DIR = wip
PUBLISHED_DIR = published
TO_PUBLISH_DIR = to-publish

PUBLISH_CMD = $(SCRIPTS_DIR)/publish
UNPUBLISH_CMD = $(SCRIPTS_DIR)/unpublish


.PHONY: publish
publish: export SEPI_BLOG_TO_PUBLISH_DIR=$(TO_PUBLISH_DIR)
publish: export SEPI_BLOG_PUBLISHED_DIR=$(PUBLISHED_DIR)
publish: 
	@$(PUBLISH_CMD)

.PHONY: unpublish
unpublish:
	@$(UNPUBLISH_CMD) $(POST)
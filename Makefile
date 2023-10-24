SCRIPTS_DIR = scripts
WIP_DIR = wip
TO_PUBLISH_DIR = to-publish
PUBLISHED_DIR = published
NEW_CMD = $(SCRIPTS_DIR)/new.py
PUBLISH_CMD = $(SCRIPTS_DIR)/publish.py


export SEPI_BLOG_TO_PUBLISH_DIR = $(TO_PUBLISH_DIR)
export SEPI_BLOG_PUBLISHED_DIR = $(PUBLISHED_DIR)

new:
	@python3 $(NEW_CMD)


publish:
	@python3 $(PUBLISH_CMD)


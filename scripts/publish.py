import os
from utils import utils

host = "prose.sh"
to_publish_dir = os.environ["SEPI_BLOG_TO_PUBLISH_DIR"]
published_dir = os.environ["SEPI_BLOG_PUBLISHED_DIR"]
scpCommand = "scp"

utils.force_create_dir(to_publish_dir)
utils.force_create_dir(published_dir)

wip_files = utils.list_files_in_dir(published_dir)

for file in wip_files:
  post = utils.path_join([published_dir, file])
  if not utils.run_shell_command([scpCommand, post, f"{host}:/"]):
    print(f"failed to upload {post} to {host}")
    continue

  published_post = utils.path_join([published_dir, file])
  utils.move_file(post, published_post)
  print(f"successfully uploaded {post} to {host} and moved to {published_dir}")

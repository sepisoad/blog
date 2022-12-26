import sys
import os
import re
from datetime import date
from utils import utils

host = "prose.sh"
to_publish_dir = os.environ["SEPI_BLOG_TO_PUBLISH_DIR"]
regex = r"^\d\d\d\d-\d\d-\d\d-new\.md"

utils.force_create_dir(to_publish_dir)
wip_files = utils.list_files_in_dir(to_publish_dir)
found = len(list(filter(lambda i: re.match(regex, i), wip_files))) > 0
if found:
  print(f"👀 there is already an new file created in '{to_publish_dir}' dir")
  sys.exit(0)

t = date.today()
file_name = f"{t.year}-{t.month}-{t.day}-new.md"
file_path = utils.path_join([to_publish_dir, file_name])
file_content = f"""---
title: TODO
date: {t.year}/{t.strftime("%b").lower()}/{t.day}
tags: []
---
"""
utils.create_file_with_content(file_path, file_content)
print(f"📝 created new empty post file: '{file_path}'")

from flask import Flask, render_template
from markdown import markdown
import frontmatter
import os


app = Flask(__name__, template_folder='templates')


@app.get('/')
def home_page():
  posts = get_posts_info('./src/content/posts')
  return render_template('posts.html', posts=posts)


@app.get('/post-<int:id>.html')
def post_page(id):
  posts = get_posts_info('./src/content/posts')
  post = posts[id - 1]
  meta, content = read_markdown(post['file'])
  return render_template('post.html', meta=meta, content=content)


@app.get('/tag-<name>.html')
def tag_page(name):
  tags = get_tags_map('./src/content/posts')
  posts = tags[name]
  return render_template('tag.html', name=name, posts=posts)


def read_markdown(path):
  with open(path) as file:
    data = frontmatter.loads(file.read())
    return data.metadata, markdown(
      data.content, extensions=['fenced_code', 'attr_list', 'tables', 'codehilite', 'nl2br']
    )


def get_posts_info(path):
  posts = [file for file in os.listdir(path) if file.endswith('.md')]
  infos = [
    {
      'meta': frontmatter.load(f'./src/content/posts/{info}').metadata,
      'file': f'./src/content/posts/{info}',
    }
    for info in posts
  ]
  infos = sorted(infos, key=lambda i: i['meta']['date'])
  infos = [{**info, 'idx': idx + 1} for idx, info in enumerate(infos)]

  return infos


def get_tags_map(path):
  posts = get_posts_info(path)
  titles_tags = [
    {
      'tags': info['meta']['tags'],
      'title_idx': {'idx': info['idx'], 'title': info['meta']['title']},
    }
    for info in posts
  ]

  tags_map = {}
  for title_tags in titles_tags:
    title_idx = title_tags['title_idx']
    tags = title_tags['tags']
    for tag in tags:
      if tag in tags_map:
        tags_map[tag].append(title_idx)
      else:
        tags_map[tag] = [title_idx]

  return tags_map

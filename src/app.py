from flask import Flask, render_template, Response, request
from markdown import markdown
from datetime import datetime
import xml.etree.ElementTree as ET
import frontmatter
import os

blog_title = "Sepi's Blog"
blog_url = "https://sepi.me/"
author_name = "Sepehr Aryani"
app = Flask(__name__, template_folder='templates')


@app.get('/')
def home_page():
    posts = get_posts_info('./src/content/posts')
    return render_template('posts.html', posts=posts)


@app.get('/post-<int:id>.html')
def post_page(id):
    url = request.url
    posts = get_posts_info('./src/content/posts')
    post = posts[id - 1]
    meta, content = read_markdown(post['file'])
    return render_template('post.html', meta=meta, content=content, url=url)


@app.get('/tag-<name>.html')
def tag_page(name):
    tags = get_tags_map('./src/content/posts')
    posts = tags[name]
    return render_template('tag.html', name=name, posts=posts)


@app.get('/feed.atom')
def atom():
    payload = generate_atom('./src/content/posts')
    return Response(payload, mimetype='application/atom+xml')


@app.get('/email-added.html')
def email_added():
    return render_template('email-added.html')


@app.get('/email-exists.html')
def email_exists():
    return render_template('email-exists.html')


@app.get('/email-invalid.html')
def email_invalid():
    return render_template('email-invalid.html')


def read_markdown(path):
    with open(path) as file:
        data = frontmatter.loads(file.read())
        return data.metadata, markdown(
            data.content, extensions=[
                'fenced_code', 'attr_list', 'tables', 'codehilite', 'nl2br']
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


def generate_atom(path):
    posts = get_posts_info(path)

    feed = ET.Element("feed", {"xmlns": "http://www.w3.org/2005/Atom"})

    title = ET.SubElement(feed, "title")
    title.text = blog_title
    
    link = ET.SubElement(feed, "link")
    link.set("href", blog_url)

    link2 = ET.SubElement(feed, "link")
    link2.set("href", f"{blog_url}feed.atom")
    link2.set("rel", "self")
    link2.set("type", "application/atom+xml")

    author = ET.SubElement(feed, "author")
    authorname = ET.SubElement(author, "name")
    authorname.text = author_name

    id = ET.SubElement(feed, "id")
    id.text = blog_url

    updated = ET.SubElement(feed, "updated")
    updated.text = datetime.utcnow().isoformat() + "Z"

    idx = 0
    for post in posts:
        idx = idx + 1

        entry = ET.SubElement(feed, "entry")

        title = ET.SubElement(entry, "title")
        title.text = post["meta"]["title"]

        id = ET.SubElement(entry, "id")
        id.text = f"{blog_url}post-{idx}"

        link = ET.SubElement(entry, "link")
        link.set("href", f"{blog_url}post-{idx}")

        updated_val = datetime.strptime(str(post["meta"]["date"]), "%Y-%m-%d")
        updated = ET.SubElement(entry, "updated")
        updated.text = str(updated_val.isoformat() + "Z")

    return ET.tostring(feed, encoding="unicode")

from flask_frozen import Freezer
from src import app

app.app.config['FREEZER_BASE_URL'] = 'https://sepi.me'
app.app.config['FREEZER_RELATIVE_URLS'] = True
app.app.config['FREEZER_DESTINATION'] = '../public'
app.app.config['FREEZER_DEFAULT_MIMETYPE'] = 'text/html'
frozen_app = Freezer(app.app)

@frozen_app.register_generator
def post_page():
    posts = app.get_posts_info('./src/content/posts')
    for post in posts:
        yield {'id': post["idx"]}

@frozen_app.register_generator
def tag_page():
    tags = app.get_tags_map('./src/content/posts')
    for tag in tags:
        yield {'name': tag}

if __name__ == '__main__':
	frozen_app.freeze()
	# app.app.run(host='localhost', port=1987, debug=True)

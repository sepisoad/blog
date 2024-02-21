---
title: 'How my blog works'
date: 2024-02-17
tags: [web, python, ssg, flask]
---

I recently discovered [Frozen Flask](https://github.com/Frozen-Flask/Frozen-Flask) and was thrilled by its simplicity as a static site generator, especially since I'm familiar with [Flask](https://github.com/pallets/flask/) from previous projects. This led me to switch my blog from [zola](https://www.getzola.org/) to "Frozen Flask" due to dissatisfaction with the former, particularly in handling custom tags and inadequate documentation. The migration process took just a few hours around midday.

Frozen Flask is straightforward, converting a Flask app into static pages. For dynamic content like my blog posts and tags, I set up custom generators for Frozen Flask to create the necessary HTML pages.

My blog primarily consists of a single static homepage, with posts represented by markdown files named /post-<id>.html, where <id> is a sequential number assigned based on the post's date.

Each post includes front matter for the title, date, and tags, which facilitate the conversion of markdown to HTML. I've also mapped tags to their respective posts, enhancing navigation despite the blog's modest size.

I'm pleased with the outcome, as it allows me to leverage Python for intuitive site management.

The blog is hosted on GitHub, with deployment via Cloudflare upon pushes to the master branch. I chose Cloudflare for its complimentary analytics, offering insights without code modifications.

The blog's code is available [here](https://github.com/sepisoad/blog)

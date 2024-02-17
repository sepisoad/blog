---
title: 'My pain points with Emacs code search and how I fixed them'
date: 2023-10-22
tags: [emacs, programming]
---

I love [Emacs](https://www.gnu.org/software/emacs/), but one of the things I miss from Visual Studio Code is a good code search feature.
The [built-in grep command](https://www.gnu.org/software/emacs/manual/html_node/emacs/Grep-Searching.html) is powerful, but it's not very easy to use, 
and the search results can be difficult to navigate, especially in large codebases.

There are many third-party packages that try to solve this problem, but most of them have the same issues: 
they're either difficult to use or the search results are hard to navigate.

However, there is one package called [rg.el](https://github.com/dajva/rg.el) that does a great job of fixing both of these problems.

rg.el is a wrapper for the [ripgrep](https://github.com/BurntSushi/ripgrep) command-line tool, which is a very fast and powerful code search tool.
ripgrep understands [file types](https://github.com/BurntSushi/ripgrep/blob/master/GUIDE.md#manual-filtering-file-types) and comes with a good set of defaults, 
so you don't need to worry about writing complex regex patterns.

rg.el also has a fantastic transient-based UI system that makes it easy to manipulate the search results. 
For example, you can easily exclude (or include) certain patterns from the results by adding a `--glob` flag to your search.

For example, if you're working on a Go project and you want to search for the function `encodeBase64`, 
you can use the following command to exclude all test files from the results:

```bash
rg-project encodeBase64 --glob='!*test.go'
```

This is great, but there's one issue. `rg.el` only allows you to specify one `--glob` flag at a time. This is fine in some cases, 
but there are times when you need to exclude multiple patterns.

Fortunately, there's a workaround. You can set the global variable `rg-command-line-flags` to an array of strings of custom flags, 
and all of those strings will be passed to `ripgrep` command.

if you're unsure how to do this, here's a step-by-step example:

1) Press `M-:` to activate the **eval prompt** in the minibuffer.
2) Set the variable to your desired values, for instance: 
```lisp
(setq rg-command-line-flags '("-g '!*_test.go'" "-g '!*foo.go'")).
```

You only need to do this once, and all subsequent searches will be affected by it. To disable this behavior, simply set `rg-command-line-flags` to `nil`.

I wish rg.el supported multiple filters in its UI, but this workaround is fine for me for the time being.

## Conclusion
rg.el is a great code search package for Emacs. It's easy to use and the search results are easy to navigate. 
If you're looking for a good code search solution for Emacs, I highly recommend rg.el.



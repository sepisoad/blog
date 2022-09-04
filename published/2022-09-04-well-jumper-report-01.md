---
title: Well Jumper Progress Report 1
date: 04/sep/2022
tags: [game, odin, raylib, 3d, programming]
---

I've been working on a few enterprise projects lately and started to fill bored and exhausted. so I set out to work on something fun and refreshing. I came up with the idea of a simple but fun game and decided to dedicated a small portion of my time to work on it. I do not want disclose the game details, instead I want to gradually give reports on my progress here.

For this game I wanted to use [raylib](https://www.raylib.com/) as it provides a really nice and simple API for creating all sorts of games. The library is written in C which is a wise choice and I like it. However I did not want to deal with the C quirks and kill fun. Fortunately there are [numerous language bindings](https://github.com/raysan5/raylib/blob/master/BINDINGS.md) for raylib. Among all the supported languages I was only interested in the followings:

- Zig
- Hare
- Odin
- Lua
- Wren
- Go
- JS

Obviously I had to select one language and stick with it. I was reluctant to use Go and JS because I use them on a daily basis. [Hare](https://harelang.org/) seems really cool but I only works on open source OSes so it is out of the list as I use OSX. I really like [Zig](https://ziglang.org/) but I could not get it to work with raylib under OSX even though it is officially supported!. The same thing happened to me when I tried to use [Lua](https://www.lua.org/) and [Wren](https://wren.io/). So I was only left with Odin.

Fortunately [Odin](https://odin-lang.org/) worked out of the box, as the compiler comes with the raylib binding. Also its syntax looks really similar to Go, in fact it looks much cleaner compared to Go. I like the language, however It is really soon for me to have an opinion on the language.

For code hosting I decided to use [sourcehut](https://sr.ht/), you can find the source code [here](https://sr.ht/~sepisoad/game/)

As I mentioned earlier I did not want to go crazy with this side project and I decided to not use a deadline at all. The game will be created in small iterations. My first task was to setup a small window and print hello to it.

```perl
package main

import "core:fmt"
import ray "vendor:raylib"

WINDOW_WIDTH :: 400
WINDOW_HEIGHT :: 400
WINDOW_TITLE :: "well jumper"

main :: proc() {
  ray.InitWindow(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)
  
  for !ray.WindowShouldClose() { 
    ray.BeginDrawing()
      ray.ClearBackground(ray.BLACK)
      ray.DrawText("work in progress ...", 20, 20, 20, ray.WHITE)
    ray.EndDrawing()
  }

  ray.CloseWindow()
}
```

the above code look really simple and descriptive, the only thing to note here is that on like 6 to 8 we have defined constant values. below is the result:

[![Screenshot-2022-09-04-at-22-35-34.png](https://i.postimg.cc/9QcbnG2d/Screenshot-2022-09-04-at-22-35-34.png)](https://postimg.cc/pp1K95pr)
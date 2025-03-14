---
title: 'Understanding Memory Alignment in Quake 1'
date: 2024-08-25
tags: [c, quake, game, performance]
---

As I was diving into the Quake 1 source code, I came across many strange and intriguing pieces of code. It's fascinating to see how the developers squeezed every ounce of performance out of the hardware available at the time. I’ve decided to start a series of blog posts to unpack some of these coding tricks and optimizations. Today, I want to focus on one line that particularly caught my attention:

```c
size = (size + sizeof(cache_system_t) + 15) & ~15;
```

At first, this line seemed like a bit of arcane magic, something you might gloss over without a second thought. But as I dug deeper, I realized it’s a brilliant example of how the Quake 1 developers handled memory alignment, a crucial aspect of game performance that often goes unnoticed.

## Breaking Down the Code

This line is all about ensuring that memory is aligned to make the game run as smoothly as possible. In simpler terms, it’s a way to make sure the data in memory is lined up in a way that the CPU can access it quickly and efficiently, here’s what’s happening

#### First, Some Math:

```c
size + sizeof(cache_system_t) + 15
```

- `size` is the original size of a memory block or data structure.
- `sizeof(cache_system_t)` adds the size of a structure called cache_system_t.
- `15` is added to ensure the final size is a nice, round multiple of 16 bytes, which helps with alignment.

#### Then, a Bitwise Operation:

```c
& ~15
```

- This operation clears out the last four bits of the sum, effectively rounding it down to the nearest multiple of 16. The result is a number that is perfectly aligned for memory.


## Why the Magic Number 15?

You might be wondering: why add 15? Why not just add 16 if we’re trying to align to multiples of 16? The trick here is that adding 15 ensures that any leftover bytes push the total just enough to round up to the next multiple of 16. If the number is already a multiple of 16, it stays put. If not, it moves up to the nearest multiple without overshooting, which could happen if you added 16. For example If the total is 73, adding 15 brings it to 88, which is correctly rounded down to 80 (the nearest multiple of 16). If you added 16 instead, you might accidentally skip a multiple, which could mess up memory alignment.

## Why Does This Matter in a Game Like Quake 1?

Memory alignment is critical in a fast-paced game like Quake 1 because it allows the CPU to access data more efficiently. Aligned data can be read and processed faster, which is crucial when every frame counts. The developers of Quake 1 were well aware of this and used clever tricks like this one to ensure their game ran as smoothly as possible on the hardware of the time.


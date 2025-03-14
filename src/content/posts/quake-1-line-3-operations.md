---
title: 'One Line, Three Tricks: Unpacking a Quake 1 Gem'
date: 2025-03-14
tags: [c, quake, game, performance]
---

While diving into the Quake 1 source code, I stumbled across a clever line in the `GL_MakeAliasModelDisplayLists` function that’s worth unpacking:

```c
*cmds++ = count = *loadcmds++;
```

This single line does a surprising amount of work, blending assignment, dereferencing, and pointer incrementing into a compact expression. If you’re familiar with C, you’ll know it’s a language that loves efficiency—and this is a perfect example of that ethos in action. Let’s break it down step by step.

### What’s Happening Here?

This line appears in a loop that processes texture coordinate data for Quake’s alias models (think 3D character meshes). The variables involved are:
 - `cmds`: a pointer to an integer array where processed data is being stored.
 - `count`: an integer that holds the number of elements to process in this iteration.
 - `loadcmds`: a pointer to an integer array containing the source data.

The expression 
```c
*cmds++ = count = *loadcmds++
```
combines three operations:

1. **Dereference and assign from the right**: `*loadcmds++` reads the value at the current position of `loadcmds` and increments the pointer to the next position afterward.
2. **Assign to count**: The value from `*loadcmds++` is assigned to `count`.
3. **Dereference and assign to the left**: The value of `count` is written to the current position of `cmds`, and then `cmds` is incremented.

In **C**, the assignment operator (`=`) evaluates to the assigned value, and the post-increment operator (`++`) updates the pointer after the value is used. This chaining makes the whole thing work seamlessly.


### Why Is This Cool?

At first glance, it might look like a recipe for confusion, but it’s actually a brilliant optimization:

- **Compactness**: It performs three critical tasks—reading, storing, and advancing pointers—in one line, reducing the need for separate statements.

- **Efficiency**: By chaining assignments, it minimizes temporary variables and leverages C’s expression evaluation rules.

- **Readability (to the initiated)**: For seasoned C programmers, this idiom signals intent clearly: “Copy data from one buffer to another while advancing both pointers.”

### How It Works in Context

In the Quake code, this line is part of a loop that copies and scales texture coordinates. The loadcmds array holds raw data, and count determines how many coordinates to process (or signals the end of the data if it’s zero). The processed data is written to cmds. By using this trick, the code efficiently sets up count for the loop’s logic while building the output buffer in one fell swoop.
Here’s what it might look like expanded:

```c
count = *loadcmds;  // Get the value
loadcmds++;         // Move to the next source position
*cmds = count;      // Store it
cmds++;             // Move to the next destination position
```

The original line does all this in a single expression, showcasing the elegance of C’s operator precedence and side effects.

### Final Thoughts

This trick is a reminder of why Quake’s source code remains a treasure trove for programmers. It’s not just about making games—it’s about pushing hardware to its limits with clever, concise solutions. If you’re reading through the Quake source, keep an eye out for more of these little masterpieces. They’re a testament to the ingenuity of id Software’s developers in the ’90s.

---
title: 'how to run deno in watch mode'
date: 2022-08-26
tags: [deno, programming, javascript]
---

[deno](https://deno.land) is awesome in many ways, you can setup a project that makes use of external libaries in a matter of seconds, you do not need the stupid `package.json` file and also you do not need to install countless libraries just to run a hello world http server.

deno has a really nice and consistent cli interface and you can quickly learn how to get it do what you want simply by following the cli help parameters. also the documentations is really neat.

deno comes with a [REPL](https://deno.land/manual@v1.25.0/tools/repl) which is OK, speciallt if you compare to `node.js`, however there are rooms for improvements, like for example after you are dropped into the repl there is no way for you to reload an already loaded module. I mean compared to lisps the REPL that comes with deno leaves a lot to be desired.

but there are always some workaround, so for now what you can do is to run the deno in watch mode and have it watch the entry file or basically any file you desire and then put some `console.log`s around to see the changes in live.

for example here is a simple setup:

```
├ app.js
└ module-a.js
```

---

```js
//app.js
import * as M from "./module-a.js"

console.log(M.add(2, 3)) // => 5
```

---

```js
//module-a.js
const add = (a, b) => {
  return a + b
}

const PI = 3.14

export {
  add,
  PI
}
```

now you can run the deno with the following arguments:

```bash
deno run --allow-all --watch app.js
```

in fact `allow-all` is not required but it is nice to have it while you are in development mode as it gives deno full permissions (e.g network, file, ...)

+++
title = "type check go interface implementations on compile time"
date = "2022-08-02" 
[taxonomies]
tags=["go", "programming", "interface"]
+++

interfaces in **go** are a bit different from other languages namely **java** and **c#**, in go you do not explicitly define a concrete implementation for an interface, like what you do in say java. in fact interfaces are impelmented implicitly, in other words an struct implments an interface once in contains all the method defined in an interface.

for example lets say we have the following interfaces:

```go
package x

type Fooer interface {
  Foox(in string) int
  Fooy(in int) string
}
```

```go
package y

type Bazer interface {
  Baz(in string) string
}
```

now these interfaces are implemented in the following struct:

```go
package sample

type Bar {}

func (b Bar) Foox(in string) int { /*some code goes here*/ }

func (b Bar) Fooy(in int) string { /*some code goes here*/ }

func (b Bar) Baz(in string) string { /*some code goes here*/ }
```

notice that we did not mentioned the name of the above interfaces, heck we did not even import those modules, yet golang knows that `Bar` is compatible with both `Fooer` and `Bazer`. this is possible because go compiler only cares about the contracts that each interface defines, and the contract is simple the methods definiton.

this makes the code very cleaner and less hairy when you are in a large code base, however anything that is used implicitly can change behinde the scene and bit you when you do not expect. one way to quickly cacth errors when you deviate from the interfaces contracts is to write something like this at the top of the file that implements an interface or interfaces:

```go
package sample

import (
  "x" //package that defines Fooer
  "y" //package that defines Bazer
)

var _ x.Fooer = Bar{} // makes sure that Bar implements Fooer
var _ y.Bazer = Bar{} // makes sure that Bar implements Bazer

type Bar {}

// the same code as before
```

now if you change anything in your implementation code or if something changes on the interfaces side you get a clean compiler error complaining that you are deviating from the interface.

nice?

![meme](https://i.giphy.com/media/Od0QRnzwRBYmDU3eEO/giphy.webp)

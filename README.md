# mc-easyCalc
An easy-to-use calculator by sending messages in Minecraft server. Based on mana9er-core.

## In-game Usage

For help information, you can type:

```
!calc help
```

For a simple example:

```
!calc 27*64
```

Then the server should show (broadcasting using `/say`):

```
[Server] [EasyCalc] 1728
```

You can use `_` to indicate the answer of last expression (notice that this is shared by all players, which allows you to use the answer of other player's expression):

```
!calc _ + 1
```

The server should show:

```
[Server] [EasyCalc] 1729
```

## Parser

We use [Lark-Parser](https://github.com/lark-parser/lark) to generate a parser for parsing arithmetic expressions. We don't use the python built-in function `eval` because we want to avoid any possible injection vulnerability.

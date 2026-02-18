# ANSI escape codes

> [Link to a gist!](https://gist.github.com/fnky/458719343aabd01cfb17a3a4f7296797.js)

To add some formatting/colour to a string in the terminal, you can do the following:

```python
"\033[<code>m" + <string-to-be-formatted> + "\033[0m"
```

| style         | code | style           | code | style            | code |
| ------------- | ---- | --------------- | ---- | ---------------- | ---- |
| bold          | 1    | gray            | 30   | blue             | 34   |
| italic        | 3    | red             | 31   | magenta          | 35   |
| underline     | 4    | green           | 32   | cyan             | 36   |
| strikethrough | 9    | yellow          | 33   | white            | 37   |
|               |      | inverted-gray   | 40   | inverted-blue    | 44   |
|               |      | inverted-red    | 41   | inverted-magenta | 45   |
|               |      | inverted-green  | 42   | inverted-cyan    | 46   |
|               |      | inverted-yellow | 43   | inverted-white   | 47   |

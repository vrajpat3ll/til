# Basics of HTML

> documentation can be found [here](https://developer.mozilla.org/en-US/docs/Web/HTML)!

HyperText Markup Language is the standard used to create structure of webapages. It defines the content and layout through a system of _tags_ and _attributes_.

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>My First Web Page</title>
  </head>
  <body>
    <h1>Hello, World!</h1>
    <p>This is my first HTML page.</p>
  </body>
</html>
```

## Common Tags

| Tag      | Name           | Use case                                                                      |
| -------- | -------------- | ----------------------------------------------------------------------------- |
| h1 to h6 | heading        | Bold and big title                                                            |
| p        | paragraph      | put content in a paragraph                                                    |
| a        | anchor         | for linking the text to some hyperlink                                        |
| ul       | unordered list | list without numbering                                                        |
| ol       | ordered list   | list with numbering                                                           |
| li       | list item      | used with `ul`/`ol` to fill the lists                                         |
| img      | image          | for images                                                                    |
| div      | div            | container for some content(takes entire space)                                |
| span     | span           | container for some content(indentical to `div` but takes only what is needed) |
| table    | table          | for creating a table                                                          |
| form     | form           | for creating a form with custom inputs                                        |

## Attributes

They are associated with _tags_.

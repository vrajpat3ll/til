# Intro to CSS

> documentation can be found [here](https://developer.mozilla.org/en-US/docs/Web/CSS)!

Cascading Style Sheets, or CSS is a styling language used to describe the presentation of HTML/XML documents.

It describes how elements should be rendered in webpages, on paper or other media.

## Adding CSS to an HTML document

- You can add the code in another file named `styles.css`, and link it by adding the following line to the document:

```html
<link rel="stylesheet" href="path/to/styles.css" />
```

OR we can have it inline (a bad practice, usually) as well, or even in the document itself as follows:

```html
<style>
  p {
    color: purple;
  }
</style>
```

---

```css
h1 {
  color: red;
}
```

This line of code changes the headings created by h1 tags to red color.

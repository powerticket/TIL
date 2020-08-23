# CSS

> Cascading Style Sheets

## Cascading

### Definition

1. Inline style
2. Embedding style
3. Link style



### Cascading order

1. `!important`
2. Inline style
3. ID selector
4. Class selector
5. Type selector
6. Universal selector
7. Source order



#### Selector

| Priority | Selector  | Expression |
| -------- | --------- | ---------- |
| 1        | ID        | .id        |
| 2        | Class     | .class     |
| 3        | Type      | type       |
| 4        | Universal | *          |



##### e.g.

```css
#id {
  font-size: 1rem;
}

.class {
  font-size: 1rem;
}

header {
  font-size: 1rem;
}

* {
  font-size: 1rem;
}
```



##### Child selector

`parent > child`

##### Descendant selector

`parent descendant`





## Unit

### Size

- px - pixel, fixed size
- % - percentage, relative size
- em - relative size of inheritance
- rem - relative size of root em
- viewport - relative size of device's display area



### Color

- keyword - e.g. red, blue, black
- RGB - Red, Green, Blue, hexadecimal or functional expression
- RGBA - RGB + transparent
- HSL - Hue, Saturation, Lightness
- HSLA - HSL + transparent



## Box model

### Box size

`box-sizing`

- content-box - default
- border-box



### Margin collapsing





## Display

### `block`

Line changing

`div`, `ul`, `ol`, `li`, `p`, `hr`, `form`



### `inline`

No line changing

`span`, `a`, `img`, `input`, `label`, `strong`, `b`, `em`, `i`



### `inline-block`



### `none`

It makes content disappeared, even space.

cf. `visibility: hidden;` - It makes content disappeared only, not space.



## Position

`static`

`relative`

`absolute`

`fixed`
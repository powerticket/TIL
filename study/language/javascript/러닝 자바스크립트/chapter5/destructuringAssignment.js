const obj = {
  a: 1,
  b: 2,
  c: 3,
  d: 4,
}

let a, b, c, d
({a, b, c, d} = obj)

console.log(a)
console.log(b)
console.log(c)
console.log(d)

const arr = [1, 2, 3, 4, 5]
const [x, y, ...rest] = arr
console.log(x)
console.log(y)
console.log(rest)

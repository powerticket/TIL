let x;
console.log(x)
console.log(x = 15)
console.log(x)
console.log(10/2)

let y = 2
const r1 = y++ + y++  // 2 + 3, y = 4
const r2 = ++y + ++y  // 5 + 6, y = 6
const r3 = y++ + ++y  // 6 + 8, y = 8
const r4 = ++y + y++  // 9 + 9, y = 10

console.log(r1)
console.log(r2)
console.log(r3)
console.log(r4)

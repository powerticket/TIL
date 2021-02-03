// string to number
const numStr1 = '33.3'
const num1 = Number(numStr1)
const numStr2 = '33..3'
const num2 = Number(numStr2)

console.log(numStr1, typeof numStr1)
console.log(num1, typeof num1)
console.log(numStr2, typeof numStr2)
console.log(num2, typeof num2)

// parsing number
const a = parseInt("16 volts", 10)
const b = parseInt("3a", 16)
const c = parseFloat("15.5")

console.log(a, typeof a)
console.log(b, typeof b)
console.log(c, typeof c)

// date value
const d = new Date()
const ts = d.valueOf()

console.log(d, typeof d)
console.log(ts, typeof ts)

// ternary operator
const bool = true
const n = b ? 1 : 0

console.log(bool, typeof bool)
console.log(n, typeof n)

// number to string
const num3 = 33.5
const numStr3 = num3.toString()

console.log(num3, typeof num3)
console.log(numStr3, typeof numStr3)

// number to boolean
const num = 0
const b1 = !num
const b2 = !!num
const b3 = !!!!!num
const b4 = Boolean(num)

console.log(num)
console.log(b1)
console.log(b2)
console.log(b3)
console.log(b4)

const hello = 'hello'
const dialog = 'Sam looked up, and said "hello, old friend!", as Max wlaked in.'
const imperative = "Don't do that!";
const dialog1 = "He looked up and said \"don't do that!\" to Max."
const dialog2 = 'He looked up and said "don\'t do that!" to Max.'
const interpolation = "Wow!"
const backtik = `new in ES6: ${interpolation}`
let currentTemp = 19.5
const message = `The current temperature is ${currentTemp}\u00b0C`
const multiline1 = 'line1\
line2'
const multiline2 = 'line1\n\
line2'
const tab = '\tthis is a tab.'
const result1 = 3 + '30'  // 3 to string
const result2 = 3 * '30'  // '30' to number
const result3 = '30' * 3  // '30' to number

console.log(hello)
console.log(dialog)
console.log(imperative)
console.log(dialog1)
console.log(dialog2)
console.log(backtik)
console.log(message)
console.log(multiline1)
console.log(multiline2)
console.log(tab)
console.log(result1)
console.log(result2)
console.log(result3)

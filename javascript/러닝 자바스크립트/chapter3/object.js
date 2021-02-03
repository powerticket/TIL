const obj = {}
console.log(obj, typeof obj)
obj["color"] = 'red'
console.log(obj, typeof obj)
obj.color = 'yellow'
console.log(obj, typeof obj)
obj["not an identifier"] = 3
console.log(obj, typeof obj)

const sam1 = {
  name: 'Sam',
  age: 4,
}
const sam2 = { name: 'Sam', age: 4 }

console.log(sam1)
console.log(sam2)
console.log(sam1 === sam2)

const sam3 = { name: 'Sam', age: 4 }
sam3.speak = function speak () { return 'Meow!' }

console.log(sam3)
console.log(sam3.speak())

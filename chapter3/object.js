const obj = {}
console.log(obj, typeof obj)
obj["color"] = 'red'
console.log(obj, typeof obj)
obj.color = 'yellow'
console.log(obj, typeof obj)
obj["not an identifier"] = 3
console.log(obj, typeof obj)

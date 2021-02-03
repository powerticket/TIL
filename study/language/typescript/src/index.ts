console.log('Hello, TypeScript!')

const name = 'Jeon'
const age = 30
const gender = 'male'

function sayHi (name: string, age: number, gender: string): void {
  console.log(`Hi ${name}, you are ${age} and a ${gender}. Right?`)
}
const sayHello = (name: string, age: number, gender: string): string => {
  return `Hello ${name}, you are ${age} and a ${gender}. Right?`
}

sayHi(name, age, gender)
sayHi('Wonpyo', 30, 'male')
console.log(sayHello('Wonpyo', 30, 'male'))

export {}

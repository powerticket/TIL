class Human {
  public gender: string
  public age: number
  public name: string
  constructor (name: string, age: number, gender?: string) {
    this.name = name
    this.age = age
    this.gender = gender
  }
}

const jeon1 = new Human('Jeon', 30)
const jeon2 = new Human('Jeon', 30, 'male')

const sayHi = (person: Human): string => {
  return `Hello, ${person.name}. You are a ${person.gender} and ${person.age} years old.`
}

console.log(sayHi(jeon1))
console.log(sayHi(jeon2))

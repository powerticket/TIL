interface Human {
  gender: string,
  age: number,
  name: string,
}

const person = {
  age: 30,
  gender: 'male',
  name: 'Jeon'
}

const sayHi = (person: Human): string => {
  return `Hello, ${person.name}. You are a ${person.gender} and ${person.age} years old.`
}

console.log(sayHi(person))

export {}

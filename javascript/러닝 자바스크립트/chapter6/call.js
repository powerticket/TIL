const bruce = { name: "Bruce" };
const madeline = { name: "Madeline" };

function greet () {
  return `Hello, I'm ${this.name}`;
}

console.log(greet());
console.log(greet.call(bruce));
console.log(greet.call(madeline));

function update (birthYear, occupation) {
  this.birthYear = birthYear;
  this.occupation = occupation;
}

console.log(bruce)
console.log(madeline)

update.call(bruce, 1992, 'doctor');
update.call(madeline, 1988, 'engineer');

console.log(bruce)
console.log(madeline)

const bruce = { name: "Bruce" };
const madeline = { name: "Madeline" };

function update (birthYear, occupation) {
  this.birthYear = birthYear;
  this.occupation = occupation;
}

console.log(bruce)
console.log(madeline)

update.apply(bruce, [1992, 'doctor']);
update.apply(madeline, [1988, 'engineer']);

console.log(bruce)
console.log(madeline)

console.log(Math.min(1, 2, 3, 4, 5));
console.log(Math.max(1, 2, 3, 4, 5));
console.log(Math.min(...[1, 2, 3, 4, 5]));
console.log(Math.max(...[1, 2, 3, 4, 5]));
console.log(Math.min.apply(null, [1, 2, 3, 4, 5]));
console.log(Math.max.apply(null, [1, 2, 3, 4, 5]));

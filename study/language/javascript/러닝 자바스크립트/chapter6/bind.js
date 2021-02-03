const bruce = { name: "Bruce" };
const madeline = { name: "Madeline" };

function update (birthYear, occupation) {
  this.birthYear = birthYear;
  this.occupation = occupation;
}

updateBruce = update.bind(bruce);
updateBruceMadeline = updateBruce.bind(madeline);
updateBruce2000 = update.bind(bruce, 2000);

console.log(bruce);
console.log(madeline);
updateBruce(1800, 'captain');
console.log(bruce);
console.log(madeline);
updateBruce.call(madeline, 1992, 'doctor');
console.log(bruce);
console.log(madeline);
updateBruce.apply(madeline, [1700, 'warrior']);
console.log(bruce);
console.log(madeline);
updateBruceMadeline(1100, 'king');
console.log(bruce);
console.log(madeline);
updateBruce2000('student')
console.log(bruce);
console.log(madeline);

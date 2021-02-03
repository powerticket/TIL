function getSentenceObject({ verb, object, subject }) {
  return `${subject} ${verb} ${object}`;
}

const obj = {
  object: 'JavaScript',
  subject: 'I',
  verb: 'love',
}

console.log(getSentenceObject(obj))

function getSentenceArray([ object, subject, verb ]) {
  return `${subject} ${verb} ${object}`;
}

const arr = ['JavaScript', 'I', 'love'];

console.log(getSentenceArray(arr))

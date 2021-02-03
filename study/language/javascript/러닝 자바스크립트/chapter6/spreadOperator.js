function addPrefix1(prefix, ...words) {
  const prefiexedWords = [];
  for (let i = 0; i < words.length; i++) {
    prefiexedWords.push(prefix + words[i]);
  }
  return prefiexedWords;
}

console.log(addPrefix1('con', 'verse', 'vex'));

function addPrefix2(prefix, words) {
  const prefiexedWords = [];
  for (let word of words) {
    prefiexedWords.push(prefix + word);
  }
  return prefiexedWords;
}

console.log(addPrefix2('con', ['verse', 'vex']));

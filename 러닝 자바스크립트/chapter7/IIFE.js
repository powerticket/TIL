const f = (function () {
  console.log('executed!')
  let count = 0;
  return function () {
    return `I have benn called ${++count} times`;
  }
})();

console.log(f());
console.log(f());
console.log(f());

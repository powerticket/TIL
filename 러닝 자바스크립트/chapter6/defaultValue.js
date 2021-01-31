function f(a, b = 2, c = 3) {
  return a + b + c;
}

console.log(f(1, 3, 5));
console.log(f(1, 3));
console.log(f(1));
console.log(f());

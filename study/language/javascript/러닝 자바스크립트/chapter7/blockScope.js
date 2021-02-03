console.log('before block');
{
  console.log('inside block');
  const x= 3;
  console.log(x);
}
console.log('outside block');
// console.log(x)

const x = 5;
{
  const x = 3;
  {
    const x = 4;
    console.log(x);
  }
  console.log(x)
}
console.log(x)
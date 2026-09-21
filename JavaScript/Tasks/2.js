function sumCommaString(str) {
  let numbers = str.split(",");
  let total = 0;
  for (let i = 0; i < numbers.length; i++) {
    total = total + parseFloat(numbers[i]);
  }
  return total;
}

console.log(sumCommaString("1.5, 2.3, 3.1, 4, 5.5, 6, 7, 8, 9, 10.9"));
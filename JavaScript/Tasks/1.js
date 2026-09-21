function sumNumbersInString(str) {
  let sum = 0;
  for (let i = 0; i < str.length; i++) {
    let char = str[i];
    if (char >= "0" && char <= "9") {
      sum = sum + Number(char);
    }
  }
  return sum;
}

console.log(sumNumbersInString("foo8bar8cat2tc2"));
// https://www.codewars.com/kata/59c633e7dcc4053512000073/train/javascript
// We shall assign the following values: a = 1, b = 2, c = 3, .... z = 26.
// For example, for the word "zodiacs", let's cross out the vowels. We get: "z o d ia cs"

function solve(s) {
  s = s.split(/[aeiou]/g).filter(i => i)
  return s.map(chars => chars.split('').map(x =>x.charCodeAt(0) - 'a'.charCodeAt(0) + 1 ).reduce((acc,val) => acc += val)).sort(sorting)[0]
}
function sorting(a,b) {
  return b-a;
}

console.log(solve("zodiacs"))
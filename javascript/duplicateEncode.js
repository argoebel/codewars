// https://www.codewars.com/kata/54b42f9314d9229fd6000d9c/train/javascript
// The goal of this exercise is to convert a string to a new string where each character in the new string is "(" if that character appears only once in the original string, or ")" if that character appears more than once in the original string. Ignore capitalization when determining if a character is a duplicate.

// Examples
// "din"      =>  "((("
// "recede"   =>  "()()()"
// "Success"  =>  ")())())"
// "(( @"     =>  "))(("
// Notes

// Assertion messages may be unclear about what they display in some languages. If you read "...It Should encode XXX", the "XXX" is the expected result, not the input!

// function duplicateEncode(word) {
//   var encoded = word.toLowerCase();
//   word
//     .toLowerCase()
//     .split("")
//     .forEach((element) => {
//       word.toLowerCase().split(element).length == 2
//         ? (encoded = encoded.split(element).join("1"))
//         : (encoded = encoded.split(element).join("2"));
//     });

//   return encoded.split("1").join("(").split("2").join(")");
// }

function duplicateEncode(word) {
  return word
    .toLowerCase()
    .split("")
    .map((element, index, w) => {
      return w.indexOf(element) == w.lastIndexOf(element) ? "(" : ")";
    })
    .join("");
}

console.log(duplicateEncode("Success"));

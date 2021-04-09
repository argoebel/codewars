// https://www.codewars.com/kata/57eb8fcdf670e99d9b000272/train/javascript
// Given a string of words, you need to find the highest scoring word.
// Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.
// You need to return the highest scoring word as a string.
// If two words score the same, return the word that appears earliest in the original string.
// All letters will be lowercase and all inputs will be valid.

// function high(x){
//   let maxVal = 0
//   let maxText = ''
//   x.split(' ').forEach(element => {
//     let temp = 0
//     for (let i = 0; i < element.length; i++) {
//       temp += element.charCodeAt(i) - 'a'.charCodeAt(0) + 1
//     }
//     if (maxVal < temp) {
//       maxVal = temp
//       maxText = element
//     }
//   });
//   return maxText
// }


// use mapping 
// function high(words) {

//   const alpha = ' abcdefghijklmnopqrstuvwxyz';
//   const score = word => word.split('').reduce((a, b) => a + alpha.indexOf(b), 0);

//   return words
//     .split(' ')
//     .map((word, pos) => ({ word: word, pos: pos, score: score(word) }))
//     .sort((a, b) => a.score - b.score || b.pos - a.pos)
//     .pop()
//     .word;
// }


// use reduce
function high(x){
  return x.split(' ').reduce((accum, current)=>{
      return score(current) > score(accum)? current:accum;  
  })
}

function score(word){
  return word.split('').reduce((accum,current)=>{return accum+(current.charCodeAt()-96)},0)
}



console.log(high('what time are we climbing up the volcano'))
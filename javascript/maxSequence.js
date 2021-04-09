// var maxSequence = function(arr){
//   let maxVal = 0
//   arr.forEach((element, index) => {
//     let varInd = index + 1
//     while (varInd <= arr.length) {
//       if (arr.slice(index, varInd).reduce((acc, val) => acc + val) > maxVal) {
//         maxVal = arr.slice(index, varInd).reduce((acc, val) => acc + val)
//       }
//       varInd++
//     }
//   });
//   return maxVal
// }

var maxSequence = function(arr){
  let maxVal = 0
  arr.forEach((element, index) => {
    for (let varInd = index+1; varInd <= arr.length; ++varInd) {
      maxVal = Math.max(arr.slice(index, varInd).reduce((acc, val) => acc + val), maxVal)
    }
  });
  return maxVal
}

console.log(maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
// function countSheeps(arrayOfSheep) {
//   return arrayOfSheep.reduce(function(acc, val) {
//     return val == 1 ? acc += 1 : acc += 0
//   })
// }


function countSheeps(arr) {
  return arr.filter(Boolean).length;
}
console.log(countSheeps([0,0,0]))

console.log(countSheeps([true,  true,  true,  false,
  true,  true,  true,  true ,
  true,  false, true,  false,
  true,  false, false, true ,
  true,  true,  true,  true ,
  false, false, true,  true ]))

console.log(countSheeps([]))


console.log(countSheeps([true,  true,  true,  false,
  true,  true,  true,  true ,
  true,  false, true,  false,
  true,  false, false, true ,
  true,  true,  true,  true ,
  false, false, undefined,  null ]))

console.log(countSheeps([null, null, null, null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,]))

console.log(countSheeps([false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, false, ]))

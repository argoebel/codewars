// https://www.codewars.com/kata/54da5a58ea159efa38000836/solutions/javascript
// Description:
// Given an array, find the integer that appears an odd number of times.

// There will always be only one integer that appears an odd number of times.

function findOdd(A) {
  let integerArr = [];
  let countArr = [];
  A.forEach((element) => {
    if (integerArr.includes(element) == false) {
      integerArr.push(element);
      countArr.push(1);
    } else {
      countArr[integerArr.indexOf(element)] =
        countArr[integerArr.indexOf(element)] + 1;
    }
  });
  let val = 0;
  countArr.forEach((element) => {
    if (element % 2 == 1) {
      val = integerArr[countArr.indexOf(element)];
    }
  });
  return val;
}

// other solutions

const findOdd10 = (xs) => xs.reduce((a, b) => a ^ b);

function findOdd11(A) {
  var obj = {};
  A.forEach(function (el) {
    obj[el] ? obj[el]++ : (obj[el] = 1);
  });

  for (prop in obj) {
    if (obj[prop] % 2 !== 0) return Number(prop);
  }
}

console.log(findOdd([20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5]));

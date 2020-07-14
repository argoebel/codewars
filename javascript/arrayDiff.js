// https://www.codewars.com/kata/523f5d21c841566fde000009/train/javascript
// Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.

// It should remove all values from list a, which are present in list b.

// arrayDiff([1,2],[1]) == [2]
// If a value is present in b, all of its occurrences must be removed from the other:

// arrayDiff([1,2,2,2,3],[2]) == [1,3]

// my solutions

function arrayDiff1(a, b) {
  for (var i = 0; i < b.length; i++) {
    var pos = 0;
    while (pos <= a.length) {
      if (a[pos] == b[i]) {
        a.splice(pos, 1);
      } else {
        pos += 1;
      }
    }
  }
  return a;
}

function arrayDiff2(a, b) {
  return a.filter((element) => !b.includes(element));
}

// other solutions

function array_diff10(a, b) {
  return a.filter((e) => !b.includes(e));
}

function array_diff11(a, b) {
  return a.filter(function (x) {
    return b.indexOf(x) == -1;
  });
}

console.log(arrayDiff2([3, 4], [3]));
console.log(arrayDiff2([], [4, 5]));
console.log(arrayDiff2([1, 8, 2], []));

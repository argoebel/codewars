// https://www.codewars.com/kata/525f3eda17c7cd9f9e000b39/train/javascript
// This time we want to write calculations using functions and get the results. Let's have a look at some examples:

// seven(times(five())); // must return 35
// four(plus(nine())); // must return 13
// eight(minus(three())); // must return 5
// six(dividedBy(two())); // must return 3
// Requirements:

// There must be a function for each number from 0 ("zero") to 9 ("nine")
// There must be a function for each of the following mathematical ops: plus, minus, times, dividedBy (divided_by in Ruby and Python)
// Each calculation consist of exactly one op and two numbers
// The most outer function represents the left operand, the most inner function represents the right operand
// Divison should be integer division. For example, this should return 2, not 2.666666...:
// eight(dividedBy(three()));

// my solutions

// function zero(op) {
//   return op ? eval(`0${op}`) : 0;
// }
// function one(op) {
//   return op ? eval(`1${op}`) : 1;
// }
// function two(op) {
//   return op ? eval(`2${op}`) : 2;
// }
// function three(op) {
//   return op ? eval(`3${op}`) : 3;
// }
// function four(op) {
//   return op ? eval(`4${op}`) : 4;
// }
// function five(op) {
//   return op ? eval(`5${op}`) : 5;
// }
// function six(op) {
//   return op ? eval(`6${op}`) : 6;
// }
// function seven(op) {
//   return op ? eval(`7${op}`) : 7;
// }
// function eight(op) {
//   return op ? eval(`8${op}`) : 8;
// }
// function nine(op) {
//   return op ? eval(`9${op}`) : 9;
// }
// function plus(operand) {
//   return `+${operand}`;
// }
// function minus(operand) {
//   return `-${operand}`;
// }
// function times(operand) {
//   return `*${operand}`;
// }
// function dividedBy(operand) {
//   return `/${operand}|0`;
// }

function zero(op) {
  return op ? op(0) : 0;
}
function one(op) {
  return op ? op(1) : 1;
}
function two(op) {
  return op ? op(2) : 2;
}
function three(op) {
  return op ? op(3) : 3;
}
function four(op) {
  return op ? op(4) : 4;
}
function five(op) {
  return op ? op(5) : 5;
}
function six(op) {
  return op ? op(6) : 6;
}
function seven(op) {
  return op ? op(7) : 7;
}
function eight(op) {
  return op ? op(8) : 8;
}
function nine(op) {
  return op ? op(9) : 9;
}
function plus(b) {
  return function op(a) {
    return a + b;
  };
}
function minus(b) {
  return function op(a) {
    return a - b;
  };
}
function times(b) {
  return function op(a) {
    return a * b;
  };
}
function dividedBy(b) {
  return function op(a) {
    return (a / b) | 0;
  };
}

console.log(seven(times(five())));
console.log(eight(dividedBy(three())));

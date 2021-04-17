function count (string) {  
    var count = {};
    string.split('').forEach(function(s) {
        console.log(s)
        count[s] ? count[s]++ : count[s] = 1;
    });
    return count;
  }

console.log(count('aba'))
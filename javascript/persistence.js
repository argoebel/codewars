function persistence(num) {
  let i = 0
  while (String(num).length > 1) {
    num = String(num).split('').reduce((acc, val) => {
      return acc * Number(val)
    })
    i++
  }
  return i
}

console.log(persistence(39))
// https://www.codewars.com/kata/57f8ff867a28db569e000c4a/train/javascript
// Modify the kebabize function so that it converts a camel case string into a kebab case.
// function kebabize(str) {
//   return str.replace(/[A-Z0-9]/g, x => {
//     return Number(x) == x ? '' : '-' + x.toLowerCase()
//   })
// }

// function kebabize(str) {
//   console.log(str)
//   str = str.replace(/[0-9]/g, '')
//   str[0] = str[0].toLowerCase()
//   return str.replace(/[A-Z]/g, x => '-' + x.toLowerCase())
// }

// function kebabize(str) {
//   str = str.replace(/[0-9]/g, '')
//   return str.substr(0,1).toLowerCase() + str.substr(1).replace(/[A-Z]/g, x => '-' + x.toLowerCase())
// }

function kebabize(str) {
  return str.replace(/[0-9]/g, '').split(/(?=[A-Z])/g).join('-').toLowerCase()
}


console.log(kebabize('camelsHave3Humps'))
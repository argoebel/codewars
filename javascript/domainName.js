// https://www.codewars.com/kata/514a024011ea4fb54200004b/train/javascript
// Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:

// domainName("http://github.com/carbonfive/raygun") == "github"
// domainName("http://www.zombie-bites.com") == "zombie-bites"
// domainName("https://www.cnet.com") == "cnet"

function domainName(url) {
  return url
    .replace("http://", "")
    .replace("https://", "")
    .replace("www.", "")
    .split(".")[0];
}
domainName("http://github.com/carbonfive/raygun");
domainName("http://google.com");
domainName("http://google.co.jp");
domainName("www.xakep.ru");
domainName("https://youtube.com");

#!/usr/bin/node
const len = process.argv.length;
let big;
let bigt = 0;
if (len <= 2) {
  console.log(0);
} else {
  for (let i = 2; i < len; i++) {
    if (parseInt(process.argv[i]) > bigt) {
      big = bigt;
      bigt = parseInt(process.argv[i]);
    } else if (parseInt(process.argv[i]) > big) {
      big = parseInt(process.argv[i]);
    }
  }
}
console.log(big);

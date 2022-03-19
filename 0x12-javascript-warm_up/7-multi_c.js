#!/usr/bin/node
let x = parseInt(process.argv[2]);

if (x > 0) {
  while (x !== 0) {
    console.log('C is fun');
    x--;
  }
} else if (x < 0) {

} else {
  console.log('Missing number of occurrences');
}

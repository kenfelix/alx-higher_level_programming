#!/usr/bin/node
let x = parseInt(process.argv[2]);

if (x) {
  while (x !== 0) {
    console.log('C is fun');
    x--;
  }
} else {
  console.log('Missing number of occurrences');
}

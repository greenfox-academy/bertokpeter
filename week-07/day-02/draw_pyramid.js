'use strict';

let lineCount = 4;

// Write a program that draws a
// pyramid like this:
//
//
//    *
//   ***
//  *****
// *******
//
// The pyramid should have as many lines as lineCount is

for (let i = 1; i < lineCount+1; ++i) {
    console.log(" ".repeat(lineCount-i) + "*".repeat(i*2-1));
}
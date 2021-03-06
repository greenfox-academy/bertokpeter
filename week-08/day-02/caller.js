'use strict';

// Implement the selectLastEvenNumber function that takes an array and callback,
// it should call the callback immediately with the last even number on the array


function printNumber(num) {
  console.log(num);
}

selectLastEvenNumber([2, 5, 7, 8, 9, 11], printNumber); // should print 8

function selectLastEvenNumber(numList, callback) {
    let lastEven = numList.filter(number => number%2 === 0);
    callback(lastEven[lastEven.length-1]);
}
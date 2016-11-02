console.log("Getting started with javascript");

var myNumber = 10;
console.log(myNumber);

var myArray = [10, "tommy", [10, 90, 12], "fred"]
console.log(myArray);
console.log(myArray[2]);
console.log(myArray[2][1]);

// for item in array: -- with python

for (var i = 0 ; i < myArray.length ; i++ ) {
  // var item = myArray[i];
  //console.log(item);
  console.log(myArray[i]);
}

// object literal in js is equivalent to dictionary in py
var myObject = {
  myName: "tommy",
  myAge: "23"
};
console.log(myObject["myName"]);
// OR
console.log(myObject.myName);


// function
var myFunc = function(x, y) {
  return x * y;
};
console.log(myFunc(9, 4));

// another way to do a for loop
var sillyArray = [9, 8, 3, 6, 1, 2, 999];

var loopFunc = function(item) {
  console.log(item);
};

sillyArray.forEach(loopFunc);

sillyArray.forEach(function(item) {
  console.log(item);
});

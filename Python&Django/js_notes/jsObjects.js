// Objects refer to a specific thing in JS, KVPs
// Objects are a collection of properties
// Keys are not set as strings
var carInfo = {make: "Toyota", year: 1990, model: "Camry"};

// when searching for a key, it needs to b passed in as a string
carInfo["make"];

// You can also put arrays in JS Objects
var myNewO = {a: "hello", b: [1,2,3], c: {inside: ["a", "b"]}}
// In order to parse nested arrays, you need to use multiple brackets
// Below will return 'b'
myNewO["c"]["inside"][1];

// add/change values to an object, below will change the year to 2006
carInfo["year"] = 2006;
// Ypu can also edit the value of the key, depending on its data type
carInfo["year"] += 1;

// This will show the object in the console
// This will help with viewing very lorge objects
console.dir(carInfo);

// You can iterate through Objects like this, however there is no set order for keys, and will display in random order
for (key in carInfo) {
    // This will show only the keys of the Object
    console.log(key);
    // This will show the values and keys
    console.log(carInfo[key]);
}

// Object methods
// You can apply functions as a value for a key
var myObj = {
    name: "Jose",
    // use the FUNCTION keyford to define the key as a function
    // the THIS keyword refers to the value within the object
    greet: function() {
        console.log("Hello " + this.name);
    }
}
// Youwould call it like this
console.log(myObj.greet())

// calling the Object will only show the variable keys, not the functions
// To see the function as well, use the console.dir() method


// Array methods for JS

var myArray = ['one','two','three'];

var lastItem = myArray.pop(); // removes last item from array and assigns to a variable

var lastKeptItem = myArray[myArray.length -1]  // returns last item in array without removing it

// This will iterate through the array and print each item
for (word of myArray) {
    console.log(word);
}

// You can also do FOR/EACH to cycle through an array and do something for each itme in it
// This will alert each item in the array
myArray.forEach(alert);

function addAwesome(name) {
    console.log(name+ ' is awesome!');
}

var topics = ['python','django','science'];

// You can also call functions as you cycle through the array
topics.forEach(addAwesome);

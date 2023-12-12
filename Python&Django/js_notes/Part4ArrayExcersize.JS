// Arrays project
// will need the add, remove, display, and quit features

// array of names
var names = [];

// function to add, remove, display, and quit the array
function addName() {
    var newName = prompt('What name would you like to add?');
    names.push(newName);
    console.log(names);
}

function removeName() {
    var oldName = prompt('What name would you like to remove?');
    // .indexOf will return the index of the name in the array
    var index = names.indexOf(oldName)
    // .splice will remove the name from the array
    names.splice(index,1);
    console.log(names);
}

function displayNames() {
    console.log(names);
}
 function quit() {
    console.log('Goodbye!');
    request = 'quit';
 }

//  prompts for user input/logic
var userCheck = prompt('Are you a student of this class? (y/n): ');
var request = '#'

if (userCheck == 'y') {
    while (request !== 'quit') {
        var userInput = prompt('What would you like to do? (add/remove/display/quit): ');
        if (userInput == 'add') {
            addName();
        } else if (userInput == 'remove') {
            removeName();
        } else if (userInput == 'display') {
            displayNames();
        } else if (userInput == 'quit') {
            quit();
        } else {
            alert('Sorry, I don\'t understand.');
        }
    }
}
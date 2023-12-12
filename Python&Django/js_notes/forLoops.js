// for loops

// JS forloops have 3 statements used in a for loop, it will look something like this
// for (statement1; statement2; statement3) {
    // code block to be executed
// }

// statement1 is executed before the loop (the code block) starts.
// statement2 defines the condition for running the loop (the code block).
// statement3 is executed each time after the loop (the code block) has been executed.

// for loop that prints all even numbers from 1 to 10, same as the WHILE loop
for (var i = 0; i < 5; i++) {
    console.log('Number is ' + i);
}

// This for loop prints each letter in the var word
var word = 'ABCDEFGHIJK';

for (let i = 0; i < word.length; i++) {
    console.log(word[i]);
}
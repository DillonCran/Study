var x = 0;

while (x < 5) {
    console.log('x is currently: ' + x);
    console.log('x is still less than 5, adding 1 to x');

    if (x === 3) {
        console.log('x is equal to 3!');
        break;
    }

    x = x + 1;
} 


// while loop that prints all even numbers from 1 to 10
var Y = 0;

while (Y <= 10) {
    if (Y % 2 == 0) {
        console.log(Y);
    }
    Y += 1;
}
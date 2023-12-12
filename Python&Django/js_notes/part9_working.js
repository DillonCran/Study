// Secret spy challenge


// prompts
var _spyName = prompt('what is your full name?: ');
var _splitName = _spyName.split(' ');
var _spyFirst = _splitName[0];
var _spyLast = _splitName[1];
console.log(_spyFirst);
console.log(_spyLast);

var _spyAge = prompt('how old are you?: ');
console.log(_spyAge);

var _spyHeight = prompt('how tall are you? (cm): ');
console.log(_spyHeight);

var _spyPet = prompt('what is your pets name?');
var _splitPet = _spyPet.at(-1);
console.log(_splitPet);

// logic

if (_spyFirst[0] === _spyLast[0] && _spyAge > 20 && _spyAge < 30 && _spyHeight >= 170 && _splitPet === 'y') {
  alert('Welcome Comrade! You\'ve passed the Spy Test!');
  console.log('weve got you now!')
} else {
    console.log('youre not a spy!')
}


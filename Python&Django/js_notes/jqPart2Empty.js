// 

var h1Clicks = 0;
$('h1').click(
    
    function() {
    if (h1Clicks % 2 == 0) {
    $(this).text('CHANGED HERE!')
    } else {
    $(this).text('CHANGED BACK!')
    }
    h1Clicks++;
});

$('li').click(function() {
    console.log('any li was clicked')
});

// Keypresses
// This function turns on and off the class 'turnBlue' on h3 when typing into the text box
// $('input').eq(0).keypress(function(){
//     $('h3').toggleClass('turnBlue');
// })

// This function prints the event object to the console when typing into the text box
// In the console log you can see the event paramater WHICH at the bottom that has a unicode number that corrilates to the letter typed
$('input').keypress(function(event){
    console.log(event);
})

// This function listens for a specific key press in the event tag
$('input').eq(0).keypress(function(event){
    if (event.which === 13) {
        $('h3').toggleClass('turnBlue');
    }
})

// ON method
$('h1').on('dblclick',function(){
    $(this).toggleClass('turnBlue');
})

// effects
$('input').eq(1).on('click',function(){

    $('.container').fadeOut(3000);
})
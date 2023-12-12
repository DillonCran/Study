var hot = false
var temp = 60

if (temp>80) {
    console.log('hot outside!')
} else if (temp <= 80 && temp >= 50) {
    console.log('average temp outside')
} else if (temp < 50 && temp >= 32) {
    console.log('its pretty cold out')
} else {
    console.log('its very cold out')
}

console.log(hot)

var ham = 10
var cheese = 10

var report = '#'

if (ham >= 10 && cheese >= 10) {
    report = 'Strong sales of Ham & Cheese'
} else if (ham === 0 && cheese === 0) {
    report = 'Nothing sold!'
} else {    
    report = 'Sales are Decent'
}

console.log(report);

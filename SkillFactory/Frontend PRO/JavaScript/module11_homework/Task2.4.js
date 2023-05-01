let num1 = 3;
let num2 = 15;

const IIFE = function() {
    let num = num1
    function increment() {
        if (num == num2) {
            clearInterval(intervalID)
        }
        console.log(num)
        num++
    }
    return increment
}()

let intervalID = setInterval(IIFE, 1000)

function getFirstNumber(num1) {
    return function (num2) {
        return num1 + num2
    }
}

let getSecondNumber = getFirstNumber(3)

console.log(getSecondNumber(2))
let num = 277;

function simpleNumberFinder(num) {
    if (num > 1000 || isNaN(num) || typeof num != "number") {
        return "Данные неверны!"
    } else {
        for (let i = 2; i < num; i++) {
            if (num % i == 0) {
                return "Число не является простым"
            }
        } if (num < 2) {
            return "Число не является простым"
        } else {
            return "Число простое"
        }
    }
}

console.log(simpleNumberFinder(num))
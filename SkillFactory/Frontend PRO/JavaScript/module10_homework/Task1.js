var a = prompt("Enter number: ");

if (typeof +a == "number" && a != "") {
	if (isNaN(a)) {
		console.log("Увы, кажется вы ошиблись")
	} else if (+a % 2 == 0) {
		console.log("Число чётное")
	} else {
		console.log("Число нечётное")
	}
} else {
	console.log("Увы, кажется вы ошиблись")
}
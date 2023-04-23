function reverser(string) {
	var string = string.split("").reverse().join("")
	return string
}

console.log(reverser("Hello"))
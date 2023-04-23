const arr = [1, 1, 1, 1, 1];
var result = true;

for (let i = 1; i < arr.length; i++) {

	if (arr[i - 1] !== arr[i]) {
		result = false
	}

}

console.log(result)
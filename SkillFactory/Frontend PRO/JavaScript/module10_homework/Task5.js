var arr = [6, 3, 9, 1];

console.log("Количество элементов в массиве: " + arr.length)

let result = arr.map(function(item, index, array) {
	console.log(`Элемент массива с индексом ${index}: ` + item)
});
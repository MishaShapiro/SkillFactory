var arr = [1, 2, 3, 4, 55, 67, 77, NaN, null];
var chet = 0;
var nechet = 0;
var zeroCounterStr = "", zeroCounter = 0


arr.forEach(function(item, index, array) {
	if (typeof item == "number" && !(isNaN(item))) {
		if (item % 2 == 0) {
			chet++
			if (item == 0) {
				zeroCounter++
				zeroCounterStr = `Также есть ${zeroCounter} нулей`;
			}
		} else {
			nechet++
		}
	}
});

console.log(`В массиве ${chet} чётных элементов и ${nechet} нечётных. ` + zeroCounterStr)
var newMap = new Map;
newMap.set("string", "type")
newMap.set(true, "values")
newMap.set(123, "count")
newMap.set(null, null)

for (var key of newMap.keys()) {
	console.log(`Ключ - ${key}, значение - ${newMap.get(key)}`)
}
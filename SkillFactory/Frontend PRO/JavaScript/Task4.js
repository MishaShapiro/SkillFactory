function random(min, max) {  
  var count = Math.floor(Math.random() * (min + max))
  return count
}

console.log(random(0, 100))
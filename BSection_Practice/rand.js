const dejavu = [0, 1, 6, 11, 12]
var ranint = 0
while (ranint in dejavu) {
    var ranint = Math.floor(Math.random() * (12 - 1 + 1)) + 1;
}
console.log(ranint)
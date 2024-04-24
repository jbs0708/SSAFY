const numbers1 = [1, 2, 3, 4, 5]

console.log(numbers1.reduce(function (acc, cur) {
    acc.push(cur*2)
    return acc;
}, []))
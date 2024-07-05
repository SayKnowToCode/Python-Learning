let n = 10;
console.log("For n = ", n);
let newArray = new Array(n);

for (let i = 0; i < n; i++) {
    newArray[i] = i + 1;
}

for (let i = n - 1; i >= 1; i--) {
    // Example usage:
    let randomInt = Math.floor(Math.random() * i);
    let temp = newArray[i];
    newArray[i] = newArray[randomInt];
    newArray[randomInt] = temp;
}

console.log(newArray);
console.log(newArray.length);
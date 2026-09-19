// This version is just a list of numbers in the command line.

// for (i, i>=100, i++) {
//    console.log(i);
//}

for (let i = 1; i <= 100; i++) {
    let word = "";
    if (i % 3 == 0) {word += "Fizz";}
    if (i % 5 == 0) {word += "Buzz";}
    if (word == "") {word = i;}
    console.log(word);
}
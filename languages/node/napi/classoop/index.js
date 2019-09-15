//index.js
const testAddon = require('./build/Release/testaddon.node');

console.log('addon',testAddon);
console.log(testAddon.hello());

console.log(testAddon.add(1,2));

//c++ oop test
console.log("***************************************");
console.log("Doble oop class tests");
console.log("***************************************");
const classInstance = new testAddon.WrapperClass(4.3);
console.log('Testing class initial value '+classInstance.getValue());
console.log('After adding 3.3 its '+classInstance.add(3.3));

// module.exports = testAddon;
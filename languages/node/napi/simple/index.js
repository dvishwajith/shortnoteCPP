//index.js
const testAddon = require('./build/Release/testaddon.node');

console.log('addon',testAddon);
console.log(testAddon.hello());

console.log(testAddon.add(1,2));

module.exports = testAddon;
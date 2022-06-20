const fs = require('fs');
const data = fs.readFileSync('input.txt', 'utf8');

const [a,b] = data.split('\r\n')

const numA = a.split(' ').map(elem => parseInt(elem))
const numB = +b
const sum = numA.reduce((elem,res) => elem + res, 0)

let money = 0

if (numB <= sum) {
    money = 0
}else{
    money = numB - sum
}


fs.writeFileSync('output.txt', `${money}`, 'utf8')
## Metasyntax

### while

```
while (condition)
	statement
```



### if...else

```
if (condition)
	statement1
[else
	statement2]
```



### do...while

```
do
	statement
while (condition);
```



### switch

```
switch (expression) {
	case value1:
		statement1
		[break;]
	case value2:
		statement2
		[break;]
	case valueN:
		statementN
		[break;]
	default:
		statement
		[break;]
}
```



### for

```
for ([initialization]; [condition]; [final-expression])
	statement
```



### for...in

```
for (variable in object)
	statement
```



#### e.g.

```javascript
const player = { name: 'Thomas', rank: 'Midshipman', age: 25 }
for (let prop in player) {
    if (!player.hasOwnProperty(prop)) continue
    console.log(prop + ': ' + player[prop])
}
```



### for...of(ES6)

```
for(variable of object)
	statement
```



#### e.g.

```javascript
const ranNum = [Math.random(), Math.random(), Math.random()]
for (let r of ranNum)
    	console.log(`Random number: ${r}`)
```


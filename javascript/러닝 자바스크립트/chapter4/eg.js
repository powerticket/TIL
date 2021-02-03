const player = { name: 'Thomas', rank: 'Midshipman', age: 25 }
for (let prop in player) {
    if (!player.hasOwnProperty(prop)) continue
    console.log(prop + ': ' + player[prop])
}

const ranNum = [Math.random(), Math.random(), Math.random()]
for (let r of ranNum)
      console.log(`Random number: ${r}`)

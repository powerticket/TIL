console.log('main.js is loaded.')

// jQuery
$(document).ready(function() {
  'use strict'
  console.log('main.js with jQuery is loaded.')
  paper.install(window)
  paper.setup(document.getElementById('mainCanvas'))

  // drawing
  const c = Shape.Circle(200, 200, 80)
  c.fillColor = 'black'
  const text = new PointText(200, 200)
  text.justification = 'center'
  text.fontSize = 20
  text.fillColor = 'white'
  text.content = 'Hello, World!'
  // const c = Shape.Circle(200, 200, 50)
  // c.fillColor = 'green'
  // let c;
  // for (let x = 25; x < 400; x += 50) {
  //   for (let y = 25; y < 400; y += 50) {
  //     c = Shape.Circle(x, y, 20)
  //     c.fillColor = 'green'
  //   }
  // }
  // const tool = new Tool()
  // tool.onMouseDown = function (event) {
  //   // const c = Shape.Circle(event.point.x, event.point.y, 20)
  //   const c = Shape.Circle(event.point, 20)
  //   c.fillColor = 'green'
  // }
  paper.view.draw()
})

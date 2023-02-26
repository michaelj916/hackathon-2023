// frequency / mod => x and y
let fX, fY, mX, mY;

function setup() {
//create the boxed window??
  createCanvas(window.innerWidth - 25, window.innerHeight - 150).parent("canvas").
  //create random number when the clocks the window
  mouseClicked(rand);
  //What does this do???????
  colorMode(RGB)
  //what does this do?????
  noFill()
  //setting the speed at which we view the roatation
  frameRate(120)  
}
 //function for making random x and y coordinated between values paramaterized
function rand() {
  fX = floor(random(6000, 10000))
  fY = floor(random(6000, 10000))
  mX = floor(random(6000, 10000))
  mY = floor(random(6000, 10000))
}

//
function addVert(i) {
  curveVertex(
    sin(i * fX + radians(frameCount * 3)) * cos(i * mX) * width / 2,
    sin(i * fY) * cos(i * mY) * height / 2
  )
}

//function for
function draw() {
  background(0);
  let i = 0;
  clear()

  translate(width / 2, height / 2)
  beginShape()
  fill('#000000d0')
  addVert(i)
  for (i; i < TWO_PI; i += TWO_PI / 180) {
    addVert(i)
  }
  addVert(i)
  endShape()
}
var colorWell1;
var colorWell2;
var effect;
var selectedeffect;
var defaultColor1 = "#0000ff";
var defaultColor2 = "#ff0000";
var defaultEffect = "static";
var r1 = 255
var g1 = 0
var b1 = 0
var r2 = 0 //todo: change so color is dynamic, not set to only 2 colors
var g2 = 0
var b2 = 255

window.addEventListener("load", startup, false);

function startup() {
  effect = document.querySelector("#selectedeffect");
  colorWell1 = document.querySelector("#colorWell1");
  colorWell2 = document.querySelector("#colorWell2");
  colorWell2Label = document.querySelector("#colorWell2Label");
  colorWell2.hidden = true
  colorWell2Label.hidden = true
  colorWell1.value = defaultColor1;
  colorWell2.value = defaultColor2;
  effect.value = defaultEffect;
  selectedeffect = defaultEffect;
  colorWell1.addEventListener("change", update1, false);
  colorWell2.addEventListener("change", update2, false);
  effect.addEventListener("input", effectChange, false);
  colorWell1.select();
  colorWell2.select();
}

function update1(event) {
  console.log(hexToRgb(event.target.value));
  console.log(String(effect))
  color = hexToRgb(event.target.value);
  r1 = color.r;
  g1 = color.g;
  b1 = color.b;
}

function update2(event) {
  console.log(hexToRgb(event.target.value));
  console.log(String(effect))
  color = hexToRgb(event.target.value);
  r2 = color.r;
  g2 = color.g;
  b2 = color.b;
}

function effectChange(event) {
  selectedeffect = event.target.value
  if (selectedeffect == "colorwipe") {
    colorWell1.disabled = false;
    colorWell2.hidden = false;
    colorWell2Label.hidden = false;
  } else if (selectedeffect == "rainbow") {
    colorWell1.disabled = true;
    colorWell2.hidden = true;
    colorWell2Label.hidden = true;
  } else {
    colorWell1.disabled = false;
    colorWell2.hidden = true;
    colorWell2Label.hidden = true;
  }
  console.log(selectedeffect)
}

function hexToRgb(hex) {
  var result = /^#?([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})$/i.exec(hex);
  return result ? {
    r: parseInt(result[1], 16),
    g: parseInt(result[2], 16),
    b: parseInt(result[3], 16)
  } : null;
} //https://stackoverflow.com/questions/5623838/rgb-to-hex-and-hex-to-rgb

import lightstrip as ls
import neopixel
import board

from flask import Flask, jsonify, render_template, request

app = Flask(__name__)
pixels = neopixel.NeoPixel(board.D18, 300, bpp = 3, brightness = 0.1)
lightstrip = ls.LightStrip(pixels)

@app.route("/")

def main():
    return render_template('index.html')

@app.route('/turnonlights')
def turnonlights():
    lightstrip.turnOn()
    return jsonify(status="success")


@app.route('/turnofflights')
def turnofflights():
    lightstrip.turnOff()
    return jsonify(status="success")


@app.route('/seteffect')
def seteffect():
    r1 = request.args.get("r1")
    g1 = request.args.get("g1")
    b1 = request.args.get("b1")
    r2 = request.args.get("r2")
    g2 = request.args.get("g2")
    b2 = request.args.get("b2")
    effect = request.args.get("effect")
    print("r1: " + r1)
    print("g1: " + g1)
    print("b1: " + g1)
    print("r2: " + r2)
    print("g2: " + g2)
    print("b2: " + b2)
    print(effect)
    lightstrip.setEffect(effect, (int(r1), int(g1), int(b1)), (int(r2), int(g2), int(b2)))
    return jsonify(status="success")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5050)

from flask import Flask,render_template,flash, Response,jsonify

app = Flask(__name__)
from arduino import Connection

app.config['SECRET_KEY'] = '1de2d95051ff6e819cdb7c62c92bdd5f'
arduino = Connection('/dev/cu.usbmodem143201',9600)
arduino.readData()

light = [0]*10
humidity = [0]*10
tempC = [0]*10
moisture = [0]*10

def update(l, new):
    l.pop(0)
    l.append(new)
    return l

@app.route("/", methods=['GET','POST'])
def home():
    # light = arduino.getLightIntensity()
    # humidity = arduino.getHumidity()
    # tempC = arduino.getTempC()
    # tempF = arduino.getTempF()
    # moisture = arduino.getMoistureValue()
    data = arduino.getData();
    return render_template('home.html',data = data)

@app.route('/data')
def data():
    data = arduino.readData()
    Ylight = update(light,data[0])
    Yhumidity = update(humidity,data[1])
    YtempC = update(tempC, data[2])
    Ymoisture = update(moisture, data[4])
    x = list(range(0,10))
    print(data)
    return jsonify({'light': {'x': x,'y':Ylight},
                    'humidity':{'x': x,'y':Yhumidity},
                    'tempC':{'x': x,'y':YtempC},
                    'tempF': data[3],
                    'moisture':{'x': x,'y':Ymoisture}})

if __name__ == '__main__':
    app.run(debug=True)
    


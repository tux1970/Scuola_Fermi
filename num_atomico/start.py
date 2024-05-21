from flask import Flask, render_template, request
import periodictable

app = Flask(__name__)
ip_addr="0.0.0.0"
port_addr="8090"

def get_element_info(atomic_number):
    try:
        element = periodictable.elements[atomic_number]
        info = {
            'name': element.name,
            'symbol': element.symbol,
            'atomic_number': element.number,
            'atomic_weight': element.mass,
            'density': element.density
        }
        return info
    except KeyError:
        return None

@app.route('/', methods=['GET', 'POST'])
def index():
    element_info = None
    if request.method == 'POST':
        try:
            atomic_number = int(request.form['atomic_number'])
            element_info = get_element_info(atomic_number)
        except ValueError:
            element_info = "Elemento non valido, inserire un nuovo numero atomico."
    return render_template('index.html', element_info=element_info)

if __name__ == '__main__':
    app.run(host=ip_addr, port=port_addr)

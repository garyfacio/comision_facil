from flask import Flask, render_template

# Crear la aplicación Flask
app = Flask(__name__)

# Configuración básica
app.config['SECRET_KEY'] = 'comision-facil-2025'

@app.route('/')
def index():
    """Página principal de Comisión Fácil"""
    return render_template('index.html')

@app.route('/como-funciona')
def como_funciona():
    """Página detallada de cómo funciona el servicio"""
    return render_template('como_funciona.html')

@app.route('/contacto')
def contacto():
    """Página de contacto"""
    return render_template('contacto.html')

if __name__ == '__main__':
    # Ejecutar la aplicación en modo debug para desarrollo
    app.run(debug=True, host='0.0.0.0', port=5000)
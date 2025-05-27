from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def para_decimal(numero_str, base):
    """
    Converte um número em forma de string de uma base para decimal.
    """
    digitos = '0123456789ABCDEF'
    numero_str = numero_str.upper()
    decimal = 0

    for i, digito in enumerate(reversed(numero_str)):
        if digito not in digitos[:base]:
            raise ValueError(f'Dígito inválido para base {base}: {digito}')
        valor = digitos.index(digito)
        decimal += valor * (base ** i)
    return decimal

def de_decimal(numero, base):
    """
    Converte um número decimal para a base especificada.
    """
    if numero == 0:
        return '0'
    digitos = '0123456789ABCDEF'
    resultado = ''

    while numero > 0:
        resto = numero % base
        resultado = digitos[resto] + resultado
        numero //= base

    return resultado

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/equipe')
def equipe():
    return render_template('equipe.html')

@app.route('/conversor')
def conversor():
    return render_template('conversor.html')

@app.route('/converter', methods=['POST'])
def converter():
    numero = request.form['numero']
    base_origem = request.form['base_origem']
    base_destino = request.form['base_destino']

    try:
        # Mapeando bases
        bases = {
            'decimal': 10,
            'binario': 2,
            'octal': 8,
            'hexadecimal': 16
        }

        if base_origem not in bases or base_destino not in bases:
            return jsonify({'erro': 'Base inválida!'})

        base_origem_valor = bases[base_origem]
        base_destino_valor = bases[base_destino]

        # Conversão para decimal
        decimal = para_decimal(numero, base_origem_valor)

        # Conversão para destino
        if base_destino == 'decimal':
            resultado = str(decimal)
        else:
            resultado = de_decimal(decimal, base_destino_valor)

        return jsonify({'resultado': resultado})
    except Exception as e:
        return jsonify({'erro': str(e)})

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, request, jsonify
import numpy as np
from os import environ, getpid
from waitress import serve
#from multiprocessing import cpu_count

app = Flask(__name__)


@app.route('/')
def hello():
    return f'Hello World from Worker {getpid()}'


@app.route('/matrixmult', methods=['POST'])
def matrix_multiply():
    data = request.get_json()
    A = data.get('A')
    B = data.get('B')

    if A is None or B is None:
        return jsonify({'error': 'Matrix A or B is missing.'}), 400

    try:
        # Convert lists to numpy arrays
        matrix_a = np.array(A)
        matrix_b = np.array(B)

        # Perform matrix multiplication
        product = np.dot(matrix_a, matrix_b)

        # Send the result as a response
        return jsonify({'product': product.tolist()})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    #port = int(environ.get('PORT', 3000))
    port = 5000
    app.run(host='0.0.0.0', port=port)

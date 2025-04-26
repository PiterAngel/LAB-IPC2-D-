from flask import Flask, render_template, request, jsonify, send_file
import xml.etree.ElementTree as ET
import os
from utils.xml_processor import process_xml, validate_xml

app = Flask(__name__)

# Ruta al archivo XML
XML_FILE = 'autorizaciones.xml'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ayuda')
def ayuda():
    return render_template('ayuda.html')

@app.route('/api/cargar-archivo', methods=['POST'])
def cargar_archivo():
    if 'file' not in request.files:
        return jsonify({'error': 'No se encontró ningún archivo'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No se seleccionó ningún archivo'}), 400

    if not file.filename.endswith('.xml'):
        return jsonify({'error': 'El archivo debe ser XML'}), 400

    try:
        # Guardar temporalmente el archivo
        temp_path = 'temp_upload.xml'
        file.save(temp_path)

        # Validar y procesar el XML
        if not validate_xml(temp_path):
            os.remove(temp_path)
            return jsonify({'error': 'El archivo XML no es válido'}), 400

        # Procesar el archivo XML
        result = process_xml(temp_path)
        os.remove(temp_path)

        return jsonify({'message': 'Archivo procesado correctamente', 'result': result})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/consultar-datos', methods=['GET'])
def consultar_datos():
    try:
        if not os.path.exists(XML_FILE):
            return jsonify({'error': 'No hay datos disponibles'}), 404

        # Leer el archivo XML
        tree = ET.parse(XML_FILE)
        root = tree.getroot()

        # Convertir XML a diccionario para enviar como JSON
        data = {}
        for autorizacion in root.findall('AUTORIZACION'):
            fecha = autorizacion.find('FECHA').text.strip()
            facturas_recibidas = autorizacion.find('FACTURAS_RECIBIDAS').text.strip()
            facturas_correctas = autorizacion.find('FACTURAS_CORRECTAS').text.strip()

            data[fecha] = {
                'facturas_recibidas': facturas_recibidas,
                'facturas_correctas': facturas_correctas,
                'errores': {}
            }

            errores = autorizacion.find('ERRORES')
            for error_type in errores:
                data[fecha]['errores'][error_type.tag] = error_type.text.strip()

        return jsonify(data)

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/reset', methods=['POST'])
def reset():
    try:
        if os.path.exists(XML_FILE):
            os.remove(XML_FILE)
        return jsonify({'message': 'Sistema reiniciado correctamente'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/enviar', methods=['POST'])
def enviar():
    try:
        data = request.json
        if not data or 'solicitudes' not in data:
            return jsonify({'error': 'No se recibieron solicitudes'}), 400

        # Aquí iría la lógica para procesar las solicitudes
        # y generar los códigos de autorización

        return jsonify({'message': 'Solicitudes procesadas correctamente'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/estudiante', methods=['GET'])
def estudiante():
    info = {
        'nombre': 'Nombre del Estudiante',
        'carnet': '123456789',
        'curso': 'IPC2'
    }
    return jsonify(info)

@app.route('/api/documentacion', methods=['GET'])
def documentacion():
    docs = {
        'titulo': 'Documentación del Proyecto 3',
        'descripcion': 'API para autorización de DTE'
    }
    return jsonify(docs)

if __name__ == '__main__':
    app.run(debug=True)
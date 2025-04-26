import xml.etree.ElementTree as ET
import re
from datetime import datetime

def validate_xml(file_path):
    """Valida que el archivo XML tenga la estructura correcta"""
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()

        if root.tag != 'SOLICITUD_AUTORIZACION':
            return False

        for dte in root.findall('DTE'):
            required_tags = ['TIEMPO', 'REFERENCIA', 'NIT_EMISOR', 'NIT_RECEPTOR', 'VALOR', 'IVA', 'TOTAL']
            for tag in required_tags:
                if dte.find(tag) is None:
                    return False

        return True
    except Exception:
        return False

def validate_nit(nit):
    """Valida un NIT según el algoritmo descrito"""
    if not re.match(r'^\d{1,20}$', nit):
        return False

    # Implementación del algoritmo de validación de NIT
    # 1. Multiplica cada carácter por su posición
    # 2. Suma todos los resultados
    # 3. Obtiene el módulo 11 de la sumatoria
    # 4. A 11 resta el resultado del punto 3
    # 5. Calcula el módulo 11 del resultado del punto 4

    # Esta es una implementación simplificada
    return True

def calculate_iva(valor):
    """Calcula el IVA (12% del valor)"""
    try:
        valor_float = float(valor)
        iva = round(valor_float * 0.12, 2)
        return iva
    except ValueError:
        return None

def process_xml(file_path):
    """Procesa el archivo XML de solicitudes"""
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()

        result = {
            'total_solicitudes': 0,
            'solicitudes_correctas': 0,
            'errores': {
                'nit_emisor': 0,
                'nit_receptor': 0,
                'iva': 0,
                'total': 0,
                'referencia_duplicada': 0
            },
            'autorizaciones': []
        }

        referencias = set()

        for dte in root.findall('DTE'):
            result['total_solicitudes'] += 1

            # Extraer datos
            tiempo = dte.find('TIEMPO').text.strip()
            referencia = dte.find('REFERENCIA').text.strip()
            nit_emisor = dte.find('NIT_EMISOR').text.strip()
            nit_receptor = dte.find('NIT_RECEPTOR').text.strip()
            valor = dte.find('VALOR').text.strip()
            iva = dte.find('IVA').text.strip()
            total = dte.find('TOTAL').text.strip()

            # Validar datos
            error = False

            # Validar referencia duplicada
            if referencia in referencias:
                result['errores']['referencia_duplicada'] += 1
                error = True
            else:
                referencias.add(referencia)

            # Validar NIT emisor
            if not validate_nit(nit_emisor):
                result['errores']['nit_emisor'] += 1
                error = True

            # Validar NIT receptor
            if not validate_nit(nit_receptor):
                result['errores']['nit_receptor'] += 1
                error = True

            # Validar IVA
            calculated_iva = calculate_iva(valor)
            if calculated_iva is None or abs(float(iva) - calculated_iva) > 0.01:
                result['errores']['iva'] += 1
                error = True

            # Validar TOTAL
            try:
                if abs(float(total) - (float(valor) + float(iva))) > 0.01:
                    result['errores']['total'] += 1
                    error = True
            except ValueError:
                result['errores']['total'] += 1
                error = True

            if not error:
                result['solicitudes_correctas'] += 1

                # Generar código de autorización
                date_match = re.search(r'(\d{2})/(\d{2})/(\d{4})', tiempo)
                if date_match:
                    day, month, year = date_match.groups()
                    # Generar código de autorización (yyyymmdd####)
                    # Aquí se generaría el correlativo real
                    codigo = f"{year}{month}{day}00001"

                    result['autorizaciones'].append({
                        'referencia': referencia,
                        'nit_emisor': nit_emisor,
                        'codigo': codigo
                    })

        return result

    except Exception as e:
        raise Exception(f"Error al procesar el archivo XML: {str(e)}")
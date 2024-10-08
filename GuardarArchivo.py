from xml.etree import ElementTree, cElementTree
from xml.dom import minidom


class NuevoArchivo():

    def __init__(self, lista, directorio, dispositivo, tiempo_muestreo, numero_muestras, velocidad):

        root = ElementTree.Element('Laboratorio_Control_Automatico')

        # ----------------------- Configuración -----------------------
        child1 = ElementTree.SubElement(root, "Configuracion")

        elemento = ElementTree.SubElement(child1, 'Dispositivo')
        elemento.text = dispositivo

        elemento = ElementTree.SubElement(child1, 'Velocidad')
        elemento.text = str(velocidad)

        elemento = ElementTree.SubElement(child1, 'Tiempo_Muestreo')
        elemento.text = str(tiempo_muestreo)

        elemento = ElementTree.SubElement(child1, 'Numero_Muestras')
        elemento.text = str(numero_muestras)

        for i in range(2, len(lista)):
            actual = lista[i].cabeza

            while actual is not None:

                if actual.tipo == "Linea":
                    child1 = ElementTree.SubElement(root, actual.tipo)

                    elemento = ElementTree.SubElement(child1, 'Nombre')
                    elemento.text = actual.nombre

                    elemento = ElementTree.SubElement(child1, 'Bloque_Inicio')
                    elemento.text = actual.bloqueInicio

                    elemento = ElementTree.SubElement(child1, 'Bloque_Fin')
                    elemento.text = actual.bloqueFin

                    elemento = ElementTree.SubElement(child1, 'Nodos')
                    elemento.text = str(actual.nodos)

                if actual.tipo == "ADC":
                    child1 = ElementTree.SubElement(root, actual.tipo)

                    elemento = ElementTree.SubElement(child1, 'Nombre')
                    elemento.text = actual.nombre

                    elemento = ElementTree.SubElement(child1, 'Posicion_X')
                    elemento.text = str(actual.posicionx)

                    elemento = ElementTree.SubElement(child1, 'Posicion_Y')
                    elemento.text = str(actual.posiciony)

                    elemento = ElementTree.SubElement(child1, 'Entrada_1')
                    elemento.text = actual.entrada

                    elemento = ElementTree.SubElement(child1, 'Salida_1')
                    elemento.text = actual.salida

                    elemento = ElementTree.SubElement(child1, 'Variable_Rango')
                    elemento.text = str(actual.variable_rango)

                    elemento = ElementTree.SubElement(child1, 'Variable_Tiempo_Muestreo')
                    elemento.text = str(actual.variable_tiempo_muestreo)

                    elemento = ElementTree.SubElement(child1, 'Variable_Ganancia')
                    elemento.text = str(actual.variable_ganancia)

                if actual.tipo == "PID":
                    child1 = ElementTree.SubElement(root, actual.tipo)

                    elemento = ElementTree.SubElement(child1, 'Nombre')
                    elemento.text = actual.nombre

                    elemento = ElementTree.SubElement(child1, 'Posicion_X')
                    elemento.text = str(actual.posicionx)

                    elemento = ElementTree.SubElement(child1, 'Posicion_Y')
                    elemento.text = str(actual.posiciony)

                    elemento = ElementTree.SubElement(child1, 'Entrada_1')
                    elemento.text = actual.entrada1

                    elemento = ElementTree.SubElement(child1, 'Entrada_2')
                    elemento.text = actual.entrada2

                    elemento = ElementTree.SubElement(child1, 'Salida_1')
                    elemento.text = actual.salida

                    elemento = ElementTree.SubElement(child1, 'Variable_Tipo_Pid')
                    elemento.text = str(actual.variable_tipo_pid)

                    elemento = ElementTree.SubElement(child1, 'Variable_Parametro_P')
                    elemento.text = str(actual.variable_parametro_p)

                    elemento = ElementTree.SubElement(child1, 'Variable_Parametro_I')
                    elemento.text = str(actual.variable_parametro_i)

                    elemento = ElementTree.SubElement(child1, 'Variable_Parametro_D')
                    elemento.text = str(actual.variable_parametro_d)

                    elemento = ElementTree.SubElement(child1, 'Variable_Parametro_C')
                    elemento.text = str(actual.variable_parametro_c)

                    elemento = ElementTree.SubElement(child1, 'Variable_Parametro_B')
                    elemento.text = str(actual.variable_parametro_b)

                    elemento = ElementTree.SubElement(child1, 'Variable_Parametro_N')
                    elemento.text = str(actual.variable_parametro_n)

                    elemento = ElementTree.SubElement(child1, 'Variable_Metodo_Integrador')
                    elemento.text = str(actual.variable_metodo_integrador)

                    elemento = ElementTree.SubElement(child1, 'Variable_Metodo_Filtro')
                    elemento.text = str(actual.variable_metodo_filtro)

                    elemento = ElementTree.SubElement(child1, 'Variable_Tiempo_Muestreo')
                    elemento.text = str(actual.variable_tiempo_muestreo)

                    elemento = ElementTree.SubElement(child1, 'Variable_Tipo_Saturador')
                    elemento.text = str(actual.variable_tipo_saturador)

                    elemento = ElementTree.SubElement(child1, 'Variable_Limite_Superior')
                    elemento.text = str(actual.variable_limite_superior)

                    elemento = ElementTree.SubElement(child1, 'Variable_Limite_Inferior')
                    elemento.text = str(actual.variable_limite_inferior)

                if actual.tipo == "PWM":
                    child1 = ElementTree.SubElement(root, actual.tipo)

                    elemento = ElementTree.SubElement(child1, 'Nombre')
                    elemento.text = actual.nombre

                    elemento = ElementTree.SubElement(child1, 'Posicion_X')
                    elemento.text = str(actual.posicionx)

                    elemento = ElementTree.SubElement(child1, 'Posicion_Y')
                    elemento.text = str(actual.posiciony)

                    elemento = ElementTree.SubElement(child1, 'Entrada_1')
                    elemento.text = actual.entrada

                    elemento = ElementTree.SubElement(child1, 'Salida_1')
                    elemento.text = actual.salida

                    elemento = ElementTree.SubElement(child1, 'Variable_Tipo')
                    elemento.text = str(actual.variable_tipo)

                    elemento = ElementTree.SubElement(child1, 'Variable_Periodo')
                    elemento.text = str(actual.variable_periodo)

                    elemento = ElementTree.SubElement(child1, 'Variable_Amplitud')
                    elemento.text = str(actual.variable_amplitud)

                if actual.tipo == "RE":
                    child1 = ElementTree.SubElement(root, actual.tipo)

                    elemento = ElementTree.SubElement(child1, 'Nombre')
                    elemento.text = actual.nombre

                    elemento = ElementTree.SubElement(child1, 'Tipo_RE')
                    elemento.text = actual.tipoRE

                    elemento = ElementTree.SubElement(child1, 'Posicion_X')
                    elemento.text = str(actual.posicionx)

                    elemento = ElementTree.SubElement(child1, 'Posicion_Y')
                    elemento.text = str(actual.posiciony)

                    elemento = ElementTree.SubElement(child1, 'Entrada_1')
                    elemento.text = actual.entrada_1

                    elemento = ElementTree.SubElement(child1, 'Entrada_2')
                    elemento.text = actual.entrada_2

                    elemento = ElementTree.SubElement(child1, 'Entrada_3')
                    elemento.text = actual.entrada_3

                    elemento = ElementTree.SubElement(child1, 'Entrada_4')
                    elemento.text = actual.entrada_4

                    elemento = ElementTree.SubElement(child1, 'Entrada_5')
                    elemento.text = actual.entrada_5

                    elemento = ElementTree.SubElement(child1, 'Entrada_6')
                    elemento.text = actual.entrada_6

                    elemento = ElementTree.SubElement(child1, 'Entrada_7')
                    elemento.text = actual.entrada_7

                    elemento = ElementTree.SubElement(child1, 'Salida_1')
                    elemento.text = actual.salida_1

                    elemento = ElementTree.SubElement(child1, 'Salida_2')
                    elemento.text = actual.salida_2

                    elemento = ElementTree.SubElement(child1, 'Variable_Tipo')
                    elemento.text = str(actual.variable_tipo)

                    elemento = ElementTree.SubElement(child1, 'Variable_N')
                    elemento.text = str(actual.variable_n)

                    elemento = ElementTree.SubElement(child1, 'Variable_M')
                    elemento.text = str(actual.variable_m)

                    elemento = ElementTree.SubElement(child1, 'Variable_Y1')
                    elemento.text = str(actual.variable_matriz_y1)

                    elemento = ElementTree.SubElement(child1, 'Variable_Y2')
                    elemento.text = str(actual.variable_matriz_y2)

                    elemento = ElementTree.SubElement(child1, 'Variable_K0')
                    elemento.text = str(actual.variable_k0)

                    elemento = ElementTree.SubElement(child1, 'Variable_Matriz_K')
                    if actual.variable_matriz_k is None:
                        elemento.text = actual.variable_matriz_k
                    else:
                        elemento.text = str(actual.variable_matriz_k)

                    elemento = ElementTree.SubElement(child1, 'Variable_Matriz_Ki')
                    if actual.variable_matriz_ki is None:
                        elemento.text = actual.variable_matriz_ki
                    else:
                        elemento.text = str(actual.variable_matriz_ki)

                if actual.tipo == "CTE":
                    child1 = ElementTree.SubElement(root, actual.tipo)

                    elemento = ElementTree.SubElement(child1, 'Nombre')
                    elemento.text = actual.nombre

                    elemento = ElementTree.SubElement(child1, 'Posicion_X')
                    elemento.text = str(actual.posicionx)

                    elemento = ElementTree.SubElement(child1, 'Posicion_Y')
                    elemento.text = str(actual.posiciony)

                    elemento = ElementTree.SubElement(child1, 'Salida_1')
                    elemento.text = actual.salida

                    elemento = ElementTree.SubElement(child1, 'Variable_Constante')
                    elemento.text = str(actual.variable_constante)

                if actual.tipo == "FT":
                    child1 = ElementTree.SubElement(root, actual.tipo)

                    elemento = ElementTree.SubElement(child1, 'Nombre')
                    elemento.text = actual.nombre

                    elemento = ElementTree.SubElement(child1, 'Tipo_FT')
                    elemento.text = actual.tipoFT

                    elemento = ElementTree.SubElement(child1, 'Posicion_X')
                    elemento.text = str(actual.posicionx)

                    elemento = ElementTree.SubElement(child1, 'Posicion_Y')
                    elemento.text = str(actual.posiciony)

                    elemento = ElementTree.SubElement(child1, 'Entrada_1')
                    elemento.text = actual.entrada_1

                    elemento = ElementTree.SubElement(child1, 'Entrada_2')
                    elemento.text = actual.entrada_2

                    elemento = ElementTree.SubElement(child1, 'Salida_1')
                    elemento.text = actual.salida

                    elemento = ElementTree.SubElement(child1, 'Variable_Orden')
                    elemento.text = str(actual.variable_orden)

                    elemento = ElementTree.SubElement(child1, 'Variable_Numerador')
                    elemento.text = str(actual.variable_numerador)

                    elemento = ElementTree.SubElement(child1, 'Variable_Denominador')
                    elemento.text = str(actual.variable_denominador)

                if actual.tipo == "PFT":
                    child1 = ElementTree.SubElement(root, actual.tipo)

                    elemento = ElementTree.SubElement(child1, 'Nombre')
                    elemento.text = actual.nombre

                    elemento = ElementTree.SubElement(child1, 'Tipo_PFT')
                    elemento.text = actual.tipoPFT

                    elemento = ElementTree.SubElement(child1, 'Posicion_X')
                    elemento.text = str(actual.posicionx)

                    elemento = ElementTree.SubElement(child1, 'Posicion_Y')
                    elemento.text = str(actual.posiciony)

                    elemento = ElementTree.SubElement(child1, 'Entrada_1')
                    elemento.text = actual.entrada_1

                    elemento = ElementTree.SubElement(child1, 'Entrada_2')
                    elemento.text = actual.entrada_2

                    elemento = ElementTree.SubElement(child1, 'Salida_1')
                    elemento.text = actual.salida_1

                    elemento = ElementTree.SubElement(child1, 'Salida_2')
                    elemento.text = actual.salida_2

                    elemento = ElementTree.SubElement(child1, 'Variable_N')
                    elemento.text = str(actual.variable_n)

                    elemento = ElementTree.SubElement(child1, 'Variable_M')
                    elemento.text = str(actual.variable_m)

                    elemento = ElementTree.SubElement(child1, 'Variable_Orden')
                    elemento.text = str(actual.variable_orden)

                    elemento = ElementTree.SubElement(child1, 'Variable_Orden_2')
                    elemento.text = str(actual.variable_orden2)

                    elemento = ElementTree.SubElement(child1, 'Variable_Numerador')
                    elemento.text = str(actual.variable_numerador)

                    elemento = ElementTree.SubElement(child1, 'Variable_Denominador')
                    elemento.text = str(actual.variable_denominador)   

                    elemento = ElementTree.SubElement(child1, 'Variable_Numerador_2')
                    elemento.text = str(actual.variable_numerador2)

                    elemento = ElementTree.SubElement(child1, 'Variable_Denominador_2')
                    elemento.text = str(actual.variable_denominador2)    

                if actual.tipo == "SAT":
                    child1 = ElementTree.SubElement(root, actual.tipo)

                    elemento = ElementTree.SubElement(child1, 'Nombre')
                    elemento.text = actual.nombre

                    elemento = ElementTree.SubElement(child1, 'Posicion_X')
                    elemento.text = str(actual.posicionx)

                    elemento = ElementTree.SubElement(child1, 'Posicion_Y')
                    elemento.text = str(actual.posiciony)

                    elemento = ElementTree.SubElement(child1, 'Entrada_1')
                    elemento.text = actual.entrada

                    elemento = ElementTree.SubElement(child1, 'Salida_1')
                    elemento.text = actual.salida

                    elemento = ElementTree.SubElement(child1, 'Variable_Limite_Superior')
                    elemento.text = str(actual.variable_limite_superior)

                    elemento = ElementTree.SubElement(child1, 'Variable_Limite_Inferior')
                    elemento.text = str(actual.variable_limite_inferior)

                

                if actual.tipo == "QDEC":
                    child1 = ElementTree.SubElement(root, actual.tipo)

                    elemento = ElementTree.SubElement(child1, 'Nombre')
                    elemento.text = actual.nombre

                    elemento = ElementTree.SubElement(child1, 'Posicion_X')
                    elemento.text = str(actual.posicionx)

                    elemento = ElementTree.SubElement(child1, 'Posicion_Y')
                    elemento.text = str(actual.posiciony)

                    elemento = ElementTree.SubElement(child1, 'Entrada_1')
                    elemento.text = actual.entrada

                    elemento = ElementTree.SubElement(child1, 'Salida_1')
                    elemento.text = actual.salida

                    elemento = ElementTree.SubElement(child1, 'Variable_Tamano_Contador')
                    elemento.text = str(actual.variable_tamano_contador)

                    elemento = ElementTree.SubElement(child1, 'Variable_Tiempo_Muestreo')
                    elemento.text = str(actual.variable_tiempo_muestreo)

                    elemento = ElementTree.SubElement(child1, 'Variable_Ganancia')
                    elemento.text = str(actual.variable_ganancia)

                if actual.tipo == "ENTP":
                    child1 = ElementTree.SubElement(root, actual.tipo)

                    elemento = ElementTree.SubElement(child1, 'Nombre')
                    elemento.text = actual.nombre

                    elemento = ElementTree.SubElement(child1, 'Posicion_X')
                    elemento.text = str(actual.posicionx)

                    elemento = ElementTree.SubElement(child1, 'Posicion_Y')
                    elemento.text = str(actual.posiciony)

                    elemento = ElementTree.SubElement(child1, 'Entrada_1')
                    elemento.text = actual.entrada

                    elemento = ElementTree.SubElement(child1, 'Variable_Nombre_Bloque')
                    elemento.text = actual.variable_nombre_bloque

                if actual.tipo == "SALP":
                    child1 = ElementTree.SubElement(root, actual.tipo)

                    elemento = ElementTree.SubElement(child1, 'Nombre')
                    elemento.text = actual.nombre

                    elemento = ElementTree.SubElement(child1, 'Posicion_X')
                    elemento.text = str(actual.posicionx)

                    elemento = ElementTree.SubElement(child1, 'Posicion_Y')
                    elemento.text = str(actual.posiciony)

                    elemento = ElementTree.SubElement(child1, 'Salida_1')
                    elemento.text = actual.salida

                    elemento = ElementTree.SubElement(child1, 'Variable_Nombre_Bloque')
                    elemento.text = actual.variable_nombre_bloque

                if actual.tipo == "DAC":
                    child1 = ElementTree.SubElement(root, actual.tipo)

                    elemento = ElementTree.SubElement(child1, 'Nombre')
                    elemento.text = actual.nombre

                    elemento = ElementTree.SubElement(child1, 'Posicion_X')
                    elemento.text = str(actual.posicionx)

                    elemento = ElementTree.SubElement(child1, 'Posicion_Y')
                    elemento.text = str(actual.posiciony)

                    elemento = ElementTree.SubElement(child1, 'Entrada_1')
                    elemento.text = actual.entrada

                    elemento = ElementTree.SubElement(child1, 'Salida_1')
                    elemento.text = actual.salida

                    elemento = ElementTree.SubElement(child1, 'Variable_Rango')
                    elemento.text = str(actual.variable_rango)

                    elemento = ElementTree.SubElement(child1, 'Variable_Tiempo_Muestreo')
                    elemento.text = str(actual.variable_tiempo_muestreo)

                    elemento = ElementTree.SubElement(child1, 'Variable_Ganancia')
                    elemento.text = str(actual.variable_ganancia)

                if actual.tipo == "FLT":
                    child1 = ElementTree.SubElement(root, actual.tipo)

                    elemento = ElementTree.SubElement(child1, 'Nombre')
                    elemento.text = actual.nombre

                    elemento = ElementTree.SubElement(child1, 'Posicion_X')
                    elemento.text = str(actual.posicionx)

                    elemento = ElementTree.SubElement(child1, 'Posicion_Y')
                    elemento.text = str(actual.posiciony)

                    elemento = ElementTree.SubElement(child1, 'Entrada_1')
                    elemento.text = actual.entrada

                    elemento = ElementTree.SubElement(child1, 'Salida_1')
                    elemento.text = actual.salida

                    elemento = ElementTree.SubElement(child1, 'Variable_A1')
                    elemento.text = str(actual.variable_a1)

                    elemento = ElementTree.SubElement(child1, 'Variable_A2')
                    elemento.text = str(actual.variable_a2)

                    elemento = ElementTree.SubElement(child1, 'Variable_B0')
                    elemento.text = str(actual.variable_b0)

                    elemento = ElementTree.SubElement(child1, 'Variable_B1')
                    elemento.text = str(actual.variable_b1)

                    elemento = ElementTree.SubElement(child1, 'Variable_B2')
                    elemento.text = str(actual.variable_b2)

                if actual.tipo == "SCOPE":
                    child1 = ElementTree.SubElement(root, actual.tipo)

                    elemento = ElementTree.SubElement(child1, 'Nombre')
                    elemento.text = actual.nombre

                    elemento = ElementTree.SubElement(child1, 'Posicion_X')
                    elemento.text = str(actual.posicionx)

                    elemento = ElementTree.SubElement(child1, 'Posicion_Y')
                    elemento.text = str(actual.posiciony)

                    elemento = ElementTree.SubElement(child1, 'Entrada_1')
                    elemento.text = actual.entrada

                    elemento = ElementTree.SubElement(child1, 'Salida_1')
                    elemento.text = actual.salida

                    elemento = ElementTree.SubElement(child1, 'Variable_Nombre_Bloque')
                    elemento.text = actual.variable_nombre_bloque

                if actual.tipo == "STEP":
                    child1 = ElementTree.SubElement(root, actual.tipo)

                    elemento = ElementTree.SubElement(child1, 'Nombre')
                    elemento.text = actual.nombre

                    elemento = ElementTree.SubElement(child1, 'Posicion_X')
                    elemento.text = str(actual.posicionx)

                    elemento = ElementTree.SubElement(child1, 'Posicion_Y')
                    elemento.text = str(actual.posiciony)

                    elemento = ElementTree.SubElement(child1, 'Salida_1')
                    elemento.text = actual.salida

                    elemento = ElementTree.SubElement(child1, 'Variable_Escalon')
                    elemento.text = str(actual.variable_escalon)

                    elemento = ElementTree.SubElement(child1, 'Variable_Valor_Inicial')
                    elemento.text = str(actual.variable_valor_inicial)

                    elemento = ElementTree.SubElement(child1, 'Variable_Valor_Final')
                    elemento.text = str(actual.variable_valor_final)

                if actual.tipo == "TRAPECIO":
                    child1 = ElementTree.SubElement(root, actual.tipo)

                    elemento = ElementTree.SubElement(child1, 'Nombre')
                    elemento.text = actual.nombre

                    elemento = ElementTree.SubElement(child1, 'Posicion_X')
                    elemento.text = str(actual.posicionx)

                    elemento = ElementTree.SubElement(child1, 'Posicion_Y')
                    elemento.text = str(actual.posiciony)

                    elemento = ElementTree.SubElement(child1, 'Salida_1')
                    elemento.text = actual.salida

                    elemento = ElementTree.SubElement(child1, 'Variable_Amplitud')
                    elemento.text = str(actual.variable_amplitud)

                    elemento = ElementTree.SubElement(child1, 'Variable_Tiempo_Inicio')
                    elemento.text = str(actual.variable_tiempo_inicio)

                    elemento = ElementTree.SubElement(child1, 'Variable_Tiempo_Rampa')
                    elemento.text = str(actual.variable_tiempo_rampa)

                    elemento = ElementTree.SubElement(child1, 'Variable_Tiempo_Alto')
                    elemento.text = str(actual.variable_tiempo_alto)

                if actual.tipo == "DER":
                    child1 = ElementTree.SubElement(root, actual.tipo)

                    elemento = ElementTree.SubElement(child1, 'Nombre')
                    elemento.text = actual.nombre

                    elemento = ElementTree.SubElement(child1, 'Posicion_X')
                    elemento.text = str(actual.posicionx)

                    elemento = ElementTree.SubElement(child1, 'Posicion_Y')
                    elemento.text = str(actual.posiciony)

                    elemento = ElementTree.SubElement(child1, 'Entrada_1')
                    elemento.text = actual.entrada

                    elemento = ElementTree.SubElement(child1, 'Salida_1')
                    elemento.text = actual.salida_1

                    elemento = ElementTree.SubElement(child1, 'Salida_2')
                    elemento.text = actual.salida_2

                if actual.tipo == "SUM":
                    child1 = ElementTree.SubElement(root, actual.tipo)

                    elemento = ElementTree.SubElement(child1, 'Nombre')
                    elemento.text = actual.nombre

                    elemento = ElementTree.SubElement(child1, 'Posicion_X')
                    elemento.text = str(actual.posicionx)

                    elemento = ElementTree.SubElement(child1, 'Posicion_Y')
                    elemento.text = str(actual.posiciony)

                    elemento = ElementTree.SubElement(child1, 'Entrada_1')
                    elemento.text = actual.entrada_1

                    elemento = ElementTree.SubElement(child1, 'Entrada_2')
                    elemento.text = actual.entrada_2

                    elemento = ElementTree.SubElement(child1, 'Salida_1')
                    elemento.text = actual.salida

                if actual.tipo == "REST":
                    child1 = ElementTree.SubElement(root, actual.tipo)

                    elemento = ElementTree.SubElement(child1, 'Nombre')
                    elemento.text = actual.nombre

                    elemento = ElementTree.SubElement(child1, 'Posicion_X')
                    elemento.text = str(actual.posicionx)

                    elemento = ElementTree.SubElement(child1, 'Posicion_Y')
                    elemento.text = str(actual.posiciony)

                    elemento = ElementTree.SubElement(child1, 'Entrada_1')
                    elemento.text = actual.entrada_1

                    elemento = ElementTree.SubElement(child1, 'Entrada_2')
                    elemento.text = actual.entrada_2

                    elemento = ElementTree.SubElement(child1, 'Salida_1')
                    elemento.text = actual.salida

                actual = actual.siguiente

        tree = cElementTree.ElementTree(root)

        t = minidom.parseString(ElementTree.tostring(root)).toprettyxml()
        tree1 = ElementTree.ElementTree(ElementTree.fromstring(t))

        tree1.write(directorio, encoding='utf-8', xml_declaration=True)

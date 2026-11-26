
# Fase 5 - Evaluación Final POA
# Solución Problema 3 - Control de inventario y reabastecimiento

def calcular_cantidad_pedido(stock_actual: int, stock_minimo: int) -> int:
    """
    Calcula cuántas unidades faltan por pedir si el inventario está
    por debajo del mínimo permitido.
    """
    if stock_actual < stock_minimo:
        return stock_minimo - stock_actual
    else:
        return 0

def generar_reporte_reabastecimiento(matriz_inventario: list) -> None:
    """
    Recorre toda la matriz del inventario y muestra en pantalla
    qué artículos necesitan pedido y cuántas unidades se requieren.
    """
    print("=" * 60)
    print("REPORTE DE PRODUCTOS POR REABASTECER")
    print("=" * 60)
    print(f"{'ARTÍCULO':<35} | {'UNIDADES A PEDIR':>20}")
    print("-" * 60)

    for articulo in matriz_inventario:
        # Sacamos los datos de cada columna: [Código, Nombre, Stock actual, Stock mínimo]
        codigo = articulo[0]
        nombre = articulo[1]
        stock_actual = articulo[2]
        stock_minimo = articulo[3]

        # Calculamos si hace falta pedir mercancía para este producto
        cantidad_a_pedir = calcular_cantidad_pedido(stock_actual, stock_minimo)
        print(f"{nombre:<35} | {cantidad_a_pedir:>15} unid.")

    print("=" * 60)

def main():
    # Matriz con los datos del inventario
    # Estructura: [Código, Nombre del artículo, Stock actual, Stock mínimo requerido]
    inventario = [
        ["ART 1", "Mouse Inalámbrico", 12, 20],
        ["ART 2", "Teclado USB", 15, 10],
        ["ART 3", "Memoria USB 32GB", 4, 8],
        ["ART 4", "Cable HDMI", 25, 25],
        ["ART 5", "Audífonos de diadema", 3, 12],
        ["ART 6", "Parlantes Bluetooth", 40, 30]
    ]
    
    generar_reporte_reabastecimiento(inventario)

if __name__ == "__main__":
    main()
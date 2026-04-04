"""
Nivel 1: Análisis Léxico - Alfabeto (Σ = {I, V, X, L, C, D, M})
"""

def validar_simbolos(cadena: str) -> bool:
    """
    Valida si todos los caracteres de la cadena pertenecen al alfabeto romano.

    💡 PISTA: Usa .strip() para eliminar espacios en blanco laterales
    💡 PISTA: Retorna False si la cadena está vacía después de eliminar espacios
    💡 PISTA: Recuerda: espacios en blanco laterales NO deben afectar la validación

    Args:
        cadena (str): La cadena a evaluar. Ej: "XIV"

    Returns:
        bool: True si la cadena es completamente válida, False en caso contrario.

    Examples:
        >>> validar_simbolos("XIV")
        True
        >>> validar_simbolos("MCMXCIV")
        True
        >>> validar_simbolos("ABCD")
        False
        >>> validar_simbolos("X-IV")
        False
        >>> validar_simbolos("")
        False
        >>> validar_simbolos("  XIV  ")
        True
    """

    cadena = cadena.strip()

    if cadena == "":
        return False

    a = "IXVLCDM"
    i = 0
    while i < len(cadena):
        caracter = cadena[i]
        j = 0
        encontrado = False
        while j < len(a):
            if caracter == a[j]:
                encontrado = True
                break
            j += 1
        if not encontrado:
            return False
        i += 1
    return True

print(validar_simbolos("  XIV  "))

print(validar_simbolos("XIV"))

#raise NotImplementedError()

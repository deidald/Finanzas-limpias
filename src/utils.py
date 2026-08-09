"""Módulo de funciones de utilidad para Finanzas Limpias."""


def formato_moneda(cantidad: float) -> str:
    """Formatea un valor numérico a formato de moneda (ej: $1,250.50)."""
    return f"${cantidad:,.2f}"

"""Módulo de funciones de utilidad."""

def formato_moneda(cantidad: float) -> str:
    """Retorna una cantidad formateada como moneda ($ standard)."""
    return f"${cantidad:,.2f}"

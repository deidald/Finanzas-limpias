"""Pruebas unitarias para utilidades."""

from src.utils import formato_moneda

def test_formato_moneda():
    assert formato_moneda(1250.5) == "$1,250.50"
    assert formato_moneda(0) == "$0.00"

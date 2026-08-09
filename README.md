# Finanzas Limpias 💰

Estructura base del proyecto en Python lista para el desarrollo y control de versiones con Git/GitHub.

---

## 📁 Estructura del Proyecto

```
Finanzas-limpias/
├── src/                    # Código fuente principal
│   ├── __init__.py
│   └── utils.py
├── tests/                  # Pruebas unitarias
│   ├── __init__.py
│   └── test_utils.py
├── .env.example            # Plantilla de variables de entorno
├── .gitignore              # Archivos y carpetas ignorados por Git
├── main.py                 # Punto de entrada principal
├── requirements.txt        # Archivo de dependencias
└── README.md               # Documentación del proyecto
```

---

## 🚀 Guía de Inicio Rápido

### 1. Crear y activar un entorno virtual

En PowerShell (Windows):
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

> **Nota en PowerShell:** Si el sistema bloquea la ejecución de scripts, ejecuta una vez:  
> `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`

### 2. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 3. Ejecutar el programa

```bash
python main.py
```

---

## 🔀 Cómo crear y publicar una rama en GitHub

1. **Crear tu rama local de trabajo:**
   ```bash
   git checkout -b feature/mi-nueva-funcionalidad
   ```

2. **Vincular con tu repositorio de GitHub (si aún no lo has conectado):**
   ```bash
   git remote add origin https://github.com/TU_USUARIO/Finanzas-limpias.git
   git push -u origin main
   ```

3. **Guardar cambios en tu rama:**
   ```bash
   git add .
   git commit -m "feat: descripción de los cambios"
   ```

4. **Subir tu rama a GitHub:**
   ```bash
   git push -u origin feature/mi-nueva-funcionalidad
   ```

# 🧹 Simulador de Robot Aspiradora Inteligente

Este proyecto es un simulador de un robot aspiradora desarrollado en **Python** y **Flask**. El robot navega en una matriz de 10x10, recogiendo basura en distintas posiciones y utilizando varios patrones de movimiento para limpiar el espacio; la simulación ofrece una interfaz visual para observar los movimientos y la limpieza de la matriz.

La documentación del codigo fue generada en VS con Tabnine.

---

## 🌟 Características

- **Generación de basura aleatoria**: Colocación de basura en la matriz al iniciar y durante la simulación.
- **Modos de movimiento**:
  - **Aleatorio**: Movimiento aleatorio en la matriz.
  - **Ruta corta**: Movimiento hacia la posición de basura más cercana.
  - **Serpiente**: Movimiento en zigzag, similar a una serpiente.
  - **Espiral**: Movimiento en patrón de espiral desde el centro de la matriz.
- **Recogida de basura**: El robot recoge y elimina basura cuando pasa por encima de ella.
- **Interfaz visual**: Representación en tiempo real de la posición del robot y de la basura en la matriz.

---

## 📦 Instalación

### Requisitos previos

- **Python 3.x**
- **Flask** (instalable con `pip`)

### Pasos de instalación

1. **Clona el repositorio**:
   ```bash
   git clone https://github.com/AngelJGC/IA-Proyecto.git
2. **Instala Flask**:
   ```bash
   pip install flask
3. **Ejecuta la aplicación**:
   ```bash
   python app.py
4. **Accede a la interfaz: Abre tu navegador y ve a**:
   ```bash
   http://127.0.0.1:5000
---

## 🧑‍💻 Uso del Código
**Archivos Principales**
1. app.py: Código principal de la aplicación, donde se definen las rutas de Flask, las funciones de movimiento y recogida de basura, y los modos de limpieza.
2. interfaz.html: Archivo HTML en la carpeta templates para la interfaz visual.

**Rutas de la API**
1. /: Página principal que carga la interfaz de la simulación.
2. /move: Ejecuta el movimiento de la aspiradora en la matriz.
3. /reset_matrix: Reinicia la matriz, colocando nueva basura y reiniciando el contador de basura recolectada.
4. /set_mode?mode=<modo>: Cambia el modo de movimiento. Los valores posibles para <modo> son random, short route, spiral y snake.



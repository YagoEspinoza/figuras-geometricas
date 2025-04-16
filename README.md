# Figuras Geometricas
## Desarrollador
| Apellidos y nombres       |
|---------------------------|
| Espinoza Tiza Yago Imanol |

# Correcciones de estilo con pylint

Este proyecto fue analizado con `pylint`, y se corrigieron varios errores para cumplir con las normas de estilo de Python (PEP 8). A continuación se describen los errores reportados y cómo se solucionaron.

---

## Errores y soluciones

- **`C0304: Final newline missing`**  
  - **Descripción:** El archivo no tenía una línea en blanco al final.  
  - **Solución:** Se agregó una línea en blanco al final del archivo.

- **`C0114: Missing module docstring`**  
  - **Descripción:** Faltaba un docstring explicando el propósito general del módulo.  
  - **Solución:** Se añadió un docstring al inicio del archivo describiendo el contenido del módulo.

- **`C0103: Module name "FiguraGeometrica" doesn't conform to snake_case naming style`**  
  - **Descripción:** El nombre del archivo usaba *CamelCase*. Python recomienda usar *snake_case*.  
  - **Solución:** El archivo fue renombrado de `FiguraGeometrica.py` a `figura_geometrica.py`.

- **`W0107: Unnecessary pass statement`**  
  - **Descripción:** Se usó la palabra clave `pass` en un método que ya tenía un docstring, lo cual era innecesario.  
  - **Solución:** Se eliminó la línea con `pass` del método `calcular_area()`.

- **`R0903: Too few public methods (1/2)`**  
  - **Descripción:** Las clases tenían solo un método público, lo cual puede ser demasiado simple para justificar una clase.  
  - **Solución:** Se desactivó esta advertencia con `# pylint: disable=too-few-public-methods`, ya que el diseño del programa lo justifica.

- **`C0115: Missing class docstring`**  
  - **Descripción:** Las clases no tenían un docstring que describiera su propósito.  
  - **Solución:** Se agregó un docstring a cada clase explicando qué representa y cuál es su función.

---

Con estas correcciones, el código cumple con las recomendaciones de estilo de Python y obtiene una mejor puntuación al usar `pylint`.

 

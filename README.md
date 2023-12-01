# Examen Final Ingenieria de Software

Alumno: Sebastian Chu


# Pregunta 3

Se realizarían los siguientes cambios en el código:

### Modificar el método de realizar_pago en app.py:
Antes de procesar la transacción, verificar si el valor de la transacción supera los 200 soles. Si supera los 200 soles, no realizar la transacción y devolver un código de estado o mensaje de error adecuado.

### Agregar casos de prueba nuevos:
Agregar casos de prueba adicionales que verifiquen el comportamiento correcto del sistema cuando se supera el límite de 200 soles en un día.


En cuanto al riesgo de "romper" lo que ya funciona, depende de los cambios y de cómo esté estructurado el código. Si los cambios son mínimos y bien encapsulados en el método realizar_pago, y si las pruebas existentes son sólidas, el riesgo de introducir errores en otras partes del sistema es bajo. Sin embargo, siempre hay un riesgo al realizar cambios en un sistema, incluso si son cambios pequeños. Para mitigar este riesgo, es fundamental tener un conjunto sólido de pruebas unitarias y realizar pruebas exhaustivas después de realizar los cambios.

#### Nuevos casos de prueba:

1. Caso de éxito para límite diario inferior:
- Intentar realizar una transacción de 199 soles.
- Verificar que la transacción se realiza con éxito.
- Caso de éxito para límite diario superior:

2. Caso de éxito para límite diario superior:
- Intentar realizar una transacción de 200 soles.
- Verificar que la transacción se realiza con éxito.
- Caso de error para límite diario excedido:

3. Caso de error para límite diario excedido:
- Intentar realizar una transacción de 201 soles.
- Verificar que la transacción no se realiza y se recibe un mensaje de error adecuado.
- Caso de éxito para múltiples transacciones en un día:

4. Caso de éxito para múltiples transacciones en un día:
- Realizar una transacción de 150 soles.
- Realizar otra transacción de 50 soles.
- Verificar que ambas transacciones se realizan con éxito.
- Intentar realizar una tercera transacción de 1 sol y verificar que se recibe un mensaje de error indicando que se ha alcanzado el límite diario.
  

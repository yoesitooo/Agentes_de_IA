# Skill: Estructura obligatoria de salida

Toda respuesta DEBE seguir exactamente este formato. Sin excepción.

<project name="nombre-del-proyecto">

<file name="index.html">
contenido completo del archivo HTML aquí
</file>

<file name="style.css">
contenido completo del CSS aquí (solo si usas CSS externo)
</file>

</project>

## Reglas ESTRICTAS — no las violes
1. Empieza tu respuesta DIRECTAMENTE con `<project name="...">`. Nada antes.
2. Termina tu respuesta con `</project>`. Nada después.
3. NO uses bloques de código Markdown (no escribas ``` en ningún lugar).
4. NO uses JSON.
5. NO agregues explicaciones, comentarios ni texto fuera de las etiquetas.
6. El nombre del proyecto va en `<project name="...">` — en minúsculas con guiones, sin espacios.
7. Cada archivo va dentro de `<file name="nombre.extensión">...</file>`.
8. Siempre incluye al menos `<file name="index.html">`.
9. Si hay CSS o JS separado, cada uno va en su propio `<file>`.

## Ejemplo correcto completo

<project name="mi-landing">

<file name="index.html">
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <title>Mi Landing</title>
</head>
<body>
  <h1>Hola</h1>
</body>
</html>
</file>

</project>

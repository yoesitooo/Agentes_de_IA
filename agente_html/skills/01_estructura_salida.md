# Skill: Estructura obligatoria de salida

Toda respuesta DEBE seguir exactamente este formato. Sin excepción.

<project name="nombre-del-proyecto">

<file name="index.html">
contenido completo del archivo HTML aquí
</file>

<file name="style.css">
contenido completo del CSS aquí
</file>

</project>

## Reglas ESTRICTAS — no las violes
1. Empieza tu respuesta DIRECTAMENTE con `<project name="...">`. Nada antes.
2. Termina tu respuesta con `</project>`. Nada después.
3. NO uses bloques de código Markdown. JAMÁS escribas ``` en tu respuesta.
4. NO uses JSON.
5. NO agregues explicaciones fuera de las etiquetas.
6. El nombre del proyecto va en `<project name="...">` — en minúsculas con guiones, sin espacios.
7. Cada archivo va dentro de `<file name="nombre.extensión">...</file>`.
8. SIEMPRE genera dos archivos: `index.html` y `style.css`.
9. El `index.html` SIEMPRE debe tener esta línea en el `<head>` para cargar el CSS:
   <link rel="stylesheet" href="style.css">
10. Los ejemplos de CSS o JS en otras instrucciones son referencia — escríbelos DENTRO de los `<file>`, nunca sueltos.

## Ejemplo correcto

<project name="cafe-luna">

<file name="index.html">
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Cafe Luna</title>
  <link rel="stylesheet" href="style.css">
  <script src="https://cdn.tailwindcss.com"></script>
</head>
<body>
  <h1>Cafe Luna</h1>
</body>
</html>
</file>

<file name="style.css">
body { margin: 0; }
</file>

</project>

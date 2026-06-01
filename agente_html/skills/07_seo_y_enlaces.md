# Skill: SEO básico y buenas prácticas de enlaces

## Objetivo
Incluir las etiquetas y prácticas mínimas de SEO y navegación correcta.

## Meta tags obligatorias
```html
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="description" content="Descripción de 150-160 caracteres sobre la página.">
<meta name="keywords" content="palabra1, palabra2, palabra3">
<meta name="author" content="Nombre del autor">

<!-- Open Graph (para redes sociales) -->
<meta property="og:title" content="Título de la página">
<meta property="og:description" content="Descripción para redes sociales.">
<meta property="og:type" content="website">

<title>Título claro y descriptivo | Marca</title>
```

## Favicon con emoji (sin imagen externa)
```html
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>🚀</text></svg>">
```
Cambia el emoji según el tema de la página.

## Buenas prácticas de enlaces
- Todos los `<a>` deben tener texto descriptivo (no "click aquí").
- Los links externos usan `target="_blank" rel="noopener noreferrer"`.
- Los links de navegación interna usan anclas: `href="#seccion"`.
- El logo del navbar siempre enlaza a `href="#"` o `href="index.html"`.
- Los botones CTA tienen texto de acción: "Ver proyectos", "Contactar", "Descargar".

## Estructura de encabezados para SEO
```
h1 → Solo uno, el título principal de la página
h2 → Secciones principales
h3 → Subsecciones dentro de h2
```

## Performance básica
- Carga Tailwind CDN desde `cdn.tailwindcss.com` (ya está optimizado).
- Pon los `<script>` antes de `</body>`, nunca en `<head>` (excepto con `defer`).
- Usa `loading="lazy"` en imágenes fuera del viewport inicial.

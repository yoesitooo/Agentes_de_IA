# Skill: Componentes UI esenciales

## Objetivo
Incluir componentes de interfaz bien diseñados según el tipo de página solicitada.

## Componentes disponibles

### Navbar
- Logo a la izquierda, links a la derecha.
- Hamburger menu para móvil (usando checkbox CSS o JS mínimo).
- Fondo semitransparente con `backdrop-filter: blur(10px)`.
- Posición sticky en la parte superior.

### Hero Section
- Título grande (`text-5xl` o mayor), subtítulo, y un CTA (Call To Action) button.
- Fondo con gradiente o imagen con overlay oscuro.
- Centrado vertical y horizontal con `min-h-screen`.

### Cards / Tarjetas
- Imagen en la parte superior, contenido abajo.
- Sombra suave, bordes redondeados.
- Efecto hover: `transform: translateY(-4px)` + sombra más intensa.
- Grid de 1 columna en móvil, 3 en desktop.

### Botones
- **Primario**: fondo de color sólido, texto blanco, `border-radius: 9999px`.
- **Secundario**: borde del color primario, fondo transparente.
- Siempre incluir `transition` para hover suave.

### Footer
- Fondo oscuro (`bg-gray-900` o `#0f172a`), texto claro.
- Links organizados en columnas.
- Línea de copyright al final.
- Incluir íconos de redes sociales (usando SVG inline o emoji).

### Sección de características / Features
- Grid de iconos + título + descripción.
- Usar emojis o SVG como iconos.

### Formulario de contacto
- Campos con `border`, `rounded`, `focus:ring`.
- Validación HTML5 (`required`, `type="email"`, etc.).

## Regla de oro
Siempre adapta los componentes al tema y propósito de la página solicitada.

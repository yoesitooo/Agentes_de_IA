# Skill: Componentes UI esenciales

## Objetivo
Incluir componentes de interfaz bien diseñados según el tipo de página solicitada.

## Componentes disponibles

### Navbar
- Logo a la izquierda, links a la derecha.
- Fondo semitransparente con backdrop-filter: blur(10px).
- Posición sticky en la parte superior.
- Incluir menú hamburger para móvil con este patrón (solo CSS, sin JS):
  - Un `<input type="checkbox" id="menu-toggle">` oculto
  - Un `<label for="menu-toggle">` con las 3 líneas (☰)
  - El menú se muestra/oculta con `#menu-toggle:checked ~ nav ul { display: flex; }`

### Hero Section
- SIEMPRE envolver el contenido del hero en un `<div class="flex flex-col items-center justify-center text-center">` o equivalente.
- La sección en sí lleva `min-h-screen flex items-center justify-center`.
- Incluye: título `<h1>`, subtítulo `<p>` y botón CTA.
- El botón CTA debe tener texto de acción específico ("Ver menú", "Reservar mesa", etc.), no "Click aquí".

### Cards / Tarjetas
- Siempre incluye: emoji o ícono SVG en la parte superior, título, descripción y precio/detalle.
- Efecto hover con transform y sombra en el CSS.
- Grid de 1 columna en móvil, 3 en desktop.
- Ejemplo de card completa:
  <div class="card">
    <div class="card-icon">☕</div>
    <h3>Espresso</h3>
    <p>Intenso y aromático, preparado con granos seleccionados.</p>
    <span class="price">$2.50</span>
  </div>

### Botones
- Primario: fondo sólido, texto blanco, border-radius: 9999px.
- Secundario: borde del color primario, fondo transparente.
- Siempre incluir transition en el CSS para hover suave.

### Footer
- Fondo oscuro, texto claro.
- Año dinámico con JS: `<span id="year"></span>` + `document.getElementById('year').textContent = new Date().getFullYear()`
- Links de redes sociales con SVG icons o emojis.

### Sección de contenido (Features, Menú, Servicios)
- Padding generoso: al menos py-16 px-4.
- Encabezado de sección centrado con `<h2>` y una línea decorativa o subtítulo.
- Grid responsivo para los elementos.

## Regla de oro
- Genera contenido específico y creíble para el negocio pedido. NO uses placeholders como "descripción del producto" o "texto de ejemplo".
- Cada item del menú/servicio debe tener nombre real, descripción real y precio real.

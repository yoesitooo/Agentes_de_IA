# Skill: Estilos visuales modernos

## Objetivo
Crear páginas visualmente atractivas usando Tailwind CSS vía CDN o CSS puro moderno.

## Opción A — Tailwind CSS (recomendado por defecto)
Incluye este CDN en el `<head>`:
```
<script src="https://cdn.tailwindcss.com"></script>
```
Luego usa clases de Tailwind directamente en el HTML. Ejemplos de clases útiles:

- Fondos con gradiente: `bg-gradient-to-br from-indigo-500 to-purple-600`
- Tarjetas: `bg-white rounded-2xl shadow-lg p-6 hover:shadow-xl transition-shadow`
- Botones: `bg-blue-600 text-white px-6 py-3 rounded-full hover:bg-blue-700 transition-colors font-semibold`
- Hero section: `min-h-screen flex items-center justify-center text-center`
- Grid responsivo: `grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6`
- Tipografía: `text-4xl font-bold text-gray-900`, `text-lg text-gray-600`

## Opción B — CSS puro moderno
Si no usas Tailwind, usa variables CSS y propiedades modernas:
```css
:root {
  --primary: #6366f1;
  --primary-dark: #4f46e5;
  --surface: #ffffff;
  --text: #1f2937;
  --text-muted: #6b7280;
  --radius: 1rem;
  --shadow: 0 4px 24px rgba(0,0,0,0.08);
}
* { box-sizing: border-box; margin: 0; padding: 0; }
body { font-family: 'Segoe UI', system-ui, sans-serif; color: var(--text); }
```
Usa `display: grid` y `display: flex` para layouts. Usa `clamp()` para tipografía fluida.

## Paletas de colores sugeridas
- **Moderno**: Indigo `#6366f1` + Purple `#a855f7`
- **Profesional**: Blue `#3b82f6` + Slate `#64748b`
- **Cálido**: Orange `#f97316` + Amber `#f59e0b`
- **Verde natural**: Emerald `#10b981` + Teal `#14b8a6`
- **Oscuro elegante**: `#0f172a` fondo + `#38bdf8` acento

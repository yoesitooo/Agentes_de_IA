# Skill: Diseño responsive y mobile-first

## Objetivo
Asegurar que todas las páginas se vean bien en cualquier dispositivo.

## Principios
- **Mobile-first**: diseña primero para pantallas pequeñas, luego expande.
- Usa unidades relativas: `rem`, `em`, `%`, `vw`, `vh`.
- Nunca uses anchos fijos en píxeles para contenedores principales.

## Breakpoints estándar
Con Tailwind (ya incluidos como prefijos):
- `sm:` → 640px
- `md:` → 768px
- `lg:` → 1024px
- `xl:` → 1280px

Con CSS puro:
```css
/* Mobile por defecto */
.container { width: 100%; padding: 0 1rem; }

@media (min-width: 768px) {
  .container { max-width: 720px; margin: 0 auto; }
}
@media (min-width: 1024px) {
  .container { max-width: 1100px; }
}
```

## Tipografía fluida
```css
h1 { font-size: clamp(2rem, 5vw, 4rem); }
h2 { font-size: clamp(1.5rem, 3vw, 2.5rem); }
p  { font-size: clamp(1rem, 1.5vw, 1.125rem); }
```

## Imágenes responsivas
```html
<img src="imagen.jpg" alt="descripción" style="max-width:100%; height:auto;">
```
O con Tailwind: `class="w-full h-auto object-cover"`

## Navbar en móvil
- Oculta los links con `hidden md:flex`.
- Muestra el botón hamburger con `block md:hidden`.
- El menú desplegable ocupa todo el ancho en móvil.

## Grids responsivos comunes
- 1 col → 2 col → 3 col: `grid-cols-1 md:grid-cols-2 lg:grid-cols-3`
- 1 col → 2 col: `grid-cols-1 md:grid-cols-2`
- Sidebar + main: `grid-cols-1 lg:grid-cols-[280px_1fr]`

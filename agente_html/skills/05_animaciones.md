# Skill: Animaciones y micro-interacciones

## Objetivo
Agregar animaciones sutiles que mejoren la experiencia sin distraer.

## Animaciones de entrada (scroll o carga)
Incluye este CSS para animaciones de entrada al cargar la página:

```css
@keyframes fadeInUp {
  from { opacity: 0; transform: translateY(30px); }
  to   { opacity: 1; transform: translateY(0); }
}
@keyframes fadeIn {
  from { opacity: 0; }
  to   { opacity: 1; }
}
.animate-fade-up {
  animation: fadeInUp 0.6s ease forwards;
}
.animate-fade-up:nth-child(2) { animation-delay: 0.1s; }
.animate-fade-up:nth-child(3) { animation-delay: 0.2s; }
.animate-fade-up:nth-child(4) { animation-delay: 0.3s; }
```

## Hover effects
```css
.card:hover {
  transform: translateY(-6px);
  box-shadow: 0 20px 40px rgba(0,0,0,0.15);
  transition: all 0.3s ease;
}
.btn:hover {
  transform: scale(1.03);
  transition: transform 0.2s ease;
}
```

## Gradiente animado (para fondos de hero)
```css
@keyframes gradientShift {
  0%   { background-position: 0% 50%; }
  50%  { background-position: 100% 50%; }
  100% { background-position: 0% 50%; }
}
.hero-gradient {
  background: linear-gradient(135deg, #6366f1, #a855f7, #3b82f6);
  background-size: 200% 200%;
  animation: gradientShift 6s ease infinite;
}
```

## Reglas de uso
- Usa `transition` en lugar de `animation` para hover (más eficiente).
- Limita las animaciones a `opacity` y `transform` para evitar repaints.
- No abuses: máximo 2-3 tipos de animación por página.
- Agrega `prefers-reduced-motion` para accesibilidad:
```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after { animation-duration: 0.01ms !important; transition-duration: 0.01ms !important; }
}
```

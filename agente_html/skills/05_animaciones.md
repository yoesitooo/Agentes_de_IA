# Skill: Animaciones y efectos visuales

## Objetivo
Toda página generada debe tener animaciones visibles y atractivas. No es opcional.

---

## 1. Animaciones al hacer scroll — AOS (OBLIGATORIO)

Incluye SIEMPRE estos dos tags en el `<head>`:
  <link href="https://unpkg.com/aos@2.3.4/dist/aos.css" rel="stylesheet">

Y antes de `</body>`:
  <script src="https://unpkg.com/aos@2.3.4/dist/aos.js"></script>
  <script>AOS.init({ duration: 700, once: true, offset: 80 });</script>

Luego agrega atributos `data-aos` a los elementos que deben animarse al hacer scroll:

- Sección entera entrando desde abajo:      data-aos="fade-up"
- Card de izquierda a derecha:              data-aos="fade-right"
- Card de derecha a izquierda:              data-aos="fade-left"
- Elemento con zoom:                        data-aos="zoom-in"
- Con delay entre cards del mismo grid:     data-aos-delay="100" (sumar 100 por cada card)

Ejemplo correcto para una sección de cards:
  <div data-aos="fade-up">
    <h2>Nuestros servicios</h2>
  </div>
  <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
    <div class="card" data-aos="zoom-in" data-aos-delay="0">...</div>
    <div class="card" data-aos="zoom-in" data-aos-delay="150">...</div>
    <div class="card" data-aos="zoom-in" data-aos-delay="300">...</div>
  </div>

---

## 2. Hero con gradiente animado (OBLIGATORIO en hero)

En style.css, la clase `.hero` siempre debe tener:
  .hero {
    background: linear-gradient(135deg, #6366f1, #a855f7, #3b82f6, #06b6d4);
    background-size: 300% 300%;
    animation: gradientShift 8s ease infinite;
  }
  @keyframes gradientShift {
    0%   { background-position: 0% 50%; }
    50%  { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
  }

Y el contenido del hero SIEMPRE dentro de un wrapper con flex-col:
  <section class="hero min-h-screen flex items-center justify-center">
    <div class="flex flex-col items-center justify-center text-center gap-6 px-4">
      <h1 class="text-5xl md:text-7xl font-bold text-white" data-aos="fade-down">Título</h1>
      <p class="text-xl text-white/80 max-w-2xl" data-aos="fade-up" data-aos-delay="200">Subtítulo</p>
      <a href="#" class="btn-primary" data-aos="fade-up" data-aos-delay="400">CTA</a>
    </div>
  </section>

---

## 3. Hover effects en CSS (SIEMPRE incluir)

  .card {
    transition: transform 0.3s ease, box-shadow 0.3s ease;
  }
  .card:hover {
    transform: translateY(-8px) scale(1.02);
    box-shadow: 0 24px 48px rgba(99, 102, 241, 0.2);
  }

  .btn-primary {
    background: linear-gradient(135deg, #6366f1, #a855f7);
    color: white;
    padding: 0.875rem 2rem;
    border-radius: 9999px;
    font-weight: 600;
    transition: transform 0.2s ease, box-shadow 0.2s ease;
    display: inline-block;
    text-decoration: none;
  }
  .btn-primary:hover {
    transform: translateY(-2px) scale(1.05);
    box-shadow: 0 8px 24px rgba(99, 102, 241, 0.4);
  }

---

## 4. Barra de navegación con efecto scroll

Agrega este script para que el navbar cambie al hacer scroll:
  <script>
    window.addEventListener('scroll', () => {
      const nav = document.querySelector('header');
      nav.classList.toggle('shadow-xl', window.scrollY > 50);
      nav.classList.toggle('bg-white/95', window.scrollY > 50);
      nav.classList.toggle('backdrop-blur-sm', window.scrollY > 50);
    });
  </script>

Y el header debe empezar con: class="fixed top-0 w-full z-50 transition-all duration-300 bg-transparent"

---

## 5. Regla de oro
Cada sección de la página debe tener al menos un atributo data-aos.
Cada card en un grid debe tener data-aos="zoom-in" con data-aos-delay incremental.
El hero siempre tiene gradiente animado.

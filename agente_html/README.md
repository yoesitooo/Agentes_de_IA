# Agente HTML — Generador de páginas web con IA

Agente local/cloud que genera páginas HTML modernas y visualmente atractivas usando un modelo de IA. Soporta **Ollama (local)**, **OpenAI**, **Anthropic (Claude)** y **NVIDIA NIM (gratis)** — elige el que prefieras.

---

## Requisitos

- Python 3.10 o superior
- (Opcional) Ollama instalado si usas modelos locales → https://ollama.com

---

## Instalación

```bash
# 1. Clona el repositorio
git clone https://github.com/yoesitooo/Agentes_de_IA.git
cd Agentes_de_IA/agente_html

# 2. Instala dependencias
pip install -r requirements.txt

# 3. Solo si usas Anthropic:
pip install anthropic
```

---

## Configuración del proveedor

Copia el archivo de ejemplo y edítalo:

```bash
# Linux / Mac
cp .env.example .env

# Windows
copy .env.example .env
```

Abre `.env` y elige tu proveedor:

### Opción A — NVIDIA NIM (gratis, sin instalar nada local)
La más fácil para empezar. Obtén tu key gratis en https://build.nvidia.com

```env
PROVIDER=nvidia
NVIDIA_API_KEY=nvapi-xxxxxxxxxxxxxxxxxxxx
NVIDIA_MODEL=abacusai/dracarys-llama-3.1-70b-instruct
```

### Opción B — Ollama (sin costo, corre en tu PC)
```env
PROVIDER=ollama
OLLAMA_MODEL=qwen2.5-coder:7b
```
Descarga el modelo antes de correr:
```bash
ollama pull qwen2.5-coder:7b
```

### Opción C — OpenAI
```env
PROVIDER=openai
OPENAI_API_KEY=sk-xxxxxxxx
OPENAI_MODEL=gpt-4o-mini
```

### Opción D — Anthropic (Claude)
```env
PROVIDER=anthropic
ANTHROPIC_API_KEY=sk-ant-xxxxxxxx
ANTHROPIC_MODEL=claude-haiku-4-5-20251001
```

---

## Uso

```bash
python agent.py
```

Escribe tu solicitud en lenguaje natural y el agente genera la página completa:

```
============================================================
  Agente generador de páginas HTML modernas
  Proveedor activo: NVIDIA  (modelo: abacusai/dracarys-llama-3.1-70b-instruct)
  Escribe 'salir' para terminar.
============================================================

Solicitud: Crea un portafolio para un desarrollador web llamado Alex Torres
```

El agente genera los archivos, los guarda en `workspace/` y **abre el resultado automáticamente en el navegador**.

---

## Ejemplos de prompts probados

Estos prompts fueron probados y generaron páginas funcionales:

### Portafolio personal
```
Crea un portafolio personal moderno para un desarrollador web llamado Alex Torres,
con hero animado, seccion de habilidades con cards de tecnologias,
seccion de proyectos destacados y footer con links a GitHub y LinkedIn
```
**Resultado:** página con hero degradado animado, 6 cards de tecnologías (HTML, CSS, JS, React, Node, MongoDB), sección de proyectos en grid, navbar responsive y footer con iconos.

### Landing page de negocio
```
Crea una landing page moderna para una cafeteria llamada Cafe Luna,
con hero animado, seccion de menu con cards, horarios y footer con redes sociales
```
**Resultado:** hero con gradiente animado, 3 cards de menú con emojis y precios, sección de horarios, footer con iconos SVG de Instagram, Facebook y Twitter.

### Más ejemplos para probar
```
Solicitud: Hazme una página de inicio para una app de fitness con hero animado y planes de precios
Solicitud: Crea una página de producto para unos audífonos inalámbricos con specs y botón de compra
Solicitud: Genera una página 404 creativa con mensaje divertido y botón para volver al inicio
Solicitud: Crea una landing page para un estudio de fotografía con galería y formulario de contacto
```

---

## Estructura del proyecto

```
agente_html/
├── agent.py            ← Punto de entrada, bucle interactivo
├── config.py           ← Lee variables de entorno (.env)
├── skill_loader.py     ← Carga instrucciones desde skills/
├── project_writer.py   ← Parsea respuesta, aplica fixes y abre el navegador
├── .env.example        ← Plantilla de configuración (sin keys reales)
├── .gitignore          ← Excluye .env y workspace generado
├── requirements.txt    ← Dependencias Python
├── skills/             ← Instrucciones del agente en Markdown
│   ├── 01_estructura_salida.md   ← Formato XML obligatorio de respuesta
│   ├── 02_html_moderno.md        ← HTML5 semántico
│   ├── 03_estilos_visuales.md    ← Tailwind CSS + paletas de color
│   ├── 04_componentes_ui.md      ← Navbar, cards, hero, footer, etc.
│   ├── 05_animaciones.md         ← CSS animations y micro-interacciones
│   ├── 06_responsive.md          ← Mobile-first y breakpoints
│   └── 07_seo_y_enlaces.md       ← Meta tags, Open Graph, favicon
└── workspace/          ← Proyectos generados (ignorado por git)
    ├── cafe-luna/
    │   ├── index.html
    │   └── style.css
    └── alex-torres-portafolio/
        ├── index.html
        └── style.css
```

---

## Cómo agregar skills

Cada archivo `.md` en `skills/` es una instrucción que el agente sigue siempre.
Para agregar comportamiento nuevo:

1. Crea `skills/08_mi_skill.md`
2. Escribe las instrucciones en lenguaje natural
3. El agente las carga automáticamente al correr

---

## Notas técnicas

- Las páginas usan **Tailwind CSS via CDN** — no necesitan build steps, se abren directo en el navegador.
- `project_writer.py` aplica correcciones automáticas al HTML generado: enlaza el CSS si el modelo lo olvidó, apila el hero verticalmente y pone el año del footer dinámico con JS.
- El archivo `.env` nunca se sube al repo (está en `.gitignore`). Cada persona pone su propia key.

# Agente HTML — Generador de páginas web con IA

Agente local/cloud que genera páginas HTML modernas y visualmente atractivas usando un modelo de IA. Soporta **Ollama (local)**, **OpenAI** y **Anthropic (Claude)** — elige el que prefieras.

---

## Requisitos

- Python 3.10 o superior
- (Opcional) Ollama instalado si usas modelos locales → https://ollama.com

---

## Instalación

```bash
# 1. Clona el repositorio
git clone <url-del-repo>
cd agente_html

# 2. Instala dependencias base
pip install -r requirements.txt

# 3. Si usas OpenAI, instala también:
pip install openai

# 4. Si usas Anthropic, instala también:
pip install anthropic
```

---

## Configuración del proveedor

Copia el archivo de ejemplo y edítalo:

```bash
cp .env.example .env
```

Abre `.env` y elige tu proveedor:

### Opción A — Ollama (sin costo, corre en tu PC)
```env
PROVIDER=ollama
OLLAMA_MODEL=qwen2.5-coder:7b
```
Asegúrate de tener el modelo descargado:
```bash
ollama pull qwen2.5-coder:7b
```

### Opción B — OpenAI
```env
PROVIDER=openai
OPENAI_API_KEY=sk-xxxxxxxx
OPENAI_MODEL=gpt-4o-mini
```

### Opción C — Anthropic (Claude)
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

El agente te pedirá una solicitud. Ejemplos:

```
Solicitud: Crea una landing page para una cafetería llamada "Café Luna" con menú, galería y contacto
Solicitud: Genera un portafolio personal para un desarrollador frontend con sección de proyectos
Solicitud: Hazme una página de inicio para una app de fitness con hero animado y precios
Solicitud: Crea una página 404 creativa con un mensaje divertido y botón para volver al inicio
```

El agente:
1. Genera el HTML/CSS/JS completo
2. Guarda los archivos en `workspace/<nombre-proyecto>/`
3. Abre automáticamente el resultado en tu navegador

---

## Estructura del proyecto

```
agente_html/
├── agent.py           ← Punto de entrada del agente
├── config.py          ← Lee variables de entorno (.env)
├── skill_loader.py    ← Carga instrucciones desde skills/
├── project_writer.py  ← Guarda archivos y abre el navegador
├── .env.example       ← Plantilla de configuración
├── requirements.txt   ← Dependencias Python
├── skills/            ← Instrucciones del agente (Markdown)
│   ├── 01_estructura_salida.md
│   ├── 02_html_moderno.md
│   ├── 03_estilos_visuales.md
│   ├── 04_componentes_ui.md
│   ├── 05_animaciones.md
│   ├── 06_responsive.md
│   └── 07_seo_y_enlaces.md
└── workspace/         ← Proyectos HTML generados (se crea automáticamente)
```

---

## Cómo agregar o modificar skills

Cada archivo `.md` en `skills/` es una instrucción que el agente sigue. Para agregar una nueva skill:

1. Crea un archivo `skills/08_mi_skill.md`
2. Escribe las instrucciones en lenguaje natural
3. El agente las cargará automáticamente la próxima vez que se ejecute

---

## Notas

- Las páginas generadas usan **Tailwind CSS via CDN** — no necesitan build steps.
- Los proyectos se guardan en `workspace/` y pueden abrirse directamente en el navegador.
- El agente no ejecuta código JavaScript en el servidor; todo es HTML estático.

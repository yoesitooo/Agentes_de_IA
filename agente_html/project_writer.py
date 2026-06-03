import re
import webbrowser
from pathlib import Path
from typing import Optional, List, Tuple

WORKSPACE_DIR = Path(__file__).parent / "workspace"


def _strip_markdown_fences(text: str) -> str:
    return re.sub(r"```[a-zA-Z]*\n?", "", text)


def _patch_html(html: str) -> str:
    """
    Correcciones automáticas a patrones que los modelos generan mal de forma consistente.
    """
    # 1. Hero sin flex-col: si el hero tiene flex pero no flex-col, apila verticalmente
    html = re.sub(
        r'(class="[^"]*hero[^"]*flex(?!\s+flex-col)[^"]*")',
        lambda m: m.group(0).replace('flex ', 'flex flex-col '),
        html
    )

    # 2. Año hardcodeado en footer: reemplaza con JS dinámico
    # Cubre: "© 2023", "&copy; 2023", "2023 Nombre", "Copyright 2023"
    html = re.sub(
        r'(&copy;|©|[Cc]opyright)?\s*(19|20)\d{2}',
        lambda m: (m.group(1) + ' ' if m.group(1) else '') + '<span id="footer-year"></span>',
        html
    )
    if 'footer-year' in html and 'footer-year' not in html.split('<script')[-1]:
        html = html.replace(
            '</body>',
            '  <script>document.getElementById("footer-year").textContent=new Date().getFullYear();</script>\n</body>'
        )

    # 3. style.css enlazado: si hay archivo style.css generado pero no hay <link> para él, lo agrega
    if 'href="style.css"' not in html and '</head>' in html:
        html = html.replace(
            '</head>',
            '  <link rel="stylesheet" href="style.css">\n</head>'
        )

    return html


def extract_project_name(response_text: str) -> str:
    match = re.search(r'<project\s+name="([^"]+)">', response_text)
    if not match:
        raise ValueError(
            'No se encontró <project name="..."> en la respuesta.\n'
            "El modelo no siguió el formato de salida definido en las skills."
        )
    raw = match.group(1).strip()
    safe = re.sub(r"[^a-zA-Z0-9\-_]", "-", raw).strip("-") or "proyecto"
    return safe


def extract_files(response_text: str) -> List[Tuple[str, str]]:
    pattern = r'<file\s+name="([^"]+)">\s*(.*?)\s*</file>'
    files = re.findall(pattern, response_text, re.DOTALL)
    if not files:
        raise ValueError(
            "No se encontraron etiquetas <file>...</file> en la respuesta.\n"
            "El modelo no siguió el formato de salida definido en las skills."
        )
    return files


def save_project_from_response(response_text: str, open_browser: bool = True) -> Path:
    clean_text = _strip_markdown_fences(response_text)

    project_name = extract_project_name(clean_text)
    files = extract_files(clean_text)

    project_dir = WORKSPACE_DIR / project_name
    project_dir.mkdir(parents=True, exist_ok=True)

    main_html: Optional[Path] = None

    for filename, content in files:
        file_path = project_dir / filename
        file_path.parent.mkdir(parents=True, exist_ok=True)

        # Aplica correcciones automáticas solo a archivos HTML
        final_content = _patch_html(content.strip()) if filename.endswith(".html") else content.strip()

        file_path.write_text(final_content, encoding="utf-8")
        print(f"  [OK] {file_path}")

        if filename.endswith(".html") and main_html is None:
            main_html = file_path

    print(f"\nProyecto guardado en: {project_dir}")

    if open_browser and main_html:
        url = main_html.resolve().as_uri()
        print(f"Abriendo en navegador: {url}")
        webbrowser.open(url)

    return project_dir

import re
import webbrowser
from pathlib import Path
from typing import Optional, List, Tuple

WORKSPACE_DIR = Path(__file__).parent / "workspace"


def _strip_markdown_fences(text: str) -> str:
    """Elimina bloques ```...``` que algunos modelos locales añaden alrededor del XML."""
    return re.sub(r"```[a-zA-Z]*\n?", "", text)


def extract_project_name(response_text: str) -> str:
    match = re.search(r'<project\s+name="([^"]+)">', response_text)
    if not match:
        raise ValueError(
            'No se encontró <project name="..."> en la respuesta.\n'
            "El modelo no siguió el formato de salida definido en las skills."
        )
    return match.group(1).strip()


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
    # Limpia bloques markdown que modelos locales pueden agregar
    clean_text = _strip_markdown_fences(response_text)

    project_name = extract_project_name(clean_text)
    files = extract_files(clean_text)

    project_dir = WORKSPACE_DIR / project_name
    project_dir.mkdir(parents=True, exist_ok=True)

    main_html: Optional[Path] = None

    for filename, content in files:
        file_path = project_dir / filename
        file_path.parent.mkdir(parents=True, exist_ok=True)
        file_path.write_text(content.strip(), encoding="utf-8")
        print(f"  ✓ {file_path}")

        if filename.endswith(".html") and main_html is None:
            main_html = file_path

    print(f"\nProyecto guardado en: {project_dir}")

    if open_browser and main_html:
        url = main_html.resolve().as_uri()
        print(f"Abriendo en navegador: {url}")
        webbrowser.open(url)

    return project_dir

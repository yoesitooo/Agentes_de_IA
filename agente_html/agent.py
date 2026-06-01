import config
from skill_loader import load_all_skills
from project_writer import save_project_from_response


def build_system_prompt() -> str:
    skills = load_all_skills()
    return f"""Eres un agente especializado en generar páginas web HTML modernas y visualmente atractivas.

Tienes las siguientes instrucciones (skills) que DEBES seguir siempre:

{skills}

IMPORTANTE: Responde ÚNICAMENTE con las etiquetas <project> y <file>. Nunca uses bloques de código Markdown.
"""


def _ollama_content(response) -> str:
    # Soporta tanto ollama <0.4 (TypedDict/dict) como >=0.4 (Pydantic)
    try:
        return response.message.content
    except AttributeError:
        return response["message"]["content"]


def ask_agent(user_prompt: str) -> str:
    system_prompt = build_system_prompt()
    messages = [{"role": "user", "content": user_prompt}]
    provider = config.PROVIDER

    if provider == "ollama":
        try:
            import ollama as ollama_lib
        except ImportError:
            raise RuntimeError("La librería 'ollama' no está instalada. Ejecuta: pip install ollama")
        try:
            response = ollama_lib.chat(
                model=config.OLLAMA_MODEL,
                messages=[
                    {"role": "system", "content": system_prompt},
                    *messages,
                ],
            )
        except Exception as e:
            if "connection" in str(e).lower() or "refused" in str(e).lower():
                raise RuntimeError(
                    f"No se pudo conectar a Ollama en {config.OLLAMA_BASE_URL}.\n"
                    "  → ¿Está Ollama corriendo? Ejecuta: ollama serve\n"
                    f"  → ¿Tienes el modelo? Ejecuta: ollama pull {config.OLLAMA_MODEL}"
                ) from e
            raise
        return _ollama_content(response)

    elif provider == "openai":
        try:
            from openai import OpenAI
        except ImportError:
            raise RuntimeError("La librería 'openai' no está instalada. Ejecuta: pip install openai")
        if not config.OPENAI_API_KEY:
            raise RuntimeError("OPENAI_API_KEY está vacía. Agrégala en el archivo .env")
        client = OpenAI(api_key=config.OPENAI_API_KEY)
        response = client.chat.completions.create(
            model=config.OPENAI_MODEL,
            messages=[
                {"role": "system", "content": system_prompt},
                *messages,
            ],
        )
        return response.choices[0].message.content

    elif provider == "anthropic":
        try:
            import anthropic as anthropic_lib
        except ImportError:
            raise RuntimeError("La librería 'anthropic' no está instalada. Ejecuta: pip install anthropic")
        if not config.ANTHROPIC_API_KEY:
            raise RuntimeError("ANTHROPIC_API_KEY está vacía. Agrégala en el archivo .env")
        client = anthropic_lib.Anthropic(api_key=config.ANTHROPIC_API_KEY)
        response = client.messages.create(
            model=config.ANTHROPIC_MODEL,
            max_tokens=8096,
            system=system_prompt,
            messages=messages,
        )
        return response.content[0].text

    elif provider == "nvidia":
        try:
            from openai import OpenAI
        except ImportError:
            raise RuntimeError("La librería 'openai' no está instalada. Ejecuta: pip install openai")
        if not config.NVIDIA_API_KEY:
            raise RuntimeError("NVIDIA_API_KEY está vacía. Obtén una gratis en build.nvidia.com y agrégala en .env")
        client = OpenAI(api_key=config.NVIDIA_API_KEY, base_url=config.NVIDIA_BASE_URL)
        response = client.chat.completions.create(
            model=config.NVIDIA_MODEL,
            messages=[
                {"role": "system", "content": system_prompt},
                *messages,
            ],
        )
        return response.choices[0].message.content

    else:
        raise ValueError(
            f"PROVIDER='{provider}' no válido. Opciones: ollama | openai | anthropic | nvidia\n"
            "Edita el archivo .env para cambiarlo."
        )


def main():
    env_path = __import__("pathlib").Path(__file__).parent / ".env"
    if not env_path.exists():
        print("[AVISO] No se encontró el archivo .env")
        print(f"  → Copia .env.example a .env y configura tu proveedor:")
        print(f"  → cp .env.example .env   (Linux/Mac)")
        print(f"  → copy .env.example .env  (Windows)\n")

    print("=" * 60)
    print("  Agente generador de páginas HTML modernas")
    print(f"  Proveedor activo: {config.PROVIDER.upper()}", end="")
    if config.PROVIDER == "ollama":
        print(f"  (modelo: {config.OLLAMA_MODEL})")
    elif config.PROVIDER == "openai":
        print(f"  (modelo: {config.OPENAI_MODEL})")
    elif config.PROVIDER == "anthropic":
        print(f"  (modelo: {config.ANTHROPIC_MODEL})")
    elif config.PROVIDER == "nvidia":
        print(f"  (modelo: {config.NVIDIA_MODEL})")
    else:
        print()
    print("  Escribe 'salir' para terminar.")
    print("=" * 60)
    print()

    while True:
        try:
            prompt = input("Solicitud: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nSaliendo...")
            break

        if not prompt:
            continue

        if prompt.lower() in ("salir", "exit", "quit"):
            break

        print("\nGenerando página HTML...\n")

        try:
            answer = ask_agent(prompt)
        except RuntimeError as e:
            print(f"\n[ERROR] {e}\n")
            continue
        except Exception as e:
            print(f"\n[ERROR inesperado] {e}\n")
            continue

        print("--- RESPUESTA DEL AGENTE ---")
        print(answer[:600] + ("..." if len(answer) > 600 else ""))
        print("----------------------------\n")

        try:
            project_dir = save_project_from_response(answer, open_browser=True)
            print(f"\nProyecto generado en: {project_dir}\n")
        except ValueError as e:
            print(f"\n[ERROR al guardar archivos] {e}")
            print("El modelo no siguió el formato esperado.")
            print("Respuesta completa:\n")
            print(answer)

        print()


if __name__ == "__main__":
    main()

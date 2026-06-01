from pathlib import Path

SKILLS_DIR = Path(__file__).parent / "skills"


def load_skill(skill_name: str) -> str:
    skill_path = SKILLS_DIR / f"{skill_name}.md"
    if not skill_path.exists():
        raise FileNotFoundError(f"No existe la skill: {skill_path}")
    return skill_path.read_text(encoding="utf-8")


def load_all_skills() -> str:
    skills_content = []
    for skill_file in sorted(SKILLS_DIR.glob("*.md")):
        content = skill_file.read_text(encoding="utf-8")
        skills_content.append(content)
    return "\n\n---\n\n".join(skills_content)

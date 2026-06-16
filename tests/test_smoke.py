"""Smoke tests para hermes-skills-pack."""
import pytest
from pathlib import Path


def test_skills_dir_exists():
    """skills/ deve existir e ter skills."""
    skills_dir = Path(__file__).parent.parent / "skills"
    assert skills_dir.exists(), f"skills/ nao encontrado em {skills_dir}"
    skills = [d for d in skills_dir.iterdir() if d.is_dir()]
    assert len(skills) > 0, "skills/ vazio"


def test_skill_md_files():
    """Cada skill deve ter SKILL.md."""
    skills_dir = Path(__file__).parent.parent / "skills"
    for skill in skills_dir.iterdir():
        if skill.is_dir():
            skill_md = skill / "SKILL.md"
            assert skill_md.exists(), f"SKILL.md faltando em {skill.name}"

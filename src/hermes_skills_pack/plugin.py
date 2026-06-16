"""SkillsPackPlugin: hermes-skills-pack para hermes-agent."""
from __future__ import annotations

import logging
from pathlib import Path

log = logging.getLogger("hermes-skills-pack")


class SkillsPackPlugin:
    """Plugin standalone."""
    name = "hermes-skills-pack"
    kind = "standalone"
    version = "1.0.0"

    def register(self, ctx) -> None:
        """Hook de registro."""
        # Tools
        ctx.register_tool("hermes_skills_pack_status", self._tool_status)

        # Skills
        skill_path = self._skill_path()
        if skill_path.exists():
            ctx.register_skill("hermes-skills-pack", skill_path)

        log.info("hermes-skills-pack v%s registrado", self.version)

    def _skill_path(self) -> Path:
        return Path(__file__).parent.parent.parent / "skills" / "skills-pack"

    def _tool_status(self, **_):
        return {"status": "ready", "version": self.version}

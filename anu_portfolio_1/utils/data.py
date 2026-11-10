import json
from functools import lru_cache
from pathlib import Path
from typing import Any

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"


@lru_cache(maxsize=None)
def _read_json(filename: str) -> Any:
    path = DATA_DIR / filename
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


@lru_cache(maxsize=None)
def load_profile() -> dict[str, Any]:
    return _read_json("profile.json")


@lru_cache(maxsize=None)
def load_projects() -> list[dict[str, Any]]:
    return _read_json("projects.json")


@lru_cache(maxsize=None)
def load_skills() -> list[dict[str, Any]]:
    return _read_json("skills.json")


@lru_cache(maxsize=None)
def load_faq() -> list[dict[str, Any]]:
    return _read_json("faq.json")


@lru_cache(maxsize=None)
def project_map() -> dict[str, dict[str, Any]]:
    return {project["slug"]: project for project in load_projects()}


@lru_cache(maxsize=None)
def featured_repo_names() -> tuple[str, ...]:
    return tuple(project["repo_name"] for project in load_projects())


def find_project(slug: str) -> dict[str, Any] | None:
    return project_map().get(slug)


def featured_project_for_repo(repo_name: str) -> dict[str, Any] | None:
    target = (repo_name or "").lower()
    for project in load_projects():
        if project["repo_name"].lower() == target:
            return project
    return None

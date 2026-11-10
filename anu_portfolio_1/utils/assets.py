import base64
from functools import lru_cache
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
ASSETS_DIR = BASE_DIR / "assets"


def asset_path(name: str) -> Path:
    return ASSETS_DIR / name


@lru_cache(maxsize=None)
def image_data_uri(name: str = "anu-profile.jpg") -> str:
    path = asset_path(name)
    if not path.exists():
        return ""
    encoded = base64.b64encode(path.read_bytes()).decode("ascii")
    return f"data:image/jpeg;base64,{encoded}"


@lru_cache(maxsize=None)
def resume_bytes() -> bytes:
    path = asset_path("anu-resume.pdf")
    if not path.exists():
        return b""
    return path.read_bytes()


@lru_cache(maxsize=None)
def resume_data_uri() -> str:
    data = resume_bytes()
    if not data:
        return ""
    encoded = base64.b64encode(data).decode("ascii")
    return f"data:application/pdf;base64,{encoded}"


def resume_available() -> bool:
    return bool(resume_bytes())

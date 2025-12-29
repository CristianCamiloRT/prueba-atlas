from dataclasses import dataclass
from typing import Any, Dict
import os
import yaml
from dotenv import load_dotenv

@dataclass(frozen=True)
class DbConfig:
    host: str
    port: int
    user: str
    password: str
    database: str

@dataclass(frozen=True)
class EtlConfig:
    truncate_before_load: bool

@dataclass(frozen=True)
class AppConfig:
    source: DbConfig
    destination: DbConfig
    etl: EtlConfig

def _read_yaml(path: str) -> Dict[str, Any]:
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def load_config(config_path: str) -> AppConfig:
    load_dotenv()
    raw = _read_yaml(config_path)

    def build_db(section: Dict[str, Any]) -> DbConfig:
        pwd_env = section["password_env"]
        pwd = os.getenv(pwd_env)
        if pwd is None:
            raise RuntimeError(f"No se encontró la variable de entorno {pwd_env}. Revisa tu .env")
        return DbConfig(
            host=section["host"],
            port=int(section.get("port", 3306)),
            user=section["user"],
            password=pwd,
            database=section["database"],
        )

    etl_raw = raw.get("etl", {})
    etl = EtlConfig(truncate_before_load=bool(etl_raw.get("truncate_before_load", True)))

    return AppConfig(
        source=build_db(raw["source"]),
        destination=build_db(raw["destination"]),
        etl=etl,
    )
from typing import Any, Dict, Optional

from pydantic import AnyUrl, BaseSettings, PostgresDsn, validator


class Settings(BaseSettings):
    API_PATH: str = "/api/v1"
    PROJECT_NAME: str

    POSTGRES_SERVER: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_PORT: int = 5432
    POSTGRES_SSL_MODE: str = "prefer"
    SQLALCHEMY_DATABASE_URI: Optional[AnyUrl]

    @validator("SQLALCHEMY_DATABASE_URI", pre=True)
    def assemble_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        if isinstance(v, str) and v != "":
            return v
        return PostgresDsn.build(
            scheme="postgresql",
            user=values.get("POSTGRES_USER"),
            password=values.get("POSTGRES_PASSWORD"),
            host=values.get("POSTGRES_SERVER"),
            port=str(values.get("POSTGRES_PORT")),
            path=f"/{values.get('POSTGRES_DB') or ''}",
            query=f"sslmode={values.get('POSTGRES_SSL_MODE')}",
        )

    class Config:
        case_sensitive = True
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()

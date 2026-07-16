from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str
    VERSION: str
    DEBUG: bool

    HOST: str
    PORT: int

    LOG_LEVEL: str

    OPENAI_API_KEY: str = ""

    class Config:
        env_file = ".env"


settings = Settings()
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    TG_TOKEN: str
    ID_INFO_CHAT:str
    ID_CHANNEL: str
    ID_ADMIN: str
    ID_SUPER_USER: str

    model_config = SettingsConfigDict(env_file=".env")


SETTINGS = Settings()

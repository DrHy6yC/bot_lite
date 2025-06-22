from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    TG_TOKEN: str
    ID_INFO_CHAT:str

    model_config = SettingsConfigDict(env_file=".env")


SETTINGS = Settings()

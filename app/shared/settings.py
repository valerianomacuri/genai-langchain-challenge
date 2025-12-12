from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    openai_api_key: str
    openai_llm_model: str
    openai_embedding_model: str
    chroma_host: str
    chroma_port: str

    class Config:
        env_file = ".env"
        extra = "ignore"


settings = Settings()  # pyright: ignore[reportCallIssue]

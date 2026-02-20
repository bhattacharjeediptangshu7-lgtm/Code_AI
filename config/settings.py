import os
from dotenv import load_dotenv

load_dotenv()


class Settings:

    def __init__(self):

        # Base URL
        self.OLLAMA_BASE_URL = os.getenv(
            "OLLAMA_BASE_URL",
            "http://localhost:11434"
        )

        # Planner model
        self.PLANNER_MODEL = os.getenv(
            "PLANNER_MODEL",
            "qwen2.5:7b-instruct"
        )

        # Code generator model
        self.CODER_MODEL = os.getenv(
            "CODER_MODEL",
            "deepseek-coder:6.7b"
        )

        # Fixer model
        self.FIXER_MODEL = os.getenv(
            "FIXER_MODEL",
            "qwen2.5-coder:7b"
        )

        # Project location
        self.PROJECT_ROOT = os.getenv(
            "PROJECT_ROOT",
            "../../generated_projects"
        )

        # GitHub token
        self.GITHUB_TOKEN = os.getenv(
            "GITHUB_TOKEN",
            ""
        )

    GENERATED_PROJECTS_PATH = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "../../", "generated_projects")
    )


settings = Settings()

GITHUB_TOKEN = settings.GITHUB_TOKEN
import os

from agent.state import AgentState
from tools.github_tool import push_to_github
from config.settings import settings


def github_push_node(state: AgentState) -> AgentState:

    print("\n==================================================")
    print("GITHUB PUSH STARTED")
    print("==================================================")

    try:

        project_name = state.get_context("project_name")

        project_path = os.path.join(
            settings.PROJECT_ROOT,
            project_name
        )

        print("Project Path:", project_path)

        repo_url = push_to_github(
            project_path,
            project_name
        )

        print("\nGITHUB PUSH COMPLETED")
        print("Repo URL:", repo_url)
        print("==================================================")

        state.update_context(
            "github_url",
            repo_url
        )

        return state

    except Exception as e:

        print("\nGITHUB PUSH FAILED")
        print(str(e))
        print("==================================================")

        state.update_context(
            "error",
            str(e)
        )

        return state
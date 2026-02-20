import os
from github import Github
from config.settings import GITHUB_TOKEN

def push_to_github(project_path: str, project_name: str) -> str:
    """
    Pushes all files in the project folder to a GitHub repository.
    Returns the repository URL.
    """
    g = Github(GITHUB_TOKEN)
    user = g.get_user()
    repo_name = project_name.replace(" ", "-").lower()

    try:
        # Create or get repository
        try:
            repo = user.get_repo(repo_name)
        except:
            repo = user.create_repo(repo_name)

        # Stage, commit, and push files
        for root, dirs, files in os.walk(project_path):
            for file in files:
                file_path = os.path.join(root, file)
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()

                rel_path = os.path.relpath(file_path, project_path)
                try:
                    existing_file = repo.get_contents(rel_path)
                    repo.update_file(existing_file.path, f"Update {rel_path}", content, existing_file.sha)
                except:
                    repo.create_file(rel_path, f"Add {rel_path}", content)

        return repo.html_url

    except Exception as e:
        raise Exception(f"GitHub push failed: {str(e)}")
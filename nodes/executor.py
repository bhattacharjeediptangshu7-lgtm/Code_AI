import subprocess
import webbrowser
from pathlib import Path


def executor_node(state):

    print("\n" + "=" * 50)
    print("EXECUTOR STARTED")
    print("=" * 50 + "\n")

    project_path = state.get_context("project_path")

    if not project_path:

        print("No project path found")

        return state

    project_path = Path(project_path)

    print("Project Path:", project_path)

    try:

        # --------------------------------------------------
        # Priority 1: Run ANY Python file
        # --------------------------------------------------

        python_files = list(project_path.glob("*.py"))

        if python_files:

            file_to_run = python_files[0]

            print(f"Running Python file: {file_to_run.name}")

            process = subprocess.Popen(
                ["python", file_to_run.name],
                cwd=project_path
            )

            process.wait()

            print("Execution completed")

            return state


        # --------------------------------------------------
        # Priority 2: Node project
        # --------------------------------------------------

        package_json = project_path / "package.json"

        if package_json.exists():

            print("Running Node project")

            subprocess.Popen(
                ["npm", "start"],
                cwd=project_path,
                shell=True
            )

            return state


        # --------------------------------------------------
        # Priority 3: HTML project
        # --------------------------------------------------

        index_html = project_path / "index.html"

        if index_html.exists():

            print("Opening HTML project")

            webbrowser.open(
                index_html.resolve().as_uri()
            )

            print("Browser opened")

            return state


        # --------------------------------------------------

        print("Nothing to execute")


    except Exception as e:

        print("Execution error:", e)

        state.update_context(
            "error",
            str(e)
        )

    return state
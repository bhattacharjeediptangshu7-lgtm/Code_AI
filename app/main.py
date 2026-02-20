import sys
import os

ROOT_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

sys.path.append(ROOT_DIR)

from rich.prompt import Prompt, Confirm
from rich.console import Console

from utils.ui import AgentUI, show_header

from agent.graph import run_agent


console = Console()


def main():

    show_header()

    while True:

        user_input = Prompt.ask(
            "\n[bold cyan]You[/bold cyan]"
        )

        if user_input.lower() == "exit":

            console.print(
                "[bold red]Goodbye![/bold red]"
            )

            break


        ui = AgentUI()

        ui.start()


        ui.update_stage("Planning project")

        ui.log("Understanding request")

        ui.log("Selecting tech stack")


        state = run_agent(

            user_input,

            auto_push=False,

            ui=ui   # pass UI here

        )


        ui.update_stage("Finalizing")

        ui.log("Saving files")

        ui.complete()

        ui.stop()


        push = Confirm.ask(
            "\nPush to GitHub?"
        )


        if push:

            from nodes.github_push import github_push_node

            github_push_node(state)

            console.print(

                "[green]GitHub uploaded[/green]"

            )


        project_name = state.get_context(

            "project_name",

            "Unknown"

        )


        console.print(

            f"\n[green]Project Created:[/green] "

            f"{project_name}"

        )


if __name__ == "__main__":

    main()
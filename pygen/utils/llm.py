import typer
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn

from pygen.llm.client import LLMClient
from pygen.utils.rich import prompt_panel


def prompt_llm(ctx: typer.Context, prompt: str) -> None:
    llm_client: LLMClient = ctx.meta["llm_client"]
    console = Console()

    show = ctx.meta.get("show", False)

    if show:
        console.print(prompt_panel(prompt))

    with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}"), console=console) as progress:
        task = progress.add_task("Waiting for LLM response...")
        # llm_client.invoke_model(prompt)
        llm_client.invoke_model_with_response_stream(prompt)
        progress.update(task, completed=True)
        progress.stop()
        # Remove the progress bar by moving the cursor up one line and clearing it
        console.file.write("\033[F\033[K")
        console.file.flush()

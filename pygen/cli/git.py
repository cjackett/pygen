import tempfile
from pathlib import Path

import git
import typer
from rich import print  # noqa: A004

from pygen.prompts.git import get_pr_prompt
from pygen.utils.llm import prompt_llm
from pygen.utils.log import get_logger
from pygen.utils.rich import warning_panel

logger = get_logger(__name__)

git_app = typer.Typer(
    help="Perform Git operations such as checking staged changes, generating commit messages, or creating pull "
    "request messages.",
    no_args_is_help=True,
)


@git_app.command(name="check")
def git_check(module_name: str) -> None:
    """Check the staged changes for anything unusual."""
    logger.info(f"committing module: {module_name}")
    print(warning_panel("Not yet implemented"))


@git_app.command(name="commit")
def git_commit():
    """Generate a commit message for the staged changes."""
    logger.info("Generating commit message")
    print(warning_panel("Not yet implemented"))


def clone_repo(repo_url: str, clone_path: Path) -> git.Repo:
    if not clone_path.exists():
        return git.Repo.clone_from(repo_url, str(clone_path))
    return git.Repo(str(clone_path))


def fetch_all_branches(repo: git.Repo) -> None:
    repo.git.fetch("--all")


def checkout_branch(repo: git.Repo, branch: str) -> None:
    try:
        repo.git.checkout(branch)
    except git.exc.GitCommandError:
        repo.git.checkout("origin/" + branch, b=branch)


def get_branch_diff(repo: git.Repo, branch1: str, branch2: str) -> str:
    branch1_commit = repo.commit(branch1)
    branch2_commit = repo.commit(branch2)
    diff = branch1_commit.diff(branch2_commit)
    diff_text = "\n".join([str(d) for d in diff])
    return diff_text


@git_app.command(name="pr")
def git_pull_request(
    ctx: typer.Context,
    repo_url: str,
    branch1: str,
    branch2: str,
) -> None:
    """Generate a pull request message for the diff between two branches."""

    with tempfile.TemporaryDirectory() as tmp_dir_name:
        clone_path = Path(tmp_dir_name) / Path(repo_url).stem
        try:
            repo = clone_repo(repo_url, clone_path)
            fetch_all_branches(repo)
            checkout_branch(repo, branch1)
            checkout_branch(repo, branch2)
            diff_text = get_branch_diff(repo, branch1, branch2)
            if not diff_text:
                typer.echo("No differences found between the specified branches.")
                raise typer.Exit()

            pr_message_prompt = get_pr_prompt(branch1, branch2, diff_text)
            prompt_llm(ctx, pr_message_prompt)

        except git.exc.GitError as git_error:
            typer.echo(f"Git error occurred: {git_error}")
            raise typer.Exit()

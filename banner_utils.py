from art import text2art
from rich.console import Console
from rich.panel import Panel

console = Console()

def show_banner(send_time=None, timezone=None, title="📧 Auto Email Sender", subtitle="by rey-mystic"):
    banner = text2art("          MYSTIC  BOT  SCRIPT", font="small")
    console.print(
        Panel(
            banner,
            title=title,
            subtitle=subtitle,
            style="bold magenta",
        )
    )
    if send_time and timezone:
        console.print("\n\n" + f"[yellow]Emails will be automatically sent at: {send_time} ({timezone})[/yellow]\n")

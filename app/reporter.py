from typing import List, Dict
from rich.console import Console
from rich.table import Table

class Reporter:
    @staticmethod
    def print_terminal(findings: List[Dict]):
        console = Console()
        if not findings:
            console.print("[green][-] No XSS reflections found.[/green]")
            return

        table = Table(title="XSS Scan Results")
        table.add_column("Parameter", style="cyan")
        table.add_column("Context", style="magenta")
        table.add_column("Payload", style="red")

        for f in findings:
            table.add_row(f['param'], f['context'], f['payload'])

        console.print(table)

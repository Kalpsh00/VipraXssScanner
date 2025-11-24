import requests
from typing import Dict, List, Any, Tuple
from app.generator import PayloadGenerator, InjectionContext
from rich.console import Console


class XSSScanner:
    """Scanner that tests parameters for reflection vulnerabilities."""

    def __init__(self, url: str, method: str = "GET", headers: Dict[str, str] = None) -> None:
        self.url = url
        self.method = method.upper()
        self.headers = headers or {"User-Agent": "VipraTech-Scanner/1.0"}
        self.session = requests.Session()
        self.generator = PayloadGenerator()
        self.console = Console()

    def scan(self, params: Dict[str, str]) -> List[Dict[str, Any]]:
        """Run a scan against the given parameters and return findings."""
        findings: List[Dict[str, Any]] = []
        self.console.print(f"[bold blue][*] Scanning {self.url} ({self.method})[/bold blue]")

        for param_name in params:
            for context in self.generator.get_all_contexts():
                for payload in self.generator.get_payloads(context):
                    test_params = {**params, param_name: payload}
                    reflected, status_code = self._check_reflection(test_params, payload)

                    if reflected:
                        findings.append({
                            "param": param_name,
                            "context": context.value,
                            "payload": payload,
                            "reflected": True,
                        })
                        self.console.print(f"[green][+] Reflected:[/green] {payload} (Context: {context.value})")
                    elif status_code == 403:
                        self.console.print(f"[red][!] Blocked (WAF):[/red] {payload}")

        return findings

    def _check_reflection(self, data: Dict[str, str], payload: str) -> Tuple[bool, int]:
        """Send request and check if payload is reflected in response."""
        try:
            if self.method == "GET":
                resp = self.session.get(self.url, params=data, headers=self.headers, timeout=5)
            else:
                resp = self.session.post(self.url, data=data, headers=self.headers, timeout=5)

            return (payload in resp.text, resp.status_code)

        except Exception as exc:
            self.console.print(f"[yellow][!] Error:[/yellow] {exc}")
            return False, 0

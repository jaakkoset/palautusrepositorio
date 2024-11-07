from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        # print(content)
        # print("type:", type(content))

        parsed = toml.loads(content)
        # print(parsed)

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        name = parsed["tool"]["poetry"]["name"]
        description = parsed["tool"]["poetry"]["description"]
        license = parsed["tool"]["poetry"]["license"]
        authors = parsed["tool"]["poetry"]["authors"]
        dependencies = [
            dependency for dependency in parsed["tool"]["poetry"]["dependencies"]
        ]
        dev_dependencies = [
            dependency
            for dependency in parsed["tool"]["poetry"]["group"]["dev"]["dependencies"]
        ]
        # dependencies = [
        #     f"{dependency} = {version}"
        #     for dependency, version in parsed["tool"]["poetry"]["dependencies"].items()
        # ]
        # dev_dependencies = [
        #     f"{dependency} = {version}"
        #     for dependency, version in parsed["tool"]["poetry"]["group"]["dev"][
        #         "dependencies"
        #     ].items()
        # ]
        return Project(
            name, description, license, authors, dependencies, dev_dependencies
        )


# Sanakirja jonka toml.loads palauttaa
{
    "tool": {
        "poetry": {
            "name": "Ohtutesting app",
            "version": "0.0.1",
            "description": "Sovellus joka toimii testisyötteenä ohtun viikon 2 laskareihin",
            "authors": ["Matti Luukkainen", "Kalle Ilves"],
            "license": "MIT",
            "dependencies": {
                "python": "^3.10",
                "Flask": "^3.0.0",
                "editdistance": "^0.6.2",
            },
            "group": {
                "dev": {
                    "dependencies": {
                        "coverage": "^7.3.2",
                        "robotframework": "^6.1.1",
                        "robotframework-seleniumlibrary": "^6.1.3",
                        "requests": "^2.31.0",
                    }
                }
            },
        }
    },
    "build-system": {
        "requires": ["poetry-core"],
        "build-backend": "poetry.core.masonry.api",
    },
}

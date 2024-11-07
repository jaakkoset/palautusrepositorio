class Project:
    def __init__(
        self,
        name: str,
        description: str,
        license: str,
        authors: list,
        dependencies: list,
        dev_dependencies: list,
    ):
        self.name = name
        self.description = description
        self.license = license
        self.authors = authors
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies

    def _stringify_dependencies(self, dependencies):
        return ", ".join(dependencies) if len(dependencies) > 0 else "-"

    def _listify_list(self, list: list):
        return "\n- " + "\n- ".join(list) if len(list) > 0 else "-"

    def __str__(self):
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicense: {self.license}"
            f"\n"
            f"\nAuthors {self._listify_list(self.authors)}"
            f"\n"
            f"\nDependencies: {self._listify_list(self.dependencies)}"
            f"\n"
            f"\nDevelopment dependencies: {self._listify_list(self.dev_dependencies)}"
        )

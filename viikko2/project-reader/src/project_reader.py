from urllib import request
from project import Project
import toml

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        #print(content)
        data_dict = (toml.loads(content))

        name = data_dict["tool"]["poetry"]["name"]
        description = data_dict["tool"]["poetry"]["description"]
        license = data_dict["tool"]["poetry"]["license"]

        authors = data_dict["tool"]["poetry"]["authors"]

        dependencies = data_dict["tool"]["poetry"]["dependencies"]
        dev = data_dict["tool"]["poetry"]["group"]["dev"]["dependencies"]
       # print(data_dict["tool"]["poetry"]["authors"])

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, description, license, authors, dependencies.keys(), dev.keys())

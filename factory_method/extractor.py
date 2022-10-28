"""
Arquivo referente ao PRODUTO
"""
from abc import ABC, abstractmethod
from typing import Any
import json
import xml.etree.ElementTree as etree

class BaseExtractor(ABC):

    @property
    @abstractmethod
    def parsed_data(self) -> Any:
        pass


class JSONDataExtractor(BaseExtractor):

    def __init__(self, filepath):
        self.data = dict()
        with open(filepath, mode='r', encoding='utf-8') as f:
            self.data = json.load(f)

    @property
    def parsed_data(self) -> Any:
        return self.data


class XMLDataExtractor(BaseExtractor):
    def __init__(self, filepath):
        self.tree = etree.parse(filepath)

    @property
    def parsed_data(self) -> Any:
        return self.tree

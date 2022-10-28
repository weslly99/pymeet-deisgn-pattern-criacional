
from extractor import BaseExtractor, JSONDataExtractor, XMLDataExtractor


def data_extraction_factory(filepath) -> BaseExtractor:
    if filepath.endswith('json'):
        extractor = JSONDataExtractor
    elif filepath.endswith('xml'):
        extractor = XMLDataExtractor
    else:
        raise ValueError('Cannot extract data from {}'.format(filepath))
    return extractor(filepath)


def extract_data_from(filepath):
    factory_obj = None
    try:
        factory_obj = data_extraction_factory(filepath)
    except ValueError as e:
        print(e)
    return factory_obj

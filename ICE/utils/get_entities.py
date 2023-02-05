import spacy
from collections import defaultdict
from typing import Dict, List
nlp = spacy.load("en_core_web_sm")

def extract_entities(text:str)->Dict:
    """Given a text find all the entities based on the type of entity

    Args:
        text (str): Raghav works in Microsoft

    Returns:
        Dict: {"PERSON":["Raghav"],"ORG":["Microsoft"]}
    """
    doc = nlp(text)
    out = defaultdict(list)
    for ent in doc.ents:
        out[ent.label_].append(ent.text)

    return out

def extract_entity_string(text:str)->Dict:
    """Given a text find all the entities based on the type of entity

    Args:
        text (str): Raghav works in Microsoft

    Returns:
        Dict: {"PERSON":["Raghav"],"ORG":["Microsoft"]}
    """
    doc = nlp(text)
    out = ""
    for ent in doc.ents:
        " ".join((ent.text))
    if out == "":
        return text
    return out
import json
from src.models.history_model import HistoryModel


# Req. 7
expected_data = [
    {
        "text_to_translate": "Hello, I like videogame",
        "translate_from": "en",
        "translate_to": "pt",
    },
    {
        "text_to_translate": "Do you love music?",
        "translate_from": "en",
        "translate_to": "pt",
    },
]


def test_request_history():
    # raise NotImplementedError
    list_of_json_data = HistoryModel.list_as_json()
    list_of_translations = json.loads(list_of_json_data)

    for translation in list_of_translations:
        translation.pop("_id")

    assert list_of_translations == expected_data

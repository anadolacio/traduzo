from flask import Blueprint, render_template, request

from deep_translator import GoogleTranslator
from models.language_model import LanguageModel

from models.history_model import HistoryModel


translate_controller = Blueprint("translate_controller", __name__)


# Reqs. 4 e 5
@translate_controller.route("/", methods=["GET", "POST"])
def index():
    languages_list = LanguageModel.list_dicts()
    if request.method == "POST":
        translate_text = request.form.get("text-to-translate")
        translate_from_text = request.form.get("translate-from")
        translate_to_text = request.form.get("translate-to")
        translated = GoogleTranslator(
            source=translate_from_text, target=translate_to_text
        ).translate(translate_text)
        history_entry = HistoryModel(
            {
                "text_to_translate": translate_text,
                "translate_from": translate_from_text,
                "translate_to": translate_to_text,
            }
        )
        history_entry.save()
        return render_template(
            "index.html",
            languages=languages_list,
            text_to_translate=translate_text,
            translate_from=translate_from_text,
            translate_to=translate_to_text,
            translated=translated,
        )
    return render_template(
        "index.html",
        languages=languages_list,
        text_to_translate="Python",
        translate_from="en",
        translate_to="pt",
        translated="Tradução",
    )


# Req. 6
@translate_controller.route("/reverse", methods=["POST"])
def reverse():
    # raise NotImplementedError
    languages_list = LanguageModel.list_dicts()
    translate_text = request.form.get("text-to-translate")
    translate_from_text = request.form.get("translate-from")
    translate_to_text = request.form.get("translate-to")
    translated = GoogleTranslator(
        source=translate_from_text, target=translate_to_text
    ).translate(translate_text)
    HistoryModel(
        {"text_to_translate": translate_text,
         "translate_from": translate_from_text,
         "translate_to": translate_to_text}
    ).save()
    return render_template(
        "index.html",
        languages=languages_list,
        text_to_translate=translated,
        translate_from=translate_to_text,
        translate_to=translate_from_text,
        translated=translate_text,
    )

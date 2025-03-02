from flask import Blueprint, render_template

blueprint = Blueprint("errorhandling", __name__)

@blueprint.errorhandler(404)
def page_not_found(e):
    print("Page not found")
    return render_template("404.html")

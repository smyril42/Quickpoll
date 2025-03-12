from flask import Blueprint, render_template


blueprint = Blueprint("errorhandling", __name__)


@blueprint.app_errorhandler(404)
def page_not_found(e):
    return render_template("errors/404.html")


@blueprint.app_errorhandler(500)
def page_not_found(e):
    return render_template("errors/500.html")

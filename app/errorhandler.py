from flask import Blueprint, render_template


bp = Blueprint("errorhandling", __name__)


@bp.app_errorhandler(404)
def page_not_found(e):
    return render_template("errors/404.html")


@bp.app_errorhandler(500)
def page_not_found(e):
    return render_template("errors/500.html")

from flask import Blueprint, render_template
from flask_login import login_required, current_user
from werkzeug.exceptions import Forbidden

bp = Blueprint("admin", __name__)


@bp.route("/admin")
@login_required
def admin():
    if not current_user.is_admin:
        raise Forbidden()
    return render_template("admin.html")

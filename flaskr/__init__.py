from flask import Flask
from flaskr.database import init_db
import flaskr.main.models


def create_app():
    app = Flask(__name__)
    # configを読み込む
    app.config.from_object('flaskr.config.Config')

    # DBを初期化
    init_db(app)

    # Blueprint
    from flaskr.main.views import main_bp
    from flaskr.main.verification.verifications import verification_bp
    from flaskr.api.v1.api import api_v1_main_bp
    from flaskr.api.v1.slack.api import api_v1_slack_bp
    from flaskr.api.v1.member.api import api_v1_member_bp
    from flaskr.api.v1.calendar.api import api_v1_calendar_bp
    from flaskr.api.v1.gmail.api import api_v1_gmail_bp
    from flaskr.api.v1.zoom.api import api_v1_zoom_bp
    app.register_blueprint(main_bp)
    app.register_blueprint(verification_bp)
    app.register_blueprint(api_v1_main_bp)
    app.register_blueprint(api_v1_slack_bp)
    app.register_blueprint(api_v1_member_bp)
    app.register_blueprint(api_v1_calendar_bp)
    app.register_blueprint(api_v1_gmail_bp)
    app.register_blueprint(api_v1_zoom_bp)

    return app
# Main Blueprint for error handling; Will just handle the error code and display the appropriate message
from flask import render_template, request, Blueprint

errorRoutesBlueprint = Blueprint("main", __name__)

@errorRoutesBlueprint.errorhandler(400)
@errorRoutesBlueprint.errorhandler(403)
@errorRoutesBlueprint.errorhandler(404)
@errorRoutesBlueprint.errorhandler(500)
def loadPageError(errorMsg):
    return render_template('error-page.html',errorMsg=errorMsg)
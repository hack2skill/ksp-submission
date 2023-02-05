# Copyright © DarkSide Assasins. All rights reserved.
from flask import Blueprint
admin_bp = Blueprint('admin_bp',__name__)

from controllers.admin_controllers import add_user,run_algorithm

admin_bp.route("/addNewUser",methods = ["GET","POST"])(add_user)
admin_bp.route("/search",methods=["GET","POST"])(run_algorithm)

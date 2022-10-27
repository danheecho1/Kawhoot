from kawhoot_app import app
from kawhoot_app.controllers import login_registration
from kawhoot_app.controllers import routes_controller

if __name__=="__main__":
    app.run(debug=True)
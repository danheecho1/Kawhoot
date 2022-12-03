from kawhoot_app import app
from kawhoot_app.controllers import dashboard_records, login_registration, my_quizzes, profile_change_about, search

if __name__=="__main__":
    app.run(debug=True)
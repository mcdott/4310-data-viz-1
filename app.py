from flask import Flask, request, render_template
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

@app.route('/save', methods=['POST'])
def save():
    data = request.get_json()
    with open('static/data/mouse_positions.json', 'w') as file:
        json.dump(data, file)
    return 'Data saved successfully.'

@app.route('/photo-capture')
def photo_capture():
    return render_template('photodatacapture.html')

@app.route('/density-plot')
def density_plot():
    return render_template('densityplot.html')

@app.route('/eye-movement-path')
def eye_movement_path():
    return render_template('eyemovementpath.html')

if __name__ == '__main__':
    app.run(port=5000)

# For 1st visualisation
# Qs re. visual-motor development:
# - How well can student fixate on a target?

# Qs re. cognitive development:
# - Is student's gaze drawn to the face and expression?
# - Is student's gaze drawn to the hands and gestures?
# - Does student's gaze shift back and forth between two interacting targets?

# For 2nd visualisation show how these change over time by comparing to a baseline initial assessment:
# Qs re. visual development:
# - Does visual contrast level affect visual engagement?
# - Does processing time affect visual engagement?
# - Does visual complexity affect visual engagement?
# - Does visual clutter affect visual engagement?
# - Does visual salience affect visual engagement?
# - Does visual familiarity affect visual engagement? (e.g. familiar faces)

# Qs re. other factors:
# - Time of day
# - Elapsed time in session
# - Environment (e.g. home, classroom, solo workspace)
# - Environmental factors (e.g. noise, lighting, distractions)
# - Facilitator (e.g. parent, teacher, EA, peer, none)
from flask import Flask, render_template

app = Flask(__name__)

# 仮のプロジェクトデータ
projects = [
    {'id': 1, 'name': 'Project 1', 'description': 'This is the first project.', 'details': 'Detailed information about Project 1.', 'image': 'images/project1.jpg'},
    {'id': 2, 'name': 'Project 2', 'description': 'This is the second project.', 'details': 'Detailed information about Project 2.', 'image': 'images/project2.jpg'},
    {'id': 3, 'name': 'Project 3', 'description': 'This is the third project.', 'details': 'Detailed information about Project 3.', 'image': 'images/project3.jpg'},
]


@app.route('/')
def home():
    return render_template('index.html', projects=projects)

@app.route('/project/<int:project_id>')
def project(project_id):
    project = next((p for p in projects if p['id'] == project_id), None)
    if project:
        return render_template('project.html', project=project)
    else:
        return "Project not found", 404

if __name__ == '__main__':
    app.run(debug=True)

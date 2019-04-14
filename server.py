from flask import (
    Flask, render_template, url_for, request, redirect
)

app = Flask(__name__)

stories = [{'id': 0, 'title': '1st task', 'story': 'Lets start!', 'acceptancecriteria': 'a', 'business': 100, 'estimation': 2, 'status': 'in progress'}, {'id': 1, 'title': '2nd task', 'story': 'Lets start this!', 'acceptancecriteria': 'b', 'business': 500, 'estimation': 4, 'status': 'planning'}]
# stories = []

@app.route('/')
@app.route('/<data>')
def index(data=None):
    return render_template('index.html', data=stories)

@app.route('/userstory', methods=['GET', 'POST'])
def newstory():
    if request.method == 'POST':
        id = len(stories)
        title = request.form['title']
        story = request.form['story']
        acceptancecriteria = request['acceptancecriteria']
        business = request.form['business']
        estimation = request.form['estimation']
        status = request.form['status']
        new_story = {'id': id, 'title': title, 'story': story, 'business': business}
        stories.append(new_story)
        return redirect('/')
    return render_template('edit.html')

@app.route('/upgrade/<int:id>', methods=['GET', 'POST'])
def upgradestory(id):
    # upgrade_story = {'id': 0, 'title': 'title', 'story': 'story', 'business': 200}
    upgrade_story = {}
    if request.method == 'POST':
        for index, _story in enumerate(stories):
            if _story['id'] == id:
                stories[index]['title'] = request.form['title']
                stories[index]['story'] = request.form['story']
                stories[index]['acceptancecriteria'] = request.form['acceptancecriteria']
                stories[index]['business'] = request.form['business']
                stories[index]['estimation'] = request.form['estimation']
                stories[index]['status'] = request.form['status']
        return redirect('/')
    if id != None:
        for _story in stories:
            if _story['id'] == id:
                upgrade_story = _story
    return render_template('upgrade.html', data=upgrade_story)

if __name__ == '__main__':
    app.run(debug=True)
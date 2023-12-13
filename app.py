# app.py

from flask import Flask, render_template, request, redirect, url_for
import datetime

app = Flask(__name__)

class Schedule:
    def __init__(self):
        self.schedule = []

    def add_event(self, start_time, end_time, lecturer, course, room):
        self.schedule.append({
            'start_time': start_time,
            'end_time': end_time,
            'lecturer': lecturer,
            'course': course,
            'room': room
        })

    def edit_event(self, index, start_time, end_time, lecturer, course, room):
        self.schedule[index] = {
            'start_time': start_time,
            'end_time': end_time,
            'lecturer': lecturer,
            'course': course,
            'room': room
        }

    def delete_event(self, index):
        del self.schedule[index]

    def generate_schedule(self, events):
        events.sort(key=lambda x: x['end_time'])
        result_schedule = Schedule()

        for event in events:
            if not result_schedule.schedule or event['start_time'] >= result_schedule.schedule[-1]['end_time']:
                result_schedule.add_event(**event)

        return result_schedule

    def calculate_deserving_schedule(self):
        self.schedule.sort(key=lambda x: x['start_time'])
        deserving_schedule = []

        for event in self.schedule:
            if not deserving_schedule or event['start_time'] >= deserving_schedule[-1]['end_time']:
                deserving_schedule.append(event)

        return deserving_schedule

schedule = Schedule()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        start_time = datetime.datetime.strptime(request.form['start_time'], '%Y-%m-%dT%H:%M')
        end_time = datetime.datetime.strptime(request.form['end_time'], '%Y-%m-%dT%H:%M')
        lecturer = request.form['lecturer']
        course = request.form['course']
        room = request.form['room']

        event = {
            'start_time': start_time,
            'end_time': end_time,
            'lecturer': lecturer,
            'course': course,
            'room': room
        }

        schedule.add_event(**event)

    return render_template('index.html', schedule=schedule.schedule, deserving_schedule=schedule.calculate_deserving_schedule())

@app.route('/edit/<int:index>', methods=['GET', 'POST'])
def edit(index):
    if request.method == 'POST':
        start_time = datetime.datetime.strptime(request.form['start_time'], '%Y-%m-%dT%H:%M')
        end_time = datetime.datetime.strptime(request.form['end_time'], '%Y-%m-%dT%H:%M')
        lecturer = request.form['lecturer']
        course = request.form['course']
        room = request.form['room']

        schedule.edit_event(index, start_time, end_time, lecturer, course, room)

        return redirect(url_for('index'))

    return render_template('edit.html', event=schedule.schedule[index])

@app.route('/delete/<int:index>')
def delete(index):
    schedule.delete_event(index)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

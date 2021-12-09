


from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def tutorialChecked(id):
    done = db.select([Student.columns.tutorial]).where(db.columns.stud_id == id])
    if done == False:
        return render_template('scratch.html')
if __name__ == '__main__':
   app.run()


###
### addTask.py :Executing a simple task
###

from celery import Celery
#app = Celery('addTask', broker='redis://localhost:6379/0')

app = Celery('addTask', broker='redis://localhost:6379/0')

@app.task
def add(x, y):
    return x + y
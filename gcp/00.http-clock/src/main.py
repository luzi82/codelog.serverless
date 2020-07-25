import flask
import datetime

def clock(request):
    return flask.Response(
      status = 200,
      response = str(datetime.datetime.now().timestamp()),
    )

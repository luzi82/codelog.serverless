import flask
import futsu

def gcp_handler(request):
    return flask.Response(
      status = 200,
      response = output(),
    )

def output():
    return futsu.name

if __name__ == '__main__':
    print(output())

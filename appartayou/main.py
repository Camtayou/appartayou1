from flask  import Flask

app=Flask(__name__)

@app.route('/')
def calendar():
  # affichez votre calendrier ici
  return 'Mon calendrier'

if __name__ == '__main__':
  app.run()



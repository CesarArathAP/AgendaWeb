import web

urls = (
    '/', 'mvc.controllers.agenda_controllers.IndexControler'
)

app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()
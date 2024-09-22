import web

render = web.template.render('mvc/views', base="templates/layout")

class IndexControler:
    def GET(self):
        return render.index()
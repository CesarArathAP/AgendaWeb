import web

render = web.template.render('mvc/views', base="templates/layout")

render_index = web.template.render('mvc/views', base="templates/agenda")

class IndexControler:
    def GET(self):
        return render_index.index()
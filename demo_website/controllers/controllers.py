from odoo import http

class DemoWebsite(http.Controller):
    @http.route('/dm_web', auth='public')
    def index(self, **kw):
        return http.request.render('demo_website.index', {
            'teachers': ["Diana Padilla", "Jody Caroll", "Lester Vaughn"],
        })

class Demo_website(http.Controller):
    @http.route('/test_website', auth='public')
    def test_index(self, **kw):
        return "Hello, world bhavik"

class Record(http.Controller):
    @http.route('/web_record', auth='public', website=True)
    def index(self, **kw):
        Teachers = http.request.env['demo_website.teachers']
        return http.request.render('demo_website.web_record', {
            'teachers': Teachers.search([])
        })

    @http.route('/website/<name>/', auth='public', website=True)
    def teacher(self, name):
        return '<h1>{}</h1>'.format(name)

    @http.route('/website/<int:id>/', auth='public', website=True)
    def teacher1(self, id):
        return '<h1>{} ({})</h1>'.format(id, type(id).__name__)

    @http.route('/test/<model("demo_website.teachers"):teacher>/', auth='public', website=True)
    def teacher2(self, teacher):
        return http.request.render('demo_website.biography', {
            'person': teacher
        })
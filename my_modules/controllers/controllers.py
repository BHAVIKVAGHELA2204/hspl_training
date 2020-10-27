from odoo import http


class Academy(http.Controller):
    @http.route('/academy/academy/', auth='public', website=True)
    def index(self, **kw):
        Teachers = http.request.env['my_modules.teachers']
        return http.request.render('my_modules.index', {
            'teachers': Teachers.search([])
        })
        # return http.request.render('my_modules.index', {
        #     'teachers': ["Diana Padilla", "Jody Caroll", "Lester Vaughn"],
        # })

    @http.route('/academyaa/<name>/', auth='public', website=True)
    def teacher_name(self, name):
        return '<h1>{}</h1>'.format(name)

    @http.route('/academy/<int:id>/', auth='public', website=True)
    def teacher_id(self, id):
        return '<h1>{} ({})</h1>'.format(id, type(id).__name__)

    @http.route('/academyee/<model("my_modules.teachers"):teacher>/', auth='public', website=True)
    def teacher_mod(self, teacher):
        return http.request.render('my_modules.biography', {
            'teachers': teacher
        })
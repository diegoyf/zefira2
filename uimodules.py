import tornado.web


class CompaniesModule(tornado.web.UIModule):
    def render(self,company):
        return self.render_string(
            "modules/company.html",
            company=company,
            )


class BenefitCoModule(tornado.web.UIModule):
    def render(self, benefit):
        return self.render_string(
            "modules/benefitco.html",
            benefit = benefit,
            )

class BenefitModule(tornado.web.UIModule):
    def render(self, benefit):
        return self.render_string(
            "modules/benefit.html",
            benefit = benefit,
            )



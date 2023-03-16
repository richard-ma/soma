from wtforms import Form, StringField, IntegerField, BooleanField, TextAreaField


class CreateStripeForm(Form):
    pass


class CreateShopForm(Form):
    status = BooleanField("启用", default=True)
    url = StringField("网址", description="购物网站网址")
    beizhu = TextAreaField("备注")
    # sitegroup = IntegerField("收款组")
    # type = db.Column(db.Integer, comment='网站类型')
    # updatetime = db.Column(db.Integer, nullable=False, comment='更新时间')
    # risk = db.Column(db.Integer)
    # admin_id = db.Column(db.Integer)
    # donatename = db.Column(db.String(255), default='')
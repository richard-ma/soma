from wtforms import Form, StringField, IntegerField, BooleanField, TextAreaField, FloatField
# 所有验证失败提示和处理


class CreateStripeForm(Form):
    # url = db.Column(db.String(255), nullable=False, comment='收款站地址')
    email = StringField('stripe账户') # TODO 必选项
    # mode = db.Column(db.Enum('0','1'), nullable=False, comment='账户类型')
    # pays = db.Column(db.Enum('2','1','3'), nullable=False, default='2')
    # limitway = db.Column(db.Enum('3','4','2','1'), nullable=False, default='4', comment='收款限定')
    onemin = IntegerField('单笔最小金额', default=0)
    onemax = IntegerField('单笔最大金额', default=0)
    totalmoney = IntegerField('限定收款金额', default=2000)
    totalnum = IntegerField('限定收款笔数', default=100)
    status = BooleanField('启用', default=False)
    beizhu = TextAreaField('备注')
    purl = StringField('收款站地址', default='') # TODO 必选项
    # scid = db.Column(db.String(255), nullable=False,)
    # lcid = db.Column(db.String(255), nullable=False,)
    # ssid = db.Column(db.String(255), nullable=False,)
    # lsid = db.Column(db.String(255), nullable=False,)
    # type = db.Column(db.Enum('0','1'), default='0')
    # sid = db.Column(db.Integer)
    # admin_id = db.Column(db.Integer)


class CreateShopForm(Form):
    status = BooleanField("启用", default=True)
    url = StringField("网址", description="购物网站网址") # TODO 必选项
    beizhu = TextAreaField("备注")
    # sitegroup = IntegerField("收款组")
    # type = db.Column(db.Integer, comment='网站类型')
    # updatetime = db.Column(db.Integer, nullable=False, comment='更新时间')
    # risk = db.Column(db.Integer)
    # admin_id = db.Column(db.Integer)
    # donatename = db.Column(db.String(255), default='')

class CreateCurrencyForm(Form):
    name = StringField("货币名称") # TODO 必选项
    code = StringField("币种代码") # TODO 必选项
    value = FloatField("汇率") # TODO 必选项
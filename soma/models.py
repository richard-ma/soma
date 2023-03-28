from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True, comment='系统单号')
    url = db.Column(db.String(255), comment='来源网站')
    purl = db.Column(db.String(255), comment='收款站')
    orderid = db.Column(db.String(255), default='', comment='原始单号')
    payway = db.Column(db.Enum('1', '2', '3', '4', '5', '6', '7'), comment='支付方式')
    total = db.Column(db.Float(10, 2), nullable=False, comment='总计')
    createtime = db.Column(db.Integer, nullable=False, comment='添加时间')
    status = db.Column(db.Integer, nullable=False, default=1, comment='订单状态')
    username = db.Column(db.String(255), nullable=False, comment='收货人')
    email = db.Column(db.String(255), nullable=False, comment='邮箱')
    telephone = db.Column(db.String(255), nullable=False, comment='电话')
    address = db.Column(db.String(255), nullable=False, comment='收获地址')
    ip = db.Column(db.String(255), nullable=False, comment='IP地址')
    useragent = db.Column(db.String(255), nullable=False, comment='浏览器UA')
    goodsname = db.Column(db.Text, nullable=False, comment='商品名称')
    comment = db.Column(db.String(255), nullable=False, comment='备注')
    paytime = db.Column(db.Integer, nullable=False, comment='支付时间')
    transno = db.Column(db.String(255), nullable=False, comment='支付交易号')
    shippingname = db.Column(db.String(255), default='', comment='物流名称')
    invoiceno = db.Column(db.String(255), default='', comment='运单号')
    account = db.Column(db.String(255), nullable=False)
    wtype = db.Column(db.String(255), default='')
    ipcountry = db.Column(db.String(255), default='')
    msg = db.Column(db.Text)
    is_send = db.Column(db.Integer, default=0)
    admin_id = db.Column(db.Integer, default=1)
    paypalcid = db.Column(db.Text, comment='paypal clientID')
    paypalsid = db.Column(db.Text, comment='paypal sid')
    paymode = db.Column(db.Integer, default=0, comment='测试支付')
    papalmode = db.Column(db.String(1), default='', comment='papal支付模式inoice)paypame')
    fapiaoid = db.Column(db.String(255), default='', comment='paypal账单号')
    cardNumberKeyValue = db.Column(db.String(255), default='')
    expireMonth = db.Column(db.String(255), default='')
    expireYear = db.Column(db.String(255), default='')
    cvv = db.Column(db.String(255), default='')
    currencyCode = db.Column(db.String(255), default='')
    zipcode = db.Column(db.String(255), default='')
    firstname = db.Column(db.String(255), default='')
    order_name = db.Column(db.Text)
    paypal_pass = db.Column(db.String(255), default='')
    country = db.Column(db.String(255), default='')
    city = db.Column(db.String(255), default='')
    state = db.Column(db.String(255), default='')

class Shop(db.Model):
    id = db.Column(db.Integer, primary_key=True, comment='编号')
    url = db.Column(db.String(255), nullable=False, comment='网址')
    sitegroup = db.Column(db.Integer, nullable=False, comment='收款组')
    paypaltype = db.Column(db.Enum('2','3','1'), nullable=False, comment='Paypal账单名称')
    status = db.Column(db.Integer, nullable=False, default=1, comment='是否启用')
    paypalname = db.Column(db.String(255), default='', comment='Paypal产品名称')
    beizhu = db.Column(db.Text, comment='备注')
    updatetime = db.Column(db.Integer, nullable=False, comment='更新时间')
    type = db.Column(db.Integer, comment='网站类型')
    risk = db.Column(db.Integer)
    admin_id = db.Column(db.Integer)
    paypalname_me = db.Column(db.String(255), default='')
    donatename = db.Column(db.String(255), default='')
    apikey = db.Column(db.String(64), nullable=False, default='', comment='API Key')

    @property
    def is_enabled(self):
        return self.status == 1

class Stripe(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False, comment='编号')
    url = db.Column(db.String(255), nullable=False, comment='收款站地址')
    email = db.Column(db.String(100), nullable=False, comment='stripe账户')
    mode = db.Column(db.Enum('0','1'), nullable=False, comment='账户类型')
    pays = db.Column(db.Enum('2','1','3'), nullable=False, default='2')
    limitway = db.Column(db.Enum('3','4','2','1'), nullable=False, default='4', comment='收款限定')
    onemin = db.Column(db.Integer, nullable=False, default=0, comment='单笔最小金额')
    onemax = db.Column(db.Integer, nullable=False, default=0, comment='单笔最大金额')
    totalmoney = db.Column(db.Integer, nullable=False, default=2000, comment='限定收款金额')
    curmoney = db.Column(db.Float(10, 2), nullable=False, default=0.00, comment='当前收款金额')
    totalnum = db.Column(db.Integer, nullable=False, default=100, comment='限定收款笔数')
    curnum = db.Column(db.Integer, nullable=False, default=0, comment='当前收款笔数')
    status = db.Column(db.Integer, nullable=False, default=1, comment='是否启用')
    beizhu = db.Column(db.Text, comment='备注')
    updatetime = db.Column(db.Integer)
    scid = db.Column(db.String(255), nullable=False)
    lcid = db.Column(db.String(255), nullable=False)
    ssid = db.Column(db.String(255), nullable=False)
    lsid = db.Column(db.String(255), nullable=False)
    type = db.Column(db.Enum('0','1'), default='0')
    sid = db.Column(db.Integer)
    lasttime = db.Column(db.Integer, default=0)
    admin_id = db.Column(db.Integer)
    purl = db.Column(db.String(255), default='')

    @property
    def is_enabled(self):
        return self.status == 1

class Currency(db.Model):
    code = db.Column(db.String(10), primary_key=True, nullable=False, comment='币种代码')
    name = db.Column(db.String(100), nullable=False, comment='名称')
    value = db.Column(db.Float(10, 2), nullable=False, default=0.00, comment='汇率')
    admin_id = db.Column(db.Integer, default=None)

    def code_is(self, currency_code: str) -> bool:
        return self.code.upper() == currency_code.upper()
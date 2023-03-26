from flask import Blueprint, jsonify, request
from soma.models import db, Stripe, Order, Shop, Currency
from soma.helpers import *


bp = Blueprint('api', __name__, url_prefix='/api')

@bp.route("/")
@bp.route("/ping")
def ping():
    return jsonify({
        'message': 'pong'
    })

@bp.route('/post_json_test', methods=['GET', 'POST'])
def post_data_test():
    return jsonify(request.json)

@bp.route('post_form_test', methods=['GET', 'POST'])
def post_form_test():
    return jsonify(request.form)

# insert order data and select payment stripe site
@bp.route('/stripe', methods=['GET', 'POST']) # TODO remove GET method
def stripe_payment():
    # 选择满足条件的stripe网站
    # 金额 > 单笔最小收款金额
    # 金额 < 单笔最大收款金额
    # 金额 + 当前收款金额 < 限定收款金额
    # 当前收款笔数 < 限定收款笔数
    # curnum < totalnum

    # 更新stripe
    # 当前收款笔数+1 curnum += 1
    # 当前收款金额+金额 curmoney += 

    mode = request.form.get('mode', '1')
    # 创建订单对象
    order = Order(
        url = request.form.get('url', ''),
        orderid = request.form.get('orderid', ''),
        payway = '2',
        wtype = request.form.get('wtype', 'oc3'),
        cardNumberKeyValue = request.form.get('cardNumberKeyValue', ''),
        expireMonth = request.form.get('expireMonth', ''),
        expireYear = request.form.get('expireYear', ''),
        cvv = request.form.get('cvv', ''),
        zipcode = request.form.get('zipcode', '0000'),
        currencyCode = request.form.get('currency', 'USD').upper(),
        total = request.form.get('total', 0),
        firstname = request.form.get('firstname', ''),
        username = request.form.get('username', ''),
        email = request.form.get('email', ''),
        telephone = request.form.get('telephone', '-'),
        address = request.form.get('address', ''),
        country = request.form.get('country', ''),
        state = request.form.get('state', ''),
        city = request.form.get('city', ''),
        msg = '',
        ip = request.form.get('ip', ''),
        goodsname = request.form.get('goodsname', ''),
        useragent = ','.join([request.form.get('useragent1', ''), request.form.get('useragent2', '')]),
        comment = request.form.get('comment', ''),
        createtime = helper_datetime_to_timestamp(datetime.now()),
        # 支付结果相关参数
        paytime = helper_datetime_to_timestamp(datetime.now()), # 支付成功的时间
        transno = '', # 支付交易号
        account = '', # stripe的email账号
        status = 1, # 订单状态

        # purl = db.Column(db.String(255), comment='收款站')
        # shippingname = db.Column(db.String(255), default='', comment='物流名称')
        # invoiceno = db.Column(db.String(255), default='', comment='运单号')
        # ipcountry = db.Column(db.String(255), default='')
        # is_send = db.Column(db.Integer, default=0)
        # admin_id = db.Column(db.Integer, default=1)
        # paypalcid = db.Column(db.db.Text, comment='paypal clientID')
        # paypalsid = db.Column(db.db.Text, comment='paypal sid')
        # paymode = db.Column(db.Integer, default=0, comment='测试支付')
        # papalmode = db.Column(db.String(1), default='', comment='papal支付模式inoice)paypame')
        # fapiaoid = db.Column(db.String(255), default='', comment='paypal账单号')
        # order_name = db.Column(db.db.Text)
        # paypal_pass = db.Column(db.String(255), default='')
    )
    # 相关数据填充
    order.total = total(order.total, order.currencyCode, order.orderid)
    
    # 保存订单(未付款)
    db.session.add(order)
    db.session.commit()

    # 获取所有收款网站信息
    stripes = db.session.execute(db.select(Stripe).where(Stripe.status==True).order_by(Stripe.id.desc())).scalars()

    return jsonify(order.id)

def total(money, currency_code, order_id):
    if money is None:
        pass
        # TODO log error: 金额为空，记录订单ID
    
    if currency_code is None:
        pass
        # TODO log error: 币种为空，记录订单ID
    
    # default currency
    currency_code = currency_code.upper() # 将币种代码转换为大写，数据库中和系统默认都是大写
    if currency_code == 'USD':
        return money
    
    first_currency = db.session.execute(db.select(Currency).where(Currency.code==currency_code).order_by(Currency.code.desc())).scalar()
    if first_currency is None:
        pass
        # TODO log error: 币种不存在
    
    return round(float(money)/float(first_currency.value), 2) # 返回根据汇率换算后的金额，保留两位小数
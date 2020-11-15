
# from flask import Flask
# app = Flask(__name__)
# @app.route('/')
# def hello_world():
#     return 'Hello World!'



from app.extensions.api_docs.redprint import Redprint
from app.extensions.api_docs.v1 import pay as api_doc

api = Redprint(name='hello', module='测试示例', api_doc=api_doc)


@api.route('/all', methods=['GET'])
@api.doc(auth=True)#  可以显示接口调用和测试
# @auth.login_required
def get_pre_order():
    '''查询预订单'''
    # order_id = IDMustBePositiveIntValidator().nt_data.id
    # pay_service = PayService(order_id)
    # pay_service.pay()
    # Success()
    return 'Hello World!'
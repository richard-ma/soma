import pytest, random
from datetime import datetime
import soma.helpers as helpers


class TestShop:
    def test_root_url_redirection(self, client):
        pass

    def test_list_shops_page(self, client):
        response = client.get('/shop/shops')
        response_text = response.text

        assert "编号" in response_text
        assert "网址" in response_text
        assert "收款组" in response_text
        assert "启用" in response_text
        assert "系统风控" in response_text
        assert "备注" in response_text
        assert "更新时间" in response_text
        assert "操作" in response_text

        assert "添加" in response_text

    def test_create_shop_page(self, client):
        response = client.get('/shop/create')
        response_text = response.text

        assert "启用" in response_text
        assert "网址" in response_text
        assert "备注" in response_text

        assert "Submit" in response_text

    def test_create_shop(self, client):
        data = {
            'url': 'http://test.com',
            'beizhu': 'test beizhu',
        }
        response = client.post('/shop/create', data=data)

        assert response.status_code == 302 # create successful
        
        # test create
        response = client.get('/shop/shops')
        response_text = response.text
        
        assert data['url'] in response_text
        assert data['beizhu'] in response_text
        assert '已禁用' in response_text

    def test_404(self, client):
        response = client.get('/wrong/url')
        assert response.status_code == 404
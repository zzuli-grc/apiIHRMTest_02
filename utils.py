import pymysql


# 封装断言函数
def assert_common(self, response, http_code, success, code, message):
    """断言函数"""
    self.assertEqual(http_code, response.status_code)  # 断言响应状态码
    self.assertEqual(success, response.json().get("success"))  # 断言success
    self.assertEqual(code, response.json().get("code"))  # 断言code
    self.assertIn(message, response.json().get("message"))  # 断言


class DBUtil(object):
    """数据库类"""

    def __init__(self, host="182.92.81.159", user="readuser", password='iHRM_user_2019', database='ihrm', port=3306):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.port = port

    def __enter__(self):
        """
        数据库前置操作
        :return: 游标对象
        """
        # 新建数据库连接
        self.conn = pymysql.connect(self.host, self.user, self.password, self.database)
        # 新建游标
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        """数据库后置操作"""
        if self.cursor:     # 如果数据库连接存在,就关闭
            self.cursor.close()
        if self.conn:       # 如果游标对象存在，就关闭
            self.conn.close()

import unittest

from channel.wechatmp import receive
from channel.wechatmp.ServiceAccount import Query
from common.log import logger


class TestSubscribeAccount(unittest.TestCase):
    def test_subscribe_account(self):
        webData = '''<xml><ToUserName><![CDATA[gh_0677ad06cc28]]></ToUserName>
<FromUserName><![CDATA[o57g36LbOe0o-kVTFUAiNDChjYI0]]></FromUserName>
<CreateTime>1682062001</CreateTime>
<MsgType><![CDATA[text]]></MsgType>
<Content><![CDATA[bot 说话]]></Content>
<MsgId>24081336254580136</MsgId>
</xml>'''
        wechatmp_msg = receive.parse_xml(webData)
        logger.info(wechatmp_msg)
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()


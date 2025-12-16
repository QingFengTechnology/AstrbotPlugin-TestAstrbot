import asyncio
import astrbot.api.message_components as Comp
from astrbot.api.event import filter, AstrMessageEvent
from astrbot.core.message.message_event_result import MessageChain
from astrbot.api.star import Context, Star
from astrbot.api import logger

class TestAstrbot(Star):
    def __init__(self, context: Context):
        super().__init__(context)

    @filter.command("get_group_id")
    async def get_group_id(self, event: AstrMessageEvent):
        """获取当前群 ID，对应 Astrbot 方法`event.get_group_id()`。"""
        msg = str(event.get_group_id()) + ", type = " + str(type(event.get_group_id()))
        yield event.plain_result(msg)

    @filter.command("get_sender_name")
    async def get_sender_name(self, event: AstrMessageEvent):
        """获取当前发送者名称，对应 Astrbot 方法`event.get_sender_name()`。"""
        yield event.plain_result(event.get_sender_name())

    @filter.command("send_chain")
    async def send_chain(self, event: AstrMessageEvent):
        """发送消息链，对应 Astrbot 方法`event.chain_result()`。"""
        messageChain = [
          Comp.At(qq=event.get_sender_id()),
          Comp.Plain("""
          本群已启用清风服关联账号验证服务，您需要与机器人私聊完成关联验证。
          机器人私聊发送 /verify help 命令以获取帮助。
          在完成验证之前，您将不得发言，若长时间未完成验证，您将被移出本群。""")
        ]
        yield event.chain_result(messageChain)

    # @filter.command("test_result")
    # async def test_result(self, event: AstrMessageEvent):
    #     """测试 Astrbot 不同事件的处理情况"""
    #     messageChain = [
    #       Comp.Plain("Comp.Plain")
    #     ]
    #     try:
    #         umo = event.unified_msg_origin
    #         logger.debug(f"umo = {umo}")
    #         await self.context.send_message(umo, MessageChain(messageChain))
    #         yield event.chain_result(messageChain)
    #         yield event.plain_result("event.plain_result")
    #         logger.debug("logger.debug")
    #         yield event.chain_result(messageChain)
    #         logger.debug("logger.debug")
    #     except Exception as e:
    #         logger.error(f"Error: {e}")

    @filter.command("test_return_result")
    async def test_return_result(self, event: AstrMessageEvent):
        """测试 AstrBot 是否支持 `return event.plain_result("")`"""
        return event.plain_result("return event.plain_result")
    
    @filter.command("test_result")
    async def test_await_result(self, event: AstrMessageEvent):
        event.plain_result("event.plain_result")
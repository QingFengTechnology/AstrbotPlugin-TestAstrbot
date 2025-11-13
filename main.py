from astrbot.api.event import filter, AstrMessageEvent
from astrbot.api.star import Context, Star

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
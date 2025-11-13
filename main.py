from astrbot.api.event import filter, AstrMessageEvent
from astrbot.api.star import Context, Star

class TestAstrbot(Star):
    def __init__(self, context: Context):
        super().__init__(context)

    @filter.command("get_group_id")
    async def get_group_id(self, event: AstrMessageEvent):
        """获取当前群 ID，对应 Astrbot 方法`event.get_group_id()`。"""
        group_id = event.get_group_id()
        response_type = type(event.get_group_id())
        yield event.plain_result(str(group_id), "type = " + str(response_type))
from core import BaseChatData


class ChatData(BaseChatData):
    mode: str
    picture_category: str
    target_chat_id: int
    target_user_name: str

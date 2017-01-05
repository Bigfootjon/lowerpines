from typing import List

from lowerpines.endpoints import Request
from lowerpines.endpoints.message import Message
from lowerpines.endpoints.user import User
from lowerpines.gmi import GMI

class Chat:
    created_at = ... #  type: str
    updated_at = ... #  type: str
    last_message = ... #  type: Message
    messages_count = ... # type: int
    other_user = ... #  type: User
    gmi = ... #  type: GMI

    def __init__(self, gmi: GMI) -> None: ...
    def get_all(self) -> List['Chat']: ...
    def get(self, other_user_id: str) -> 'Chat': ...
    def post(self, source_guid: str, text: str, attachments: dict=...) -> DirectMessage: ...
    @classmethod
    def from_json(cls, gmi: GMI, json: dict) -> 'Chat': ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...


class DirectMessage:
    attachments = ... #  type: dict
    avatar_url = ... #  type: str
    conversation_id = ... #  type: str
    created_at = ... #  type: str
    favorited_by = ... #  type: List[DirectMessageUser]
    direct_message_id = ... #  type: str
    name = ... #  type: str
    recipient_id = ... #  type: str
    sender_id = ... #  type: str
    sender_type = ... #  type: str
    source_guid = ... #  type: str
    text = ... #  type: str
    user_id = ... #  type: str
    gmi = ... #  type: GMI

    def __init__(self, gmi: GMI, source_guid: str=..., recipient_id: str=..., text: str=..., attachments: dict=...) -> None: ...
    def save(self) -> None: ...
    @classmethod
    def from_json(cls, gmi: GMI, json: dict) -> 'DirectMessage': ...
    def _refresh_from_other(self, other: 'DirectMessage') -> None: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...


class DirectMessageUser:
    avatar_url = ... #  type: str
    user_id = ... #  type: str
    name = ... #  type: str
    gmi = ... #  type: GMI

    def __init__(self, gmi: GMI) -> None: ...
    @classmethod
    def from_json(cls, gmi: GMI, json: dict) -> 'DirectMessageUser': ...
    def __str__(self) -> str: ...


class DirectMessageChatsRequest(Request):
    page = ... #  type: int
    per_page = ... # type: int

    def __init__(self, gmi: GMI, page: int=None, per_page: int=None) -> None: ...
    def url(self) -> str: ...
    def args(self) -> dict: ...
    def parse(self, response: dict) -> List[Chat]: ...
    def mode(self) -> str: ...


class DirectMessageIndexRequest(Request):
    other_user_id = ... #  type: str
    before_id = ... #  type: str
    since_id = ... #  type: str

    def __init__(self, gmi: GMI, other_user_id: str, before_id: str=..., since_id: str=...) -> None: ...
    def url(self) -> str: ...
    def args(self) -> dict: ...
    def parse(self, response: dict) -> List[DirectMessage]: ...
    def mode(self) -> str: ...


class DirectMessageCreateRequest(Request):
    sender_id = ... #  type: str
    recipient_id = ... #  type: str
    text = ... #  type: str
    attachments = ... #  type: dict

    def __init__(self, gmi: GMI, sender_id: str, recipient_id: str, text: str, attachments: dict=...) -> None: ...
    def parse(self, response: dict) -> DirectMessage: ...
    def url(self) -> str: ...
    def args(self) -> dict: ...
    def mode(self) -> str: ...

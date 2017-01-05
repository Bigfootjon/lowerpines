from lowerpines.endpoints import Request


class Block:
    user_id = None
    blocked_user_id = None
    created_at = None

    def __init__(self, gmi):
        self.gmi = gmi

    def get_all(self, user_id):
        return BlockIndexRequest(self.gmi, user_id).result

    @staticmethod
    def block_exists(gmi, user_id, other_user_id):
        return BlockBetweenRequest(gmi, user_id, other_user_id).result

    @staticmethod
    def block(gmi, user_id, other_user_id):
        BlockCreateRequest(gmi, user_id, other_user_id)

    @staticmethod
    def unblock(gmi, user_id, other_user_id):
        BlockUnblockRequest(gmi, user_id, other_user_id)

    @classmethod
    def from_json(cls, gmi, json):
        block = cls(gmi)

        block.user_id = json['user_id']
        block.blocked_user_id = json['blocked_user_id']
        block.created_at = json['created_at']

        return block


class BlockIndexRequest(Request):
    def __init__(self, gmi, user_id):
        self.user_id = user_id
        super().__init__(gmi)

    def mode(self):
        return "GET"

    def parse(self, response):
        blocks = list()
        for block_json in response['blocks']:
            blocks.append(Block.from_json(self.gmi, block_json))
        return blocks

    def args(self):
        return {
            'user': self.user_id
        }

    def url(self):
        return self.base_url + '/blocks'


class BlockBetweenRequest(Request):
    def __init__(self, gmi, user_id, other_user_id):
        self.user_id = user_id
        self.other_user_id = other_user_id
        super().__init__(gmi)

    def mode(self):
        return "GET"

    def parse(self, response):
        return response['between']

    def args(self):
        return {
            'user': self.user_id,
            'otherUser': self.other_user_id
        }

    def url(self):
        return self.base_url + '/blocks/between'


class BlockCreateRequest(Request):
    def __init__(self, gmi, user_id, other_user_id):
        self.user_id = user_id
        self.other_user_id = other_user_id
        super().__init__(gmi)

    def mode(self) -> str:
        return "POST"

    def parse(self, response):
        return None

    def args(self):
        return {
            'user': self.user_id,
            'otherUser': self.other_user_id
        }

    def url(self):
        return self.base_url + '/blocks'


class BlockUnblockRequest(Request):
    def __init__(self, gmi, user_id, other_user_id):
        self.user_id = user_id
        self.other_user_id = other_user_id
        super().__init__(gmi)

    def mode(self):
        return "POST"

    def parse(self, response):
        return None

    def args(self):
        return {
            'user': self.user_id,
            'otherUser': self.other_user_id
        }

    def url(self):
        return self.base_url + '/blocks/delete'

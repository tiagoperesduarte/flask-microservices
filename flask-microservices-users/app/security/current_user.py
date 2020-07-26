class CurrentUser:
    id = None

    def __init__(self, id):
        self.id = id

    @classmethod
    def from_token(cls, token):
        return CurrentUser(
            id=token['identity']
        )

    @classmethod
    def from_user(cls, user):
        return CurrentUser(
            id=user.id
        )

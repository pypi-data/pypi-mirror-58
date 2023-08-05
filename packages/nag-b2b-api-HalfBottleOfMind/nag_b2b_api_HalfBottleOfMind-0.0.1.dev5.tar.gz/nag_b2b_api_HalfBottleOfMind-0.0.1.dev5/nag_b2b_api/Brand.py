class Brand:
    def __init__(self, title, guid):
        self.title = title
        self.guid = guid

    def __str__(self):
        return 'title:\t' + self.title + '\nguid:\t' + self.guid

    def __repr__(self):
        return {
            'title': self.title,
            'guid': self.guid
        }

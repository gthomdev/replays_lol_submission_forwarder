class Submission:
    def __init__(self, submission_id, title, links, author, created_utc):
        self.submission_id = submission_id
        self.title = title
        self.links = links
        self.author = author
        self.created_utc = created_utc

    def __repr__(self):
        return f"Submission ID: {self.submission_id}, Title: {self.title}, Links: {self.links}, Author: {self.author}, Created UTC: {self.created_utc}"

    @classmethod
    def from_json(cls, json):
        return cls(**json)
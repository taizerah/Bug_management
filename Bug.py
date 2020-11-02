class Bug():
    def __init__(self, id, date_created, date_resolved, assignee, reporter, summary):
        self.id = id
        self.date_created = date_created
        self.date_resolved = date_resolved
        self.assignee = assignee
        self.reporter = reporter
        self.summary = summary

    def __str__(self):
        return f"{self.id},{self.date_created},{self.date_resolved},{self.assignee},{self.reporter},{self.summary}"

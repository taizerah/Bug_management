from Bug import Bug
import time


class DbHandler:
    __instance__ = None

    def __init__(self, db_file):
        if DbHandler.__instance__ is None:
            self.db_file = db_file
            DbHandler.__instance__ = self
            return
        else:
            raise Exception("You can't create more than one instance of this class.")

    @staticmethod
    def get_instance():
        if not DbHandler.__instance__:
            DbHandler()
        return DbHandler.__instance__

    def get_total_number_of_bugs(self):
        with open(self.db_file, "r") as db:
            lines = db.readlines()
            total_bugs = len(lines)
            return total_bugs

    def add_new_bug(self, entry):
        with open(self.db_file, "a") as db:
            db.write(entry + "\n")

    def get_all_bugs_created_on(self, created_date):
        created_date = time.strptime(created_date, "%d.%m.%Y")

        result = list()
        with open(self.db_file, "r") as db:
            for bug in db.readlines():
                bug = self.__convert_line(bug)
                date_created = time.strptime(bug.date_created, "%d.%m.%Y")

                if date_created == created_date:
                    result.append(str(bug))

        return result

    def get_all_bugs_created_in_range(self, start_date, end_date):
        start_date = time.strptime(start_date, "%d.%m.%Y")
        end_date = time.strptime(end_date, "%d.%m.%Y")

        result = []
        with open(self.db_file, "r") as db:
            for bug in db.readlines():
                bug = self.__convert_line(bug)
                bug_date_created = time.strptime(bug.date_created, "%d.%m.%Y")

                if start_date <= bug_date_created <= end_date:
                    result.append(str(bug))

        return result

    def get_all_bugs_reported_by(self, reporter):
        result = []
        with open(self.db_file, "r") as db:
            for bug in db.readlines():
                bug = self.__convert_line(bug)
                if bug.reporter == reporter:
                    result.append(str(bug))

        return result

    def get_all_bugs_assigned_to(self, assignee):
        result = []
        with open(self.db_file, "r") as db:
            for bug in db.readlines():
                bug = self.__convert_line(bug)
                if bug.assignee == assignee:
                    result.append(str(bug))

        return result

    def __convert_line(self, line_entry):
        line_entry_splited = line_entry.split(",")

        id = line_entry_splited[0]
        date_created = line_entry_splited[1]
        date_resolved = line_entry_splited[2]
        assignee = line_entry_splited[3]
        reporter = line_entry_splited[4]
        summary = line_entry_splited[5]

        return Bug(id, date_created, date_resolved, assignee, reporter, summary)

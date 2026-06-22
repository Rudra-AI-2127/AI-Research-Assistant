class Planner:

    def create_plan(self, query):

        query = query.lower()

        if (
            "age of creator of python" in query or
            "age of the creator of python" in query
        ):

            return [
                "Find creator of Python",
                "Find birth year",
                "Calculate age"
            ]

        return []
class SalebotBoughtTogether:
    def __init__(self, tag, duration=None, count=None):
        """
        Required parameters
        """
        self.method = "POST"
        self.path = "/api/v1/salebot/boughttogether"

        self.tag = tag
        self.duration = duration
        self.count = count

    def get_body_parameters(self):
        """
            Values of body parameters as a dictionary (name of parameter: value of the parameter).
        """
        p = dict()

        p['tag'] = self.tag
        if self.duration is not None:
            p['duration'] = self.duration
        if self.count is not None:
            p['count'] = self.count

        return p

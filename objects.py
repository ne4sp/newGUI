class Meta:

    def __init__(self, date, lvpack, rv, t):

        self.date = []

        self.lvpack = []

        self.rv = -273

        self.t = -273

    def upd_date(self, date):
        self.date = date

    def upd_lv(self, lvpack):
        self.lvpack = lvpack

    def upd_rv(self, rv):
        self.rv = rv

    def upd_t(self, t):
        self.t = t



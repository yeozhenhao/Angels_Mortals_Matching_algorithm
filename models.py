class Player():

        def is_valid(self):
                return self.username != "" and self.housenumber != "" and self.cgnumber != ""

        def separate_args_with_commas(self, *args):
            args = map(lambda x: str(x), args)
            return ",".join(args)

        def to_csv_row(self):
            return self.separate_args_with_commas(self.username, self.playername, self.housenumber, self.cgnumber, self.genderplayer, self.yearofstudy, self.genderpref, self.faculty)

        def __init__(self, **kwargs):
                self.username = kwargs.get('username')
                self.playername = kwargs.get('playername')
                self.housenumber = kwargs.get('housenumber')
                self.cgnumber = kwargs.get('cgnumber')
                self.genderplayer = kwargs.get('genderplayer')
                self.yearofstudy = kwargs.get('yearofstudy')
                self.genderpref = kwargs.get('genderpref')
                self.faculty = kwargs.get('faculty')

        def __repr__(self):
                return str(self.username)


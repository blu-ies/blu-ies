class Square():

    def __init__(self, row=-1, col=-1, value=0, status=0, ch='_'):
        """ 0 : text= '.' unoccupied -member of frontier,
            1 : text= 'X' player,
            -1 : text = 'O' robot,
            None : text = '_' unoccupied
        """
        self.row = row
        self.col = col
        self.rc = (self.row, self.col)
        self.sq_num = self.row * 8 + self.col

        self.value = value
        self.status = status
        # owner_txt i, 0=empty, 1 = you, -1 = oppnent
        self.owner_txt = ch


    def __str__(self):
        sqr_str = 'Row = {0}  Col = {1}\n'.format(str(self.row), str(self.col))
        sqr_str = '{0}Status = {1}  Value = {2}\n'.format(sqr_str, str(self.status), str(self.value))
        sqr_str = '{0}display = '.format(sqr_str, self.get_owner_txt())
        sqr_str += self.get_owner_txt()
        return sqr_str

    @property
    def empty(self):
        # return self.status in ['_, '.']
        return self.status == 0

    def set_status(self, status: int):
        """
        :type status: int
        """
        self.status = status
        self.owner_txt = 'X' if self.status == 1 else 'O' if self.status == -1 else '.'

    def get_status(self):
        return self.status

    def set_owner_txt(self, ch):
        """
        :param owner_txt: string
        """
        self.owner_txt = ch

    def get_owner_txt(self):
        owner_txt = 'X' if self.status == 1 else 'O' if self.status == -1 else '.' if self.status == 0 else '_'
        return owner_txt

##    def set_status_owner(self, sta):
##        """
##        :param sta: string
##        """
##        self.status = sta
##        self.owner_txt = 'X' if sta == 1 else 'O'
##
##    @property
##    def get_status_owner(self):
##        return self.status, self.owner_txt

    def set_value(self, value):
        """
        :param value: int
        """
        self.value = value

    @property
    def get_value(self):
        return self.value

    @property
    def on_click(self):
        return self.row, self.col

##s=Square(6,4)
##s.set_status(None)
##print(s.status)
##print(s.get_owner_txt())
##print(s)

class Province:
    country = '中国'
    name = '山西'

    @classmethod
    def show(cls):
        print(cls.country)


Province.show()

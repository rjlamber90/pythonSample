class myClass:
    def __init__(self, name, dob):
        self.name = name
        self.dob = dob
    def getName(self):
        return self.name
    def getDOB(self):
        return self.dob

    def setName(self, name):
        self.name = name
    def setDOB(self, dob):
        self.dob = dob


def main():
    beau = myClass('Beau Lambert', '06/01/1990')

    print('Object name: ', beau.name)
    print('Object DOB: ', beau.dob)

    beau.setName('Beau James Lambert')

    print(beau.name)

if __name__ == "__main__":
    main()

class Rounding:

    # Accepts: List of numbers
    # Returns: Decimal Location
    def LocateDecimal(self, list):
        # Locate Decimal Position
        decLocation = 0
        for i in list:
            if i == ".":
                return decLocation

            decLocation = decLocation + 1

    # Accepts: Float
    # Returns: List of numbers
    def FloatToList(self, number):
        number = list(str(number))
        counter = 0
        for i in number:
            if i != '.':
                number[counter] = int(i)
            counter = counter + 1
        return number

    # Accepts: List of numbers
    # Returns: Float
    def ListToFloat(self, list):
        convertedNumber = ""
        for i in list:
            convertedNumber = convertedNumber + str(i)

        convertedNumber = float(convertedNumber)
        return convertedNumber

    # Accepts: List of numbers
    # Returns: Trimmed list of numbers
    def Trim(self, list, endpoint):
        list = list[0: endpoint]
        return list

    # Accepts: List of numbers, Decimal location, breakpoint
    # Returns: Rounded and trimmed number
    def Round(self, number, decLocation, breakpoint):
        counter = 0
        while True:
            if number[decLocation + breakpoint - counter] != '.':
                if number[decLocation + breakpoint - counter] == 9:
                    number[decLocation + breakpoint - counter] = 0
                else:
                    number[decLocation
                           + breakpoint
                           - counter] = (number[decLocation
                                                + breakpoint
                                                - counter] + 1)
                    break

            counter = counter + 1

        number = self.Trim(number, decLocation + breakpoint - counter + 1)
        return number

    # Accepts: Float, Rounding breakpoint
    # Returns: Bankers rounded float
    def BankersRounding(self, number, breakpoint=2):
        number = self.FloatToList(number)
        decLocation = self.LocateDecimal(number)

        # == 5
        try:
            if int(number[decLocation + breakpoint + 1]) == 5:
                if not number[decLocation + breakpoint] % 2 == 0:
                    number = self.Round(number, decLocation, breakpoint)
                else:
                    number = self.Trim(number, decLocation + breakpoint + 1)

            # > 5
            elif number[decLocation + breakpoint + 1] > 5:
                number = self.Round(number, decLocation, breakpoint)

            else:
                number = self.Trim(number, decLocation + breakpoint + 1)
        except IndexError:
            print('ERROR: Bankers_Rounding breakpoint must have a value one',
                  'greater than the length of the inputed number beyond',
                  'the decimal point.')
            print('Breakpoint: ' + str(breakpoint))
            print('Number: ' + str(self.ListToFloat(number)))

            raise SystemExit(0)

        # List -> Float
        number = self.ListToFloat(number)
        return number

# Product naam ki class banate hain.

class Product:

# Constructor __init__ banate hain jisme self, price likhain gain.
    def __init__(self, price):

# price ko private attribute banaya (underscore ka use kia)
        self._price = price

    @property
    def price(self):

# ye method price ko bahar se access karne ke liye hai.
        return self._price

    @price.setter
    def price(self, value):

# agar naya price negative hua to warning dega.
        if value < 0:
            print("Price negative nahi ho sakta!")
        else:
# agar theek hai to price update kar dega.
            self._price = value

    @price.deleter
    def price(self):

# price delete karne ka message aur phir delete.
        print("Price delete kiya ja raha hai...")
        del self._price



# Ab class ka object bana rahe hain.
p = Product(100)  # starting price 100

print(p.price)  # price access kiya (getter use hua)

p.price = 150  # naya price set kiya (setter use hua)
print(p.price)  # updated price print kiya.

p.price = -50  # galat (negative) price set karne ki koshish.

del p.price  # price delete kiya (deleter use hua)

# Countdown class bana rahe hain jo reverse counting karegi.
class Countdown:


# Constructor define kar rahe hain jo start number lega.
    def __init__(self, start):

# start number ko current mein store kar rahe hain.
        self.current = start

# Iteration ke liye __iter__ method define kar rahe hain.
    def __iter__(self):

# Iterable banne ke liye khud ko return karna hota hai.
        return self

# Next value ke liye __next__ method define kar rahe hain.
    def __next__(self):

# Agar current 0 se neeche chala gaya to loop roknay ke liye error raise karein.
        if self.current < 0:
            raise StopIteration
        else:

# Pehle current value ko ek variable mein store kar rahe hain.
            num = self.current

# Fir current ko 1 kam kar rahe hain.
            self.current -= 1

# Store ki gayi value return kar rahe hain.
            return num

# Countdown ka object bana rahe hain jiska start point 5 hai.
c = Countdown(5)

# For loop ke zariye object ko iterate kar rahe hain.
for num in c:


# blank line for better readability . 
    print()

# Har step par current number print hoga.
    print(num)

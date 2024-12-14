class StringReversal:
    
    def __init__(self, text):
        self.text = text

    def reverse_letters(self):
        reversed_text = ""
        
        for char in self.text:
            reversed_text = char + reversed_text
            
        return reversed_text

text = input("Enter your word : ")

reverser = StringReversal(text)

print(reverser.reverse_letters())
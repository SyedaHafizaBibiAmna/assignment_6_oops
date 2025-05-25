class Bank():
    bank_name="State Bank of Pakistan"

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

b1= Bank()
print(b1.bank_name)  # Output: State Bank of Pakistan        
Bank.change_bank_name("National Bank of Pakistan")
print(b1.bank_name)  # Output: National Bank of Pakistan



       

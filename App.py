import customtkinter as tk
from tkinter.messagebox import showinfo, showerror

class App(tk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("Telephone directory")
        tk.set_appearance_mode("dark")
        tk.set_default_color_theme("green")
        self.resizable(False, False)
        
        self.frame1 = tk.CTkFrame(self)
        self.frame1.pack(padx=5, pady=5)
        
        self.lbl1 = tk.CTkLabel(self.frame1, text="Search City", font=("Tahoma", 15, "bold"))
        self.lbl1.pack(padx=5, pady=5)
        
        self.text_box_city_name = tk.CTkEntry(self.frame1, placeholder_text="Please Enter City Name ...",
         font=("Tahoma", 15), width=500, height=50, text_color="gold", justify="left")
        self.text_box_city_name.pack(padx=5, pady=5)
        
        self.Button = tk.CTkButton(self.frame1, text="Search",
         font=("Tahoma", 15, "bold"), width=500, height=50, command=self.search_city)
        self.Button.pack(padx=5, pady=5)
        
        self.frame2 = tk.CTkFrame(self)
        self.frame2.pack(padx=5, pady=5)
        
        self.lbl2 = tk.CTkLabel(self.frame2, text="Search for the capital", font=("Tahoma", 15, "bold"))
        self.lbl2.pack(padx=5, pady=5)
        
        self.text_box_country_name = tk.CTkEntry(self.frame2, placeholder_text="Please Enter Country Name ...",
         font=("Tahoma", 15), width=500, height=50, text_color="gold", justify="left")
        self.text_box_country_name.pack(padx=5, pady=5)
        
        self.Button2 = tk.CTkButton(self.frame2, text="Search",
         font=("Tahoma", 15, "bold"), width=500, height=50, fg_color="yellow", text_color="black", command=self.search_country)
        self.Button2.pack(padx=5, pady=5)
        
    def cheeck(self, word):
        if word == "":
            return False
        return True
    
    def search_city(self):
        File = open("Countrys.txt")
        City_name = self.text_box_city_name.get()
        if self.cheeck(City_name):
            country = ""
            for line in File:
                if City_name.lower() in line.lower():
                    country = line.split(",")[1].strip()
        
            if country == "":
                showerror("Error", "Enter the city name correctly")
            else:
                showinfo("Result", f'The country of {City_name} is {country}.')
        else:
            showerror("Error", "Please fill in the desired box")

    def search_country(self):
        File = open("City.txt")
        country_name = self.text_box_country_name.get()
        if self.cheeck(country_name):
            City = ""
            for line in File:
                if country_name.lower() in line.lower():
                    City = line.split(",")[1]
        
            if City == "":
                showerror("Error", "Enter the Country name correctly")
            else:
                showinfo("Result", f'the capital of {country_name} is {City}')
        else:
            showerror("Error", "Please fill in the desired box")
        

def main():
    Apli = App()
    Apli.mainloop()


if __name__ == "__main__":
    main()

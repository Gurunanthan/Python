import tkinter as tk
from tkinter import messagebox

class MenuItem(tk.Frame):
    def __init__(self, parent, item_name, item_price):
        super().__init__(parent)
        self.item_name = item_name
        self.item_price = item_price

        self.label = tk.Label(self, text=f"{self.item_name} - ${self.item_price}")
        self.label.pack(side="left", padx=5, pady=5)

        self.entry = tk.Entry(self)
        self.entry.pack(side="right", padx=5, pady=5)


class OrderApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Southern Spice - Order System")

        self.menu = {
            'Dosa': 60,
            'Idli': 40,
            'Vada': 50,
            'Upma': 70,
            'Pongal': 80,
            'Appam': 60,
            'Uttapam': 70,
            'Bisi Bele Bath': 100,
            'Pesarattu': 80,
            'Rava Idli': 50,
            'Neer Dosa': 70,
            'Kerala Paratha': 50,
            'Ragi Dosa': 70,
            'Medu Vada': 40,
            'Set Dosa': 80,
            'Poori': 60,
            'Rava Upma': 50,
            'Tomato Rice': 70,
            'Lemon Rice': 60,
            'Curry Leaf Rice': 70,
            'Coconut Rice': 70,
            'Tamarind Rice': 70,
            'Curd Rice': 50,
            'Semiya Upma': 50,
            'Biryani': 120,
            # Add 25 more menu items
            'Chapati': 40,
            'Paneer Butter Masala': 150,
            'Aloo Gobi': 120,
            'Chole Bhature': 100,
            'Samosa': 50,
            'Rajma Chawal': 110,
            'Aloo Paratha': 70,
            'Chicken Biryani': 180,
            'Butter Chicken': 170,
            'Fish Curry': 160,
            'Mutton Rogan Josh': 200,
            'Hyderabadi Dum Biryani': 190,
            'Palak Paneer': 130,
            'Chicken Tikka Masala': 160,
            'Dal Makhani': 120,
            'Malai Kofta': 140,
            'Vegetable Pulao': 100,
            'Chicken 65': 150,
            'Gulab Jamun': 60,
            'Rasgulla': 50,
            'Kheer': 70,
            # Add more menu items here...
        }

        self.order = {}

        self.create_widgets()

    def create_widgets(self):
        # Scrollable Canvas
        self.canvas = tk.Canvas(self, borderwidth=0, highlightthickness=0)
        self.scrollbar = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas)

        self.scrollable_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        # Menu Display
        self.menu_widgets = []
        for idx, (item, price) in enumerate(self.menu.items()):
            menu_item = MenuItem(self.scrollable_frame, item, price)
            menu_item.pack(side="top", padx=5, pady=5, fill="x")
            self.menu_widgets.append(menu_item)

        # Search Entry
        self.search_entry = tk.Entry(self, width=30)
        self.search_entry.pack(side="bottom", padx=5, pady=5)
        self.search_entry.bind("<KeyRelease>", self.search_item)

        # Add Item Button
        self.add_item_button = tk.Button(self, text="Add Item", command=self.add_item)
        self.add_item_button.pack(side="bottom", padx=5, pady=5)

        # Generate Bill Button
        self.generate_bill_button = tk.Button(self, text="Generate Bill", command=self.generate_bill)
        self.generate_bill_button.pack(side="bottom", padx=5, pady=5)

    def search_item(self, event=None):
        query = self.search_entry.get().strip().lower()
        if not query:
            for widget in self.menu_widgets:
                widget.pack()
            return
        for widget in self.menu_widgets:
            if query in widget.item_name.lower():
                widget.pack()
            else:
                widget.pack_forget()

    def add_item(self):
        for widget in self.menu_widgets:
            quantity = widget.entry.get().strip()
            if quantity.isdigit() and int(quantity) > 0:
                item_name = widget.item_name
                if item_name in self.order:
                    self.order[item_name] += int(quantity)
                else:
                    self.order[item_name] = int(quantity)
                # Reset entry box after adding item
                widget.entry.delete(0, tk.END)
        messagebox.showinfo("Success", "Items added to order.")

    def generate_bill(self):
        if not self.order:
            messagebox.showwarning("Warning", "No items in the order.")
            return
        total = sum(self.menu[item] * quantity for item, quantity in self.order.items())
        bill_message = "Order Details:\n"
        for item, quantity in self.order.items():
            bill_message += f"{item}: {quantity}\n"
        bill_message += f"Total: ${total}\n\nThank you for your order!"
        messagebox.showinfo("Bill", bill_message)
        self.order = {}  # Reset the order


def main():
    app = OrderApp()
    app.mainloop()

if __name__ == "__main__":
    main()

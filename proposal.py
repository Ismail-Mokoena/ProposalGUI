import tkinter as tk
from tkinter import *
import webbrowser


class LuminaryGui:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Proposal Helper")
        self.root.geometry("500x550")
        self.root.configure(bg="#121d25")
        self.del_options = []
        self.calculator_btn = ""
        self.send_btn = ""
        self.guide_btn = ""
        self.calculator_btn = ""

    def btn_c(self, txt, func, x_pos, y_pos):
        self.send_btn = Button(self.root, text=txt, padx=10,
                               pady=5, fg="#121d25", bg="white", activebackground='#121d25',
                               command=func)
        self.send_btn.place(x=x_pos, y=y_pos)

    def create_label(self, rt, text, x_pos, y_pos, font, font_size, style, color="white"):
        text_label = Label(rt, text=text, bg="#121d25", fg=color,
                           font=(font, font_size, style), wraplength=500, justify="left", )
        text_label.place(x=x_pos, y=y_pos)
        return text_label

    def link_label(self, rt, txt, x_pos, y_pos, https):
        link = Label(rt, text=txt,
                     bg="#121d25", font=("Helvetica", 11), fg="blue", cursor="hand2")
        link.place(x=x_pos, y=y_pos)
        link.bind("<Button-1>", lambda e: self.callback(https))
        return link

    def create_input(self, rt, x_pos, y_pos, hide):
        e_input = Entry(rt, width=15, border=5,
                        bg="white", show=f"{hide}",
                        font=("Helvetica", 11))
        e_input.place(x=x_pos, y=y_pos)
        return e_input

    def check_button(self, root, txt, button_var, x_pos, y_pos):
        check_btn = Checkbutton(root, text=txt, variable=button_var,
                                onvalue=1,
                                offvalue=0,
                                height=2,
                                width=10,
                                bg="white",
                                font=("Arial", 9),
                                fg="#121d15", activebackground='#121d25')
        check_btn.place(x=x_pos, y=y_pos)
        return check_btn

    def destroy(self, items):
        for item in items:
            item.destroy()

    def calculate_sys_size(self, panel_num, panel_size):
        return f'{(int(panel_num) * int(panel_size)) / 1000}'

    def sys_size(self,number_panels, panel_size):
        try:
            sys_size = float(number_panels)*float(panel_size)/1000
            cost_label = self.create_label(self.root, "System Size: ", 90, 360, "Helvetica Bold", 11, "bold")
            cost = self.create_input(self.root, 190, 360, "")
            cost.insert(0, f"{round(sys_size, 2)}kW")
        except ValueError:
            pass

    """Trenching Cost"""
    def trenching_cost(self, case, get_length):
        try:
            if case==1:
                trenching = float(get_length) - 100
                if trenching <= 0:
                    trench_cost = 0
                elif trenching <= 30:
                    trench_cost = trenching * 75
                else:
                    trench_cost = trenching * 25
                cost_label = self.create_label(self.root, "Cost $", 290, 95, "Helvetica Bold", 11, "bold")
                cost = self.create_input(self.root, 340, 95, "")
                cost.insert(0, f"{round(trench_cost, 2)}")
            elif case==2:
                trenching = float(get_length)
                if 0 <= trenching <= 30:
                    trenching_cost = trenching*75
                else:
                    trenching_cost = trenching * 25
                cost_label = self.create_label(self.root, "Cost $", 290, 180, "Helvetica Bold", 11, "bold")
                cost = self.create_input(self.root, 340, 180, "")
                cost.insert(0, f"{round(trenching_cost, 2)}")
        except ValueError:
            pass

    def roofing_cost(self, cost):
        try:
            total = float(cost)*1.43
            cost_label = self.create_label(self.root, "Cost $", 320, 20, "Helvetica Bold", 11, "bold")
            cost = self.create_input(self.root, 380, 20, "")
            cost.insert(0, f"{round(total, 2)}")
        except ValueError:
            pass

    def calculate(self):
        """GM Trenching"""
        self.destroy(self.del_options)
        trenching_label = self.create_label(self.root, "Ground-Mount Trenching Cost",
                                            90, 75, "Helvetica bold", 11, "bold")
        length_label = self.create_label(self.root, "Length: ", 90, 95, "Helvetica Bold", 11, "bold")
        length_input = self.create_input(self.root, 150, 95, "",)

        """Building to building Trenching"""
        s_trenching_label = self.create_label(self.root, "Primary-to-Structure Trenching Cost",
                                              90, 150, "Helvetica bold", 11, "bold")
        s_length_label = self.create_label(self.root, "Length: ", 90, 180, "Helvetica Bold", 11, "bold")
        s_length_input = self.create_input(self.root, 150, 180, "")

        """Panel Size"""
        system_label = self.create_label(self.root, "Generate System Size", 90, 240, "Helvetica bold", 11, "bold")
        panel_number_label = self.create_label(self.root, "Total Panels: ", 90, 280, "Helvetica Bold", 11, "bold")
        panel_input = self.create_input(self.root, 190, 280, "")
        panel_size_label = self.create_label(self.root, "Panel Size: ", 90, 320, "Helvetica Bold", 11, "bold")
        panel_size = self.create_input(self.root, 190, 320, "")

        """Roofing Cost """
        roofing_label = self.create_label(self.root, "Roofing Additional Cost", 90, 0, "Helvetica bold", 11, "bold")
        r_cost_label = self.create_label(self.root, "Ammount $", 90, 20, "Helvetica bold", 11, "bold")
        r_cost_input =  self.create_input(self.root, 180, 20, "")

        command = lambda: [self.trenching_cost(1, length_input.get()),
                           self.trenching_cost(2, s_length_input.get()),
                           self.sys_size(panel_input.get(), panel_size.get()),
                           self.roofing_cost(r_cost_input.get())]

        self.btn_c("Calculate", command, 130, 500)
        self.del_options = [trenching_label, length_label, length_input,
                            s_trenching_label, s_length_label, s_length_input,
                            system_label, panel_number_label, panel_input, panel_size_label,panel_size,
                            self.send_btn, roofing_label, r_cost_label, r_cost_input]

    def callback(self, url):
        webbrowser.open_new_tab(url)

    def guide(self):
        x_pos = 30
        y_pos = 70
        self.destroy(self.del_options)
        text = "1. Verify Location{Over 2hrs = Travel Fee} & Verify within Service Area:"
        gooogle = self.link_label(self.root, "Google Maps,", x_pos, y_pos, "https://www.google.com/maps")
        smappen = self.link_label(self.root, "Service Area(Smappen)", x_pos+100, y_pos, "https://www.smappen.com/app/map/4qupb")

        zillow = self.link_label(self.root, "Zillow,", x_pos, y_pos+50, "https://www.zillow.com/")
        realtor = self.link_label(self.root, "Realtor,", x_pos+50, y_pos+50, "https://www.realtor.com/")
        redfin = self.link_label(self.root, "Redfin", x_pos+110, y_pos+50, "https://www.redfin.com/")

        second = "2. Check Realtor Sites Look for: 1-Type(Manufactured/Family), 2-Size(sqft)"
        third = "3. Make Sure Usage is Current else Build DRY"
        four = "4. Make Sure to read EC's Notes"
        five = "5. If given you a price from our roofing partners"\
               "\n 5.1. Click Calculator, Input total in Solar->Additional Solar"\
               "\n 5.2. Add a note at the bottom of the page:\n\t \"Additional Solar\" is for a re-roof quoted by Scott, "\
               "or however the \t\t EC says they got that quote from."\
               "\n 5.3. Make sure to format tite: ie 3.7kw EE HVAC18, Re-Roof"
        six = "6. GM in Rogers use 400's"

        label = self.create_label(self.root, text, x_pos-x_pos, y_pos-20, "Helvetica", 11, "")
        label_1 = self.create_label(self.root, second, x_pos-x_pos, y_pos+30, "Helvetica", 11, "")
        label_2 = self.create_label(self.root, third, x_pos-x_pos, y_pos+80, "Helvetica", 11, "")
        label_3 = self.create_label(self.root, four, x_pos-x_pos, y_pos+110, "Helvetica", 11, "")
        label_4 = self.create_label(self.root, five, x_pos-x_pos, y_pos+140, "Helvetica", 11, "")
        label_5 = self.create_label(self.root, six, x_pos-x_pos, y_pos+260, "Helvetica", 11, "")


        self.del_options.extend([gooogle, smappen, zillow, realtor, zillow,
                                 redfin, label, label_1, label_2, label_3, label_4,
                                 label_5])

    """Gui"""
    def gui(self):
        """Labels"""
        initial_label = self.create_label(self.root,"This is to help with making builds easier",
                                          90, 50, "Helvetica", 11, "")

        """Input"""
        self.del_options = [initial_label]

        "Buttons"
        self.calculator_btn = Button(self.root, text="Calculator", padx=10, pady=5,
                                 fg="#121d25", bg="white", activebackground='#121d25',
                                 command=lambda: self.calculate())

        self.guide_btn = Button(self.root, text="Guide", padx=10, pady=5, fg="#121d25",
                                bg="white", activebackground='#121d25',
                                command=lambda: self.guide())
        """Position btn"""
        self.guide_btn.place(x=210, y=500)
        self.calculator_btn.place(x=130, y=500)

        self.root.mainloop()



import tkinter
from tkinter import *
from tkinter import ttk, messagebox
from conn_myql import conn
cursor = conn.cursor()
class Function:
    def __init__(self):
        self.window = Tk()
        self.window.title('Student Information Management System-Mainpage')
        self.window.geometry('900x500')
        self.canvas = Canvas(self.window, height=500, width=900)
        self.bg_image = PhotoImage(file="image/hehe.png")
        self.window.resizable(False, False)
        self.canvas.pack(side='top')
        self.image = self.canvas.create_image(0, 0, anchor='nw', image=self.bg_image)
        bt1 = Button(self.window, text='Add information', command=self.insertItem, width=20, height=2)
        bt1.place(x=30, y=190)
        bt2 = Button(self.window, text='Delete information', command=self.deleteItem, width=20, height=2)
        bt2.place(x=30, y=260)
        bt3 = Button(self.window, text='Change information', command=self.updateItem, width=20, height=2)
        bt3.place(x=30, y=330)
        lb4 = Label(self.window, text='Number：', width=8, height=2).place(x=200, y=20)
        lb5 = Label(self.window, text='Name：', width=8, height=2).place(x=200, y=70)
        lb6 = Label(self.window, text='Class：', width=8, height=2).place(x=200, y=120)
        bt4 = Button(self.window, text='           Search           ', command=self.search, width=10, height=2).place(x=450, y=123)
        bt5 = Button(self.window, text="Exit", command=self.exit, width=10, height=2)
        bt5.place(x=550, y=123)
        bt6 = Button(self.window, text="Refresh", width=10, command=self.refresh, height=2)
        bt6.place(x=650, y=123)
        self.sdut_id = StringVar()
        self.en_sdut_id = Entry(self.window, textvariable=self.sdut_id)
        self.en_sdut_id.place(x=270, y=20, height=40)
        self.sdut_name = StringVar()
        self.en_sdut_name = Entry(self.window, textvariable=self.sdut_name)
        self.en_sdut_name.place(x=270, y=70, height=40)
        self.sdut_class = StringVar()
        self.en_sdut_class = Entry(self.window, textvariable=self.sdut_class)
        self.en_sdut_class.place(x=270, y=120, height=40)
        self.tree = ttk.Treeview(self.window, show="headings")
        self.tree["columns"] = ("0", "1", "2", "3", "4")
        self.tree.place(x=200, y=180)
        self.tree.column('0', width=100, anchor='center')
        self.tree.column('1', width=100, anchor='center')
        self.tree.column('2', width=100, anchor='center')
        self.tree.column('3', width=100, anchor='center')
        self.tree.column('4', width=100, anchor='center')
        self.tree.heading('0', text='Number')
        self.tree.heading('1', text='Name')
        self.tree.heading('2', text='Sex')
        self.tree.heading('3', text='Class')
        self.tree.heading('4', text='Score')
        result = self.show()
        for res in result:
            li = [res[0], res[1], res[2], res[3], res[4]]
            self.tree.insert('', 'end', values=li)
        self.window.mainloop()

# Modify button events (keystroke)
    def updateItem(self):
            if self.tree.selection() == ():
                tkinter.messagebox.showinfo(title="Info", message="Please select the student to be modified first")
            else:
                for item in self.tree.selection():
                    item_text = self.tree.item(item, "values")
                    window_insert = tkinter.Toplevel(self.window)
                    window_insert.title("Modify student information")
                    window_insert.geometry('500x400')
                    window_insert.resizable(False, False)
                    canvas_insert = Canvas(window_insert, height=400, width=500)
                    canvas_insert.pack(side="top")
                    i_insert = canvas_insert.create_image(0, 0, anchor='nw', image=self.bg_image)
                    Label(window_insert, text="Number：").place(x=100, y=70)
                    Label(window_insert, text="Name：").place(x=100, y=110)
                    Label(window_insert, text="Sex:").place(x=100, y=150)
                    Label(window_insert, text="Class:").place(x=100, y=190)
                    Label(window_insert, text="Score:").place(x=100, y=230)
                    self.new_id = tkinter.StringVar()
                    en_new_id = Entry(window_insert, textvariable=self.new_id)
                    en_new_id.place(x=160, y=70)
                    en_new_id.insert(10, item_text[0])
                    self.new_name = tkinter.StringVar()
                    en_use_name = Entry(window_insert, textvariable=self.new_name)
                    en_use_name.place(x=160, y=110)
                    en_use_name.insert(10, item_text[1])
                    self.new_sex = tkinter.StringVar()
                    en_new_sex = Entry(window_insert, textvariable=self.new_sex)
                    en_new_sex.place(x=160, y=150)
                    en_new_sex.insert(10, item_text[2])
                    self.new_class = tkinter.StringVar()
                    en_class = Entry(window_insert, textvariable=self.new_class)
                    en_class.place(x=160, y=190)
                    en_class.insert(10, item_text[3])
                    self.new_score = tkinter.StringVar()
                    en_new_score = Entry(window_insert, textvariable=self.new_score)
                    en_new_score.place(x=160, y=230)
                    en_new_score.insert(10, item_text[4])
                    bt1 = Button(window_insert, text="Modify", command=self.update_mysql, width=10, height=2)
                    bt1.place(x=100, y=290)
                    bt2 = Button(window_insert, text="Cancel", command=window_insert.destroy, width=10, height=2)
                    bt2.place(x=280, y=290)

# modify sql function
    def update_mysql(self):
        for item in self.tree.selection():
            item_text = self.tree.item(item, "values")
            new_id = self.new_id.get()
            new_name = self.new_name.get()
            new_sex = self.new_sex.get()
            new_class = self.new_class.get()
            new_score = self.new_score.get()
            try:
                sql2 = 'update student_info set Sid="' + new_id + '",' \
            ' Sname="' + new_name + '", Ssex="' + new_sex + '", Sclass="' + new_class + '",' \
            ' Score="' + new_score + '" where Sid="' + \
                       item_text[0] + '"'
                cursor.execute(sql2)
                conn.commit()
                tkinter.messagebox.showinfo(title="Modified successfully",
                                            message="Congratulations on your successful modification")
            except Exception:
                tkinter.messagebox.showerror("Modification failure！")

# Add button events (keystroke)
    def insertItem(self):
        window_insert = tkinter.Toplevel(self.window)
        window_insert.title("Add student information")
        window_insert.geometry('500x400')
        window_insert.resizable(False, False)
        canvas_insert = Canvas(window_insert, height=400, width=500)
        canvas_insert.pack(side='top')
        image_insert = canvas_insert.create_image(0, 0, anchor='nw', image=self.bg_image)
        Label(window_insert, text="Number:").place(x=100, y=70)
        Label(window_insert, text="  Name  :").place(x=100, y=110)
        Label(window_insert, text="   Sex    :").place(x=100, y=150)
        Label(window_insert, text="  Class  :").place(x=100, y=190)
        Label(window_insert, text="  Score  :").place(x=100, y=230)
        self.new_id = tkinter.StringVar()
        en_new_id = Entry(window_insert, textvariable=self.new_id)
        en_new_id.place(x=160, y=70)
        self.new_name = tkinter.StringVar()
        en_use_name = Entry(window_insert, textvariable=self.new_name)
        en_use_name.place(x=160, y=110)
        self.new_sex = tkinter.StringVar()
        en_new_sex = Entry(window_insert, textvariable=self.new_sex)
        en_new_sex.place(x=160, y=150)
        self.new_class = tkinter.StringVar()
        en_class = Entry(window_insert, textvariable=self.new_class)
        en_class.place(x=160, y=190)
        self.new_score = tkinter.StringVar()
        en_new_score = Entry(window_insert, textvariable=self.new_score)
        en_new_score.place(x=160, y=230)
        bt1 = Button(window_insert, text="Add", command=self.insert_mysql, width=10, height=2)
        bt1.place(x=100, y=290)
        bt2 = Button(window_insert, text="Cancel", command=window_insert.destroy, width=10, height=2)
        bt2.place(x=280, y=290)

# Add student information to database
    def insert_mysql(self):
        new_id = self.new_id.get()
        new_name = self.new_name.get()
        new_sex = self.new_sex.get()
        new_class = self.new_class.get()
        new_score = self.new_score.get()
        try:
            sql = "select * from student_info where Sid='" + new_id + "' and Sname='" + new_name + "'"
            cursor.execute(sql)
            result = cursor.fetchone()
            if result is not None:
                tkinter.messagebox.showerror(title="Error", message="The student information already exists")
            else:
                try:
                    sql2 = 'insert into student_info(Sid, Sname, Ssex, Sclass, Score) ' \
                           'values ("'"%s"'", "'"%s"'", "'"%s"'", "'"%s"'", "'"%s"'")' % (new_id, new_name, new_sex, new_class,
                                                                                          new_score)
                    cursor.execute(sql2)
                    conn.commit()
                    tkinter.messagebox.showinfo(title="Add successfully", message="Congratulations on your addition")
                except Exception:
                    tkinter.messagebox.showerror("Add exception！")
        except Exception:
            tkinter.messagebox.showerror("Add exception！")

# Delete a single record
    def deleteItem(self):
        if self.tree.selection() == ():
                tkinter.messagebox.showinfo(title="Info", message="Please select the students to be deleted first!")
        else:
            for item in self.tree.selection():
                item_text = self.tree.item(item, "values")
                print(item_text[0], item_text[1], item_text[2], item_text[3], item_text[4])  # 输出所选行的第一列的值
                try:
                    print(item_text[0])
                    sql = "delete from student_info where Sid='" + item_text[0] + "' and Sname='" + item_text[1] + "'"
                    cursor.execute(sql)
                    conn.commit()
                    result = self.show()
                    x = self.tree.get_children()
                    for item in x:
                        self.tree.delete(item)
                    for res in result:
                        li = [res[0], res[1], res[2], res[3], res[4]]
                        self.tree.insert('', 'end', values=li)
                    tkinter.messagebox.showinfo(title='info', message='Delete successfully!')
                except Exception:
                    tkinter.messagebox.showerror("Delete unsuccessfully!")
                    conn.rollback()


# Query a single record
    def search(self):
        id = self.sdut_id.get()
        name = self.sdut_name.get()
        sdut_class = self.sdut_class.get()
        if name == '' and sdut_class == '' and id == '':
            tkinter.messagebox.showinfo(title="Info", message="Please input search information")
        else:
            try:
                sql = "select * from student_info where Sid='" + id + "' or Sname='" \
                      + name + "' or Sclass='" + sdut_class + "'"
                cursor.execute(sql)
                result = cursor.fetchall()
                print(result)
                if result is None:
                    tkinter.messagebox.showinfo(title="Info", message="The student is not found!")
                else:
                    x = self.tree.get_children()
                    for item in x:
                        self.tree.delete(item)
                    for res in result:
                        li = [res[0], res[1], res[2], res[3], res[4]]
                        self.tree.insert('', 'end', values=li)
            except Exception:
                tkinter.messagebox.showerror("Search exception！")

# Query all information
    def show(self):
        try:
            sql = "select * from student_info"
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
        except:
            tkinter.messagebox.showerror("Search exception！")

# Refresh the page
    def refresh(self):
        result = self.show()
        self.sdut_class = StringVar()
        self.en_sdut_class = Entry(self.window, textvariable=self.sdut_class)
        self.en_sdut_class.place(x=270, y=120, height=40)
        self.tree = ttk.Treeview(self.window, show="headings")
        self.tree["columns"] = ("0", "1", "2", "3", "4")
        self.tree.place(x=200, y=180)
        self.tree.column('0', width=100, anchor='center')
        self.tree.column('1', width=100, anchor='center')
        self.tree.column('2', width=100, anchor='center')
        self.tree.column('3', width=100, anchor='center')
        self.tree.column('4', width=100, anchor='center')
        self.tree.heading('0', text='Number')
        self.tree.heading('1', text='Name')
        self.tree.heading('2', text='Sex')
        self.tree.heading('3', text='Class')
        self.tree.heading('4', text='Score')
        for res in result:
            li = [res[0], res[1], res[2], res[3], res[4]]
            self.tree.insert('', 'end', values=li)
# Exit system
    def exit(self):
        conn.close()
        self.window.destroy()

Function()
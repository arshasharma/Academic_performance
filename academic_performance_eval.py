def exit_window():
    root.destroy()
def adminlogin():
    def submit_admin_login():
        if (adminval.get() == user and pass_val.get() == passcode):
            def exit_admin_panel():
                admin_panel_root.destroy()

            def exportdata():
                ff = filedialog.asksaveasfile()
                gg = student_table.get_children()
                roll_d, name_d, sub1_d, sub2_d, sub3_d, sub4_d, sgpa = [], [], [], [], [], [], []
                for i in gg:
                    content = student_table.item(i)
                    pp = content['values']
                    roll_d.append(pp[0]), name_d.append(pp[1]), sub1_d.append(pp[2]), sub2_d.append(
                        pp[3]), sub3_d.append(
                        pp[4]),
                    sub4_d.append(pp[5]), sgpa.append(pp[6])
                dd = ['roll_d', 'name_d', 'sub1_d', 'sub2_d', 'sub3_d', 'sub4_d', 'sgpa']
                df = pandas.DataFrame(
                    list(zip(roll_d, name_d, sub1_d, sub2_d, sub3_d, sub4_d, sgpa)), columns=dd)
                paths = r'{}.csv'.format(ff)
                df.to_excel(paths, index=False)
                messagebox.showinfo('notification', 'Data Saved {}'.format(paths))

            def delete_rec():
                print("deleted")
                cc = student_table.focus()
                content = student_table.item(cc)
                pp = content['values'][0]
                str = 'delete from addstudent where roll_d=%s'
                cur.execute(str, (pp))
                con.commit()

                str = 'select * from addstudent'
                cur.execute(str)
                data = cur.fetchall()
                student_table.delete(*student_table.get_children())
                for i in data:
                    list_values = [i[0], i[1], i[2], i[3], i[4], i[5], i[6]]
                    student_table.insert('', END, values=list_values)
                messagebox.showinfo('notification', ' deleted successfully.',parent=admin_panel_root)

            def showall():
                student_table.delete(*student_table.get_children())
                str = 'select * from addstudent'
                cur.execute(str)
                data = cur.fetchall()
                for i in data:
                    list_values = [i[0], i[1], i[2], i[3], i[4], i[5], i[6]]
                    student_table.insert('', END, values=list_values)
            # def update_btn():
            #
            #     def update_record():
            #         roll_d = up_roll_val.get()
            #         name_d = up_name_val.get()
            #         sub1_d = up_sub1_val.get()
            #         sub2_d = up_sub2_val.get()
            #         sub3_d = up_sub3_val.get()
            #         sub4_d = up_sub4_val.get()
            #
            #
            #         str = 'update addstudent set name_d=%s,sub1_d=%s,sub2_d=%s,sub3_d=%s,sub4_d=%s where roll_d=%s'
            #         cur.execute(str, (name_d, sub1_d, sub2_d, sub3_d, sub4_d, roll_d))
            #         con.commit()
            #
            #         str = 'select * from addstudent'
            #         cur.execute(str)
            #         data = cur.fetchall()
            #
            #         student_table.delete(*student_table.get_children())
            #         for i in data:
            #             list_values = [i[0], i[1], i[2], i[3], i[4], i[5]]
            #             student_table.insert('', END, values=list_values)
            #
            #         messagebox.showinfo('notification', 'Data Updated')
            #         up_record_root.destroy()
            #
            #     up_record_root = Tk()
            #     up_record_root.title("update")
            #     up_record_root.geometry("550x400+500+200")
            #     up_record_root.resizable(False, False)
            #
            #     up_sub1_val = StringVar()
            #     up_sub2_val = StringVar()
            #     up_sub3_val = StringVar()
            #     up_sub4_val = StringVar()
            #     up_name_val = StringVar()
            #     up_roll_val = StringVar()
            #     # up_sub1_val.set(0)
            #     # up_sub2_val.set(0)
            #     # up_sub3_val.set(0)
            #     # up_sub4_val.set(0)
            #
            #     up_stu_name = Label(up_record_root, text="Name", font=('Arial', 12,), relief=GROOVE, borderwidth=3, bg="white",width=15)
            #     up_stu_name.place(x=20, y=10)
            #     up_stu_name = Entry(up_record_root, font=('Arial', 12,), relief=GROOVE, borderwidth=3, bg="white", width=15,textvariable=up_name_val)
            #     up_stu_name.place(x=230, y=10)
            #
            #     up_stu_roll = Label(up_record_root, text="Roll", font=('Arial', 12,), relief=GROOVE, borderwidth=3, bg="white",width=15)
            #     up_stu_roll.place(x=20, y=70)
            #     up_stu_roll = Entry(up_record_root, font=('Arial', 12,), relief=GROOVE, borderwidth=3, bg="white", width=15,textvariable=up_roll_val)
            #     up_stu_roll.place(x=230, y=70)
            #
            #     up_sub1 = Label(up_record_root, text="SUB-1", font=('Arial', 12,), relief=GROOVE, borderwidth=3, bg="white",width=15)
            #     up_sub1.place(x=20, y=130)
            #     up_sub1 = Entry(up_record_root, font=('Arial', 12,), relief=GROOVE, borderwidth=3, bg="white", width=15,textvariable=up_sub1_val)
            #
            #     # up_sub1.insert(0, up_sub1_val.get())
            #     up_sub1.place(x=230, y=130)
            #     up_sub1_btn = Button(up_record_root, text="ADD", font=('times', 10, 'bold'), relief=GROOVE, borderwidth=2,activebackground="white", activeforeground="blue", width=10)
            #     up_sub1_btn.place(x=400, y=130)
            #
            #     up_sub2 = Label(up_record_root, text="SUB-2", font=('Arial', 12,), relief=GROOVE, borderwidth=3, bg="white",width=15)
            #     up_sub2.place(x=20, y=190)
            #     up_sub2 = Entry(up_record_root, font=('Arial', 12,), relief=GROOVE, borderwidth=3, bg="white", width=15,textvariable=up_sub2_val)
            #     up_sub2.place(x=230, y=190)
            #     # up_sub2_btn = Button(up_record_root, text="ADD", font=('times', 10, 'bold'), relief=GROOVE, borderwidth=2,activebackground="white", activeforeground="blue", width=10)
            #     # up_sub2_btn.place(x=400, y=190)
            #
            #     up_sub3 = Label(up_record_root, text="SUB-3", font=('Arial', 12,), relief=GROOVE, borderwidth=3, bg="white",width=15)
            #     up_sub3.place(x=20, y=250)
            #     up_sub3 = Entry(up_record_root, font=('Arial', 12,), relief=GROOVE, borderwidth=3, bg="white", width=15,textvariable=up_sub3_val)
            #     up_sub3.place(x=230, y=250)
            #     # up_sub3_btn = Button(up_record_root, text="ADD", font=('times', 10, 'bold'), relief=GROOVE, borderwidth=2,activebackground="white", activeforeground="blue", width=10)
            #     # up_sub3_btn.place(x=400, y=250)
            #
            #     up_sub4 = Label(up_record_root, text="SUB-4", font=('Arial', 12,), relief=GROOVE, borderwidth=3, bg="white",width=15)
            #     up_sub4.place(x=20, y=310)
            #     up_sub4 = Entry(up_record_root, font=('Arial', 12,), relief=GROOVE, borderwidth=3, bg="white", width=15,textvariable=up_sub4_val)
            #     up_sub4.place(x=230, y=310)
            #     # up_sub4_btn = Button(up_record_root, text="ADD", font=('times', 10, 'bold'), relief=GROOVE, borderwidth=2,activebackground="white", activeforeground="blue", width=10)
            #     # up_sub4_btn.place(x=400, y=310)
            #
            #     up_record_btn = Button(up_record_root, text="UPDATE", font=('times', 15, 'bold'), relief=GROOVE,borderwidth=4, activebackground="white", activeforeground="blue", width=15,
            #                             command=update_record)
            #     up_record_btn.place(x=170, y=350)
            #
            #     cc = student_table.focus()
            #     content = student_table.item(cc)
            #     pp = content['values']
            #     if (len(pp) != 0):
            #         up_roll_val.set(pp[0])
            #         up_name_val.set(pp[1])
            #         up_sub1_val.set(pp[2])
            #         up_sub2_val.set(pp[3])
            #         up_sub3_val.set(pp[4])
            #         up_sub4_val.set(pp[5])

                # record_root.mainloop()

            def add_record_btn():
                def add_to_dataframe():
                    roll_d = roll_val.get()
                    name_d = name_val.get()
                    sub1_d = sub1_val.get()
                    sub2_d = sub2_val.get()
                    sub3_d = sub3_val.get()
                    sub4_d = sub4_val.get()
                    total= int(sub1_val.get()) + int(sub2_val.get()) + int(sub3_val.get()) + int(sub4_val.get())
                    sgpa = (total * 10) / 600
                    # print(sgpa)



                    try:
                        cur.execute("insert into addstudent values (%s,%s,%s,%s,%s,%s,%s)",
                                    (roll_d, name_d, sub1_d, sub2_d, sub3_d, sub4_d,sgpa))
                        res = messagebox.showinfo('notification', 'Added Successfully', parent=record_root)
                        con.commit()

                    except:
                        messagebox.showerror('notification', 'something goes wrong..', parent=record_root)


                    str = 'select * from addstudent'
                    cur.execute(str)
                    data = cur.fetchall()
                    student_table.delete(*student_table.get_children())
                    for i in data:
                        list_values = [i[0], i[1], i[2], i[3], i[4], i[5],i[6]]
                        student_table.insert('', END, values=list_values)

                def marksentry4():
                    add_marks_root4 = Toplevel()
                    add_marks_root4.grab_set()
                    add_marks_root4.geometry("280x200+1000+400")
                    add_marks_root4.title("Subject-4")
                    add_marks_root4.resizable(False, False)
                    add_marks_root4.config(bg="lightblue")
                    def cal4():

                        res1 = (int(mid1.get()) + int(mid2.get()) + int(attendance.get()) + int(prac.get()) + int(theory.get()))
                        sub4_val.set(res1)
                        sub4.delete(0, "end")
                        sub4.insert(0, sub4_val.get())
                        # print('sv',sub1_val.get())
                        add_marks_root4.destroy()


                    mid1 = Label(add_marks_root4, text="Midsem-1", font=('Arial', 8,), relief=GROOVE, borderwidth=3,
                                 bg="white", width=15)
                    mid1.place(x=20, y=20)
                    mid1 = Entry(add_marks_root4, font=('Arial', 8,), relief=GROOVE, borderwidth=3, bg="white", width=15)
                    mid1.place(x=150, y=20)

                    mid2 = Label(add_marks_root4, text="Midsem-2", font=('Arial', 8,), relief=GROOVE, borderwidth=3,
                                 bg="white",
                                 width=15)
                    mid2.place(x=20, y=50)
                    mid2 = Entry(add_marks_root4, font=('Arial', 8,), relief=GROOVE, borderwidth=3, bg="white", width=15)
                    mid2.place(x=150, y=50)

                    attendance = Label(add_marks_root4, text="Attendance", font=('Arial', 8,), relief=GROOVE, borderwidth=3,
                                       bg="white", width=15)
                    attendance.place(x=20, y=80)
                    attendance = Entry(add_marks_root4, font=('Arial', 8,), relief=GROOVE, borderwidth=3, bg="white",
                                       width=15)
                    attendance.place(x=150, y=80)

                    prac = Label(add_marks_root4, text="Practical", font=('Arial', 8,), relief=GROOVE, borderwidth=3,
                                 bg="white",
                                 width=15)
                    prac.place(x=20, y=110)
                    prac = Entry(add_marks_root4, font=('Arial', 8,), relief=GROOVE, borderwidth=3, bg="white", width=15)
                    prac.place(x=150, y=110)

                    theory = Label(add_marks_root4, text="Theory", font=('Arial', 8,), relief=GROOVE, borderwidth=3,bg="white",width=15)
                    theory.place(x=20, y=140)
                    theory = Entry(add_marks_root4, font=('Arial', 8,), relief=GROOVE, borderwidth=3, bg="white", width=15)
                    theory.place(x=150, y=140)

                    calculate_btn = Button(add_marks_root4, text="CALCULATE", font=('times', 10, 'bold'), relief=GROOVE,borderwidth=4,activebackground="white", activeforeground="blue", width=12, command=cal4)
                    calculate_btn.place(x=90, y=165)


                def marksentry3():
                    add_marks_root3 = Toplevel()
                    add_marks_root3.grab_set()
                    add_marks_root3.geometry("280x200+1000+400")
                    add_marks_root3.title("Subject-3")
                    add_marks_root3.resizable(False, False)
                    add_marks_root3.config(bg="lightblue")
                    def cal3():

                        res1 = (int(mid1.get()) + int(mid2.get()) + int(attendance.get()) + int(prac.get()) + int(theory.get()))
                        sub3_val.set(res1)
                        sub3.delete(0, "end")
                        sub3.insert(0, sub3_val.get())
                        # print('sv',sub1_val.get())
                        add_marks_root3.destroy()


                    mid1 = Label(add_marks_root3, text="Midsem-1", font=('Arial', 8,), relief=GROOVE, borderwidth=3,
                                 bg="white", width=15)
                    mid1.place(x=20, y=20)
                    mid1 = Entry(add_marks_root3, font=('Arial', 8,), relief=GROOVE, borderwidth=3, bg="white", width=15)
                    mid1.place(x=150, y=20)

                    mid2 = Label(add_marks_root3, text="Midsem-2", font=('Arial', 8,), relief=GROOVE, borderwidth=3,
                                 bg="white",
                                 width=15)
                    mid2.place(x=20, y=50)
                    mid2 = Entry(add_marks_root3, font=('Arial', 8,), relief=GROOVE, borderwidth=3, bg="white", width=15)
                    mid2.place(x=150, y=50)

                    attendance = Label(add_marks_root3, text="Attendance", font=('Arial', 8,), relief=GROOVE, borderwidth=3,
                                       bg="white", width=15)
                    attendance.place(x=20, y=80)
                    attendance = Entry(add_marks_root3, font=('Arial', 8,), relief=GROOVE, borderwidth=3, bg="white",
                                       width=15)
                    attendance.place(x=150, y=80)

                    prac = Label(add_marks_root3, text="Practical", font=('Arial', 8,), relief=GROOVE, borderwidth=3,
                                 bg="white",
                                 width=15)
                    prac.place(x=20, y=110)
                    prac = Entry(add_marks_root3, font=('Arial', 8,), relief=GROOVE, borderwidth=3, bg="white", width=15)
                    prac.place(x=150, y=110)

                    theory = Label(add_marks_root3, text="Theory", font=('Arial', 8,), relief=GROOVE, borderwidth=3,bg="white",width=15)
                    theory.place(x=20, y=140)
                    theory = Entry(add_marks_root3, font=('Arial', 8,), relief=GROOVE, borderwidth=3, bg="white", width=15)
                    theory.place(x=150, y=140)

                    calculate_btn = Button(add_marks_root3, text="CALCULATE", font=('times', 10, 'bold'), relief=GROOVE,borderwidth=4,activebackground="white", activeforeground="blue", width=12, command=cal3)
                    calculate_btn.place(x=90, y=165)


                def marksentry2():
                    add_marks_root2 = Toplevel()
                    add_marks_root2.grab_set()
                    add_marks_root2.geometry("280x200+1000+400")
                    add_marks_root2.title("Subject-2")
                    add_marks_root2.resizable(False, False)
                    add_marks_root2.config(bg="lightblue")
                    def cal2():

                        res1 = (int(mid1.get()) + int(mid2.get()) + int(attendance.get()) + int(prac.get()) + int(theory.get()))
                        sub2_val.set(res1)
                        sub2.delete(0, "end")
                        sub2.insert(0, sub2_val.get())
                        # print('sv',sub1_val.get())
                        add_marks_root2.destroy()


                    mid1 = Label(add_marks_root2, text="Midsem-1", font=('Arial', 8,), relief=GROOVE, borderwidth=3,
                                 bg="white", width=15)
                    mid1.place(x=20, y=20)
                    mid1 = Entry(add_marks_root2, font=('Arial', 8,), relief=GROOVE, borderwidth=3, bg="white", width=15)
                    mid1.place(x=150, y=20)

                    mid2 = Label(add_marks_root2, text="Midsem-2", font=('Arial', 8,), relief=GROOVE, borderwidth=3,
                                 bg="white",
                                 width=15)
                    mid2.place(x=20, y=50)
                    mid2 = Entry(add_marks_root2, font=('Arial', 8,), relief=GROOVE, borderwidth=3, bg="white", width=15)
                    mid2.place(x=150, y=50)

                    attendance = Label(add_marks_root2, text="Attendance", font=('Arial', 8,), relief=GROOVE, borderwidth=3,
                                       bg="white", width=15)
                    attendance.place(x=20, y=80)
                    attendance = Entry(add_marks_root2, font=('Arial', 8,), relief=GROOVE, borderwidth=3, bg="white",
                                       width=15)
                    attendance.place(x=150, y=80)

                    prac = Label(add_marks_root2, text="Practical", font=('Arial', 8,), relief=GROOVE, borderwidth=3,
                                 bg="white",
                                 width=15)
                    prac.place(x=20, y=110)
                    prac = Entry(add_marks_root2, font=('Arial', 8,), relief=GROOVE, borderwidth=3, bg="white", width=15)
                    prac.place(x=150, y=110)

                    theory = Label(add_marks_root2, text="Theory", font=('Arial', 8,), relief=GROOVE, borderwidth=3,
                                   bg="white",
                                   width=15)
                    theory.place(x=20, y=140)
                    theory = Entry(add_marks_root2, font=('Arial', 8,), relief=GROOVE, borderwidth=3, bg="white", width=15)
                    theory.place(x=150, y=140)

                    calculate_btn = Button(add_marks_root2, text="CALCULATE", font=('times', 10, 'bold'), relief=GROOVE,
                                           borderwidth=4,
                                           activebackground="white", activeforeground="blue", width=12, command=cal2)
                    calculate_btn.place(x=90, y=165)


                def marksentry1():

                    add_marks_root = Toplevel()
                    add_marks_root.grab_set()
                    add_marks_root.geometry("280x200+1000+400")
                    add_marks_root.title("Subject-1")
                    add_marks_root.resizable(False, False)
                    add_marks_root.config(bg="lightblue")


                    def cal1():
                        res1 = (int(mid1.get()) + int(mid2.get()) + int(attendance.get()) + int(prac.get()) + int(theory.get()))
                        # print('rs',res1)
                        # print('sv', sub1_val.get())
                        sub1_val.set(res1)
                        sub1.delete(0, "end")
                        sub1.insert(0, sub1_val.get())
                        add_marks_root.destroy()
                        # print('sv',sub1_val.get())

                    mid1 = Label(add_marks_root, text="Midsem-1", font=('Arial', 8,), relief=GROOVE, borderwidth=3,bg="white",width=15)
                    mid1.place(x=20, y=20)
                    mid1 = Entry(add_marks_root, font=('Arial', 8,), relief=GROOVE, borderwidth=3, bg="white", width=15)
                    mid1.place(x=150, y=20)

                    mid2 = Label(add_marks_root, text="Midsem-2", font=('Arial', 8,), relief=GROOVE, borderwidth=3,
                                 bg="white",
                                 width=15)
                    mid2.place(x=20, y=50)
                    mid2 = Entry(add_marks_root, font=('Arial', 8,), relief=GROOVE, borderwidth=3, bg="white", width=15)
                    mid2.place(x=150, y=50)


                    attendance = Label(add_marks_root, text="Attendance", font=('Arial', 8,), relief=GROOVE, borderwidth=3,
                                       bg="white", width=15)
                    attendance.place(x=20, y=80)
                    attendance = Entry(add_marks_root, font=('Arial', 8,), relief=GROOVE, borderwidth=3, bg="white",
                                       width=15)
                    attendance.place(x=150, y=80)

                    prac = Label(add_marks_root, text="Practical", font=('Arial', 8,), relief=GROOVE, borderwidth=3,
                                 bg="white",
                                 width=15)
                    prac.place(x=20, y=110)
                    prac = Entry(add_marks_root, font=('Arial', 8,), relief=GROOVE, borderwidth=3, bg="white", width=15)
                    prac.place(x=150, y=110)

                    theory = Label(add_marks_root, text="Theory", font=('Arial', 8,), relief=GROOVE, borderwidth=3,
                                   bg="white",
                                   width=15)
                    theory.place(x=20, y=140)
                    theory = Entry(add_marks_root, font=('Arial', 8,), relief=GROOVE, borderwidth=3, bg="white", width=15)
                    theory.place(x=150, y=140)

                    calculate_btn = Button(add_marks_root, text="CALCULATE", font=('times', 10, 'bold'), relief=GROOVE,
                                           borderwidth=4,
                                           activebackground="white", activeforeground="blue", width=12, command=cal1)
                    calculate_btn.place(x=90, y=165)
                record_root = Tk()
                record_root.title("student")
                record_root.geometry("550x400+500+200")
                record_root.resizable(False, False)

                sub1_val = tk.StringVar()
                sub2_val = StringVar()
                sub3_val = StringVar()
                sub4_val = StringVar()
                name_val = StringVar()
                roll_val = StringVar()
                sub1_val.set(0)
                sub2_val.set(0)
                sub3_val.set(0)
                sub4_val.set(0)
                #
                # print('sv-out', sub1_val.get())
                # print('sv-out', sub2_val.get())
                # print('sv-out', sub3_val.get())
                # print('sv-out', sub4_val.get())
                stu_name = Label(record_root, text="Name", font=('Arial', 12,), relief=GROOVE, borderwidth=3, bg="white", width=15)
                stu_name.place(x=20, y=10)
                stu_name = Entry(record_root, font=('Arial', 12,), relief=GROOVE, borderwidth=3, bg="white", width=15, textvariable=name_val)
                stu_name.place(x=230, y=10)

                stu_roll = Label(record_root, text="Roll", font=('Arial', 12,), relief=GROOVE, borderwidth=3, bg="white", width=15)
                stu_roll.place(x=20, y=70)
                stu_roll = Entry(record_root, font=('Arial', 12,), relief=GROOVE, borderwidth=3, bg="white", width=15,textvariable=roll_val)
                stu_roll.place(x=230, y=70)

                sub1 = Label(record_root, text="SUB-1", font=('Arial', 12,), relief=GROOVE, borderwidth=3, bg="white",width=15)
                sub1.place(x=20, y=130)
                sub1 = Entry(record_root, font=('Arial', 12,), relief=GROOVE, borderwidth=3, bg="white", width=15,textvariable=sub1_val)
                sub1.insert(0,sub1_val.get())
                sub1.place(x=230, y=130)
                sub1_btn = Button(record_root, text="ADD", font=('times', 10, 'bold'), relief=GROOVE, borderwidth=2,activebackground="white", activeforeground="blue", width=10, command=marksentry1)
                sub1_btn.place(x=400, y=130)

                sub2 = Label(record_root, text="SUB-2", font=('Arial', 12,), relief=GROOVE, borderwidth=3, bg="white",width=15)
                sub2.place(x=20, y=190)
                sub2 = Entry(record_root, font=('Arial', 12,), relief=GROOVE, borderwidth=3, bg="white", width=15,textvariable=sub2_val)
                sub2.insert(0, sub1_val.get())
                sub2.place(x=230, y=190)
                sub2_btn = Button(record_root, text="ADD", font=('times', 10, 'bold'), relief=GROOVE, borderwidth=2,activebackground="white", activeforeground="blue", width=10,command=marksentry2)
                sub2_btn.place(x=400, y=190)

                sub3 = Label(record_root, text="SUB-3", font=('Arial', 12,), relief=GROOVE, borderwidth=3, bg="white",width=15)
                sub3.place(x=20, y=250)
                sub3 = Entry(record_root, font=('Arial', 12,), relief=GROOVE, borderwidth=3, bg="white", width=15,textvariable=sub3_val)
                sub3.insert(0, sub1_val.get())
                sub3.place(x=230, y=250)
                sub3_btn = Button(record_root, text="ADD", font=('times', 10, 'bold'), relief=GROOVE, borderwidth=2,activebackground="white", activeforeground="blue", width=10,command=marksentry3)
                sub3_btn.place(x=400, y=250)

                sub4 = Label(record_root, text="SUB-4", font=('Arial', 12,), relief=GROOVE, borderwidth=3, bg="white",width=15)
                sub4.place(x=20, y=310)
                sub4 = Entry(record_root, font=('Arial', 12,), relief=GROOVE, borderwidth=3, bg="white", width=15,textvariable=sub4_val)
                sub4.insert(0, sub1_val.get())
                sub4.place(x=230, y=310)
                sub4_btn = Button(record_root, text="ADD", font=('times', 10, 'bold'), relief=GROOVE, borderwidth=2,activebackground="white", activeforeground="blue", width=10,command=marksentry4)
                sub4_btn.place(x=400, y=310)

                add_record_btn = Button(record_root, text="ADD RECORD", font=('times', 15, 'bold'), relief=GROOVE,borderwidth=4,activebackground="white", activeforeground="blue", width=15,command=add_to_dataframe)
                add_record_btn.place(x=170, y=350)

                record_root.mainloop()

            admin_panel_root = Toplevel()
            admin_panel_root.grab_set()
            admin_panel_root.geometry("1100x700+200+50")
            admin_panel_root.title("Admin Panel")
            admin_panel_root.resizable(False, False)
            admin_panel_root.config(bg="lightblue")


            ad_login_root.destroy()

            # ----------------------------------------------------------------------------------------------------------------------
            # -----------------------------------------------SHOW DATA FRAME--------------------------------------------------------

            showdataframe = Frame(admin_panel_root, bg='white', relief=GROOVE, borderwidth=5)
            showdataframe.place(x=0, y=0, width=1100, height=650)

            style = ttk.Style()
            style.configure('Treeview.Heading', font=('times', 15, 'bold'), background='Silver')
            style.configure('Treeview', font=('arial', 15), background='Silver', foreground='black')
            scroll_x = Scrollbar(showdataframe, orient=HORIZONTAL)
            scroll_y = Scrollbar(showdataframe, orient=VERTICAL)
            student_table = Treeview(showdataframe, column=(
            'Roll', 'Name', 'Sub-1', 'Sub-2', 'Sub-3', 'Sub-4','SGPA'), yscrollcommand=scroll_y.set,
                                     xscrollcommand=scroll_x.set)

            scroll_x.pack(side=BOTTOM, fill=X)
            scroll_y.pack(side=RIGHT, fill=Y)
            scroll_x.config(command=student_table.xview)
            scroll_y.config(command=student_table.yview)
            student_table.heading('Roll', text='Roll')
            student_table.heading('Name', text='Name')
            student_table.heading('Sub-1', text='Sub-1')
            student_table.heading('Sub-2', text='Sub-2')
            student_table.heading('Sub-3', text='Sub-3')
            student_table.heading('Sub-4', text='Sub-4')
            student_table.heading('SGPA', text='SGPA')
            student_table['show'] = "headings"

            # ----------to change the size of the given columns----
            student_table.column("Roll", width=100)
            student_table.column("Name", width=200)
            student_table.column("Sub-1", width=100)
            student_table.column("Sub-2", width=100)
            student_table.column("Sub-3", width=100)
            student_table.column("Sub-4", width=100)
            student_table.column("SGPA", width=100)
            # ------------------------------------------------------
            student_table.pack(fill=BOTH, expand=1)

            # >--------------------------------------- DATA ENTRY FRAMES------------------------------------------------------------------------
            dataentryframe = Frame(admin_panel_root, bg='white', relief=GROOVE, borderwidth=5)
            dataentryframe.place(x=0, y=650, width=1100, height=80)

            # =-----------------DATA ENTRY FRAME------------------
            d1 = Button(dataentryframe, text="Add Record", font=('times', 12, 'bold'), relief=GROOVE, borderwidth=5,
                        activebackground="white", activeforeground="blue", width=15, command=add_record_btn)
            d1.place(x=10, y=5)

            d2 = Button(dataentryframe, text="Search Record", font=('times', 12, 'bold'), relief=GROOVE, borderwidth=5,
                        activebackground="white", activeforeground="blue", width=15)
            d2.place(x=160, y=5)

            d3 = Button(dataentryframe, text="Delete", font=('times', 12, 'bold'), relief=GROOVE, borderwidth=5,
                        activebackground="white", activeforeground="blue", width=15,command=delete_rec)
            d3.place(x=310, y=5)

            # d4 = Button(dataentryframe, text="Update Record", font=('times', 12, 'bold'), relief=GROOVE, borderwidth=5,
            #             activebackground="white", activeforeground="blue", width=15,command=update_btn)
            # d4.place(x=460, y=5)

            d5 = Button(dataentryframe, text="Show All", font=('times', 12, 'bold'), relief=GROOVE, borderwidth=5,
                        activebackground="white", activeforeground="blue", width=15,command=showall)
            d5.place(x=610, y=5)

            d6 = Button(dataentryframe, text="Export Data", font=('times', 12, 'bold'), relief=GROOVE, borderwidth=5,
                        activebackground="white", activeforeground="blue", width=15,command=exportdata)
            d6.place(x=760, y=5)

            d7 = Button(dataentryframe, text="Exit", font=('times', 12, 'bold'), relief=GROOVE, borderwidth=5,
                        activebackground="white", activeforeground="blue", width=15,command=exit_admin_panel)
            d7.place(x=910, y=5)
        else:
            messagebox.showerror('notification', 'Invalid username or password',parent=ad_login_root)

        # ----------------------------------------------------------------------------------------------------------------------

    ad_login_root = Toplevel()
    ad_login_root.grab_set()
    ad_login_root.geometry("400x200+530+300")
    ad_login_root.title("login")
    ad_login_root.resizable(False, False)
    ad_login_root.config(bg="lightblue")

    #     --------------------------------connect db labels------------------------------
    user = "arsha"
    passcode = "sharma"

    admin_username = Label(ad_login_root, text="USERNAME:", font=('Arial', 12,), relief=GROOVE, borderwidth=3,bg="white", width=15)
    admin_username.place(x=10, y=10)
    adminval = StringVar()
    adminval.set("username")
    adminentry = Entry(ad_login_root, font=('Arial', 12,), relief=GROOVE, borderwidth=3, bg="white", width=15,textvariable=adminval)
    adminentry.place(x=230, y=10)

    admin_pass = Label(ad_login_root, text="PASSWORD", font=('Arial', 12,), relief=GROOVE, borderwidth=3, bg="white",width=15)
    admin_pass.place(x=10, y=70)
    pass_val = StringVar()
    passentry = Entry(ad_login_root, font=('Arial', 12,), relief=GROOVE, borderwidth=3, bg="white", width=15,textvariable=pass_val)
    passentry.place(x=230, y=70)

    submit = Button(ad_login_root, text="SUBMIT", font=('times', 10, 'bold'), relief=GROOVE, borderwidth=5,activebackground="white", activeforeground="blue", command=submit_admin_login)
    submit.place(x=160, y=130)

    ad_login_root.mainloop()


from tkinter import *
import time
from tkinter import Toplevel,messagebox,filedialog
from tkinter.ttk import Treeview
from tkinter import ttk
import tkinter as tk
import pymysql
import pandas
import tkinter as tk
from PIL import ImageTk, Image


# -------------DATABASE CONNECTION---------------------------

con=pymysql.connect(host="localhost",user="root",password="",database="tnp")
cur=con.cursor()
print("connection established")
# ----==================================================================

root= Tk()
root.title("Academic Performance")
root.geometry("1100x700+200+50")
root.resizable(False,False)
root.config(bg="silver")

bgimg = "res4.jpg"

#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
img = ImageTk.PhotoImage(Image.open(bgimg))

#The Label widget is a standard Tkinter widget used to display a text or image on the screen.
panel = tk.Label(root, image = img)
panel.pack()

admin_login_btn=Button(root,text="Admin Login",font=('times',18,'bold'),relief=GROOVE,borderwidth=5,activebackground= "white",activeforeground="blue",width=20,command=adminlogin)
admin_login_btn.place(x=200,y=600)

exit_btn=Button(root,text="Exit",font=('times',18,'bold'),relief=GROOVE,borderwidth=5,activebackground= "white",activeforeground="blue",width=20 , command=exit_window)
exit_btn.place(x=600,y=600)

root.mainloop()

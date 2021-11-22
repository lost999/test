import tkinter as tk

if __name__ == '__main__':
    window = tk.Tk()
    window.title("用户注册")
    window.geometry("260x240")
    text_a = tk.Label(window, text="用户注册",font=("微软雅黑",16),).grid(row=0,column=1,rowspan=2,columnspan=2)

    x_b=tk.StringVar()
    text_b = tk.Label(window, text="学号",background="#FF1493",width=10,height=1,font=("微软雅黑",8)).grid(row=2,column=1,padx=2,pady=2)
    asd_b = tk.Entry(textvariable=x_b,bg="#FF1493").grid(row=2,column=2)

    x_c = tk.StringVar()
    text_c = tk.Label(window, text="姓名",background="#FF1493",width=10,height=1,font=("微软雅黑",8)).grid(row=3, column=1,padx=2,pady=2)
    asd_c = tk.Entry(textvariable=x_c,bg="#FF1493").grid(row=3, column=2)

    x_d = tk.StringVar()
    text_d = tk.Label(window, text="性别",background="#FF1493",width=10,height=1,font=("微软雅黑",8)).grid(row=4, column=1,padx=2,pady=2)
    asd_d = tk.Entry(textvariable=x_d,bg="#FF1493").grid(row=4, column=2)

    x_e = tk.StringVar()
    text_e = tk.Label(window, text="班级",background="#FF1493",width=10,height=1,font=("微软雅黑",8)).grid(row=5, column=1,padx=2,pady=2)
    asd_e = tk.Entry(textvariable=x_e,bg="#FF1493").grid(row=5, column=2)

    x_f = tk.StringVar()
    text_f = tk.Label(window, text="电话",background="#FF1493",width=10,height=1,font=("微软雅黑",8)).grid(row=6, column=1,padx=2,pady=2)
    asd_f = tk.Entry(textvariable=x_f,bg="#FF1493").grid(row=6, column=2)

    def say_st():
        b = x_b.get()
        c = x_c.get()
        d = x_d.get()
        e = x_e.get()
        f = x_f.get()
        print("学号:", b)
        print("姓名:", c)
        print("性别:", d)
        print("班级:", e)
        print("学号:", f)
        print("\t")

    button_a = tk.Button(window, text="注册", command=say_st,anchor="s",bg="#FF1493",width=10,font=("微软雅黑",10)).grid(row=7,column=1,rowspan=1,columnspan=2,sticky=tk.W)
    button_b = tk.Button(window, text="取消", command=window.destroy,anchor="s",bg="#FF1493",width=10,font=("微软雅黑",10)).grid(row=7,column=1,rowspan=1,columnspan=2,sticky=tk.E)
    window.mainloop()
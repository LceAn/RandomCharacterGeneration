# -*-  coding : utf-8 -*-
# @Time : 2023/2/15 18:48
# @Autor : LceAn
# @File : PassRandom-Gui.py
# @Software : PyCharm

# 封装成一个图形化程序
import tkinter as tk
import random
import string


class App:
    def __init__(self, master):
        self.master = master
        self.master.title("强密码生成器")
        self.master.resizable(False, False)

        # 设置默认值
        self.length = tk.StringVar(value="12")
        self.include_uppercase = tk.BooleanVar(value=True)
        self.include_special_chars = tk.BooleanVar(value=True)
        self.include_digits = tk.BooleanVar(value=True)
        self.random_string = tk.StringVar(value="")

        # 设置界面
        tk.Label(self.master, text="强密码生成器", font=("Arial", 16, "bold")).grid(row=0, column=0, columnspan=2,
                                                                                        pady=(20, 10))
        tk.Label(self.master, text="长度：").grid(row=1, column=0, sticky="w", padx=10, pady=5)
        tk.Entry(self.master, textvariable=self.length, width=10).grid(row=1, column=1, sticky="w", padx=10, pady=5)
        tk.Checkbutton(self.master, text="包含大小写字母", variable=self.include_uppercase).grid(row=2, column=0,
                                                                                                 columnspan=2, padx=10,
                                                                                                 pady=5, sticky="w")
        tk.Checkbutton(self.master, text="包含特殊字符", variable=self.include_special_chars).grid(row=3, column=0,
                                                                                                   columnspan=2,
                                                                                                   padx=10, pady=5,
                                                                                                   sticky="w")
        tk.Checkbutton(self.master, text="包含数字", variable=self.include_digits).grid(row=4, column=0, columnspan=2,
                                                                                        padx=10, pady=5, sticky="w")
        tk.Button(self.master, text="生成随机强密码", command=self.generate_random_string).grid(row=5, column=0,
                                                                                                columnspan=2, pady=20)
        tk.Label(self.master, text="随机强密码为：").grid(row=6, column=0, sticky="w", padx=10)
        tk.Entry(self.master, textvariable=self.random_string, width=30, state="readonly").grid(row=6, column=1,
                                                                                                sticky="w")

    def generate_random_string(self):
        try:
            length = int(self.length.get())
        except ValueError:
            length = 12

        include_uppercase = self.include_uppercase.get()
        include_special_chars = self.include_special_chars.get()
        include_digits = self.include_digits.get()

        letters = string.ascii_lowercase
        if include_uppercase:
            letters += string.ascii_uppercase
        if include_special_chars:
            letters += string.punctuation
        if include_digits:
            letters += string.digits

        self.random_string.set(''.join(random.choices(letters, k=length)))


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()

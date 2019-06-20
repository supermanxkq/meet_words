"""
自动生成会标的工具。
思路：
1.桌面应用程序
2.输入框输入会议标题
3.获取输入标题设置会标
4.预览
5.生成图片文件

"""
from PIL import Image, ImageDraw, ImageFont
import tkinter as tk
import re

# 策是非颠倒沙发的方法,阿斯顿飞的撒,阿斯顿发送到发暗示法安德森


class Windows(tk.Frame):

    #默认构造方法
    def __init__(self,master=None):
        tk.Frame.__init__(self, master)
        self.master.geometry('450x300')
        self.master.title('生成会标')
        self.create_widgets()
        self.master.mainloop()


    #创建组件
    def create_widgets(self):
        tk.Label(self.master, text='输入文字逗号隔开:').place(x=50, y=150)
        self.var_title_name = tk.StringVar()
        self.entry_title_name = tk.Entry(self.master, textvariable=self.var_title_name)
        self.entry_title_name.place(x=160, y=150)
        tk.Button(self.master, text="生成会标", command=self.generate_title, activeforeground='red', foreground='red').place(
            x=200,
            y=200)

    #绘制图片
    @staticmethod
    def draw_image(new_img, texts_value, show_image=False):
        draw = ImageDraw.Draw(new_img)
        img_size = new_img.size

        # 设置字体大小
        font_size = 120
        fnt = ImageFont.truetype('kaiticu.ttf', font_size)
        y = 150
        for i in range(0, len(texts_value)):
            x = (img_size[0] - fnt.getsize(texts_value[i])[0]) / 2
            draw.text((x, y), texts_value[i], font=fnt, fill=(255, 255, 0))
            y += 150

        if show_image:
            new_img.show()
        del draw

    #创建新的图片
    def new_image(self, width, height, text='default', color="#ea0909", show_image=False):
        new_img = Image.new('RGBA', (int(width), int(height)), color)
        self.draw_image(new_img, text, show_image)
        new_img.save(r'%s_%s_%s.png' % (width, height, text))
        del new_img

    #生成会标
    def generate_title(self):
        texts = re.split('[，,]', self.var_title_name.get())
        self.new_image(1600, 900, texts, show_image=False)


# 实例化对象
new_window = Windows()
# 测试 中华人民共和国，第十三届全国代表大会，暨全球贸易交流博览会宣讲

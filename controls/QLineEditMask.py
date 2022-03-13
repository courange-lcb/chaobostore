# 使用掩码限制QLineEdit控件的输入
"""
A    ASCⅡ字母字符是必须输入的(A-Z、a-z)
a    ASCⅡ字母字符是允许输入的，但不是必需的(A-Z、a-z)
N    ASCⅡ字母字符是必须输入的(A-Z、a-z、0-9)
n    ASCⅡ字母的允许输入的，但不是必需的(A-Z、a-z、0-9)
X    任何字符都是必须输入的
x    任何字符都是允许输入的，但不是必需的
9    ASCⅡ数字字符是必须输入的(0-9)
0    ASCⅡ数字字符是允许输入的，但不是必需的(0-9)
D    ASCⅡ数字字符是必须输入的(1-9)
d    ASCⅡ数字字符是允许输入的，但不是必需的(1-9)
#    ASCⅡ数字字符或加减符号是允许输入的，但不是必需的
H    十六进制格式字符是必须输入的(A-F、a-f、0-9)
h    十六进制格式字符是允许输入的，但不是必需的(A-F、a-f、0-9)
B    二进制格式字符是必须输入 的(0,1)
b    二进制格式字符是允许输入的，但不是必需的(0,1)
>    所有的字母字符都大写
<    所有的字母字符都小写
!    关闭大小写转换
\    使用"\"转义上面列出的字符
"""
import sys
from PyQt5.QtWidgets import *

# 从QWidget窗口类里面继承
class QLineEditMask(QWidget):
    def __init__(self):
        super(QLineEditMask,self).__init__()
        self.initUI()

    # 规范代码，初始化直接写在一个方法里
    def initUI(self):
        # 设置窗口的标题
        self.setWindowTitle('用掩码限制QLineEdit控件的输入')
        # 创建表单布局
        formLayout = QFormLayout()

        # 创建四个控件
        # 第一个，IP控件   192.168.11.11
        ipLineEdit = QLineEdit()
        # 第二个 mac地址 （mac地址也叫物理地址和局域网地址，主要用于确认网上设备的地址，类似于身份证号，具有唯一标识）
        # 如：00-16-EA-AE-3C-40就是一个MAC地址
        macLineEdit = QLineEdit()
        # 第三个 显示日期控件
        dataLineEdit = QLineEdit()
        # 第四个 许可证
        licenseLineEdit = QLineEdit()

        # 设置掩码，通过setInputMask方法
        ipLineEdit.setInputMask('000.000.000.000;_')   # 后面分号指如果没有输入时，显示为"_"
        macLineEdit.setInputMask('HH:HH:HH:HH:HH:HH;_')
        dataLineEdit.setInputMask('0000-00-00')
        licenseLineEdit.setInputMask('>AAAAA-AAAAA-AAAAA-AAAAA-AAAAA;#')   # 后面# 号指如果没有输入时，显示为"#"

        # 把这四个控件都添加到表单布局里面
        formLayout.addRow('数字掩码',ipLineEdit)
        formLayout.addRow('Mac掩码',macLineEdit)
        formLayout.addRow('日期掩码',dataLineEdit)
        formLayout.addRow("许可证掩码",licenseLineEdit)

        # 应用于表单布局
        self.setLayout(formLayout)

# 防止别的脚本调用，只有自己单独运行时，才会调用下面代码
if __name__ == '__main__':
    # 创建app实例，并传入参数
    app= QApplication(sys.argv)
    # 创建对象
    main = QLineEditMask()
    # 创建窗口
    main.show()
    # 进入程序的主循环，并通过exit函数，确保主循环安全结束(该释放资源的释放资源)
    sys.exit(app.exec_())


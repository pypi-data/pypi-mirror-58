使用 cando 编程
===
# 一 简介

cando 是基于 Python3 编写的模块，通过几个简单的函数便可以完成和 usb 转 can 模块（Cando 或者 Cando_pro）的通信，进行高效的 CAN 工具开发。

cando 后台 usb 通信基于 libusb 进行的，所以使用前请首先安装 libusb 驱动。

**Windows** 推荐使用 Zadig 工具进行安装。

1. 下载 [Zadig](https://zadig.akeo.ie/)
2. 将 Cando 或 Cando_pro 连接电脑
3. 双击运行 zadig-x.x.exe
4. 点击菜单栏中的 `Options` -> `List All Devices` 然后点击菜单栏下方的下拉列表，选择 Cando 或 Cando_pro
5. 选择下方的驱动为 libusb-win32 ，然后点击 `Replace Driver` ，等待安装完成即可

**Linux** Ubuntu18.04 默认已安装 libusb 无需安装，其他发行版本请根据情况自行安装。

好的，下面开始编写代码。

# 二 列出连接的设备

```py
import sys
from cando import *

# 获取设备列表
dev_lists = list_scan()

# 打印扫描到的Cando或Cando_pro的设备序列号
if len(dev_lists):
    for dev in dev_lists:
        serial_number = dev_get_serial_number_str(dev)
        dev_info = dev_get_dev_info_str(dev)
        print("Serial Number: " + serial_number + ', Dev Info: ' + dev_info)
else:
    sys.exit(0)
```

# 三 发送数据帧

```py
import sys
from cando import *

# 获取设备列表
dev_lists = list_scan()

# 判断是否发现设备
if len(dev_lists) == 0:
    print("Device not found!")
    sys.exit(0)

# 设置波特率：500K 采样点：87.5%
dev_set_timing(dev_lists[0], 1, 12, 2, 1, 6)

# 启动设备
dev_start(dev_lists[0], 0)

# 设置发送的数据帧
send_frame = Frame()
send_frame.is_extend = 0
send_frame.is_rtr = 0
send_frame.can_id = 0x12
send_frame.can_dlc = 8
send_frame.data = [0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08]

# 发送数据帧
dev_frame_send(dev_lists[0], send_frame)

# 停止设备
dev_stop(dev_lists[0])
```

# 四 接收数据帧

```py
import sys
from cando import *

# 获取设备列表
dev_lists = list_scan()

# 判断是否发现设备
if len(dev_lists) == 0:
    print("Device not found!")
    sys.exit(0)

# 设置波特率：500K 采样点：87.5%
dev_set_timing(dev_lists[0], 1, 12, 2, 1, 6)

# 启动设备
dev_start(dev_lists[0], 0)

# 创建接收数据帧
rec_frame = Frame()

# 阻塞读取帧数据
print("Reading...")
while True:
    if dev_frame_read(dev_lists[0], rec_frame, 10):
        break

print("Rec Frame: ")
print("    is_extend    " + str(rec_frame.is_extend))
print("    is_rtr       " + str(rec_frame.is_rtr))
print("    can_id       " + str(rec_frame.can_id))
print("    can_dlc      " + str(rec_frame.can_dlc))
print("    data         " + str(rec_frame.data))
print("    timestamp_us " + str(rec_frame.timestamp_us))

# 停止设备
dev_stop(dev_lists[0])
```

# 参考

zadig: https://zadig.akeo.ie/
libusb: http://www.libusb.org
libusb-win32: http://www.libusb.org/wiki/libusb-win32
USB: http://www.usb.org
Python: http://www.python.org
# zeroinger
提升编码效率，有效延长程序猿寿命的小工具集
## 目录
* 安装
  * 依赖条件
  * pip3安装
* 使用方法
    * 时间相关
    * Excel/CSV读写
    * 配置文件读取
    * 文本文件读写
* 更新日志
## 安装
### 依赖条件
* python>=3.6.0
* logzero==1.5.0
### pip3安装
```
pip3 install --upgrade zeroinger
```
## 使用方法
### 时间相关
#### StopWatch
```
from zeroinger.time.stopwatch import StopWatch
import time

timer = StopWatch.create_instance()
time.sleep(1)
print(timer.snapshot())
time.sleep(1)
print(timer.duriation())
timer.reset()
time.sleep(1)
print(timer.duriation())
pass
#--------------------------------
1000
2002
1003
```
### Excel/CSV相关
#### XLSX
##### 读取excel
```
from zeroinger.excel.xlsx import XLSX
test_read_file_path = os.path.join(os.path.dirname(__file__), 'read_test_file.xlsx')
data = XLSX.read_dict_sheet(test_read_file_path, 0)
print(data)
#--------------
[{'列1': 1, '列2': 4, '列3': 7}, {'列1': 2, '列2': 5, '列3': 8}, {'列1': 3, '列2': 6, '列3': 9}]
```
##### 写入excel
```
from zeroinger.excel.xlsx import XLSX
golden = [{'列1': 1, '列2': 4, '列3': 7}, {'列1': 2, '列2': 5, '列3': 8}, {'列1': 3, '列2': 6, '列3': 9}]
test_write_file_path = os.path.join(os.path.dirname(__file__), 'write_test_file.xlsx')
XLSX.write_dict_sheet(test_write_file_path, golden)
```
## 更新日志
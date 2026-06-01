# 电表OCR批量识别工具

基于 PaddleOCR 的本地AI识别工具，批量处理电表照片，自动提取站址编码和电流值，输出Excel表格。

## 功能特点

- ✅ **完全本地运行**：无需联网，保护数据隐私
- ✅ **批量处理**：自动扫描所有子文件夹
- ✅ **智能识别**：自动提取站址编码（440开头）和电流值
- ✅ **日期命名**：输出文件自动命名为 `YYYYMMDDHHMMSS.xlsx`
- ✅ **中文优化**：基于百度PaddleOCR，中文识别效果最佳

## 项目结构

```
MeterOCR-Project/
├── main.py              # 主程序
├── meter_ocr.spec       # PyInstaller打包配置
├── requirements.txt     # Python依赖
├── README.md            # 项目说明
├── LICENSE              # 开源协议
├── .gitignore           # Git忽略文件
├── build/               # 打包临时文件（自动生成）
├── dist/                # 打包输出目录（自动生成）
└── 示例文件夹/           # 放置电表照片的文件夹
    ├── 站点A/
    │   ├── 电表1.jpg
    │   └── 电表2.jpg
    └── 站点B/
        └── 电表3.jpg
```

## 快速开始

### 方法一：直接运行Python（开发者）

```bash
# 1. 克隆项目
git clone https://github.com/yourusername/MeterOCR-Project.git
cd MeterOCR-Project

# 2. 安装依赖
pip install -r requirements.txt

# 3. 创建文件夹并放入照片
mkdir 示例文件夹
# 将电表照片放入"示例文件夹"中

# 4. 运行
python main.py
```

### 方法二：使用打包好的EXE（推荐）

1. 下载 `MeterOCR.exe`
2. 在EXE同级目录创建文件夹，放入电表照片
3. 双击运行 `MeterOCR.exe`
4. 自动在当前目录生成 `20260104152119.xlsx` 等结果文件

## 打包成EXE

详细步骤请参考 [打包教程](打包教程.md)

快速打包：
```bash
pip install pyinstaller
pyinstaller meter_ocr.spec
```

打包完成后，EXE文件位于 `dist/MeterOCR.exe`

## 输出格式

| 文件夹 | 站址编码 | 电流值(A) | 文件名 | 识别状态 |
|--------|----------|-----------|--------|----------|
| 站点A | 440923908000000050 | 5.33 | 电表1.jpg | ✓ |
| 站点A | 440923908000000050 | 4.79 | 电表2.jpg | ✓ |
| 站点B | 440923908000000051 | 3.21 | 电表3.jpg | ✓ |

## 系统要求

- Windows 10/11
- 4GB+ 内存
- 2GB+ 硬盘空间

## 依赖

- Python 3.8+
- PaddleOCR 2.7+
- PaddlePaddle 2.5+
- openpyxl 3.1+

## 许可证

MIT License

## 致谢

- [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) - 百度开源OCR框架

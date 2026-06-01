# -*- mode: python ; coding: utf-8 -*-
"""
PyInstaller 打包配置文件
用于将Python程序打包成独立的EXE可执行文件
"""

import sys
from pathlib import Path

# 项目根目录
project_root = Path(SPECPATH)

# 分析主程序
a = Analysis(
    ['main.py'],                                    # 主程序入口
    pathex=[str(project_root)],                     # 项目路径
    binaries=[],                                    # 额外的二进制文件
    datas=[],                                       # 额外的数据文件
    hiddenimports=[                                 # 隐藏导入
        'paddle',
        'paddleocr',
        'paddleocr.ppstructure',
        'paddleocr.ppocr',
        'paddleocr.ppocr.utils',
        'openpyxl',
        'openpyxl.styles',
        'skimage',
        'skimage.filters',
        'skimage.morphology',
        'skimage.measure',
        'shapely',
        'shapely.geometry',
        'pyclipper',
        'lmdb',
        'tqdm',
        'visualdl',
        ' paddlenlp',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=None,
    noarchive=False,
)

# 创建PYZ归档
pyz = PYZ(a.pure, a.zipped_data, cipher=None)

# 创建可执行文件
exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='MeterOCR',                                # EXE文件名
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,                                       # 使用UPX压缩
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,                                   # 显示控制台窗口
    disable_windowed_traceback=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=None,
)

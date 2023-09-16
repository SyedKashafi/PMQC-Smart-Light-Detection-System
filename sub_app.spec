# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['sub_app.py'],
    pathex=['C:\\Users\\PERODUA\\Desktop\\Yolo-Service\\yolov5',
    'C:\\Users\\PERODUA\\Desktop\\Yolo-Service'],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)
x = 'cp39-win_amd64'
datas_upd = TOC()

for d in a.datas:
    if x not in d[0] and x not in d[1]:
        datas_upd.append(d)

a.datas = datas_upd

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='rear',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

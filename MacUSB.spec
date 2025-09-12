# -*- mode: python ; coding: utf-8 -*-
block_cipher = None
a = Analysis(
    ['MacUSB/__main__.py'], 
    pathex=['./MacUSB'], 
    binaries=[],
    datas=[
        ('MacUSB/Assets', 'Assets'),
        ('MacUSB/Mods', 'Mods'),
        ('MacUSB/Utils', 'Utils'),
        ('MacUSB/GUI', 'GUI'),
        ('MacUSB/requirements.txt', '.'),  
    ],
    hiddenimports=['tkmacosx'], 
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)
exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='MacUSB',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='MacUSB'
)

app = BUNDLE(
    coll,
    name='MacUSB.app',
    icon="./MacUSB/Assets/Logotype.icns",  
    bundle_identifier=None,
    info_plist={
        "CFBundleShortVersionString": "1.00",
        "CFBundleVersion": "1",
    }
)

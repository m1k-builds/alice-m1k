# alice.spec, alice.py to be copied from launcher/alice.py
# Run: pyinstaller alice.spec

block_cipher = None

a = Analysis(
    ['alice.py'],
    pathex=['.'],
    binaries=[],
    datas=[
        ('alice/*', 'alice'),
        ('LICENSE_ADIBSD', '.'),
        ('alice-desktop-1.3.pyw', '.'),
        ('ohm-meter-vdiv-1.3.pyw', '.'),
        ('dc-meter-source-tool-1.3.pyw', '.'),
        ('strip-chart-tool-1.3.pyw', '.'),
        ('data-logger-tool-1.3.pyw', '.'),
        ('volt-meter-tool-1.3.pyw', '.'),
    ],
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
exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='alice',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,  # Set to False if you want no terminal window
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='alice'
)
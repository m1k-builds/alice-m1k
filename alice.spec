# alice.spec
# Run: pyinstaller alice.spec

block_cipher = None

def extra_datas(mydir):
    exclude_dirs = {'.git', '__pycache__', '.idea', '.vscode'}
    files = []
    for root, dirs, filenames in os.walk(mydir):
        dirs[:] = [d for d in dirs if d not in exclude_dirs]
        for f in filenames:
            if f.endswith(('.pyc', '.pyo')):  # Example: skip compiled files if not needed
                continue
            files.append((os.path.join(root, f), os.path.relpath(os.path.join(root, f), mydir)))
    return files

# Pretty much pick up all files available, alice is to be carried over from launcher folder at build time
a = Analysis(
    ['alice.py'],
    pathex=['.'],
    binaries=[],
    datas=[
        *extra_datas('.')
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
# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['Main.py'],
    pathex=['.'],
    binaries=[],
    datas=[
        # All game assets (images, music, icon, font)
        ('Assets',     'Assets'),
        # GUI modules & guide text
        ('gui',        'gui'),
        # Character modules
        ('characters', 'characters'),
    ],
    hiddenimports=[
        # Pillow
        'PIL._tkinter_finder',
        'PIL.Image',
        'PIL.ImageTk',
        'PIL.ImageOps',
        'PIL.ImageEnhance',
        'PIL.ImageDraw',
        'PIL.ImageFont',
        # pygame
        'pygame',
        'pygame.mixer',
        # characters
        'characters.Characters',
        'characters.Maruzensky',
        'characters.Zen',
        'characters.Devourer',
        'characters.JAD',
        'characters.Giga',
        'characters.Minos',
        'characters.Pol',
        'characters.Sed',
        'characters.Russel',
        'characters.Sol_Emberload',
        'characters.Hotori',
        # gui
        'gui.Interface',
        'gui.CharacterSelect',
        'gui.BattleScene',
        'gui.Guides',
        'gui.MusicManager',
        'gui.FontLoader',
    ],
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
    name='BluRoomBattlefield',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,                          # no terminal window
    icon='Assets/BrB.ico',                  # app icon
    disable_windowed_traceback=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='BluRoomBattlefield',
)

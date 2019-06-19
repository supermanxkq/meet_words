# -*- mode: python -*-

block_cipher = None


a = Analysis(['meet_words.py'],
             pathex=['/Users/xukaiqiang/PycharmProjects/meet_words'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='meet_words',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False , icon='lightning.ico')
app = BUNDLE(exe,
             name='meet_words.app',
             icon='lightning.ico',
             bundle_identifier=None)

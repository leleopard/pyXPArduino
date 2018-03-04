# -*- mode: python -*-

block_cipher = None


a = Analysis(['pyXPArduino.py'],
             pathex=['/Users/stephaneteisserenc/Desktop/pyXPArduino'],
             binaries=[],
             datas=[('initial_config/config.xml', 'config'),
                    ('initial_config/logging_conf.json', 'config'),
                    ('initial_config/UDPSettings.xml', 'config'),
                    ('XPRefFiles/Commands.txt','XPRefFiles'),
                    ('XPRefFiles/DataRefs.txt','XPRefFiles')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='pyXPArduino',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False )
app = BUNDLE(exe,
             name='pyXPArduino.app',
             icon=None,
             bundle_identifier=None, 
             info_plist={
            'NSHighResolutionCapable': 'True'
            },
            )

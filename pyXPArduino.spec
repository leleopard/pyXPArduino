# -*- mode: python -*-

block_cipher = None


a = Analysis(['pyXPArduino.py'],
             pathex=['/home/stephane/Desktop/pyXPArduino'],
             binaries=[],
             datas=[('initial_config/config.xml', 'config'),
                    ('initial_config/logging.conf', 'config'),
                    ('initial_config/UDPSettings.xml', 'config'),
                    ('initial_config/ardConfig1.xml', 'config'),
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
          exclude_binaries=True,
          name='pyXPArduino',
          debug=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='pyXPArduino')
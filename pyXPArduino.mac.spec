# -*- mode: python -*-

block_cipher = None

working_dir = os.getcwd()

a = Analysis(['pyXPArduino.py'],
             pathex=[working_dir],
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
               
app = BUNDLE(exe,
         name='pyXPArduino.app',
         icon=None,
         bundle_identifier=None)

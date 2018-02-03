#!/usr/bin/env python

# simple program to compile and upload Arduino code using the Arduino command line

print
print "====PyArduinoBuilder====="
print

#===========================

import subprocess
import sys
import os
import shutil
import time
import fileinput

#===========================
	#	create some background data
	#		these need to reflect the details of your system

	#	where is the Arduino program
arduinoIdeVersion = {}
arduinoIdeVersion["1.5.6-r2"] = "/mnt/sda4/Programs/arduino-1.5.6-r2/arduino"
arduinoIdeVersion["1.6.3"] = "/mnt/sda4/Programs/arduino-1.6.3/arduino"

	#	where are libraries stored (/mnt/sdb1/SGT-Prog/Arduino/ is my Sketchbook directory)
arduinoExtraLibraries = "/mnt/sdb1/SGT-Prog/Arduino/libraries"

	#	where this program will store stuff
	#		these directories will be beside this Python program
compileDirName = "ArduinoTemp"
archiveDirName = "ArduinoUploadArchive"

	#	default build options
buildOptions = {}
buildOptions["action"] = "verify"
buildOptions["board"] = "arduino:avr:uno"
buildOptions["port"] = "/dev/ttyACM0"
buildOptions["ide"] = "1.5.6-r2"

	#	some other important variables - just here for easy reference
compileDir = ""
archiveDir = ""
arduinoProg = ""
inoFileName = ""
inoBaseName = ""
inoArchiveDirName = ""
archiveRequired = False
usedLibs = []
hFiles = []

#============================
	#	ensure directories exist
	#	and empty the compile directory

	#	first the directory used for compiling
pythonDir = os.path.dirname(os.path.realpath(__file__))
compileDir = os.path.join(pythonDir, compileDirName)
if not os.path.exists(compileDir):
	os.makedirs(compileDir)

existingFiles = os.listdir(compileDir)
for f in existingFiles:
	os.remove(os.path.join(compileDir,f))

	#	then the directory where the Archives are saved
archiveDir = os.path.join(pythonDir, archiveDirName)
if not os.path.exists(archiveDir):
	os.makedirs(archiveDir)

#=============================
	#	get the .ino file and figure out the build options
	#
	#	the stuff in the .ino file will have this format
	#	and will start at the first line in the file
	#		// python-build-start
	#		// action, verify
	#		// board, arduino:avr:uno
	#		// port, /dev/ttyACM0
	#		// ide, 1.5.6-r2
	#		// python-build-end

inoFileName = sys.argv[1]
inoBaseName, inoExt = os.path.splitext(os.path.basename(inoFileName))

numLines = 1  # in case there is no end-line
maxLines = 6
buildError = ""
if inoExt.strip() == ".ino":
	codeFile = open(inoFileName, 'r')

	startLine = codeFile.readline()[3:].strip()
	if startLine == "python-build-start":
		nextLine = codeFile.readline()[3:].strip()
		while nextLine != "python-build-end":
			buildCmd = nextLine.split(',')
			if len(buildCmd) > 1:
				buildOptions[buildCmd[0].strip()] = buildCmd[1].strip()
			numLines += 1
			if numLines >= maxLines:
				buildError = "No end line"
				break
			nextLine = codeFile.readline()[3:].strip()
	else:
		buildError = "No start line"
else:
	buildError = "Not a .ino file"

if len(buildError) > 0:
	print "Sorry, can't process file - %s" %(buildError)
	sys.exit()

	#	print buid Options
print "BUILD OPTIONS"
for n,m in buildOptions.iteritems():
	print "%s  %s" %(n, m)
print

#=============================
	#	get the program filename for the selected IDE
arduinoProg = arduinoIdeVersion[buildOptions["ide"]]

#=============================
	#	prepare archive stuff
	#
	#	create name of directory to save the code = name-yyyymmdd-hhmmss
	#	this will go inside the directory archiveDir
inoArchiveDirName = inoBaseName + time.strftime("-%Y%m%d-%H:%M:%S")
	#	note this directory will only be created if there is a successful upload
	#	the name is figured out here to be written into the .ino file so it can be printed by the Arduino code
	#	it will appear as char archiveDirName[] = "nnnnn";

	#	if the .ino file does not have a line with char archiveDirName[] then it will be assumed
	#		that no archiving is required
	#	check for existence of line
for line in fileinput.input(inoFileName):
	if "char archiveDirName[]" in line:
		archiveRequired = True
		break
fileinput.close()

if archiveRequired == True:
	for line in fileinput.input(inoFileName, inplace = 1):
		if "char archiveDirName[]" in line:
			print 'char archiveDirName[] = "%s";' %(inoArchiveDirName)
		else:
			print line.rstrip()
	fileinput.close()
	#~ os.utime(inoFileName, None)

#=============================
	#	figure out what libraries and .h files are used
	#	if there are .h files they will need to be copied to ArduinoTemp

	#	first get the list of all the extra libraries that exist
extraLibList = os.listdir(arduinoExtraLibraries)

	#	go through the .ino file to get any lines with #include
includeLines = []
for line in fileinput.input(inoFileName):
	if "#include" in line:
		includeLines.append(line.strip())
fileinput.close()
print "#INCLUDE LINES"
print includeLines
print

	#	now look for lines with < signifying libraries
for n in includeLines:
	angleLine = n.split('<')
	if len(angleLine) > 1:
		libName = angleLine[1].split('>')
		libName = libName[0].split('.')
		libName = libName[0].strip()
			#	add the name to usedLibs if it is in the extraLibList
		if libName in extraLibList:
			usedLibs.append(libName)
print "LIBS TO BE ARCHIVED"
print usedLibs
print

	#	then look for lines with " signifiying a reference to a .h file
	#	NB the name will be a full path name
for n in includeLines:
	quoteLine = n.split('"')
	if len(quoteLine) > 1:
		hName = quoteLine[1].split('"')
		hName = hName[0].strip()
			#	add the name to hFiles
		hFiles.append(hName)
print ".h FILES TO BE ARCHIVED"
print hFiles
print

#==============================
	#	copy the .ino file to the directory compileDir and change its name to match the directory
saveFile = os.path.join(compileDir, compileDirName + ".ino")
shutil.copy(inoFileName, saveFile)

#===============================
	#	generate the Arduino command
arduinoCommand = "%s --%s --board %s --port %s %s" %(arduinoProg, buildOptions["action"], buildOptions["board"] , buildOptions["port"], saveFile)
print "ARDUINO COMMAND"
print arduinoCommand

#===============================
	#	call the IDE
print "STARTING ARDUINO -- %s\n" %(buildOptions["action"])

presult = subprocess.call(arduinoCommand, shell=True)

if presult != 0:
	print "\nARDUINO FAILED - result code = %s \n" %(presult)
	sys.exit()
else:
	print "\nARDUINO SUCCESSFUL"
		#	if we were not uploading that is the end of things
	if buildOptions["action"] != "upload":
		sys.exit()

#================================
	#	after a successful upload we may need to archive the code
if archiveRequired == True:
	print "\nARCHIVING"
		#	create the Archive directory
	arDir = os.path.join(archiveDir, inoArchiveDirName)
	print arDir
		#	this ought to be a unique name - hence no need to check for duplicates
	os.makedirs(arDir)
		#	copy the code into the new directory
	shutil.copy(inoFileName, arDir)
		#	copy the .h files to the new directory
	for n in hFiles:
		shutil.copy(n, arDir)
		#	copy the used libraries to the new directory
	for n in usedLibs:
		libName = os.path.join(arduinoExtraLibraries, n)
		destDir = os.path.join(arDir, "libraries", n)
		shutil.copytree(libName, destDir)
	print "\nARCHIVING DONE"

sys.exit()

#==============================












 #!/usr/bin/env python

#
#    build_arduino.py - build, link and upload sketches script for Arduino
#    Copyright (c) 2010 Ben Sasson.  All right reserved.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#


import sys
import os
import optparse


EXITCODE_OK = 0
EXITCODE_NO_UPLOAD_DEVICE = 1
EXITCODE_NO_WPROGRAM = 2
EXITCODE_INVALID_AVR_PATH = 3


CPU_CLOCK = 16000000
ARCH = 'atmega328p'
ENV_VERSION = 18
BAUD = 57600
CORE = 'arduino'


COMPILERS = {
    '.c': 'avr-gcc',
    '.cpp': 'avr-g++',
}


def _exec(cmdline, debug=True, valid_exitcode=0, simulate=False):
    if debug or simulate:
        print(cmdline)
    if not simulate:
        exitcode = os.system(cmdline)
        if exitcode != valid_exitcode:
            print('-'*20 + ' exitcode %d ' % exitcode + '-'*20)
            sys.exit(exitcode)


def compile_source(source, avr_path='', target_dir=None, arch=ARCH, clock=CPU_CLOCK, include_dirs=[], verbose=False, simulate=False):
    """
    compile a single source file, using compiler selected based on file extension and translating arguments
    to valid compiler flags.
    """

    filename, ext = os.path.splitext(source)
    compiler = COMPILERS.get(ext, None)
    if compiler is None:
        print(source, 'has no known compiler')
        return

    if target_dir is None:
        target_dir = os.path.dirname(source)

    target = os.path.join(target_dir, os.path.basename(source) + '.o')
    env = dict(source=source, target=target, arch=arch, clock=clock, env_version=ENV_VERSION, compiler=compiler, avr_path=avr_path)

    # create include list, don't use set() because order matters
    dirs = [os.path.dirname(source)]
    for d in include_dirs:
        if d not in dirs:
            dirs.append(d)

    env['include_dirs'] = ' '.join('-I%s' % d for d in dirs)
    if verbose:
        env['verbose'] = '-v'
    else:
        env['verbose'] = ''
    cmdline = '%(avr_path)s%(compiler)s -c %(verbose)s -g -Os -w -ffunction-sections -fdata-sections -mmcu=%(arch)s -DF_CPU=%(clock)dL -DARDUINO=%(env_version)d %(include_dirs)s %(source)s -o%(target)s' % env
    _exec(cmdline, simulate=simulate)
    return target


def compile_directory(directory, target_dir=None, include_dirs=[], avr_path='', arch=ARCH, clock=CPU_CLOCK, verbose=False, simulate=False):
    """
    compile all source files in a given directory, return a list of all .obj files created
    """

    obj_files = []
    for fname in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, fname)):
            obj_files.append(compile_source(os.path.join(directory, fname), include_dirs=include_dirs, avr_path=avr_path, target_dir=target_dir, arch=arch, clock=clock, verbose=verbose, simulate=simulate))

    return filter(lambda o: o, obj_files)


def append_to_archive(obj_file, archive, avr_path='', verbose=False, simulate=False):
    """
    create an .a archive out of .obj files
    """

    env = dict(obj_file=obj_file, archive=archive, avr_path=avr_path)
    if verbose:
        env['verbose'] = 'v'
    else:
        env['verbose'] = ''
    cmdline = '%(avr_path)savr-ar rcs%(verbose)s %(archive)s %(obj_file)s' % env
    _exec(cmdline, simulate=simulate)


def link(target, files, arch=ARCH, avr_path='', verbose=False, simulate=False):
    """
    link .obj files to a single .elf file
    """

    env = dict(target=target, files=' '.join(files), link_dir=os.path.dirname(target), arch=arch, avr_path=avr_path)
    if verbose:
        env['verbose'] = '-v'
    else:
        env['verbose'] = ''
    cmdline = '%(avr_path)savr-gcc %(verbose)s -Os -Wl,--gc-sections -mmcu=%(arch)s -o %(target)s %(files)s -L%(link_dir)s -lm' % env
    _exec(cmdline, simulate=simulate)


def make_hex(elf, avr_path='', verbose=False, simulate=False):
    """
    slice elf to .hex (program) end .eep (EEProm) files
    """

    eeprom_section = os.path.splitext(elf)[0] + '.epp'
    hex_section = os.path.splitext(elf)[0] + '.hex'
    env = dict(elf=elf, eeprom_section=eeprom_section, hex_section=hex_section, avr_path=avr_path)
    if verbose:
        env['verbose'] = '-v'
    else:
        env['verbose'] = ''
    cmdline_make_eeprom = '%(avr_path)savr-objcopy %(verbose)s -O ihex -j .eeprom --set-section-flags=.eeprom=alloc,load --no-change-warnings --change-section-lma .eeprom=0 %(elf)s %(eeprom_section)s' % env
    _exec(cmdline_make_eeprom, simulate=simulate)
    cmdline_make_hex = '%(avr_path)savr-objcopy %(verbose)s -O ihex -R .eeprom %(elf)s %(hex_section)s' % env
    _exec(cmdline_make_hex, simulate=simulate)
    return hex_section, eeprom_section


def upload(hex_section, dev, avr_path='', dude_conf=None, arch=ARCH, core=CORE, baud=BAUD, verbose=False, simulate=False):
    """
    Upload .hex file to arduino board
    """

    env = dict(hex_section=hex_section, dev=dev, arch=arch, core=core, baud=baud, avr_path=avr_path)
    if verbose:
        env['verbose'] = '-v'
    else:
        env['verbose'] = ''
    if dude_conf is not None:
        env['dude_conf'] = '-C' + dude_conf
    else:
        env['dude_conf'] = ''
    cmdline = '%(avr_path)savrdude %(verbose)s %(dude_conf)s -p%(arch)s -c%(core)s -P%(dev)s -b%(baud)d -D -Uflash:w:%(hex_section)s:i' % env
    _exec(cmdline, simulate=simulate)


def main(argv):
    parser = optparse.OptionParser()
    parser.add_option('-d', '--directory', dest='directory', default='.', help='project directory')
    parser.add_option('-v', '--verbose', dest='verbose', default=False, action='store_true', help='be verbose')
    parser.add_option('--only-build', dest='only_build', default=False, action='store_true', help="only build, don't upload")
    parser.add_option('-u', '--upload-device', dest='upload_device', metavar='DEVICE', help='use DEVICE to upload code')
    parser.add_option('-i', '--include', dest='include_dirs', default=[], action='append', metavar='DIRECTORY', help='append DIRECTORY to include list')
    parser.add_option('-l', '--libraries', dest='libraries', default=[], action='append', metavar='DIRECTORY', help='append DIRECTORY to libraries search & build path')
    parser.add_option('-W', '--WProgram-dir', dest='wprogram_directory', metavar='DIRECTORY', help='DIRECTORY of Arduino.h and the rest of core files')
    parser.add_option('--avr-path', dest='avr_path', metavar='DIRECTORY', help='DIRECTORY where avr* programs located, if not specified - will assume found in default search path')
    parser.add_option('--dude-conf', dest='dude_conf', default=None, metavar='FILE', help='avrdude conf file, if not specified - will assume found in default location')
    parser.add_option('--simulate', dest='simulate', default=False, action='store_true', help='only simulate commands')
    parser.add_option('--core', dest='core', default=CORE, help='device core name [%s]' % CORE)
    parser.add_option('--arch', dest='arch', default=ARCH, help='device architecture name [%s]' % ARCH)
    parser.add_option('--baud', dest='baud', default=BAUD, type='int', help='upload baud rate [%d]' % BAUD)
    parser.add_option('--cpu-clock', dest='cpu_clock', default=CPU_CLOCK, metavar='Hz', action='store', type='int', help='target device CPU clock [%d]' % CPU_CLOCK)

    options, args = parser.parse_args(argv)

    if options.wprogram_directory is None or not os.path.exists(options.wprogram_directory) or not os.path.isdir(options.wprogram_directory):
        if options.verbose:
            print('WProgram directory was not specified or does not exist [%s]' % options.wprogram_directory)
        sys.exit(EXITCODE_NO_WPROGRAM)

    core_files = options.wprogram_directory

    if options.avr_path is not None:
        if not os.path.exists(options.avr_path) or not os.path.isdir(options.avr_path):
            if options.verbose:
                print('avr-path was specified but does not exist or not a directory [%s]' % options.avr_path)
            sys.exit(EXITCODE_INVALID_AVR_PATH)
        avr_path = os.path.join(options.avr_path, '')
    else:
        avr_path = ''

    # create build directory to store the compilation output files
    build_directory = os.path.join(options.directory, '_build')
    if not os.path.exists(build_directory):
        os.makedirs(build_directory)

    # compile arduino core files
    core_obj_files = compile_directory(core_files, build_directory, include_dirs=[core_files], avr_path=avr_path, arch=options.arch, clock=options.cpu_clock, verbose=options.verbose, simulate=options.simulate)

    # compile directories passed to program
    libraries_obj_files = []
    for library in options.libraries:
        libraries_obj_files.extend(compile_directory(library, build_directory, include_dirs=options.libraries + [core_files], avr_path=avr_path, arch=options.arch, clock=options.cpu_clock, verbose=options.verbose, simulate=options.simulate))

    # compile project
    project_obj_files = compile_directory(options.directory, build_directory, include_dirs=(options.include_dirs + options.libraries + [core_files]), avr_path=avr_path, arch=options.arch, clock=options.cpu_clock, verbose=options.verbose, simulate=options.simulate)

    # link project, libraries and core .obj files to a single .elf
    link_output = os.path.join(build_directory, os.path.basename(options.directory) + '.elf')
    link(link_output, project_obj_files + libraries_obj_files + core_obj_files, avr_path=avr_path, verbose=options.verbose, simulate=options.simulate)

    hex_section, eeprom_section = make_hex(link_output, avr_path=avr_path, verbose=options.verbose, simulate=options.simulate)

    # upload .hex file to arduino if needed
    if not options.only_build:
        if options.upload_device is None:
            if options.verbose:
                print('no upload device selected')
            sys.exit(EXITCODE_NO_UPLOAD_DEVICE)
        upload(hex_section, dev=options.upload_device, dude_conf=options.dude_conf, avr_path=avr_path, arch=options.arch, core=options.core, baud=options.baud, verbose=options.verbose, simulate=options.simulate)


if __name__ == '__main__':
    main(sys.argv)

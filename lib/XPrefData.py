#!/usr/bin/env python
import logging
import re
import sys, os

if getattr(sys, 'frozen', False):
	# we are running in a bundle
	working_dir = sys._MEIPASS
else:
	working_dir = os.getcwd()

XP_COMMANDS = []
XP_COMMANDS_CATEGORIES = {'All':''}

XP_CMDFILE_LINES = []

XP_DATAREFS = []
XP_DATAREFS_CATEGORIES = {'All':''}

XP_DATAREFSFILE_LINES = []

def loadXPReferenceFiles():
	logging.info('Loading XPlane commands...')
	with open(os.path.join(working_dir,"XPRefFiles/Commands.txt")) as commandsFile:
		XP_CMDFILE_LINES = commandsFile.readlines()


	for line in XP_CMDFILE_LINES:
		command_chunks = line.split(None, 1)
		command_elems = command_chunks[0].split("/")
		cmd_category = command_elems[0]+"/"+command_elems[1]
		if cmd_category in XP_COMMANDS_CATEGORIES:
			pass
		else:
			XP_COMMANDS_CATEGORIES[cmd_category] = ''


		XP_COMMANDS.append([cmd_category, command_chunks[0], command_chunks[1].rstrip()])

	logging.info('Loading XPlane datarefs...')


	with open(os.path.join(working_dir,"XPRefFiles/DataRefs.txt")) as datarefsFile:
		XP_DATAREFSFILE_LINES = datarefsFile.readlines()


	for line in XP_DATAREFSFILE_LINES:
		#command_chunks = line.split("\\t+", 3)
		command_chunks = re.split("\t+", line)

		#logging.debug(command_chunks)
		if len(command_chunks) >= 3: # ensure the line has at least 3 tab separator
			command_elems = command_chunks[0].split("/")
			nr_elems = len(command_elems)
			if nr_elems >= 3: # ensure this text looks like a dataref
				cmd_category = ''
				for i in range(0,nr_elems-1):
					cmd_category += command_elems[i]+"/"
				if cmd_category in XP_DATAREFS_CATEGORIES:
					pass
				else:
					XP_DATAREFS_CATEGORIES[cmd_category] = ''

				description = ''
				unit = ''
				if len(command_chunks)>=4:
					unit = command_chunks[3]
					for i in range(4, len(command_chunks)):
						description+= command_chunks[i]

				XP_DATAREFS.append([cmd_category,
									command_chunks[0], # dataref
									command_chunks[1].rstrip(), # type
									command_chunks[2].rstrip(), # writable
									unit,
									description.rstrip()] )

def getXPCommandList(category, filter):
	filter_upper = filter.upper()
	#logging.debug('Filter text:', filter)
	if filter !='':
		filtered_commands = [cmd for cmd in XP_COMMANDS if (filter_upper in cmd[1].upper() or filter_upper in cmd[2].upper())]
	else:
		filtered_commands = XP_COMMANDS
	if category != None and category != "All":
		command_list = [cmd for cmd in filtered_commands if cmd[0] == category]
	else:
		command_list = filtered_commands
	return command_list

def getXPDatarefList(category, filter):
	if filter is None:
		filter = ''
	filter_upper = filter.upper()
	#print('Filter text:', filter)
	if filter !='' and len(filter) >=2:
		filtered_datarefs = [dref for dref in XP_DATAREFS if (filter_upper in dref[1].upper() or filter_upper in dref[5].upper())]
	else:
		filtered_datarefs = XP_DATAREFS
	if category != None and category != "All":
		dref_list = [dref for dref in filtered_datarefs if dref[0] == category]
	else:
		dref_list = filtered_datarefs
	return dref_list

def getXPDataref(dataref):
	logging.debug('looking for dataref: '+str(dataref))
	filtered_datarefs = [dref for dref in XP_DATAREFS if (dataref == dref[1]) ]
	if len(filtered_datarefs) > 0:
		return filtered_datarefs[0]
	else:
		return ['',
				'', # dataref
				'', # type
				'', # writable
				'',
				'']

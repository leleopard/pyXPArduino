#!/usr/bin/env python

XP_COMMANDS = []
XP_COMMANDS_CATEGORIES = {'All':''}

XP_CMDFILE_LINES = []

with open("XPRefFiles/Commands.txt") as commandsFile:
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
	
print(XP_COMMANDS)
print(XP_COMMANDS_CATEGORIES)

def getXPCommandList(category, filter):
	filter_upper = filter.upper()
	#print('Filter text:', filter)
	if filter !='':
		filtered_commands = [cmd for cmd in XP_COMMANDS if (filter_upper in cmd[1].upper() or filter_upper in cmd[2].upper())]
	else:
		filtered_commands = XP_COMMANDS
	if category != None and category != "All":
		command_list = [cmd for cmd in filtered_commands if cmd[0] == category]
	else:
		command_list = filtered_commands
	return command_list
	
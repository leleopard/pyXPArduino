"""
XPrefData.py
------------
Loads and exposes the X-Plane command and dataref reference databases.

At startup, :func:`loadXPReferenceFiles` reads the two plain-text reference
files shipped with X-Plane (``XPRefFiles/Commands.txt`` and
``XPRefFiles/DataRefs.txt``) and populates four module-level lists/dicts
that the rest of the application queries:

* :data:`XP_COMMANDS` — flat list of all commands.
* :data:`XP_COMMANDS_CATEGORIES` — unique category prefixes for commands.
* :data:`XP_DATAREFS` — flat list of all datarefs with metadata.
* :data:`XP_DATAREFS_CATEGORIES` — unique category prefixes for datarefs.

Filter helpers (:func:`getXPCommandList`, :func:`getXPDatarefList`,
:func:`getXPDataref`) are used by the GUI picker dialogs.
"""

#!/usr/bin/env python
import logging
import re
import sys, os

if getattr(sys, 'frozen', False):
	# we are running in a bundle
	working_dir = sys._MEIPASS
else:
	working_dir = os.getcwd()

#: list[list]: All X-Plane commands loaded from Commands.txt.
#: Each entry is ``[category, command_id, description]``.
XP_COMMANDS = []

#: dict[str, str]: Unique top-level category strings for commands (keys).
#: Values are always empty strings — the dict is used as an ordered set.
XP_COMMANDS_CATEGORIES = {'All':''}

XP_CMDFILE_LINES = []

#: list[list]: All X-Plane datarefs loaded from DataRefs.txt.
#: Each entry is ``[category, dataref, type, writable, unit, description]``.
XP_DATAREFS = []

#: dict[str, str]: Unique top-level category strings for datarefs (keys).
#: Values are always empty strings — the dict is used as an ordered set.
XP_DATAREFS_CATEGORIES = {'All':''}

XP_DATAREFSFILE_LINES = []


def loadXPReferenceFiles():
    """Load X-Plane command and dataref reference files into module-level lists.

    Reads ``XPRefFiles/Commands.txt`` and ``XPRefFiles/DataRefs.txt`` from the
    application working directory and populates :data:`XP_COMMANDS`,
    :data:`XP_COMMANDS_CATEGORIES`, :data:`XP_DATAREFS`, and
    :data:`XP_DATAREFS_CATEGORIES`.

    This function must be called once at application startup before any of the
    picker dialogs or filter helpers are used.

    Commands file format (space-separated)::

        sim/flight_controls/flaps_down    Lower the flaps

    DataRefs file format (tab-separated)::

        sim/cockpit/switches/gear_handle_status  int  y  ratio  Gear handle position

    Raises:
        FileNotFoundError: If either reference file is missing from the
            ``XPRefFiles/`` directory.
    """
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
        command_chunks = re.split("\t+", line)

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
    """Return a filtered list of X-Plane commands.

    Filters :data:`XP_COMMANDS` by an optional category and a free-text
    search string.  Both the command ID and description are searched
    (case-insensitive).

    Args:
        category (str | None): Category prefix to restrict results to, or
            ``'All'`` / ``None`` to include every category.
        filter (str): Free-text substring to search for in the command ID or
            description.  Pass ``''`` to return all commands in the category.

    Returns:
        list[list]: Matching commands, each in the form
        ``[category, command_id, description]``.
    """
    filter_upper = filter.upper()
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
    """Return a filtered list of X-Plane datarefs.

    Filters :data:`XP_DATAREFS` by an optional category and a free-text
    search string applied to the dataref path and description
    (case-insensitive).  The search is only applied when ``filter`` is at
    least 2 characters long to avoid returning enormous unfiltered lists.

    Args:
        category (str | None): Category prefix to restrict results to, or
            ``'All'`` / ``None`` for all categories.
        filter (str | None): Free-text substring to search within the dataref
            path or description.  Pass ``''`` or ``None`` to skip filtering.

    Returns:
        list[list]: Matching datarefs, each in the form
        ``[category, dataref, type, writable, unit, description]``.
    """
    if filter is None:
        filter = ''
    filter_upper = filter.upper()
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
    """Look up a single dataref by its exact path string.

    Args:
        dataref (str): The fully-qualified dataref path to look up, e.g.
            ``'sim/cockpit/switches/gear_handle_status'``.

    Returns:
        list: The first matching dataref entry in the form
        ``[category, dataref, type, writable, unit, description]``, or a
        list of six empty strings if the dataref is not found.
    """
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

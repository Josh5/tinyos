#
#      Copyright (C) 2013 Sean Poyser
#
#  This Program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2, or (at your option)
#  any later version.
#
#  This Program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with XBMC; see the file COPYING.  If not, write to
#  the Free Software Foundation, 675 Mass Ave, Cambridge, MA 02139, USA.
#  http://www.gnu.org/copyleft/gpl.html
#

import utils
import update
import xbmc

from services.firstrun import firstrun
firstrun_thread = firstrun()     
firstrun_thread.onStart()

from services.firstrun import start
start_thread = start()     
start_thread.onStart()

utils.log("Update Service Starting")


try:
    update.checkForUpdate(silent = 1)

except Exception, e:
    utils.log('Error in TinyHTPC Update Service')
    utils.log(e)


#!/usr/bin/python3
from fabric.api import local
from datetime import datetime

def do_pack():
        """Generates a .tgz archive from the contents of the web_static folder"""
            try:
                        # Create the directory versions if it doesn't exist
                                local("mkdir -p versions")
                                        
                                                # Create the archive .tgz file
                                                        time_stamp = datetime.now().strftime("%Y%m%d%H%M%S")  # Current time
                                                                archive_path = "versions/web_static_{}.tgz".format(time_stamp)
                                                                        local("tar -cvzf {} web_static".format(archive_path))
                                                                                
                                                                                        return archive_path
                                                                                        except:
                                                                                                    return None

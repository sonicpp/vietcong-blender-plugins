# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  version 2 as published by the Free Software Foundation.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

import bpy

bl_info = {
    "name"       : "Vietcong BES (.bes)",
    "author"     : "Jan Havran",
    "version"    : (0, 1),
    "blender"    : (2, 70, 0),
    "location"   : "File > Import > BES (.bes)",
    "description": "Import Vietcong BES files",
    "wiki_url"   : "https://github.com/sonicpp/vietcong-blender-plugins",
    "category"   : "Import-Export",
}

class BESImporter(bpy.types.Operator):
    bl_idname = "import_mesh.bes"

def menu_import_bes(self, context):
    self.layout.operator(BESImporter.bl_idname, text="BES (.bes)")

def register():
    bpy.utils.register_module(__name__)
    bpy.types.INFO_MT_file_import.append(menu_import_bes)

def unregister():
    bpy.utils.unregister_module(__name__)
    bpy.types.INFO_MT_file_import.remove(menu_import_bes)

if __name__ == "__main__":
    register()


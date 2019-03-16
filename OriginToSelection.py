bl_info = {
    "name": "Origin to Selection",
    "category": "Object",
}

import bpy

class OriginToSelection(bpy.types.Operator):
    """Set the object's origin to the selection"""
    bl_idname = "object.origin_to_selection"
    bl_label = "Set Origin to Selection"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):


        bpy.ops.view3d.snap_cursor_to_selected()
        bpy.ops.object.editmode_toggle()
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
        bpy.ops.object.editmode_toggle()

        return {'FINISHED'}

def register():
    bpy.utils.register_class(OriginToSelection)


def unregister():
    bpy.utils.unregister_class(OriginToSelection)


# This allows you to run the script directly from Blender's Text editor
# to test the add-on without having to install it.
if __name__ == "__main__":
    register()        

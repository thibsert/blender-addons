bl_info = {
    "name": "Origin to Selection",
    "category": "Object",
}

import bpy

class OriginToSelection(bpy.types.Operator):
    """Set the object's origin to the selection"""      # Use this as a tooltip for menu items and buttons.
    bl_idname = "object.origin_to_selection"        # Unique identifier for buttons and menu items to reference.
    bl_label = "Set Origin to Selection"         # Display name in the interface.
    bl_options = {'REGISTER', 'UNDO'}  # Enable undo for the operator.

    def execute(self, context):        # execute() is called when running the operator.


        for area in bpy.context.screen.areas:
            if area.type == 'VIEW_3D':
                ctx = bpy.context.copy()
                ctx['area'] = area
                ctx['region'] = area.regions[-1]
                bpy.ops.view3d.snap_cursor_to_selected(ctx)
                bpy.ops.object.editmode_toggle(ctx)
                bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
                
                # take new copy of the context because it is outdated now
                ctx = bpy.context.copy()
                ctx['area'] = area
                ctx['region'] = area.regions[-1]            

                bpy.ops.object.editmode_toggle(ctx)

                break
        return {'FINISHED'} # Lets Blender know the operator finished successfully.

def register():
    bpy.utils.register_class(OriginToSelection)


def unregister():
    bpy.utils.unregister_class(OriginToSelection)


# This allows you to run the script directly from Blender's Text editor
# to test the add-on without having to install it.
if __name__ == "__main__":
    register()        
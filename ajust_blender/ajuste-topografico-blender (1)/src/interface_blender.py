
import bpy

class AjusteTopograficoPanel(bpy.types.Panel):
    bl_label = "Ajuste Topográfico"
    bl_idname = "VIEW3D_PT_ajuste_topografico"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Topografia'

    def draw(self, context):
        layout = self.layout
        layout.prop(context.scene, "csv_entrada")
        layout.prop(context.scene, "csv_apoio")
        layout.prop(context.scene, "precisao_linear")
        layout.prop(context.scene, "precisao_angular")
        layout.operator("ajuste.executar")

class ExecutarAjusteOperator(bpy.types.Operator):
    bl_idname = "ajuste.executar"
    bl_label = "Executar Ajuste"

    def execute(self, context):
        entrada = context.scene.csv_entrada
        apoio = context.scene.csv_apoio
        precisao_linear = context.scene.precisao_linear
        precisao_angular = context.scene.precisao_angular
        self.report({'INFO'}, f"Ajuste em: {entrada}, apoio: {apoio}, precisão: {precisao_linear}, {precisao_angular}")
        return {'FINISHED'}

def register():
    bpy.types.Scene.csv_entrada = bpy.props.StringProperty(name="Entradas CSV")
    bpy.types.Scene.csv_apoio = bpy.props.StringProperty(name="Pontos de Apoio CSV")
    bpy.types.Scene.precisao_linear = bpy.props.StringProperty(name="Precisão Linear")
    bpy.types.Scene.precisao_angular = bpy.props.StringProperty(name="Precisão Angular")
    bpy.utils.register_class(AjusteTopograficoPanel)
    bpy.utils.register_class(ExecutarAjusteOperator)

def unregister():
    bpy.utils.unregister_class(AjusteTopograficoPanel)
    bpy.utils.unregister_class(ExecutarAjusteOperator)

if __name__ == "__main__":
    register()

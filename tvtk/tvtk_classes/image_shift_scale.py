# Automatically generated code: EDIT AT YOUR OWN RISK
from traits import api as traits
from traitsui import api as traitsui

from tvtk import vtk_module as vtk
from tvtk import tvtk_base
from tvtk.tvtk_base_handler import TVTKBaseHandler
from tvtk import messenger
from tvtk.tvtk_base import deref_vtk
from tvtk import array_handler
from tvtk.array_handler import deref_array
from tvtk.tvtk_classes.tvtk_helper import wrap_vtk

from tvtk.tvtk_classes.threaded_image_algorithm import ThreadedImageAlgorithm


class ImageShiftScale(ThreadedImageAlgorithm):
    """
    ImageShiftScale - shift and scale an input image
    
    Superclass: ThreadedImageAlgorithm
    
    With ImageShiftScale Pixels are shifted (a constant value added)
    and then scaled (multiplied by a scalar. As a convenience, this class
    allows you to set the output scalar type similar to ImageCast.
    This is because shift scale operations frequently convert data types.
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkImageShiftScale, obj, update, **traits)
    
    clamp_overflow = tvtk_base.false_bool_trait(help=\
        """
        When the clamp_overflow flag is on, the data is thresholded so
        that the output value does not exceed the max or min of the data
        type. By default, clamp_overflow is off.
        """
    )
    def _clamp_overflow_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetClampOverflow,
                        self.clamp_overflow_)

    def get_output_scalar_type(self):
        """
        V.get_output_scalar_type() -> int
        C++: int GetOutputScalarType()
        Set the desired output scalar type. The result of the shift and
        scale operations is cast to the type specified.
        """
        ret = self._vtk_obj.GetOutputScalarType()
        return ret
        

    def set_output_scalar_type(self, *args):
        """
        V.set_output_scalar_type(int)
        C++: void SetOutputScalarType(int a)
        Set the desired output scalar type. The result of the shift and
        scale operations is cast to the type specified.
        """
        ret = self._wrap_call(self._vtk_obj.SetOutputScalarType, *args)
        return ret

    def set_output_scalar_type_to_double(self):
        """
        V.set_output_scalar_type_to_double()
        C++: void SetOutputScalarTypeToDouble()
        Set the desired output scalar type. The result of the shift and
        scale operations is cast to the type specified.
        """
        self._vtk_obj.SetOutputScalarTypeToDouble()

    def set_output_scalar_type_to_float(self):
        """
        V.set_output_scalar_type_to_float()
        C++: void SetOutputScalarTypeToFloat()
        Set the desired output scalar type. The result of the shift and
        scale operations is cast to the type specified.
        """
        self._vtk_obj.SetOutputScalarTypeToFloat()

    def set_output_scalar_type_to_int(self):
        """
        V.set_output_scalar_type_to_int()
        C++: void SetOutputScalarTypeToInt()
        Set the desired output scalar type. The result of the shift and
        scale operations is cast to the type specified.
        """
        self._vtk_obj.SetOutputScalarTypeToInt()

    def set_output_scalar_type_to_long(self):
        """
        V.set_output_scalar_type_to_long()
        C++: void SetOutputScalarTypeToLong()
        Set the desired output scalar type. The result of the shift and
        scale operations is cast to the type specified.
        """
        self._vtk_obj.SetOutputScalarTypeToLong()

    def set_output_scalar_type_to_short(self):
        """
        V.set_output_scalar_type_to_short()
        C++: void SetOutputScalarTypeToShort()
        Set the desired output scalar type. The result of the shift and
        scale operations is cast to the type specified.
        """
        self._vtk_obj.SetOutputScalarTypeToShort()

    def set_output_scalar_type_to_unsigned_char(self):
        """
        V.set_output_scalar_type_to_unsigned_char()
        C++: void SetOutputScalarTypeToUnsignedChar()
        Set the desired output scalar type. The result of the shift and
        scale operations is cast to the type specified.
        """
        self._vtk_obj.SetOutputScalarTypeToUnsignedChar()

    def set_output_scalar_type_to_unsigned_int(self):
        """
        V.set_output_scalar_type_to_unsigned_int()
        C++: void SetOutputScalarTypeToUnsignedInt()
        Set the desired output scalar type. The result of the shift and
        scale operations is cast to the type specified.
        """
        self._vtk_obj.SetOutputScalarTypeToUnsignedInt()

    def set_output_scalar_type_to_unsigned_long(self):
        """
        V.set_output_scalar_type_to_unsigned_long()
        C++: void SetOutputScalarTypeToUnsignedLong()
        Set the desired output scalar type. The result of the shift and
        scale operations is cast to the type specified.
        """
        self._vtk_obj.SetOutputScalarTypeToUnsignedLong()

    def set_output_scalar_type_to_unsigned_short(self):
        """
        V.set_output_scalar_type_to_unsigned_short()
        C++: void SetOutputScalarTypeToUnsignedShort()
        Set the desired output scalar type. The result of the shift and
        scale operations is cast to the type specified.
        """
        self._vtk_obj.SetOutputScalarTypeToUnsignedShort()

    shift = traits.Float(0.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the shift value. This value is added to each pixel
        """
    )
    def _shift_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetShift,
                        self.shift)

    scale = traits.Float(1.0, enter_set=True, auto_set=False, help=\
        """
        Set/Get the scale value. Each pixel is multiplied by this value.
        """
    )
    def _scale_changed(self, old_val, new_val):
        self._do_change(self._vtk_obj.SetScale,
                        self.scale)

    _updateable_traits_ = \
    (('scale', 'GetScale'), ('global_warning_display',
    'GetGlobalWarningDisplay'), ('shift', 'GetShift'), ('progress_text',
    'GetProgressText'), ('debug', 'GetDebug'), ('clamp_overflow',
    'GetClampOverflow'), ('abort_execute', 'GetAbortExecute'),
    ('number_of_threads', 'GetNumberOfThreads'), ('release_data_flag',
    'GetReleaseDataFlag'), ('reference_count', 'GetReferenceCount'),
    ('progress', 'GetProgress'))
    
    _full_traitnames_list_ = \
    (['abort_execute', 'clamp_overflow', 'debug',
    'global_warning_display', 'release_data_flag', 'number_of_threads',
    'progress_text', 'scale', 'shift'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(ImageShiftScale, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit ImageShiftScale properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View((['clamp_overflow'], [], ['number_of_threads', 'scale',
            'shift']),
            title='Edit ImageShiftScale properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit ImageShiftScale properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            

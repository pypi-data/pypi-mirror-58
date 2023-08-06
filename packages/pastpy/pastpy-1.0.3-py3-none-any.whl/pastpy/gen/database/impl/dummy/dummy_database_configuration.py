import builtins


class DummyDatabaseConfiguration(object):
    class Builder(object):
        def __init__(
            self,
            images_per_object=2,
            objects=10,
        ):
            self.__images_per_object = images_per_object
            self.__objects = objects

        def build(self):
            return DummyDatabaseConfiguration(images_per_object=self.__images_per_object, objects=self.__objects)

        @classmethod
        def from_template(cls, template):
            '''
            :type template: pastpy.gen.database.impl.dummy.dummy_database_configuration.DummyDatabaseConfiguration
            :rtype: pastpy.gen.database.impl.dummy.dummy_database_configuration.DummyDatabaseConfiguration
            '''

            builder = cls()
            builder.images_per_object = template.images_per_object
            builder.objects = template.objects
            return builder

        @property
        def images_per_object(self) -> int:
            return self.__images_per_object

        @property
        def objects(self) -> int:
            return self.__objects

        def set_images_per_object(self, images_per_object: int):
            if images_per_object is None:
                raise ValueError('images_per_object is required')
            if not isinstance(images_per_object, int):
                raise TypeError("expected images_per_object to be a int but it is a %s" % builtins.type(images_per_object))
            self.__images_per_object = images_per_object
            return self

        def set_objects(self, objects: int):
            if objects is None:
                raise ValueError('objects is required')
            if not isinstance(objects, int):
                raise TypeError("expected objects to be a int but it is a %s" % builtins.type(objects))
            self.__objects = objects
            return self

        def update(self, dummy_database_configuration):
            if isinstance(dummy_database_configuration, DummyDatabaseConfiguration):
                self.set_images_per_object(dummy_database_configuration.images_per_object)
                self.set_objects(dummy_database_configuration.objects)
            elif isinstance(dummy_database_configuration, dict):
                for key, value in dummy_database_configuration.items():
                    getattr(self, 'set_' + key)(value)
            else:
                raise TypeError(dummy_database_configuration)
            return self

        @images_per_object.setter
        def images_per_object(self, images_per_object: int) -> None:
            self.set_images_per_object(images_per_object)

        @objects.setter
        def objects(self, objects: int) -> None:
            self.set_objects(objects)

    class FieldMetadata(object):
        IMAGES_PER_OBJECT = None
        OBJECTS = None

        def __init__(self, name, type_, validation):
            object.__init__(self)
            self.__name = name
            self.__type = type_
            self.__validation = validation

        @property
        def name(self):
            return self.__name

        def __repr__(self):
            return self.__name

        def __str__(self):
            return self.__name

        @property
        def type(self):
            return self.__type

        @property
        def validation(self):
            return self.__validation

        @classmethod
        def values(cls):
            return (cls.IMAGES_PER_OBJECT, cls.OBJECTS,)

    FieldMetadata.IMAGES_PER_OBJECT = FieldMetadata('images_per_object', int, None)
    FieldMetadata.OBJECTS = FieldMetadata('objects', int, None)

    def __init__(
        self,
        images_per_object: int = 2,
        objects: int = 10,
    ):
        if images_per_object is None:
            raise ValueError('images_per_object is required')
        if not isinstance(images_per_object, int):
            raise TypeError("expected images_per_object to be a int but it is a %s" % builtins.type(images_per_object))
        self.__images_per_object = images_per_object

        if objects is None:
            raise ValueError('objects is required')
        if not isinstance(objects, int):
            raise TypeError("expected objects to be a int but it is a %s" % builtins.type(objects))
        self.__objects = objects

    def __eq__(self, other):
        if self.images_per_object != other.images_per_object:
            return False
        if self.objects != other.objects:
            return False
        return True

    def __hash__(self):
        return hash((self.images_per_object, self.objects,))

    def __iter__(self):
        return iter((self.images_per_object, self.objects,))

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        field_reprs = []
        field_reprs.append('images_per_object=' + repr(self.images_per_object))
        field_reprs.append('objects=' + repr(self.objects))
        return 'DummyDatabaseConfiguration(' + ', '.join(field_reprs) + ')'

    def __str__(self):
        field_reprs = []
        field_reprs.append('images_per_object=' + repr(self.images_per_object))
        field_reprs.append('objects=' + repr(self.objects))
        return 'DummyDatabaseConfiguration(' + ', '.join(field_reprs) + ')'

    @classmethod
    def builder(cls):
        return cls.Builder()

    @classmethod
    def from_builtins(cls, _dict):
        if not isinstance(_dict, dict):
            raise ValueError("expected dict")

        __builder = cls.builder()

        images_per_object = _dict.get("images_per_object")
        if images_per_object is None:
            images_per_object = 2
        __builder.images_per_object = images_per_object

        objects = _dict.get("objects")
        if objects is None:
            objects = 10
        __builder.objects = objects

        return __builder.build()

    @property
    def images_per_object(self) -> int:
        return self.__images_per_object

    @property
    def objects(self) -> int:
        return self.__objects

    @classmethod
    def read(cls, iprot):
        '''
        Read a new object from the given input protocol and return the object.

        :type iprot: thryft.protocol._input_protocol._InputProtocol
        :rtype: pastpy.gen.database.impl.dummy.dummy_database_configuration.DummyDatabaseConfiguration
        '''

        init_kwds = {}

        iprot.read_struct_begin()
        while True:
            ifield_name, ifield_type, _ifield_id = iprot.read_field_begin()
            if ifield_type == 0:  # STOP
                break
            elif ifield_name == 'images_per_object':
                init_kwds['images_per_object'] = iprot.read_i32()
            elif ifield_name == 'objects':
                init_kwds['objects'] = iprot.read_i32()
            iprot.read_field_end()
        iprot.read_struct_end()

        return cls(**init_kwds)

    def replacer(self):
        return self.Builder.from_template(template=self)

    def to_builtins(self):
        dict_ = {}
        dict_["images_per_object"] = self.images_per_object
        dict_["objects"] = self.objects
        return dict_

    def write(self, oprot):
        '''
        Write this object to the given output protocol and return self.

        :type oprot: thryft.protocol._output_protocol._OutputProtocol
        :rtype: pastpy.gen.database.impl.dummy.dummy_database_configuration.DummyDatabaseConfiguration
        '''

        oprot.write_struct_begin('DummyDatabaseConfiguration')

        oprot.write_field_begin(name='images_per_object', type=8, id=None)
        oprot.write_i32(self.images_per_object)
        oprot.write_field_end()

        oprot.write_field_begin(name='objects', type=8, id=None)
        oprot.write_i32(self.objects)
        oprot.write_field_end()

        oprot.write_field_stop()

        oprot.write_struct_end()

        return self

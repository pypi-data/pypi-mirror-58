import builtins
import pastpy.gen.database.impl.dbf.dbf_database_configuration
import pastpy.gen.database.impl.dummy.dummy_database_configuration
import pastpy.gen.database.impl.online.online_database_configuration
import typing


class DatabaseConfiguration(object):
    class Builder(object):
        def __init__(
            self,
            dbf=None,
            dummy=None,
            online=None,
        ):
            self.__dbf = dbf
            self.__dummy = dummy
            self.__online = online

        def build(self):
            return DatabaseConfiguration(dbf=self.__dbf, dummy=self.__dummy, online=self.__online)

        @property
        def dbf(self) -> typing.Union[pastpy.gen.database.impl.dbf.dbf_database_configuration.DbfDatabaseConfiguration, None]:
            return self.__dbf

        @property
        def dummy(self) -> typing.Union[pastpy.gen.database.impl.dummy.dummy_database_configuration.DummyDatabaseConfiguration, None]:
            return self.__dummy

        @classmethod
        def from_template(cls, template):
            '''
            :type template: pastpy.gen.database.database_configuration.DatabaseConfiguration
            :rtype: pastpy.gen.database.database_configuration.DatabaseConfiguration
            '''

            builder = cls()
            builder.dbf = template.dbf
            builder.dummy = template.dummy
            builder.online = template.online
            return builder

        @property
        def online(self) -> typing.Union[pastpy.gen.database.impl.online.online_database_configuration.OnlineDatabaseConfiguration, None]:
            return self.__online

        def set_dbf(self, dbf: typing.Union[pastpy.gen.database.impl.dbf.dbf_database_configuration.DbfDatabaseConfiguration, None]):
            if dbf is not None:
                if not isinstance(dbf, pastpy.gen.database.impl.dbf.dbf_database_configuration.DbfDatabaseConfiguration):
                    raise TypeError("expected dbf to be a pastpy.gen.database.impl.dbf.dbf_database_configuration.DbfDatabaseConfiguration but it is a %s" % builtins.type(dbf))
            self.__dbf = dbf
            return self

        def set_dummy(self, dummy: typing.Union[pastpy.gen.database.impl.dummy.dummy_database_configuration.DummyDatabaseConfiguration, None]):
            if dummy is not None:
                if not isinstance(dummy, pastpy.gen.database.impl.dummy.dummy_database_configuration.DummyDatabaseConfiguration):
                    raise TypeError("expected dummy to be a pastpy.gen.database.impl.dummy.dummy_database_configuration.DummyDatabaseConfiguration but it is a %s" % builtins.type(dummy))
            self.__dummy = dummy
            return self

        def set_online(self, online: typing.Union[pastpy.gen.database.impl.online.online_database_configuration.OnlineDatabaseConfiguration, None]):
            if online is not None:
                if not isinstance(online, pastpy.gen.database.impl.online.online_database_configuration.OnlineDatabaseConfiguration):
                    raise TypeError("expected online to be a pastpy.gen.database.impl.online.online_database_configuration.OnlineDatabaseConfiguration but it is a %s" % builtins.type(online))
            self.__online = online
            return self

        def update(self, database_configuration):
            if isinstance(database_configuration, DatabaseConfiguration):
                self.set_dbf(database_configuration.dbf)
                self.set_dummy(database_configuration.dummy)
                self.set_online(database_configuration.online)
            elif isinstance(database_configuration, dict):
                for key, value in database_configuration.items():
                    getattr(self, 'set_' + key)(value)
            else:
                raise TypeError(database_configuration)
            return self

        @dbf.setter
        def dbf(self, dbf: typing.Union[pastpy.gen.database.impl.dbf.dbf_database_configuration.DbfDatabaseConfiguration, None]) -> None:
            self.set_dbf(dbf)

        @dummy.setter
        def dummy(self, dummy: typing.Union[pastpy.gen.database.impl.dummy.dummy_database_configuration.DummyDatabaseConfiguration, None]) -> None:
            self.set_dummy(dummy)

        @online.setter
        def online(self, online: typing.Union[pastpy.gen.database.impl.online.online_database_configuration.OnlineDatabaseConfiguration, None]) -> None:
            self.set_online(online)

    class FieldMetadata(object):
        DBF = None
        DUMMY = None
        ONLINE = None

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
            return (cls.DBF, cls.DUMMY, cls.ONLINE,)

    FieldMetadata.DBF = FieldMetadata('dbf', pastpy.gen.database.impl.dbf.dbf_database_configuration.DbfDatabaseConfiguration, None)
    FieldMetadata.DUMMY = FieldMetadata('dummy', pastpy.gen.database.impl.dummy.dummy_database_configuration.DummyDatabaseConfiguration, None)
    FieldMetadata.ONLINE = FieldMetadata('online', pastpy.gen.database.impl.online.online_database_configuration.OnlineDatabaseConfiguration, None)

    def __init__(
        self,
        dbf: typing.Union[pastpy.gen.database.impl.dbf.dbf_database_configuration.DbfDatabaseConfiguration, None] = None,
        dummy: typing.Union[pastpy.gen.database.impl.dummy.dummy_database_configuration.DummyDatabaseConfiguration, None] = None,
        online: typing.Union[pastpy.gen.database.impl.online.online_database_configuration.OnlineDatabaseConfiguration, None] = None,
    ):
        if dbf is not None:
            if not isinstance(dbf, pastpy.gen.database.impl.dbf.dbf_database_configuration.DbfDatabaseConfiguration):
                raise TypeError("expected dbf to be a pastpy.gen.database.impl.dbf.dbf_database_configuration.DbfDatabaseConfiguration but it is a %s" % builtins.type(dbf))
        self.__dbf = dbf

        if dummy is not None:
            if not isinstance(dummy, pastpy.gen.database.impl.dummy.dummy_database_configuration.DummyDatabaseConfiguration):
                raise TypeError("expected dummy to be a pastpy.gen.database.impl.dummy.dummy_database_configuration.DummyDatabaseConfiguration but it is a %s" % builtins.type(dummy))
        self.__dummy = dummy

        if online is not None:
            if not isinstance(online, pastpy.gen.database.impl.online.online_database_configuration.OnlineDatabaseConfiguration):
                raise TypeError("expected online to be a pastpy.gen.database.impl.online.online_database_configuration.OnlineDatabaseConfiguration but it is a %s" % builtins.type(online))
        self.__online = online

        # Union check
        __present_field_count = 0
        if self.dbf is not None:
            __present_field_count = __present_field_count + 1
        if self.dummy is not None:
            __present_field_count = __present_field_count + 1
        if self.online is not None:
            __present_field_count = __present_field_count + 1
        if __present_field_count != 1:
            raise ValueError("database_configuration.DatabaseConfiguration: %d fields set in a union" % __present_field_count)

    def __eq__(self, other):
        if self.dbf != other.dbf:
            return False
        if self.dummy != other.dummy:
            return False
        if self.online != other.online:
            return False
        return True

    def __hash__(self):
        return hash((self.dbf, self.dummy, self.online,))

    def __iter__(self):
        return iter((self.dbf, self.dummy, self.online,))

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        field_reprs = []
        if self.dbf is not None:
            field_reprs.append('dbf=' + repr(self.dbf))
        if self.dummy is not None:
            field_reprs.append('dummy=' + repr(self.dummy))
        if self.online is not None:
            field_reprs.append('online=' + repr(self.online))
        return 'DatabaseConfiguration(' + ', '.join(field_reprs) + ')'

    def __str__(self):
        field_reprs = []
        if self.dbf is not None:
            field_reprs.append('dbf=' + repr(self.dbf))
        if self.dummy is not None:
            field_reprs.append('dummy=' + repr(self.dummy))
        if self.online is not None:
            field_reprs.append('online=' + repr(self.online))
        return 'DatabaseConfiguration(' + ', '.join(field_reprs) + ')'

    @classmethod
    def builder(cls):
        return cls.Builder()

    @property
    def dbf(self) -> typing.Union[pastpy.gen.database.impl.dbf.dbf_database_configuration.DbfDatabaseConfiguration, None]:
        return self.__dbf

    @property
    def dummy(self) -> typing.Union[pastpy.gen.database.impl.dummy.dummy_database_configuration.DummyDatabaseConfiguration, None]:
        return self.__dummy

    @classmethod
    def from_builtins(cls, _dict):
        if not isinstance(_dict, dict):
            raise ValueError("expected dict")

        __builder = cls.builder()

        dbf = _dict.get("dbf")
        if dbf is not None:
            dbf = pastpy.gen.database.impl.dbf.dbf_database_configuration.DbfDatabaseConfiguration.from_builtins(dbf)
        __builder.dbf = dbf

        dummy = _dict.get("dummy")
        if dummy is not None:
            dummy = pastpy.gen.database.impl.dummy.dummy_database_configuration.DummyDatabaseConfiguration.from_builtins(dummy)
        __builder.dummy = dummy

        online = _dict.get("online")
        if online is not None:
            online = pastpy.gen.database.impl.online.online_database_configuration.OnlineDatabaseConfiguration.from_builtins(online)
        __builder.online = online

        return __builder.build()

    @property
    def online(self) -> typing.Union[pastpy.gen.database.impl.online.online_database_configuration.OnlineDatabaseConfiguration, None]:
        return self.__online

    @classmethod
    def read(cls, iprot):
        '''
        Read a new object from the given input protocol and return the object.

        :type iprot: thryft.protocol._input_protocol._InputProtocol
        :rtype: pastpy.gen.database.database_configuration.DatabaseConfiguration
        '''

        init_kwds = {}

        iprot.read_struct_begin()
        while True:
            ifield_name, ifield_type, _ifield_id = iprot.read_field_begin()
            if ifield_type == 0:  # STOP
                break
            elif ifield_name == 'dbf':
                init_kwds['dbf'] = pastpy.gen.database.impl.dbf.dbf_database_configuration.DbfDatabaseConfiguration.read(iprot)
            elif ifield_name == 'dummy':
                init_kwds['dummy'] = pastpy.gen.database.impl.dummy.dummy_database_configuration.DummyDatabaseConfiguration.read(iprot)
            elif ifield_name == 'online':
                init_kwds['online'] = pastpy.gen.database.impl.online.online_database_configuration.OnlineDatabaseConfiguration.read(iprot)
            iprot.read_field_end()
        iprot.read_struct_end()

        return cls(**init_kwds)

    def replacer(self):
        return self.Builder.from_template(template=self)

    def to_builtins(self):
        dict_ = {}
        if self.dbf is not None:
            dict_["dbf"] = self.dbf.to_builtins()
        if self.dummy is not None:
            dict_["dummy"] = self.dummy.to_builtins()
        if self.online is not None:
            dict_["online"] = self.online.to_builtins()
        return dict_

    def write(self, oprot):
        '''
        Write this object to the given output protocol and return self.

        :type oprot: thryft.protocol._output_protocol._OutputProtocol
        :rtype: pastpy.gen.database.database_configuration.DatabaseConfiguration
        '''

        oprot.write_struct_begin('DatabaseConfiguration')

        if self.dbf is not None:
            oprot.write_field_begin(name='dbf', type=12, id=None)
            self.dbf.write(oprot)
            oprot.write_field_end()

        if self.dummy is not None:
            oprot.write_field_begin(name='dummy', type=12, id=None)
            self.dummy.write(oprot)
            oprot.write_field_end()

        if self.online is not None:
            oprot.write_field_begin(name='online', type=12, id=None)
            self.online.write(oprot)
            oprot.write_field_end()

        oprot.write_field_stop()

        oprot.write_struct_end()

        return self
